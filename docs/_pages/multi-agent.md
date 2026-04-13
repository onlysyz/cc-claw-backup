---
layout: default
title: 多 Agent 协作 - CC-Claw
description: 了解 CC-Claw 多 Agent 协作功能，如何让多个 AI Agent 同时工作，提升开发效率。
keywords: multi-agent, AI collaboration, 多 Agent 协作, cc-claw
---

# 多 Agent 协作

CC-Claw 支持多个 AI Agent 同时工作，专门负责不同领域，协作完成复杂目标。

## 为什么需要多 Agent？

| 方式 | 效率 | 专业化 |
|------|------|--------|
| 单体 Agent | 串行 | 一般 |
| 多 Agent | 并行 | 专业化 |

## 架构

```
Coordinator Agent (主控)
├── 分解目标
├── 分配任务
└── 整合结果
    │
    ├── Specialist: Backend   → 后端 API
    ├── Specialist: Frontend  → 前端页面
    ├── Specialist: Testing   → 测试用例
    │
    └── Reviewer             → 质量审核
```

## 快速开始

```python
from cc_claw import MultiAgentCollaboration, AgentRole

collab = MultiAgentCollaboration()

# 注册专家 Agent
backend = collab.register_agent(
    name="BackendDev",
    role=AgentRole.SPECIALIST,
    capabilities=["python", "fastapi", "postgresql"]
)

frontend = collab.register_agent(
    name="FrontendDev",
    role=AgentRole.SPECIALIST,
    capabilities=["react", "typescript", "tailwind"]
)

reviewer = collab.register_agent(
    name="CodeReviewer",
    role=AgentRole.REVIEWER,
    capabilities=["security", "performance", "code_review"]
)

# 创建协作任务
task = collab.create_task(
    description="实现博客系统 API",
    goal_id="blog-goal",
    priority=10,
    depends_on=[]
)

# 分配任务
collab.assign_task(task.id, backend.id)
```

## 任务依赖

```python
# 创建有依赖的任务
research = collab.create_task("研究需求", goal_id, priority=10)
api_task = collab.create_task(
    "实现 API",
    goal_id,
    priority=5,
    depends_on=[research.id]  # 依赖研究任务
)
frontend_task = collab.create_task(
    "实现前端",
    goal_id,
    priority=5,
    depends_on=[api_task.id]  # 依赖 API 任务
)
```

## 共享知识库

Agent 之间可以共享产物：

```python
# Agent 1 完成后共享
collab.share_knowledge(
    key="api_schema",
    value={"endpoints": 12, "models": 5},
    source_task=api_task.id
)

# Agent 2 读取
schema = collab.get_shared_knowledge("api_schema")
```

## 查看状态

```python
# 查看工作负载
workload = collab.get_agent_workload()

# 查看工作流状态
status = collab.get_workflow_status(goal_id)

# 生成报告
report = collab.generate_report(goal_id)
```

## 最佳实践

1. **专业化分工** — 每个 Agent 只做自己擅长的事
2. **清晰依赖** — 明确任务之间的依赖关系
3. **共享知识** — 通过知识库交换重要产物
4. **Reviewer 审核** — 重要任务需要 Reviewer 把关