---
layout: default
title: 持久化记忆 - CC-Claw
description: CC-Claw 持久化记忆功能详解，让 Claude Code 跨会话记住上下文和决策。
keywords: persistent memory, cc-claw memory, AI context, 持久化上下文
---

# 持久化记忆

CC-Claw 的持久化记忆让 Claude Code 跨会话记住上下文，就像有了真正的"记忆"一样。

## 为什么重要？

| 没有记忆 | 有记忆 |
|----------|--------|
| 每次会话从零开始 | 记住之前的上下文 |
| 重复解决相同问题 | 记住解决方案 |
| 忘记关键决策 | 记住所有决策 |

## 工作原理

```
会话 1                    会话 2
────────                  ────────
执行任务                  加载记忆
    ↓                         ↓
保存记忆 ──────────────→ 读取记忆
                        ↓
                    继续工作
```

## 使用方式

### 自动记录

CC-Claw 自动在以下时机记录：

1. 任务开始执行前
2. 任务完成/失败后
3. 用户做出关键决策时
4. 错误被解决时

### 手动记录

```python
from cc_claw import PersistentMemory

memory = PersistentMemory()

# 记录关键决策
memory.add_decision(
    decision="使用 PostgreSQL 而不是 MySQL",
    rationale="客户已有 PostgreSQL 经验"
)

# 记录学习
memory.add_learned(
    learning="Stripe API 需要配置 webhook 重试",
    context="支付回调不稳定"
)

# 记录错误恢复
memory.add_error_recovery(
    error="Stripe API 超时",
    solution="实现指数退避重试，最多重试 3 次"
)
```

### 搜索记忆

```python
# 搜索所有与 Stripe 相关的记忆
results = memory.search("stripe", limit=10)

for entry in results:
    print(f"[{entry.category}] {entry.content}")
```

### 恢复会话

```python
# 获取恢复上下文
context = memory.get_context_for_resume()

print(context)
# ## Session Memory - Resume Context
#
# ### Recent Task Snapshots
# - Task: 实现支付模块 - 完成
#
# ### Key Decisions
# - 使用 PostgreSQL
#
# ### Resolved Issues
# - Resolved: Stripe 超时 → 指数退避
```

## 记忆分类

| 分类 | 用途 | 重要性 |
|------|------|--------|
| `context` | 任务快照 | 3 |
| `decision` | 关键决策 | 5 |
| `error` | 错误记录 | 4 |
| `success` | 成功经验 | 4 |
| `learned` | 从实践中学习 | 3 |

## 自动清理

- 最多保留 **1000 条**记忆
- 超过 **90 天**自动清理
- 高重要性记忆优先保留

## 短期记忆

除了长期记忆，还有对话级别的短期记忆：

```python
from cc_claw import ConversationMemory

conv = ConversationMemory()
conv.add_user("继续上次的工作")
conv.add_assistant("好的...")

# 获取格式化的对话历史
history = conv.get_formatted(n=10)
```