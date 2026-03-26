# 🌸 记忆看板自动更新系统

自动化的每日记忆更新流程，将 `memory/` 目录中的记忆文件同步到 GitHub Pages 记忆看板。

---

## 📋 系统架构

```
memory/YYYY-MM-DD.md  ─┐
                       ├──> generate-memories.py ──> memories.json ──> Git Push ──> GitHub Pages
MEMORY.md             ─┘
```

---

## ⏰ 定时任务

**执行时间**: 每天 0:00 (Asia/Shanghai)

**配置文件**: `/root/.openclaw/workspace-feishu-assistant/crons/daily-memory-update.yaml`

**执行流程**:
1. 读取前一天的记忆文件 (`memory/YYYY-MM-DD.md`)
2. 调用 `generate-memories.py` 生成 `memories.json`
3. 自动 Git 提交并推送到 GitHub
4. GitHub Pages 自动部署更新
5. 发送执行结果通知到群聊

---

## 🛠️ 脚本说明

### update-daily.sh
主更新脚本，负责：
- 检查记忆文件是否存在
- 生成 memories.json
- Git 提交和推送
- 错误处理和日志输出

**使用方法**:
```bash
cd /root/.openclaw/workspace-feishu-assistant/memory-screen
./update-daily.sh
```

### generate-memories.py
Python 脚本，负责：
- 读取 `MEMORY.md` 和 `memory/*.md` 文件
- 提取预览文本和标签
- 生成结构化的 `memories.json`

**使用方法**:
```bash
python3 generate-memories.py
```

### send-feishu-notify.sh (备用)
飞书通知脚本，用于手动发送更新通知。

**使用方法**:
```bash
./send-feishu-notify.sh "更新内容" "成功"
```

---

## 📁 文件结构

```
memory-screen/
├── update-daily.sh          # 主更新脚本
├── generate-memories.py     # 数据生成脚本
├── send-feishu-notify.sh    # 通知脚本（备用）
├── memories.json            # 生成的数据文件
├── index.html               # GitHub Pages 静态页面
├── app.html                 # 本地服务器页面
├── server.py                # 本地服务器
└── README-AUTO-UPDATE.md    # 本文档
```

---

## 🔧 配置说明

### Cron 配置
```yaml
schedule: "0 0 * * *"        # 每天 0:00
timezone: "Asia/Shanghai"    # 时区
enabled: true                 # 启用
notify_on_failure: true       # 失败时通知
notify_on_success: true       # 成功时通知
timeout: 300                  # 超时 5 分钟
retry:
  max_attempts: 2             # 最多重试 2 次
  delay_seconds: 60           # 重试间隔 60 秒
```

### Git 配置
- **仓库**: `github.com/noahwang550/wdw`
- **分支**: `main`
- **提交用户**: `Aerith Bot <aerith@noah-memory.local>`

---

## 📊 监控与日志

### 查看执行日志
```bash
# 查看最新的更新日志
tail -f /root/.openclaw/workspace-feishu-assistant/memory-screen/update.log

# 查看 crons 执行记录
# (根据 OpenClaw 的 crons 系统日志位置)
```

### 检查更新状态
```bash
# 手动执行一次更新
cd /root/.openclaw/workspace-feishu-assistant/memory-screen
./update-daily.sh

# 检查 memories.json 是否更新
cat memories.json | jq '.[0].date'

# 检查 Git 状态
git status
git log --oneline -5
```

---

## ⚠️ 故障排查

### 问题 1: 记忆文件不存在
**现象**: 脚本提示 "未找到记忆文件"
**解决**: 检查 `memory/` 目录中是否有昨天的记忆文件

### 问题 2: Git 推送失败
**现象**: `git push` 失败
**解决**:
1. 检查 SSH key 配置
2. 检查仓库权限
3. 手动执行 `git push` 查看错误信息

### 问题 3: GitHub Pages 未更新
**现象**: 推送成功但网站未更新
**解决**:
1. 等待 1-2 分钟（GitHub Pages 部署延迟）
2. 清除浏览器缓存
3. 检查 GitHub Actions 部署状态

---

## 🎯 最佳实践

### 记忆文件规范
- 使用标准格式：`YYYY-MM-DD.md`
- 内容结构清晰，便于提取预览
- 包含关键词便于标签分类

### 定期维护
- 每周检查一次更新日志
- 每月清理一次过期的记忆文件
- 每季度回顾并优化生成脚本

---

## 📝 更新记录

| 日期 | 版本 | 更新内容 |
|------|------|----------|
| 2026-03-26 | 1.0 | 初始版本，实现自动化更新流程 |

---

**维护者**: Aerith 🌸
**最后更新**: 2026-03-26
