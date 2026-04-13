# Building an Autonomous Coding Agent: My 6-Month Journey with cc-claw

> Author: cc-claw Team
> Posted: Hacker News
> Topic: AI / Machine Learning

## The Problem: Claude Code Can't Work While You Sleep

I use Claude Code daily for coding tasks. It's great when I'm at my desk, but:
- It stops working the moment I close my laptop
- Complex multi-step goals require constant babysitting
- I lose context between sessions

I wanted something that would keep working autonomously — like having a tireless junior developer running 24/7.

So I built **cc-claw**, an autonomous daemon that wraps Claude Code CLI.

---

## What cc-claw Does

```
You (8am):  "cc-claw, implement the user authentication system"
                  ↓
cc-claw:    [Goal Decomposition]
            ├── Research OAuth2 providers
            ├── Design JWT structure
            ├── Implement /auth/login
            ├── Implement /auth/logout
            ├── Write tests
            └── Write API docs
                  ↓
            [Autonomous Execution]
            ├── TaskQueue with priority
            ├── Retry on API errors
            ├── Persistent memory
            └── Checkpointing
                  ↓
You (10am): "what progress on auth?"
cc-claw:    "Done /auth/login, /logout, tests passing. Working on JWT refresh."
```

---

## Key Technical Decisions

### 1. Event-Driven Architecture

The daemon communicates via WebSocket with a central server:

```python
class WebSocketManager:
    async def connect(self):
        # Persistent connection, auto-reconnect
        while True:
            try:
                await self._connect()
                await self._listen()
            except Disconnected:
                await asyncio.sleep(5)  # Reconnect with backoff
```

### 2. Priority Task Queue

User tasks interrupt autonomous work, then resume:

```python
class TaskQueue:
    def enqueue(self, task, user_initiated=False):
        if user_initiated:
            self._queue.appendleft(task)  # Priority
        else:
            self._queue.append(task)      # Background
```

### 3. Rate Limit Handling

Claude API rate limits are brutal. cc-claw tracks token usage:

```python
class TokenBudget:
    def increment_backoff(self):
        self.backoff_level += 1
        wait = 60 * (2 ** (self.backoff_level - 1))
        return wait  # 1min, 2min, 4min, 8min...
```

### 4. Persistent Memory (New in 0.1.0)

Sessions can resume intelligently:

```python
memory = PersistentMemory()
memory.add_context_snapshot(
    task="Implement auth module",
    context="FastAPI + PostgreSQL",
    result="JWT complete"
)

# Next session
resume = memory.get_context_for_resume()
# "Last session: completed JWT auth. Remaining: password reset, OAuth2."
```

---

## Architecture Overview

```
┌─────────────────────────────────────────────────┐
│                 cc-claw Client                   │
│  ┌─────────┐  ┌─────────┐  ┌───────────────┐  │
│  │Daemon   │  │Message  │  │ Autonomous    │  │
│  │Loop     │←→│Handler  │←→│ Runner        │  │
│  └────┬────┘  └────┬────┘  └───────┬───────┘  │
│       │             │               │          │
│  ┌────▼────┐  ┌────▼────┐  ┌───────▼───────┐  │
│  │Scheduler│  │Profile  │  │ TaskQueue     │  │
│  │         │  │Manager  │  │               │  │
│  └─────────┘  └─────────┘  └───────────────┘  │
│                     ↑                          │
│  ┌─────────────────┴─────────────────────────┐│
│  │           Claude Executor                 ││
│  │  execute(prompt) → JSON + Usage          ││
│  └───────────────────────────────────────────┘│
└─────────────────────────────────────────────────┘
                    ↕ WebSocket
┌─────────────────────────────────────────────────┐
│              Central Server                     │
│  - Device registration                         │
│  - Message relay                                │
│  - Token budget sync                           │
└─────────────────────────────────────────────────┘
```

---

## Lessons Learned

### What Worked
- **Goal decomposition** — Breaking goals into tasks is essential for autonomous work
- **Priority queues** — User interrupts must take priority
- **Persistent memory** — Context survival between sessions is a game changer

### What Didn't Work (Initially)
- **Infinite loops** — Need circuit breakers and max iteration limits
- **Aggressive retry** — Exponential backoff is non-negotiable
- **No checkpointing** — Every task must be idempotent or checkpointable

### What Surprised Me
- The combination of goal decomposition + autonomous execution reduced my code review time by ~40%
- Users最喜欢的是 "我睡觉了，cc-claw 在干活" 这个场景
- Multi-agent collaboration opened up new possibilities I didn't anticipate

---

## What's Next

Current development focus:
1. **Semantic memory search** — Using embeddings for natural language recall
2. **Cross-instance collaboration** — Multiple cc-claw instances working together
3. **Web UI dashboard** — Visual task management

---

## Try It

```bash
pip install cc-claw
cc-claw pair  # Register device
cc-claw daemon  # Start autonomous runner

# Set a goal
cc-claw goal "implement user auth"
```

The daemon will decompose the goal, execute tasks autonomously, and notify you via WebSocket when milestones complete.

---

## Questions?

Happy to answer questions about the architecture, specific implementation details, or how to extend cc-claw for your use case.

GitHub: https://github.com/cc-claw/cc-claw
Docs: https://docs.cc-claw.dev