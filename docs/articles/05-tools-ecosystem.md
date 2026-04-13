# cc-claw 工具生态：12 个内置工具让 AI Agent 如虎添翼

> 作者：cc-claw Team
> 首发：知乎
> 标签：AI Agent, 效率工具, Claude Code

## 前言

Claude Code 本身只能执行代码和返回文本。但真正的 AI Agent 需要与真实世界交互——读文件、操作数据库、调用 API、监控系统。

**cc-claw 内置了 12 个强大的工具类，覆盖了 Agent 开发的方方面面。**

---

## 工具全景图

```
cc-claw Tools
├── FileProcessor      文件处理（读/写/搜索）
├── DataScraper        网页爬取
├── ApiClient          HTTP API 调用
├── ProcessManager     进程管理
├── SystemInfo         系统信息
├── GitHelper          Git 操作
├── DockerHelper       Docker 容器
├── DatabaseTool       SQL 数据库
├── ImageTool          图片处理
├── NotificationTool   通知推送
├── CodeAnalysisTool   代码分析
└── MonitorTool        监控告警
```

---

## 1. FileProcessor：文件处理的瑞士军刀

```python
from cc_claw.tools import FileProcessor

# 读取文件
content = FileProcessor.read("/path/to/file.py")

# 搜索文件内容
results = FileProcessor.search(
    pattern="TODO",
    path=".",
    file_type="py"
)
# 返回: [{'file': 'main.py', 'line': 42, 'content': '# TODO: fix bug'}]

# 统计代码行数
count = FileProcessor.count_lines("/path/to/file.py")

# 查找文件
files = FileProcessor.find("*.json", path=".", recursive=True)
```

---

## 2. DataScraper：轻量级爬虫

```python
from cc_claw.tools import DataScraper

# 获取网页
result = DataScraper.fetch("https://api.github.com/users")
print(result['status'])  # 200
print(result['content'][:200])

# 提取邮箱
emails = DataScraper.extract_emails(text)
# ['user@example.com', 'admin@example.com']

# 提取链接
links = DataScraper.extract_links(html_content, base_url="https://example.com")
```

---

## 3. ApiClient：带认证的 HTTP 客户端

```python
from cc_claw.tools import ApiClient

# 基础 GET
result = ApiClient.call(
    url="https://api.github.com/repos/claude-code",
    method="GET"
)

# 带认证
result = ApiClient.call_with_auth(
    url="https://api.github.com/user/repos",
    token="ghp_xxxxx",
    method="GET"
)
```

---

## 4. DatabaseTool：SQLite 直接操作

```python
from cc_claw.tools import DatabaseTool

# 查询
results = DatabaseTool.query(
    db_path="./data.db",
    sql="SELECT * FROM users WHERE active=1 LIMIT 10"
)

# 执行（INSERT/UPDATE/DELETE）
DatabaseTool.execute(
    db_path="./data.db",
    sql="UPDATE users SET last_login=NOW() WHERE id=1"
)

# 获取表结构
schema = DatabaseTool.table_info(db_path, table="users")
```

---

## 5. MonitorTool：健康检查与告警

```python
from cc_claw.tools import MonitorTool

# 检查磁盘
disk = MonitorTool.check_disk(threshold=90)
if disk['alert']:
    print(f"⚠️ 磁盘使用率 {disk['percent']}% 超过阈值")

# 检查内存
mem = MonitorTool.check_memory(threshold=85)

# 检查 URL 可达性
health = MonitorTool.check_url("https://api.example.com/health")

# 综合健康检查
full_check = MonitorTool.health_check(port=3000)
```

---

## 6. NotificationTool：多渠道通知

```python
from cc_claw.tools import NotificationTool

# 邮件通知
NotificationTool.send_email(
    to="user@example.com",
    subject="任务完成",
    body="用户认证模块已实现完成"
)

# 本地通知（Linux/macOS）
NotificationTool.push(
    title="CC-Claw",
    body="Goal completed!",
    priority="high"
)

# Slack Webhook
NotificationTool.slack_webhook(
    webhook_url="https://hooks.slack.com/...",
    text="Deploy completed! 🚀"
)
```

---

## 7. GitHelper：Git 操作简化

```python
from cc_claw.tools import GitHelper

# 查看状态
status = GitHelper.status()
# "M  modified.py\n?? newfile.py"

# 查看变更
diff = GitHelper.diff(file="main.py")

# 查看提交历史
commits = GitHelper.log(limit=5)
# [{'hash': 'abc123', 'message': 'feat: add auth', ...}]

# 当前分支
branch = GitHelper.branch()
```

---

## 8. DockerHelper：容器管理

```python
from cc_claw.tools import DockerHelper

# 查看运行中的容器
containers = DockerHelper.ps(all=False)

# 查看日志
logs = DockerHelper.logs("container_name", lines=100)

# 重启容器
DockerHelper.restart("container_name")

# 查看资源使用
status = DockerHelper.status()
```

---

## 9. CodeAnalysisTool：代码质量分析

```python
from cc_claw.tools import CodeAnalysisTool

# 统计代码行数
loc = CodeAnalysisTool.count_lines(
    path=".",
    extensions="py,js,ts"
)
# {'total': 5420, 'by_language': {'py': 2300, 'js': 3120}}

# 查找函数定义
functions = CodeAnalysisTool.find_functions(
    path=".",
    language="python"
)

# 估算复杂度
complexity = CodeAnalysisTool.complexity(path=".", language="python")

# 分析依赖
deps = CodeAnalysisTool.dependencies(path=".")
```

---

## 10. SystemInfo：系统资源

```python
from cc_claw.tools import SystemInfo

# 磁盘使用
disk = SystemInfo.disk_usage("/")

# 内存信息
mem = SystemInfo.memory()

# CPU 负载
cpu = SystemInfo.cpu_load()
# {'1min': 2.5, '5min': 1.8, '15min': 1.2}
```

---

## 11. ProcessManager：进程控制

```python
from cc_claw.tools import ProcessManager

# 查找进程
processes = ProcessManager.list(pattern="python")

# 检查进程是否运行
is_running = ProcessManager.is_running("redis-server")

# 杀死进程
ProcessManager.kill(pid=12345, signal=15)
```

---

## 12. ImageTool：图片处理

```python
from cc_claw.tools import ImageTool

# 获取图片信息
info = ImageTool.info("photo.jpg")
# {'width': 1920, 'height': 1080, 'format': 'JPEG'}

# 生成缩略图
ImageTool.thumbnail("photo.jpg", "thumb.jpg", max_size=256)

# 转换格式
ImageTool.convert("photo.png", "photo.webp", format="WEBP")

# 压缩
ImageTool.compress("photo.jpg", "photo_compressed.jpg", quality=85)
```

---

## 工具注册表

cc-claw 提供了统一的工具获取接口：

```python
from cc_claw.tools import get_tool

# 按名称获取工具
file_tool = get_tool("file")
scraper = get_tool("scraper")

# get_tool 返回工具类，可调用其静态方法
results = FileProcessor.search("pattern", path=".")
```

---

## 扩展自定义工具

在 `tools.py` 中添加新工具只需：

```python
class MyCustomTool:
    @staticmethod
    def my_operation(param: str) -> str:
        """自定义工具操作"""
        return f"处理: {param}"

# 注册到工具表
TOOLS['mytool'] = MyCustomTool
```

---

## 实际应用场景

### 场景 1：CI/CD 自动化
```
MonitorTool.check_disk() → 磁盘不足? → NotificationTool.push("告警!")
```

### 场景 2：代码审查
```
GitHelper.diff() → CodeAnalysisTool.complexity() → 生成审查报告
```

### 场景 3：数据采集管道
```
DataScraper.fetch() → DatabaseTool.execute() → MonitorTool.check_url()
```

### 场景 4：部署监控
```
DockerHelper.ps() → MonitorTool.health_check() → NotificationTool.slack_webhook()
```

---

## 总结

cc-claw 的 12 个内置工具覆盖了 Agent 开发的常见场景：

| 工具 | 能力 | 适用场景 |
|------|------|----------|
| FileProcessor | 文件读写搜索 | 代码修改、日志分析 |
| DataScraper | 网页爬取 | 数据采集、竞品分析 |
| ApiClient | HTTP 调用 | 第三方 API 集成 |
| DatabaseTool | SQLite 操作 | 本地数据存储 |
| MonitorTool | 健康检查 | 运维监控 |
| NotificationTool | 多渠道通知 | 重要事件告警 |
| GitHelper | Git 操作 | 代码版本管理 |
| DockerHelper | 容器管理 | 部署运维 |
| CodeAnalysisTool | 代码分析 | 代码质量保障 |
| SystemInfo | 系统信息 | 资源管理 |
| ProcessManager | 进程控制 | 服务管理 |
| ImageTool | 图片处理 | 媒体处理 |

**工具生态让 cc-claw 不只是"会说话"的 AI，而是真正能做事、能落地的智能 Agent。**

---

**相关资源：**
- GitHub: https://github.com/cc-claw/cc-claw
- 文档: https://docs.cc-claw.dev/tools

需要什么工具？评论区告诉我，也许下个版本就有！