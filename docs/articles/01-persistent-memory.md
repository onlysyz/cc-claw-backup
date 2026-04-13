# 让 Claude Code 拥有"记忆"：cc-claw 持久化上下文实战

> 作者：cc-claw Team
> 首发：掘金
> 标签：Claude Code, AI Agent, 上下文管理

## 前言

用 Claude Code 写代码时，你是否遇到过这些痛点：

- 每次会话都是"从零开始"，Claude 不记得上次的工作进度
- 复杂项目分解成多个任务后，下次打开 Claude 完全不知道做到哪了
- 解决了某个 bug 后，下次遇到类似问题 Claude 又从头推理一遍

**cc-claw 0.1.0 新增了 Persistent Memory 模块，让 Claude Code 拥有了真正的持久化记忆。**

---

## 什么是持久化上下文？

传统的 AI 对话上下文只存在于单次会话中。会话结束，上下文就消失了。

cc-claw 的 Persistent Memory 在磁盘上维护了一个长期记忆库：

```
~/.config/cc-claw/memory/
├── entries.jsonl      # 所有记忆条目（append-only）
├── current_session.json
└── summaries.json
```

每次任务执行前后，cc-claw 会自动打快照（snapshot）：

```python
# 任务执行前：记录上下文
memory.add_context_snapshot(
    task_description="实现用户认证模块",
    context="项目使用 FastAPI + PostgreSQL，需要兼容 OAuth2"
)

# 任务执行后：记录结果
memory.add_context_snapshot(
    task_description="实现用户认证模块",
    context="...",
    result="完成了 JWT token 验证，POST /auth/login 接口"
)
```

下次启动 Claude Code 时，只需调用：

```python
resume_context = memory.get_context_for_resume()
# 返回格式化的上下文摘要，包含：
# - 最近的任务快照
# - 关键决策记录
# - 已解决的问题
# - 重要学习
```

---

## 核心设计

### 1. 记忆分类

每个记忆条目都有 `category` 标签：

| Category | 用途 | 重要性 |
|----------|------|--------|
| `context` | 任务快照 | 1-5 |
| `decision` | 关键决策 | 5 |
| `error` | 错误记录 | 4 |
| `success` | 成功经验 | 4 |
| `learned` | 从实践中学习 | 3-5 |

### 2. 自动摘要与淘汰

- 最多保留 **1000 条**记忆
- 超过 **90 天**的条目自动清理
- 高重要性条目优先保留

### 3. 关键词搜索

```python
# 搜索所有与"认证"相关的记忆
results = memory.search("认证", limit=5, category="error")

for entry in results:
    print(f"[{entry.timestamp}] {entry.content}")
```

---

## 实战效果

对比一下有/无持久化记忆的 Claude Code 体验：

**没有持久化记忆：**
```
User: 继续上次的工作
Claude: 我不知道上次你做了什么。我们重新开始吧。
```

**有持久化记忆（cc-claw）：**
```
User: 继续上次的工作
Claude: 上次你在实现用户认证模块，已经完成了 JWT 验证和 /auth/login 接口。
还剩下：/auth/logout、密码重置、OAuth2 第三方登录。
是否继续？
```

---

## 技术实现亮点

### ConversationMemory：短期记忆滑动窗口

除了长期记忆，cc-claw 还维护了一个短期对话历史：

```python
conv_memory = ConversationMemory()

# 追踪当前对话
conv_memory.add_user("实现一个图片上传功能")
conv_memory.add_assistant("需要确定几个问题：1) 图片大小限制？...")

# 注入到下次 system prompt
system_prompt += conv_memory.get_formatted(n=10)
```

这样 Claude 能记住当前会话中用户的修正和偏好。

### 零配置，零感知

用户不需要手动触发记忆保存。cc-claw 在以下时机自动记录：

1. 任务开始执行前
2. 任务完成/失败后
3. 用户做出关键决策时（通过 `/decide` 命令）
4. Claude 解决了某个错误时（自动记录 error recovery）

---

## 安装体验

```bash
# 安装 cc-claw
pip install cc-claw

# 启动 daemon（记忆功能默认开启）
cc-claw daemon &
```

不需要任何配置，即刻拥有持久化记忆。

---

## 总结

cc-claw 的 Persistent Memory 不是简单的"保存对话历史"，而是一个**智能上下文管理系统**：

- ✅ 自动快照任务上下文
- ✅ 分类存储决策、错误、成功经验
- ✅ 支持语义搜索
- ✅ 智能淘汰策略防止记忆膨胀
- ✅ 会话恢复（Resume）无缝衔接

**下一步**：cc-claw 正在开发基于 embedding 的语义搜索，未来你可以用自然语言搜索记忆："上次做支付模块时那个超时问题是怎么解决的？"

---

**相关链接：**
- GitHub: https://github.com/cc-claw/cc-claw
- 文档: https://docs.cc-claw.dev
- 掘金技术交流群：扫描底部二维码

如果这篇文章对你有帮助，欢迎点赞、评论、转发！