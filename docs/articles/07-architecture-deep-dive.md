# CC-Claw 架构深度解析：如何设计一个 24/7 运行的 AI Agent

> 作者：cc-claw Team
> 首发：掘金
> 标签：架构设计, AI Agent, Python, 系统设计

## 前言

我花了 6 个月时间开发 CC-Claw，期间经历了无数次架构重构。本文深度解析 CC-Claw 的核心架构设计，适合想构建类似系统的开发者。

---

## 整体架构

```
┌─────────────────────────────────────────────────────────────┐
│                        用户层                                 │
│   Telegram Bot / Lark / WebSocket CLI / HTTP API           │
└─────────────────────────────┬───────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                      消息处理层                               │
│   MessageHandler → 命令解析 → 响应生成                       │
│   - /pause, /resume, /progress, /goals                    │
│   - 自然语言处理                                            │
│   - 优先级消息插入                                        │
└─────────────────────────────┬───────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                      自主执行层                               │
│   AutonomousRunner ←→ GoalEngine ←→ TaskQueue              │
│   - 任务循环执行                                           │
│   - 目标分解                                              │
│   - 优先级调度                                            │
└─────────────────────────────┬───────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                      执行层                                  │
│   ClaudeExecutor ←→ TokenTracker ←→ RateLimiter            │
│   - Claude CLI 调用                                         │
│   - Token 统计                                            │
│   - 限流处理                                              │
└─────────────────────────────┬───────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                      工具层                                  │
│   FileProcessor | DataScraper | GitHelper | DockerHelper  │
│   DatabaseTool | MonitorTool | NotificationTool | ...      │
└─────────────────────────────────────────────────────────────┘
```

---

## 核心组件详解

### 1. 消息处理：Handler 模式

CC-Claw 使用 Handler 模式处理各种消息：

```python
class MessageHandler:
    async def handle_message(self, message: Message):
        content = message.data.get("content", "")

        # 命令路由
        if content.startswith("/pause"):
            await self._handle_pause()
        elif content.startswith("/resume"):
            await self._handle_resume()
        elif content.startswith("/progress"):
            await self._handle_progress()
        else:
            # 自然语言 → Claude 执行
            await self._handle_natural_language(message)
```

**设计要点：**
- 所有命令统一入口，便于扩展
- 支持优先级消息插队
- 异步处理，不阻塞主循环

### 2. 自主执行循环

这是 CC-Claw 的核心 — 自主_runner：

```python
async def _autonomous_runner(self):
    """自主执行循环"""
    while self._running:
        # 1. 检查自主模式是否开启
        if not self.handler.autonomous_mode:
            await asyncio.sleep(5)
            continue

        # 2. 检查 Token 预算
        if self.profile.token_budget.is_rate_limited:
            wait = self.profile.increment_backoff()
            await asyncio.sleep(wait)
            continue

        # 3. 获取当前目标
        goal = self.profile.get_active_goal()
        if not goal:
            await asyncio.sleep(5)
            continue

        # 4. 检查是否需要分解
        if not self.profile.get_tasks_for_goal(goal.id):
            await self.goal_engine.decompose_goal(goal.id)

        # 5. 获取下一个任务
        qt = await self.queue_manager.get_next_task()
        if not qt:
            await asyncio.sleep(5)
            continue

        # 6. 执行任务
        await self._execute_autonomous_task(qt)
```

### 3. 目标引擎：GPT 驱动的任务分解

```python
class GoalEngine:
    async def decompose_goal(self, goal_id: str) -> List[Task]:
        goal = self.profile.get_goal_by_id(goal_id)

        # 构建包含用户上下文的 prompt
        prompt = f"""
User Context:
- Profession: {self.profile.profession}
- Situation: {self.profile.situation}
- Goal: {goal.description}

Decompose into 5-10 concrete tasks.
Return JSON array of task strings.
"""

        # 调用 Claude 分解
        response = await self.claude.execute(prompt)

        # 解析 JSON
        tasks = self._parse_tasks(response)

        # 创建 Task 对象
        return [self.profile.add_task(t, goal_id) for t in tasks]
```

### 4. 任务队列：优先级实现

```python
class TaskQueue:
    def enqueue(self, task: Task, user_initiated: bool = False):
        qt = QueuedTask(task=task, is_user_initiated=user_initiated)

        if user_initiated:
            # 用户消息插到最前面
            self._queue.appendleft(qt)
        else:
            # 后台任务排队
            self._queue.append(qt)
```

### 5. Token 追踪与限流

```python
class TokenBudget:
    def check_and_handle_rate_limit(self, response: str):
        if "429" in response or "rate limit" in response.lower():
            self.is_rate_limited = True
            self.backoff_level += 1
            self.rate_limit_until = time.time() + (60 * 2 ** self.backoff_level)

    def increment_backoff(self) -> int:
        """返回下次重试等待时间"""
        self.backoff_level += 1
        return 60 * (2 ** (self.backoff_level - 1))  # 1min, 2min, 4min...
```

---

## 异步设计

CC-Claw 是全异步架构，充分利用 Python asyncio：

```python
class CCClawDaemon:
    async def start(self):
        # 并发启动多个服务
        await asyncio.gather(
            self.ws_manager.connect(),    # WebSocket 连接
            self.scheduler.start(),       # 定时任务调度器
            self._task_checker(),          # 任务检查循环
            self._token_checker(),         # Token 检查循环
        )

    async def _task_checker(self):
        """后台任务检查"""
        while self._running:
            due_tasks = self.scheduler.get_due_tasks()
            for task in due_tasks:
                asyncio.create_task(self._execute_scheduled_task(task))
            await asyncio.sleep(10)
```

---

## 状态管理

使用文件持久化状态：

```python
class ProfileManager:
    def _save(self):
        path = self._get_default_path()
        path.parent.mkdir(parents=True, exist_ok=True)

        data = {
            "profile": self.profile.to_dict(),
            "goals": [g.to_dict() for g in self.goals],
            "tasks": [t.to_dict() for t in self.tasks],
            "token_budget": self.token_budget.to_dict(),
        }

        # 原子写入，防止损坏
        temp_path = path.with_suffix(".tmp")
        with open(temp_path, "w") as f:
            json.dump(data, f)
        temp_path.rename(path)
```

---

## 错误处理

三层错误处理：

```python
async def _execute_autonomous_task(self, qt):
    try:
        response = await self.claude.execute(qt.task.description)

        # 检查限流
        if self._is_rate_limited(response):
            qt.task.status = TaskStatus.PENDING
            self.queue_manager.requeue_front(qt)
            await asyncio.sleep(self.profile.increment_backoff())
            return

        # 记录结果
        self.profile.complete_task(qt.task.id, response[:200])

    except RateLimitError:
        # 层1: 可恢复错误 - 重试
        await self._handle_rate_limit(qt)
    except ExecutionError as e:
        # 层2: 执行错误 - 标记失败
        self.profile.fail_task(qt.task.id, str(e))
    except Exception as e:
        # 层3: 未知错误 - 日志记录，继续执行
        logger.error(f"Unexpected error: {e}", exc_info=True)
    finally:
        self.queue_manager.queue.mark_done()
```

---

## 扩展点

CC-Claw 设计了多个扩展点：

### 1. 添加新命令

```python
# handler.py
if content.strip() == "/mycommand":
    await self._handle_mycommand(message_id, lark_open_id)
    return
```

### 2. 添加新工具

```python
# tools.py
class MyTool:
    @staticmethod
    def my_operation(param: str) -> str:
        return f"Result: {param}"

TOOLS['mytool'] = MyTool
```

### 3. 插件系统

```python
class Plugin:
    def on_task_start(self, task): pass
    def on_task_complete(self, task, result): pass
    def on_error(self, error): pass

# Daemon 加载插件
daemon.register_plugin(AgentSolveHubPlugin())
```

---

## 性能优化

### 1. 连接复用

```python
class WebSocketManager:
    async def connect(self):
        self.ws = await websockets.connect(self.url)
        # 保持连接，不每次请求都重建
```

### 2. 批量 Token 统计

```python
# 不要每次都写文件
self._pending_save = True
asyncio.create_task(self._flush_save())  # 延迟批量写入
```

### 3. 记忆压缩

```python
# 超过 1000 条记忆时压缩
if len(self.entries) > self.MAX_ENTRIES:
    self._summarize_old_entries()
    self.entries = self.entries[-self.MAX_ENTRIES:]
```

---

## 监控与调试

```python
# 结构化日志
logger.info(f"[AUTONOMOUS] Executing: {task.description[:50]}...")
logger.warning(f"Rate limited, backing off {wait}s")
logger.error(f"Task failed: {error}")

# 统计指标
metrics = {
    "tasks_completed": len([t for t in self.tasks if t.status == "completed"]),
    "tasks_failed": len([t for t in self.tasks if t.status == "failed"]),
    "total_tokens": self.token_budget.total_used,
}
```

---

## 总结

CC-Claw 的架构设计原则：

1. **分层解耦** — Handler → Runner → Executor → Tools
2. **异步优先** — 充分利用 asyncio 并发
3. **状态持久化** — JSON 文件，原子写入
4. **错误恢复** — 三层错误处理机制
5. **可扩展** — 命令、工具、插件都很容易添加

**下一步建议：**
- 添加 Redis 支持分布式状态
- 添加 Prometheus 监控
- 添加 gRPC 接口

---

**相关链接：**
- GitHub: https://github.com/cc-claw/cc-claw
- 文档: https://docs.cc-claw.dev

有问题？欢迎评论区讨论！