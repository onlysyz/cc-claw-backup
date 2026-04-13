# 30 分钟上手：用 CC-Claw 构建你的第一个自主 AI Agent

> 作者：cc-claw Team
> 首发：掘金
> 标签：入门教程, AI Agent, Claude Code, Python

## 前言

本文手把手教你在 30 分钟内，用 CC-Claw 搭建一个可以 24/7 运行的自主 AI Agent。不需要懂高深的技术，只需要会写 Python。

---

## 什么是 CC-Claw？

简单来说：**CC-Claw = Claude Code + 自主执行 + 持久记忆**

- Claude Code：Anthropic 官方 CLI 工具，可以调用 Claude AI
- CC-Claw：在 Claude Code 基础上加了"自主循环"，让它能自动工作

---

## 准备工作

### 1. 安装 Claude Code

```bash
# macOS
brew install anthropic

# 或下载
# https://docs.anthropic.com/en/docs/claude-code/initial-setup
```

验证安装：
```bash
claude --version
# claude 1.0.x
```

### 2. 安装 CC-Claw

```bash
pip install cc-claw
```

验证安装：
```bash
cc-claw --version
# cc-claw 0.1.0
```

---

## 第一步：配置

```bash
# 交互式配置向导
cc-claw setup

# 你会看到：
# Step 1: Server URL (默认 localhost)
# Step 2: Claude CLI 路径 (通常自动检测)
# Step 3: 权限模式 (选 bypassPermissions)
# Step 4: 工作目录 (默认 /tmp)
```

---

## 第二步：连接

```bash
# 注册设备
cc-claw pair

# 按提示在 Telegram 发送 /pair 获取验证码
# 输入验证码完成配对
```

---

## 第三步：启动守护进程

```bash
# 前台运行（测试用）
cc-claw start

# 后台运行（生产用）
nohup cc-claw start > cc-claw.log 2>&1 &
```

看到以下输出表示启动成功：

```
[CC-CLAW] Daemon started
[CC-CLAW] Connected to server
[CC-CLAW] Waiting for messages...
```

---

## 第四步：设置你的第一个目标

在 Telegram 发送：

```
/goal 帮我写一个计算器程序
```

CC-Claw 会：

1. **分析你的目标** → "写一个命令行计算器"
2. **分解成任务** → ["实现加减乘除", "添加错误处理", "写使用说明"]
3. **开始执行** → 自动运行

---

## 进阶：Python API 方式

如果想在代码中使用 CC-Claw：

```python
from cc_claw import CCClawDaemon, ClientConfig

# 配置
config = ClientConfig(
    device_id="your-device-id",
    device_token="your-device-token",
)

# 创建守护进程
daemon = CCClawDaemon(config)

# 启动（阻塞）
daemon.run()
```

---

## 第五步：使用持久化记忆

CC-Claw 可以跨会话记住上下文：

```python
from cc_claw import PersistentMemory, ConversationMemory

# 长期记忆
memory = PersistentMemory()

# 添加记忆
memory.add_context_snapshot(
    task="用户偏好 Python",
    context="用户是数据科学家",
    result="使用 pandas 处理数据"
)

# 获取恢复上下文
resume = memory.get_context_for_resume()
# 下次启动时，Claude 会自动加载这个上下文
```

---

## 第六步：多任务协作

```python
from cc_claw import MultiAgentCollaboration, AgentRole

collab = MultiAgentCollaboration()

# 注册专家 Agent
backend = collab.register_agent(
    name="后端开发",
    role=AgentRole.SPECIALIST,
    capabilities=["python", "fastapi", "postgresql"]
)

frontend = collab.register_agent(
    name="前端开发",
    role=AgentRole.SPECIALIST,
    capabilities=["react", "typescript"]
)

# 创建任务
task = collab.create_task(
    description="开发一个博客系统",
    goal_id="blog-goal",
    priority=10,
)

# 分配
collab.assign_task(task.id, backend.id)
```

---

## 第七步：添加智能重试

```python
from cc_claw import get_retry_manager, RetryConfig, RetryStrategy

manager = get_retry_manager()

async def call_api():
    """需要重试的函数"""
    return await some_api_call()

# 使用智能重试
result = await manager.execute(
    "api_call",
    call_api,
    config=RetryConfig(
        max_retries=3,
        base_delay=1.0,
        strategy=RetryStrategy.EXPONENTIAL_WITH_JITTER,
    )
)
```

---

## 实战示例：自动化代码审查

完整示例代码：

```python
from cc_claw import CCClawDaemon, ClientConfig, PersistentMemory
from cc_claw.tools import GitHelper

config = ClientConfig()
daemon = CCClawDaemon(config)

# 启动时设置目标
memory = PersistentMemory()

# 添加代码审查目标
memory.add(
    content="目标：每天早上审查昨天的代码改动",
    category="goal",
    importance=5
)

# CC-Claw 会自动：
# 1. 读取昨天的 git diff
# 2. 分析代码质量
# 3. 生成审查报告
# 4. 发送给你
```

---

## 常用命令速查

| 命令 | 功能 |
|------|------|
| `cc-claw start` | 启动守护进程 |
| `cc-claw status` | 查看状态 |
| `cc-claw progress` | 查看进度 |
| `cc-claw pause` | 暂停自主模式 |
| `cc-claw resume` | 恢复自主模式 |
| `cc-claw goals` | 查看所有目标 |
| `/goal <描述>` | 设置新目标 |
| `/progress` | 查看详细进度 |

---

## 常见问题

### Q: Claude CLI 需要登录吗？

是的，首次使用需要：
```bash
claude login
# 按提示完成登录
```

### Q: 怎么查看 CC-Claw 在干什么？

```bash
# 查看日志
tail -f cc-claw.log

# 或实时状态
cc-claw status
```

### Q: 能同时运行多个目标吗？

可以，但建议一次一个主目标，其他作为后台任务。

### Q: Token 消耗如何？

取决于任务复杂度。CC-Claw 有智能节流，不会浪费 Token。

---

## 下一步

学完基础后，可以探索：

1. **集成 AgentSolveHub** — 遇到错误自动搜索解决方案
2. **自定义工具** — 添加你自己的工具
3. **多 Agent 协作** — 让多个 Agent 同时工作
4. **Webhook 集成** — 和外部系统联动

---

## 示例项目

### 项目 1：自动博客写手

```python
# 目标：每天自动更新技术博客
memory.add(
    content="每天早上 8 点，检查 GitHub Trending，生成一篇技术博客",
    category="goal",
    importance=5
)
```

### 项目 2：Bug 自动修复

```python
# 目标：监控系统错误，自动尝试修复
memory.add(
    content="当 GitHub Actions 失败时，自动分析日志并提交修复 PR",
    category="goal",
    importance=5
)
```

### 项目 3：代码文档生成器

```python
# 目标：新 PR 自动生成文档
memory.add(
    content="当 PR 合并时，自动更新 API 文档",
    category="goal",
    importance=4
)
```

---

## 资源链接

- GitHub: https://github.com/onlysyz/cc-claw
- 文档: https://docs.cc-claw.dev
- Discord: https://discord.gg/cc-claw
- 示例项目: https://github.com/onlysyz/cc-claw/examples

---

**30 分钟入门完成！开始你的第一个自主 AI Agent 吧！**

有任何问题，欢迎评论区交流 🚀