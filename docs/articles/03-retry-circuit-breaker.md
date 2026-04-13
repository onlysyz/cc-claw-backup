# 让 AI Agent "健壮"起来：cc-claw 智能重试与熔断机制

> 作者：cc-claw Team
> 首发：掘金
> 标签：架构设计, AI Agent, 容错处理

## 前言

线上服务会因为网络抖动、第三方 API 限流、数据库连接池耗尽等原因偶发失败。传统代码有成熟的容错机制（重试、熔断、降级），但 AI Agent 的容错你考虑过吗？

**cc-claw 0.1.0 引入了 Smart Retry 模块，为 AI 执行提供企业级容错能力。**

---

## AI Agent 失败的常见场景

1. **网络问题** — 调用 Claude API 时网络超时
2. **API 限流** — 429 Too Many Requests
3. **Token 超限** — 单次请求超出上下文窗口
4. **服务不可用** — WebSocket 断连

这些问题如果不做处理，会导致：
- 任务执行到一半"卡死"
- 用户反复手动重试，体验差
- 错误无法追踪，难以排查

---

## Smart Retry：智能重试策略

### 多种退避算法

cc-claw 支持 5 种重试策略：

```python
from cc-claw import RetryStrategy, RetryConfig

# 1. 指数退避 + 抖动（推荐用于网络请求）
config = RetryConfig(
    strategy=RetryStrategy.EXPONENTIAL_WITH_JITTER,
    base_delay=1.0,
    max_delay=60.0
)

# 2. 纯指数退避
config = RetryConfig(
    strategy=RetryStrategy.EXPONENTIAL,
    base_delay=2.0,
    max_delay=120.0
)

# 3. 线性退避（用于对延迟敏感的场景）
config = RetryConfig(
    strategy=RetryStrategy.LINEAR,
    base_delay=0.5,
    max_delay=10.0
)

# 4. 斐波那契退避
config = RetryConfig(
    strategy=RetryStrategy.FIBONACCI,
    base_delay=1.0
)

# 5. 无延迟（仅重试，用于对延迟极敏感的场景）
config = RetryConfig(
    strategy=RetryStrategy.IMMEDIATE,
    max_retries=2
)
```

### 延迟计算可视化

```
Attempt 0 → 立即执行
Attempt 1 → 等待: 1s + jitter
Attempt 2 → 等待: 2s + jitter
Attempt 3 → 等待: 4s + jitter
Attempt 4 → 等待: 8s + jitter
...
(指数增长，最大 60s)
```

**Jitter 的作用**：防止"惊群效应"——大量请求同时失败后同时重试，再次同时到达。

---

## 预定义配置

针对不同场景，cc-claw 提供了开箱即用的配置：

```python
from cc-claw import RETRY_CONFIGS

# 网络请求重试
network_retry = RETRY_CONFIGS["network"]
# max_retries=3, base_delay=1.0, max_delay=30.0, 指数+抖动

# Claude API 专用
claude_retry = RETRY_CONFIGS["claude_api"]
# max_retries=4, base_delay=5.0, max_delay=120.0

# 数据库操作
db_retry = RETRY_CONFIGS["database"]
# max_retries=3, base_delay=0.5, max_delay=10.0, 线性退避

# 快速重试（对延迟敏感）
fast_retry = RETRY_CONFIGS["fast"]
# max_retries=2, base_delay=0.1, max_delay=1.0
```

---

## 装饰器模式：一行启用重试

```python
from cc-claw import with_retry, RetryConfig

@with_retry(operation="fetch_api", config=RetryConfig(max_retries=3))
async def fetch_user_data(url):
    response = requests.get(url)
    return response.json()
```

重试逻辑完全透明，调用方无需感知。

---

## 手动执行控制

更细粒度的控制：

```python
from cc-claw import get_retry_manager

manager = get_retry_manager()

try:
    result = await manager.execute(
        "claude_api_call",
        claude_client.execute,
        prompt,
        config=RetryConfig(
            max_retries=4,
            base_delay=5.0,
            strategy=RetryStrategy.EXPONENTIAL_WITH_JITTER,
            retry_on=(ConnectionError, TimeoutError, asyncio.TimeoutError),
            timeout=30.0
        ),
        circuit_breaker_name="claude_api"
    )
except MaxRetriesExceeded as e:
    print(f"重试耗尽: {e}")
    # 降级处理
```

---

## 熔断器（Circuit Breaker）：防止雪崩

### 什么是熔断器？

熔断器的思想来自电力系统的保险丝：

```
正常状态 (CLOSED):
  请求 → [执行] → 成功

失败累积 (OPEN):
  请求 → [拒绝] → 快速失败

试探恢复 (HALF_OPEN):
  请求 → [放行一个] → 成功则 CLOSED，失败则 OPEN
```

### 在 cc-claw 中使用

```python
# 创建熔断器
cb = manager.get_circuit_breaker("claude_api")

# 检查是否可以执行
if cb.can_execute():
    result = await claude.execute(prompt)
    cb.record_success()
else:
    print("Claude API 熔断中，排队等待...")
```

熔断器会自动管理状态：

```python
# 连续 5 次失败 → 熔断器 OPEN
cb.failure_threshold = 5

# OPEN 后等待 60s → 进入 HALF_OPEN 试探
cb.timeout = 60.0

# HALF_OPEN 连续 2 次成功 → 恢复到 CLOSED
cb.success_threshold = 2
```

---

## 重试统计

cc-claw 自动追踪所有操作的重试历史：

```python
stats = manager.get_all_stats()

print(stats)
# {
#   "operations": {
#     "claude_api_call": {
#       "attempts": 15,
#       "successes": 12,
#       "failures": 3,
#       "total_delay": 45.2,
#       "last_error": "Connection timeout after 30s"
#     }
#   },
#   "circuit_breakers": {
#     "claude_api": {
#       "state": "closed",
#       "failures": 1
#     }
#   }
# }
```

这些统计数据对于容量规划和问题排查非常有价值。

---

## 完整示例：带重试的 Claude 执行

```python
import asyncio
from cc-claw import ClaudeExecutor, get_retry_manager, RetryConfig

async def robust_execute(executor, prompt):
    manager = get_retry_manager()

    # 定义专用配置
    config = RetryConfig(
        max_retries=4,
        base_delay=3.0,
        max_delay=60.0,
        strategy=RetryStrategy.EXPONENTIAL_WITH_JITTER,
        retry_on=(ConnectionError, asyncio.TimeoutError),
        timeout=30.0
    )

    try:
        result = await manager.execute(
            "claude_execute",
            executor.execute,
            prompt,
            config=config,
            circuit_breaker_name="claude_api"
        )
        return result
    except CircuitBreakerOpen:
        return "服务暂时不可用，请稍后重试"
    except MaxRetriesExceeded:
        return "执行失败，已尝试多次"
```

---

## 与其他框架的对比

| 特性 | Tenacity | Backoff | cc-claw |
|------|---------|---------|---------|
| 异步支持 | ✅ | ✅ | ✅ |
| 熔断器 | ❌ | ❌ | ✅ |
| 抖动算法 | ✅ | ✅ | ✅ |
| 统计追踪 | ❌ | ❌ | ✅ |
| 装饰器模式 | ✅ | ❌ | ✅ |
| AI 场景优化 | ❌ | ❌ | ✅ |

---

## 最佳实践

### 1. 不要无限重试
```python
# ❌ 无限重试 — 可能导致永久阻塞
# ✅ 设置 max_retries
config = RetryConfig(max_retries=3)
```

### 2. 对不同错误区别对待
```python
# ❌ 所有错误都重试
# ✅ 只对可恢复错误重试
config = RetryConfig(
    retry_on=(ConnectionError, TimeoutError),
    # 业务逻辑错误不需要重试
)
```

### 3. 设置合理的超时
```python
# ❌ 无超时 — 可能永远等下去
# ✅ 有超时限制
config = RetryConfig(timeout=30.0)
```

### 4. 使用熔断器保护第三方服务
```python
# 对外部 API 使用熔断器
cb = get_circuit_breaker("external_api")
if not cb.can_execute():
    return fallback_response()
```

---

## 总结

cc-claw 的 Smart Retry 模块为 AI Agent 带来了工业级可靠性：

- 🔄 **智能重试** — 5 种退避算法，适应不同场景
- ⚡ **熔断保护** — 防止故障蔓延
- 📊 **统计追踪** — 问题可量化分析
- 🎯 **开箱即用** — 预置配置，一行启用

**让你的 AI Agent 7×24 小时稳定运行不再是梦想。**

---

**推荐阅读：**
- [cc-claw 持久化记忆实战]()
- [多 Agent 协作开发指南]()

有问题？评论区见！