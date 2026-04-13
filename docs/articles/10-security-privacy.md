# CC-Claw 安全与隐私：你的代码到底安全吗？

> 作者：cc-claw Team
> 首发：知乎
> 标签：安全, 隐私, AI Agent, Claude Code

## 前言

"让 AI 在我电脑上执行代码" — 这听起来有点可怕？本文详解 CC-Claw 的安全机制，让你安心使用。

---

## 核心安全原则

CC-Claw 遵循 **"代码不离开你的机器"** 原则：

```
传统 AI 服务:
你的代码 → 发送给 AI 公司服务器 → AI 处理 → 返回结果
                    ↑
            你的代码在这里！

CC-Claw:
你的代码 → 本地 Claude CLI → 本地执行 → 只发送 Prompt
                              ↑
                      代码从未离开你的电脑
```

---

## 本地执行架构

### Claude Code 执行原理

```python
class ClaudeExecutor:
    def __init__(self, config: ClientConfig):
        self.claude_path = config.claude_path

    async def execute(self, prompt: str) -> tuple:
        """执行 Claude 命令"""
        cmd = [
            self.claude_path,
            "--print",
            "--output-format", "json",
            "--prompt", prompt
        ]

        # 命令在本地执行
        process = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )

        stdout, stderr = await process.communicate()

        # 只有 Prompt 发送给 Anthropic
        # 你的代码文件从不离开本地
```

### 数据流

```
┌─────────────────────────────────────────────────────────────┐
│                        你的电脑                              │
│                                                             │
│   ┌─────────────┐    Prompt     ┌──────────────┐          │
│   │  CC-Claw   │ ──────────────→ │  Claude CLI  │          │
│   │  (本地)     │ ←────────────── │  (本地)      │          │
│   └─────────────┘   JSON 响应   └──────┬───────┘          │
│          ↑                               │                   │
│          │                               ▼                   │
│          │                        ┌──────────────┐          │
│          │                        │ Anthropic    │          │
│          │                        │ Cloud API     │          │
│          │                        │ (只有 Prompt) │          │
│          │                        └──────────────┘          │
│          │                               │                   │
│   ┌──────┴───────┐                       │                   │
│   │  执行结果     │ ←──────────────────────┘                   │
│   │  (代码输出)   │                                         │
│   └───────────────┘                                         │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 权限控制

### Claude Code 权限模式

Claude Code 有三种权限级别：

| 模式 | 描述 | 安全性 |
|------|------|--------|
| `default` | 执行敏感操作前询问 | 🛡️ 最高 |
| `bypassPermissions` | 跳过所有确认 | ⚠️ 需信任 |
| `acceptAllowedExtensions` | 只允许已批准扩展 | 🛡️ 高 |

### CC-Claw 配置

```bash
# 安装时选择权限模式
cc-claw setup

# 或手动配置
cc-claw config --set permission_mode=bypassPermissions
```

### 推荐配置

```python
# 开发环境
permission_mode = "default"  # 每次都确认

# 自动化环境
permission_mode = "bypassPermissions"  # 完全自动

# 半自动
permission_mode = "acceptAllowedExtensions"  # 扩展需确认
```

---

## 敏感信息处理

### 1. 环境变量保护

```python
class SensitiveConfig:
    """敏感配置处理"""
    SENSITIVE_KEYS = [
        "api_key",
        "password",
        "secret",
        "token",
        "private_key"
    ]

    def should_mask(self, key: str, value: str) -> bool:
        """判断是否应该掩码"""
        key_lower = key.lower()
        return any(s in key_lower for s in self.SENSITIVE_KEYS)

    def mask_value(self, value: str) -> str:
        """掩码处理"""
        if len(value) <= 8:
            return "***"
        return value[:4] + "***" + value[-4:]
```

### 2. 日志脱敏

```python
class SafeLogger:
    """安全日志记录"""
    def __init__(self):
        self.sensitive = SensitiveConfig()

    def log(self, message: str):
        """脱敏后记录"""
        # 掩码敏感信息
        for key in self.sensitive.SENSITIVE_KEYS:
            pattern = rf'{key}=["\']?([^"\'\s]+)["\']?'
            message = re.sub(
                pattern,
                f'{key}={self.sensitive.mask_value(r"\\1")}',
                message,
                flags=re.IGNORECASE
            )
        logger.info(message)
```

### 3. 文件访问控制

```python
class FileAccessControl:
    """文件访问白名单"""
    ALLOWED_PATHS = [
        os.path.expanduser("~/projects"),
        "/tmp/cc-claw",
    ]

    DENIED_PATHS = [
        os.path.expanduser("~/.ssh"),
        "/etc/passwd",
        os.path.expanduser("~/.aws"),
    ]

    def can_access(self, path: str) -> bool:
        """检查文件是否可访问"""
        abs_path = os.path.abspath(path)

        # 检查是否在白名单目录
        for allowed in self.ALLOWED_PATHS:
            if abs_path.startswith(os.path.abspath(allowed)):
                return True

        # 检查是否在黑名单
        for denied in self.DENIED_PATHS:
            if abs_path.startswith(os.path.abspath(denied)):
                return False

        # 默认拒绝
        return False
```

---

## 网络安全

### 1. WebSocket 连接加密

```python
class WebSocketManager:
    async def connect(self):
        # 使用 WSS (WebSocket Secure)
        self.ws = await websockets.connect(
            self.config.ws_url,
            ssl=ssl.create_default_context()  # TLS 加密
        )
```

### 2. Token 传输

```python
# Token 只用于身份验证，不用于存储
DEVICE_TOKEN_HASH = hashlib.sha256(device_token.encode()).hexdigest()

# 服务器验证
def verify_token(token_hash: str) -> bool:
    return token_hash in valid_hashes
```

### 3. 本地数据加密

```python
from cryptography.fernet import Fernet

class EncryptedStorage:
    def __init__(self, key_path: str):
        with open(key_path, 'rb') as f:
            self.key = f.read()
        self.cipher = Fernet(self.key)

    def save(self, data: dict, path: str):
        """加密保存"""
        json_data = json.dumps(data)
        encrypted = self.cipher.encrypt(json_data.encode())

        with open(path, 'wb') as f:
            f.write(encrypted)

    def load(self, path: str) -> dict:
        """解密加载"""
        with open(path, 'rb') as f:
            encrypted = f.read()

        json_data = self.cipher.decrypt(encrypted)
        return json.loads(json_data)
```

---

## 审计日志

### 操作审计

```python
class AuditLogger:
    def log_action(self, action: str, details: dict):
        """记录操作审计日志"""
        entry = {
            "timestamp": datetime.now().isoformat(),
            "action": action,
            "details": self._sanitize(details),
            "user": os.getenv("USER"),
            "host": platform.node(),
        }

        # 写入审计日志（不可删除）
        with open("/var/log/cc-claw/audit.log", "a") as f:
            f.write(json.dumps(entry) + "\n")
```

### 记录的操作类型

```python
AUDIT_ACTIONS = [
    "task_started",
    "task_completed",
    "task_failed",
    "file_created",
    "file_modified",
    "command_executed",
    "config_changed",
    "permission_bypass",
]
```

---

## 安全配置检查清单

```python
class SecurityChecklist:
    """部署前安全检查"""
    checks = [
        ("permission_mode", "Use 'default' or 'acceptAllowedExtensions'"),
        ("logs_directory", "Ensure logs are not world-readable"),
        ("device_token", "Use strong random token (32+ chars)"),
        ("ssl_enabled", "WebSocket must use WSS"),
        ("firewall", "Only allow必要端口"),
    ]

    def run(self) -> dict:
        results = {}
        for check, description in self.checks:
            status = self._check_config(check)
            results[check] = {
                "status": "✅ PASS" if status else "❌ FAIL",
                "description": description
            }
        return results
```

---

## 隐私保护

### 数据收集政策

| 数据 | 是否收集 | 用途 |
|------|---------|------|
| 代码内容 | ❌ 否 | — |
| API 响应 | ⚠️ 可选 | Token 统计 |
| 任务描述 | ⚠️ 最小化 | 进度显示 |
| 使用统计 | ✅ 匿名 | 产品改进 |
| 崩溃日志 | ✅ 匿名 | Bug 修复 |

### 关闭所有遥测

```python
# 完全离线运行
config = ClientConfig(
    server_api_url=None,  # 不连接任何服务器
    server_ws_url=None,
)

# CC-Claw 完全在本地运行
# 无遥测，无上传
```

---

## 常见安全问题及解决方案

### Q1: CC-Claw 会偷我的代码吗？

**不会。**
- 代码只在本地 Claude CLI 中处理
- Anthropic 服务器只收到你的 Prompt（不含文件内容）
- CC-Claw 不会上传代码到任何地方

### Q2: 如何防止误操作删除文件？

```python
# 启用回收站模式
class SafeFileOperation:
    def delete(self, path: str):
        # 不直接删除，移动到回收站
        trash_dir = Path.home() / ".cc-claw" / "trash"
        trash_dir.mkdir(exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        dest = trash_dir / f"{timestamp}_{Path(path).name}"

        shutil.move(path, dest)
```

### Q3: 如何限制 CC-Claw 的操作范围？

```python
# 只允许在项目目录操作
config = ClientConfig(
    allowed_paths=["~/projects", "~/workspace"],
    denied_paths=["~/.ssh", "/etc", "~/.aws"],
)

# 超出范围的访问被拒绝
```

---

## 安全配置示例

### 开发环境

```python
config = ClientConfig(
    permission_mode="default",  # 每次确认
    allowed_paths=["~/projects/test"],
    enable_audit=True,
    enable_encryption=False,
)
```

### 生产环境

```python
config = ClientConfig(
    permission_mode="acceptAllowedExtensions",
    allowed_paths=["/opt/app"],
    denied_paths=["~/.ssh", "/etc", "~/.aws"],
    enable_audit=True,
    enable_encryption=True,
    encryption_key="/etc/cc-claw/key",
)
```

### 完全隔离环境

```python
config = ClientConfig(
    server_api_url=None,  # 不联网
    server_ws_url=None,
    permission_mode="default",
    # 所有操作在本地
)
```

---

## 最佳实践

1. **使用最小权限** — 只授权必要的操作
2. **开启审计日志** — 记录所有敏感操作
3. **定期备份** — 防止误删
4. **使用白名单** — 只允许访问特定目录
5. **监控异常** — 检查异常行为

---

## 总结

CC-Claw 的安全设计：

| 方面 | 保护措施 |
|------|----------|
| **代码安全** | 本地执行，不上传 |
| **传输安全** | TLS 加密 |
| **存储安全** | 可选加密 |
| **访问控制** | 路径白名单 |
| **审计追踪** | 操作日志 |

**你的代码，你做主。**

---

**相关链接：**
- 安全白皮书: [链接]
- 漏洞报告: security@cc-claw.dev
- 文档: https://docs.cc-claw.dev/security

有安全问题？欢迎联系！🔒