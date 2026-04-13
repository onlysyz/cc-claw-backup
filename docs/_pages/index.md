---
layout: default
title: CC-Claw 文档 - Autonomous AI Coding Agent
description: CC-Claw 完整文档，让 Claude Code 拥有 24/7 自主工作能力。包含安装指南、API 参考、使用教程。
keywords: cc-claw, Claude Code, AI agent, autonomous coding, AI 编程, 自动编程
---

# CC-Claw 文档

<div class="hero">
  <h1>让 Claude Code 24/7 自动编程</h1>
  <p>CC-Claw 是 autonomous AI 工作伴侣，将 Claude Code 转变为不知疲倦的编程伙伴</p>
  <a href="/docs/getting-started" class="btn">快速开始 →</a>
</div>

## 核心功能

| 功能 | 描述 |
|------|------|
| [目标分解](/docs/goal-engine) | 自动将复杂目标分解为可执行任务 |
| [自主执行](/docs/autonomous-mode) | 24/7 持续工作，无需人工干预 |
| [持久化记忆](/docs/memory) | 跨会话记忆上下文和决策 |
| [多 Agent 协作](/docs/multi-agent) | 多个 Agent 同时工作 |
| [智能重试](/docs/retry) | 指数退避 + 熔断器容错 |
| [12 内置工具](/docs/tools) | 文件、API、数据库、监控等 |

## 快速开始

### 1. 安装

```bash
pip install cc-claw
```

### 2. 初始化

```bash
cc-claw pair    # 注册设备
cc-claw daemon  # 启动守护进程
```

### 3. 设置目标

```
发送: /goal 实现用户认证系统
```

## 按角色阅读

| 角色 | 推荐内容 |
|------|----------|
| 新用户 | [快速开始](/docs/getting-started) |
| 开发者 | [API 参考](/docs/api) |
| 高级用户 | [多 Agent 协作](/docs/multi-agent) |
| 贡献者 | [开发指南](/docs/contributing) |

## 最新更新

### v0.1.0 (2024-01)

- ✅ 持久化记忆模块
- ✅ 多 Agent 协作
- ✅ 智能重试 + 熔断器
- ✅ 12 个内置工具
- ✅ 目标引擎优化

[查看全部更新 →](/CHANGELOG)