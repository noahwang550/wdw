#!/bin/bash
# 手动触发 GitHub Pages 部署

REPO="noahwang550/wdw"
TOKEN=""

echo "🌸 检查 GitHub Pages 状态..."

# 检查仓库是否存在
curl -s "https://github.com/$REPO" | grep -q "404" && echo "❌ 仓库不存在" && exit 1

echo "✅ 仓库存在"
echo ""
echo "📋 请在 GitHub 上手动启用 Pages："
echo ""
echo "1. 打开：https://github.com/$REPO/settings/pages"
echo ""
echo "2. 在 'Source' 下选择："
echo "   - Deploy from a branch"
echo "   - Branch: main"
echo "   - Folder: / (root)"
echo ""
echo "3. 点击 'Save'"
echo ""
echo "4. 等待 1-2 分钟，页面将部署完成"
echo ""
echo "部署完成后访问："
echo "https://noahwang550.github.io/wdw/"
echo ""
