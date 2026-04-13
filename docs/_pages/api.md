---
layout: default
title: API 参考 - CC-Claw Python API
description: CC-Claw Python API 完整参考，包含所有模块、类、方法的详细说明。
keywords: cc-claw api, Python API, cc-claw module, API reference
---

# API 参考

## 模块概览

| 模块 | 描述 |
|------|------|
| `cc_claw` | 主包入口 |
| `cc_claw.daemon` | 守护进程 |
| `cc_claw.memory` | 持久化记忆 |
| `cc_claw.collaboration` | 多 Agent 协作 |
| `cc_claw.retry` | 智能重试 |
| `cc_claw.tools` | 内置工具 |

---

## cc_claw

主包入口。

```python
import cc_claw
print(cc_claw.__version__)  # 0.1.0
```

### 导出内容

```python
from cc_claw import (
    # 核心
    CCClawDaemon,
    ClientConfig,

    # 记忆
    PersistentMemory,
    ConversationMemory,

    # 协作
    MultiAgentCollaboration,
    AgentRole,
    TaskStatus,

    # 重试
    SmartRetry,
    RetryConfig,
    get_retry_manager,
)
```

---

## ClientConfig

配置客户端连接。

```python
from cc_claw import ClientConfig

config = ClientConfig(
    device_id="your-device-id",
    device_token="your-device-token",
    claude_path="/usr/local/bin/claude",  # 可选
    ws_url="wss://api.cc-claw.dev",       # 可选
)
```

### 参数

| 参数 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `device_id` | str | 必填 | 设备 ID |
| `device_token` | str | 必填 | 设备令牌 |
| `claude_path` | str | "claude" | Claude CLI 路径 |
| `ws_url` | str | 默认服务器 | WebSocket 服务器地址 |

---

## CCClawDaemon

主守护进程类。

```python
from cc_claw import CCClawDaemon, ClientConfig

config = ClientConfig(
    device_id="xxx",
    device_token="yyy"
)

daemon = CCClawDaemon(config)
daemon.run()
```

### 方法

#### `run()`

启动守护进程，阻塞当前线程。

```python
daemon.run()
```

---

## PersistentMemory

持久化记忆模块。

```python
from cc_claw import PersistentMemory

memory = PersistentMemory()

# 添加记忆
memory.add("用户偏好使用 FastAPI", category="learned")

# 搜索
results = memory.search("FastAPI")

# 获取恢复上下文
context = memory.get_context_for_resume()
```

### 方法

#### `add(content, category, importance, tags)`

添加新记忆。

| 参数 | 类型 | 描述 |
|------|------|------|
| `content` | str | 记忆内容 |
| `category` | str | 分类: context, decision, error, success, learned |
| `importance` | int | 重要性 1-5 |
| `tags` | List[str] | 标签列表 |

#### `search(query, limit, category)`

搜索记忆。

#### `get_recent(limit, category)`

获取最近的记忆。

#### `get_context_for_resume()`

获取用于恢复会话的上下文。

#### `get_stats()`

获取记忆统计信息。

---

## ConversationMemory

短期对话记忆。

```python
from cc_claw import ConversationMemory

conv = ConversationMemory()
conv.add_user("继续上次的工作")
conv.add_assistant("好的...")

# 获取格式化的历史
history = conv.get_formatted(n=10)
```

---

## MultiAgentCollaboration

多 Agent 协作管理。

```python
from cc_claw import MultiAgentCollaboration, AgentRole

collab = MultiAgentCollaboration()

# 注册 Agent
agent = collab.register_agent(
    name="BackendDev",
    role=AgentRole.SPECIALIST,
    capabilities=["python", "fastapi", "postgresql"]
)

# 创建任务
task = collab.create_task(
    description="实现用户认证",
    goal_id="goal-123",
    priority=10,
    depends_on=[]
)

# 分配任务
collab.assign_task(task.id, agent.id)

# 查看状态
status = collab.get_workflow_status("goal-123")
```

### AgentRole

| 值 | 描述 |
|----|------|
| `COORDINATOR` | 主控 Agent |
| `SPECIALIST` | 专家 Agent |
| `WORKER` | 工作 Agent |
| `REVIEWER` | 审核 Agent |

---

## SmartRetry

智能重试模块。

```python
from cc_claw import get_retry_manager, RetryConfig, RetryStrategy

manager = get_retry_manager()

# 执行带重试的操作
result = await manager.execute(
    "api_call",
    some_async_function,
    config=RetryConfig(
        max_retries=3,
        base_delay=1.0,
        strategy=RetryStrategy.EXPONENTIAL_WITH_JITTER
    )
)
```

### RetryConfig

```python
RetryConfig(
    max_retries=3,           # 最大重试次数
    base_delay=1.0,         # 基础延迟（秒）
    max_delay=60.0,         # 最大延迟
    strategy=RetryStrategy.EXPONENTIAL_WITH_JITTER,
    retry_on=(ConnectionError, TimeoutError),
    timeout=30.0
)
```

### RetryStrategy

| 值 | 描述 |
|----|------|
| `IMMEDIATE` | 无延迟 |
| `LINEAR` | 线性延迟 |
| `EXPONENTIAL` | 指数延迟 |
| `EXPONENTIAL_WITH_JITTER` | 指数 + 抖动（推荐） |
| `FIBONACCI` | 斐波那契延迟 |

### 预定义配置

```python
from cc_claw import RETRY_CONFIGS

network_retry = RETRY_CONFIGS["network"]   # 网络请求
claude_retry = RETRY_CONFIGS["claude_api"] # Claude API
db_retry = RETRY_CONFIGS["database"]       # 数据库
```

---

## 工具模块

### FileProcessor

```python
from cc_claw.tools import FileProcessor

content = FileProcessor.read("/path/to/file.py")
FileProcessor.write("/path/to/file.py", content)
results = FileProcessor.search("TODO", path=".", file_type="py")
```

### ApiClient

```python
from cc_claw.tools import ApiClient

result = ApiClient.call(
    url="https://api.example.com/data",
    method="GET",
    headers={"Authorization": "Bearer xxx"}
)
```

### MonitorTool

```python
from cc_claw.tools import MonitorTool

health = MonitorTool.health_check(port=3000)
disk = MonitorTool.check_disk(threshold=90)
```

### 完整工具列表

| 工具 | 描述 |
|------|------|
| `FileProcessor` | 文件读写搜索 |
| `DataScraper` | 网页爬取 |
| `ApiClient` | HTTP 调用 |
| `ProcessManager` | 进程管理 |
| `SystemInfo` | 系统信息 |
| `GitHelper` | Git 操作 |
| `DockerHelper` | Docker 管理 |
| `DatabaseTool` | SQL 操作 |
| `ImageTool` | 图片处理 |
| `NotificationTool` | 通知推送 |
| `CodeAnalysisTool` | 代码分析 |
| `MonitorTool` | 监控告警 |