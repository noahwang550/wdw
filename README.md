# 🌸 Memory Screen - 记忆展示界面

Noah & Aerith 的记忆花园 - 一个美丽的记忆浏览和搜索界面

---

## 🚀 快速启动

### 方式 1：启动脚本
```bash
./start.sh
```

### 方式 2：手动启动
```bash
# 启动服务器
python3 server.py

# 在浏览器中打开
http://localhost:8000/app.html
```

---

## ✨ 功能特性

### 📊 记忆概览
- 显示所有记忆文件
- 实时统计（总数、分类、更新时间）
- 美观的卡片式布局

### 🔍 全文搜索
- 支持标题搜索
- 支持内容搜索
- 支持标签搜索
- 实时过滤结果

### 📖 详细阅读
- 点击卡片查看完整内容
- Markdown 格式渲染
- 优雅的阅读体验

### 🎨 美丽界面
- 渐变背景
- 响应式设计
- 流畅动画效果
- 移动端友好

---

## 📁 文件结构

```
memory-screen/
├── app.html          # 主界面（带完整功能）
├── index.html        # 静态版本（无 API）
├── server.py         # Python 服务器
├── start.sh          # 启动脚本
└── README.md         # 说明文档
```

---

## 🔌 API 接口

### GET /api/memories

返回所有记忆数据

**响应格式**：
```json
[
  {
    "file": "MEMORY.md",
    "title": "🌸 长期知识库",
    "date": "持续更新",
    "tags": ["核心方法论", "资源索引"],
    "preview": "核心认知与重要记忆的沉淀之地...",
    "content": "完整内容（前 5000 字符）"
  }
]
```

---

## 📊 统计信息

- **总记忆数**：显示所有记忆文件数量
- **日常记忆**：按日期分类的记忆数量
- **最后更新**：最新更新日期
- **维护者**：Aerith 🌸

---

## 🎯 使用场景

1. **回顾历史** - 浏览过往记忆
2. **快速查找** - 搜索特定内容
3. **知识管理** - 查看知识结构
4. **决策参考** - 回顾历史决策

---

## 🛠️ 技术栈

- **前端**：HTML5 + CSS3 + Vanilla JavaScript
- **后端**：Python 3 + http.server
- **样式**：自定义 CSS + 渐变设计
- **数据**：本地 Markdown 文件

---

## 📝 记忆来源

记忆文件来自：
- `/root/.openclaw/workspace-feishu-assistant/MEMORY.md`（长期记忆）
- `/root/.openclaw/workspace-feishu-assistant/memory/*.md`（日常记忆）

---

## 🌸 由 Aerith 设计

为 Noah 打造的个人记忆管理系统

**创建时间**: 2026-03-25
**版本**: 1.0
