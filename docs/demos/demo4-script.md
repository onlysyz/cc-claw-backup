# Demo 4: "Build a REST API in One Hour with CC-Claw"

## Video Specs
- **Title**: 用 CC-Claw 一小时开发完整的 REST API（附源码）
- **Duration**: 10-15 minutes
- **Platform**: YouTube/Bilibili
- **Hook**: "Claude Code 通宵干活，我在睡觉"

---

## Scene 1: Intro (0:00-1:00)

**Visual**: Developer at desk, clock showing 6 PM

**Script**:
> "今天下午 6 点，我给 CC-Claw 设置了一个目标：一小时后醒来，我要一个完整的用户认证 REST API。"

**Show**:
```bash
cc-claw goal "实现用户认证 REST API，包含注册、登录、JWT、密码重置"
```

> "让我们看看 CC-Claw 是怎么工作的..."

---

## Scene 2: CC-Claw Decomposition (1:00-2:30)

**Visual**: Terminal showing goal decomposition

**Script**:
> "CC-Claw 首先分析目标，然后分解成具体的任务"

**Terminal**:
```
[CC-CLAW] 🎯 New goal: 实现用户认证 REST API
[CC-CLAW] 📋 Decomposing goal into tasks...

[CC-CLAW] Task 1/12: Design database schema for users
[CC-CLAW] Task 2/12: Create FastAPI project structure
[CC-CLAW] Task 3/12: Implement password hashing
[CC-CLAW] Task 4/12: Create /auth/register endpoint
[CC-CLAW] Task 5/12: Create /auth/login endpoint with JWT
...
[CC-CLAW] Task 12/12: Write API documentation

[CC-CLAW] 🚀 Starting autonomous execution...
```

---

## Scene 3: Show Execution (2:30-8:00)

**Visual**: Split screen - left shows CC-Claw working, right shows clock/time-lapse

**Script**:
> "看看 CC-Claw 是怎么执行任务的"

**Time-lapse recording suggestions**:
- Use OBS + TimeSpeed plugin for accelerated view
- Or pre-record and edit with 10x speed

**Show these task completions** (selective):

### Task 1: Database Schema
```
[CC-CLAW] 🔧 Executing: Design database schema for users
[CC-CLAW] ✅ Completed (2m 34s)
[CC-CLAW] 📊 Tokens used: 2,340
[CC-CLAW] 📝 Result: Created users table with email, password_hash, created_at
```

### Task 4: Registration Endpoint
```
[CC-CLAW] 🔧 Executing: Create /auth/register endpoint
[CC-CLAW] ✅ Completed (4m 12s)
[CC-CLAW] 📊 Tokens used: 3,890
[CC-CLAW] 📝 Result: POST /auth/register with email validation
```

### Task 5: Login Endpoint
```
[CC-CLAW] 🔧 Executing: Create /auth/login endpoint with JWT
[CC-CLAW] ✅ Completed (5m 01s)
[CC-CLAW] 📊 Tokens used: 4,210
[CC-CLAW] 📝 Result: POST /auth/login returning access + refresh tokens
```

### Show Error Recovery
```
[CC-CLAW] ⚠️ Warning: Rate limit detected (429)
[CC-CLAW] ⏳ Backing off for 60s...
[CC-CLAW] 🔄 Retrying...
[CC-CLAW] ✅ Task completed after retry
```

---

## Scene 4: Progress Check (8:00-9:30)

**Visual**: Developer wakes up, checks phone

**Script**:
> "第二天早上 7 点，我收到 CC-Claw 的进度通知"

**Telegram/Discord notification**:
```
🔔 CC-Claw Goal Update

🎯 Goal: 用户认证 REST API
📊 Progress: 10/12 tasks (83%)
⏳ Remaining:
  - Password reset flow
  - API documentation

✅ Completed:
  - Database schema
  - User registration
  - JWT authentication
  - Login/logout
  - Password hashing

💬 "核心功能已完成，还剩2个任务"
```

---

## Scene 5: Final Result (9:30-11:00)

**Visual**: Show the actual code created

**Script**:
> "看看 CC-Claw 生成的代码质量"

**Show file structure**:
```bash
auth-api/
├── app/
│   ├── __init__.py
│   ├── main.py           # FastAPI app
│   ├── models/
│   │   ├── __init__.py
│   │   └── user.py       # Pydantic models
│   ├── routers/
│   │   ├── __init__.py
│   │   └── auth.py      # Auth endpoints
│   ├── services/
│   │   ├── __init__.py
│   │   └── jwt.py       # JWT service
│   └── db/
│       ├── __init__.py
│       └── database.py   # DB connection
├── tests/
│   ├── __init__.py
│   ├── test_auth.py
│   └── test_users.py
├── requirements.txt
├── README.md
└── docker-compose.yml
```

**Show key code**:
```python
# auth.py
@router.post("/register")
async def register(user: UserRegister):
    # Hash password
    hashed = hash_password(user.password)
    # Save to DB
    db_user = await db.create_user(user.email, hashed)
    # Generate token
    token = create_access_token(db_user.id)
    return {"user": db_user, "token": token}
```

---

## Scene 6: Run Tests (11:00-12:00)

**Script**:
> "跑一下测试，看看代码质量"

```bash
pytest tests/ -v

# Expected output:
# test_register_success PASSED
# test_register_duplicate_email PASSED
# test_login_success PASSED
# test_login_invalid_password PASSED
# test_jwt_expiration PASSED

# ===================== 15 passed in 2.34s =====================
```

---

## Scene 7: API Documentation (12:00-13:00)

**Script**:
> "最后，API 文档也自动生成了"

```bash
# Start the API
uvicorn app.main:app --reload

# Open browser to http://localhost:8000/docs
# Show Swagger UI with all endpoints
```

---

## Scene 8: Summary (13:00-14:00)

**Script**:
> "总结一下这次实验"

```
┌─────────────────────────────────────────┐
│           CC-Claw 实验结果               │
├─────────────────────────────────────────┤
│  🎯 任务数: 12                          │
│  ✅ 完成数: 12                          │
│  ⏱️ 实际耗时: 45 分钟                   │
│  💰 Token 消耗: 45,230                 │
│  💵 成本: $0.90                        │
│  📝 代码行数: 1,234                     │
│  ✅ 测试通过: 15/15                     │
│  📖 文档: 自动生成                      │
└─────────────────────────────────────────┘
```

---

## Scene 9: CTA (14:00-15:00)

**Visual**: GitHub repo animation

**Script**:
> "想自己试试？去 GitHub 给我一个 Star！"

```
🔗 github.com/onlysyz/cc-claw
⭐ Star the project
📖 docs.cc-claw.dev
🎥 完整视频+源码
```

---

## YouTube SEO

**Title**: (10-15分钟) 用 CC-Claw 一小时开发完整的 REST API（附源码）

**Tags**:
```
CC-Claw, Claude Code, REST API, FastAPI, Python,
AI编程, 自动开发, 程序员, 编程教程, 开发效率
```

**Description**:
```markdown
CC-Claw 一小时开发 REST API 完整记录

⏱️ 时间戳：
0:00 项目介绍
1:00 目标分解
2:30 自主执行过程
8:00 进度检查
9:30 代码质量展示
11:00 测试运行
12:00 API 文档
13:00 总结

📦 完整源码：
https://github.com/onlysyz/cc-claw

🔧 技术栈：
- FastAPI
- PostgreSQL
- JWT
- Docker

#CC-Claw #FastAPI #Python #AI编程
```

---

## Bilibili 简介

```
CC-Claw 实验：一小时开发完整 REST API

用 CC-Claw 设置目标后睡觉
早上醒来，API 已经开发完成

包含：
✅ 数据库设计
✅ 用户注册登录
✅ JWT 认证
✅ 单元测试
✅ API 文档

附完整源码！
```