#!/bin/bash
# Memory Screen 启动脚本

echo "🌸 启动 Memory Screen..."
echo ""

cd /root/.openclaw/workspace-feishu-assistant/memory-screen

# 启动服务器
python3 server.py &

# 等待服务器启动
sleep 2

# 打开浏览器
if command -v xdg-open &> /dev/null; then
    xdg-open http://localhost:8000/app.html
elif command -v open &> /dev/null; then
    open http://localhost:8000/app.html
else
    echo "请在浏览器中打开：http://localhost:8000/app.html"
fi

echo ""
echo "✅ Memory Screen 已启动！"
echo "📊 API: http://localhost:8000/api/memories"
echo "🌸 界面：http://localhost:8000/app.html"
echo ""
echo "按 Ctrl+C 停止服务器"
