#!/bin/bash
# 每日记忆看板自动更新脚本
# 执行时间：每天 0:00
# 功能：读取前一天的记忆文件，生成 memories.json，推送到 GitHub Pages

set -e

# 配置
WORKSPACE="/root/.openclaw/workspace-feishu-assistant"
MEMORY_SCREEN_DIR="${WORKSPACE}/memory-screen"
MEMORY_DIR="${WORKSPACE}/memory"
GROUP_CHAT_ID="oc_38ec57abca24e1caf76e3bb8e9b4261d"

echo "🌸 记忆看板更新任务启动"
echo "时间：$(date '+%Y-%m-%d %H:%M:%S')"
echo ""

# 获取昨天的日期
YESTERDAY=$(date -d "yesterday" +%Y-%m-%d)
MEMORY_FILE="${MEMORY_DIR}/${YESTERDAY}.md"

echo "📅 目标日期：${YESTERDAY}"
echo "📁 记忆文件：${MEMORY_FILE}"
echo ""

# 检查记忆文件是否存在
if [ ! -f "${MEMORY_FILE}" ]; then
    echo "⚠️ 未找到记忆文件：${MEMORY_FILE}"
    echo "💬 发送通知到群聊（无记忆文件）..."
    # crons 系统会自动处理通知
    echo "跳过今日更新"
    exit 0
fi

# 检查记忆文件是否有内容
if [ ! -s "${MEMORY_FILE}" ]; then
    echo "⚠️ 记忆文件为空：${MEMORY_FILE}"
    echo "跳过今日更新"
    exit 0
fi

echo "✅ 记忆文件存在且有内容"
echo ""

# 进入 memory-screen 目录
cd "${MEMORY_SCREEN_DIR}"

# 生成 memories.json
echo "📖 生成 memories.json..."
python3 generate-memories.py
echo ""

# 检查 Git 状态
echo "🔍 检查 Git 状态..."
git status

# 如果有变更，提交并推送
if ! git diff --quiet || ! git diff --cached --quiet; then
    echo ""
    echo "📝 检测到变更，准备提交..."
    
    # 配置 Git 用户
    git config user.name "Aerith Bot"
    git config user.email "aerith@noah-memory.local"
    
    # 添加变更
    git add memories.json
    
    # 提交
    git commit -m "🌸 每日记忆更新 - ${YESTERDAY}
    
自动更新记忆看板
- 更新日期：${YESTERDAY}
- 更新内容：记忆日志
- 更新时间：$(date '+%Y-%m-%d %H:%M:%S')"
    
    # 推送
    echo ""
    echo "🚀 推送到 GitHub..."
    git push origin main
    
    echo ""
    echo "✅ 记忆看板更新完成！"
    echo "🌐 访问：https://noahwang550.github.io/wdw/"
    echo ""
    
else
    echo ""
    echo "✅ 无变更，memories.json 已是最新"
    echo ""
fi

echo "🌸 记忆看板更新任务完成"
echo "完成时间：$(date '+%Y-%m-%d %H:%M:%S')"
