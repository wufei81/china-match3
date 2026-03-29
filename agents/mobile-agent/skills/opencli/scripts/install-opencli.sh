#!/bin/bash
# opencli 安装脚本
# 用法：bash install-opencli.sh

set -e

echo "🚀 开始安装 opencli..."

# 检查 Node.js
if ! command -v node &> /dev/null; then
    echo "❌ 未检测到 Node.js，请先安装 Node.js"
    exit 1
fi

echo "✅ Node.js 版本：$(node -v)"

# 安装 opencli
echo "📦 安装 @jackwener/opencli..."
npm install -g @jackwener/opencli

# 验证安装
echo "🔍 验证安装..."
opencli --version

# 下载 Browser Bridge 扩展
echo "📥 下载 Browser Bridge 扩展..."
EXTENSION_DIR="$HOME/opencli-browser-bridge"

if [ -d "$EXTENSION_DIR" ]; then
    echo "ℹ️  扩展已存在：$EXTENSION_DIR"
else
    cd /tmp
    curl -sLO https://github.com/jackwener/opencli/releases/download/v1.5.5/opencli-extension.zip
    unzip -o opencli-extension.zip -d opencli-extension
    mv opencli-extension "$EXTENSION_DIR"
    echo "✅ 扩展已下载到：$EXTENSION_DIR"
fi

# 显示安装说明
echo ""
echo "=========================================="
echo "✅ opencli 安装完成！"
echo "=========================================="
echo ""
echo "📌 下一步：安装 Chrome 扩展"
echo ""
echo "1. 打开 Chrome 扩展页面："
echo "   chrome://extensions/"
echo ""
echo "2. 启用右上角的「开发者模式」"
echo ""
echo "3. 点击「加载已解压的扩展程序」"
echo "4. 选择目录：$EXTENSION_DIR"
echo ""
echo "5. 验证安装："
echo "   opencli doctor"
echo ""
echo "📚 常用命令："
echo "   opencli list              # 查看所有命令"
echo "   opencli zhihu hot         # 知乎热榜"
echo "   opencli bilibili hot      # B 站热门"
echo "   opencli weibo hot         # 微博热搜"
echo ""
