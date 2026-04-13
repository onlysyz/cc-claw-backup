---
layout: default
title: 快速开始 - CC-Claw 安装配置指南
description: 5 分钟内让 CC-Claw 运行起来。完整的安装、配置、首次使用指南。
keywords: cc-claw install, cc-claw setup, Claude Code 安装, AI agent 入门
---

# 快速开始

**5 分钟内让 CC-Claw 运行起来**

## 前置要求

- Python 3.9+
- Claude Code CLI ([安装指南](https://docs.anthropic.com/en/docs/claude-code))
- 网络连接

## 安装

### 方式一：PyPI 安装（推荐）

```bash
pip install cc-claw
```

### 方式二：源码安装

```bash
git clone https://github.com/onlysyz/cc-claw.git
cd cc-claw
pip install -e .
```

### 验证安装

```bash
cc-claw --version
# cc-claw 0.1.0
```

## 初始化

### 1. 注册设备

```bash
cc-claw pair
```

这会创建一个配置文件在 `~/.config/cc-claw/`

### 2. 启动守护进程

```bash
cc-claw daemon
```

看到以下输出表示启动成功：

```
[CC-CLAW] Daemon started
[CC-CLAW] Connected to server
[CC-CLAW] Waiting for messages...
```

### 3. 后台运行

```bash
# 使用 nohup
nohup cc-claw daemon > cc-claw.log 2>&1 &

# 或使用 systemd
sudo systemctl enable cc-claw
sudo systemctl start cc-claw
```

## 首次使用

### 1. 发送 /start

在 Telegram 或 Lark 中发送 `/start`

### 2. 完成引导

CC-Claw 会询问：

1. **职业** — 你是做什么的？
2. **现状** — 目前面临什么挑战？
3. **短期目标** — 你想在近期达成什么？
4. **什么是"更好"** — 成功的标准是什么？

### 3. 设置目标

```
/goal 实现用户认证系统
```

CC-Claw 会自动分解目标并开始执行！

## 基本命令

| 命令 | 描述 |
|------|------|
| `cc-claw start` | 启动守护进程 |
| `cc-claw status` | 查看状态 |
| `cc-claw progress` | 查看进度 |
| `cc-claw pause` | 暂停自主模式 |
| `cc-claw resume` | 恢复自主模式 |
| `cc-claw goals` | 查看所有目标 |
| `cc-claw tasks` | 查看任务队列 |
| `cc-claw stop` | 停止守护进程 |

## 下一步

- [配置指南](/docs/configuration) — 自定义 CC-Claw 行为
- [目标引擎](/docs/goal-engine) — 了解目标如何分解
- [内置工具](/docs/tools) — 使用 12 个内置工具