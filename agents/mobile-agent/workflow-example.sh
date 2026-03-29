#!/bin/bash
# opencli + PinchTab 集成工作流示例
# 用法：bash workflow-example.sh

set -e

echo "🚀 opencli + PinchTab 集成工作流示例"
echo "===================================="
echo ""

# 工作流 1：信息收集 + 网页交互
echo "📋 工作流 1: 收集新闻 + 网页分析"
echo "--------------------------------"

echo ""
echo "步骤 1: 使用 opencli 获取 36 氪新闻..."
opencli 36kr news -f json 2>/dev/null | jq -r '.[0:3] | .[] | "  - \(.title)"' || echo "  (获取新闻)"

echo ""
echo "步骤 2: 使用 PinchTab 导航到 36 氪..."
pinchtab nav https://36kr.com 2>/dev/null | jq -r '"  导航到：\(.url)"' || echo "  导航到 36 氪"

echo ""
echo "步骤 3: 获取页面结构..."
pinchtab snap -c 2>/dev/null | jq -r '"  页面节点数：\(.count)"' || echo "  获取页面结构"

echo ""
echo "✅ 工作流 1 完成"
echo ""

# 工作流 2：技术趋势分析
echo "📊 工作流 2: 技术趋势分析"
echo "------------------------"

echo ""
echo "步骤 1: 获取 HackerNews 热门..."
opencli hackernews top 2>/dev/null | head -5 || echo "  获取 HackerNews"

echo ""
echo "步骤 2: 获取 V2EX 最新话题..."
opencli v2ex latest 2>/dev/null | head -5 || echo "  (需要登录)"

echo ""
echo "步骤 3: 使用 PinchTab 访问 GitHub..."
pinchtab quick https://github.com/trending 2>/dev/null | head -10 || echo "  访问 GitHub Trending"

echo ""
echo "✅ 工作流 2 完成"
echo ""

# 工作流 3：内容创作辅助
echo "✍️  工作流 3: 内容创作辅助"
echo "------------------------"

echo ""
echo "步骤 1: 搜索小红书笔记..."
opencli xiaohongshu search "AI 工具" 2>/dev/null | head -5 || echo "  (需要登录)"

echo ""
echo "步骤 2: 搜索知乎话题..."
opencli zhihu search "人工智能" 2>/dev/null | head -5 || echo "  (需要登录)"

echo ""
echo "步骤 3: 使用 PinchTab 导航到写作平台..."
pinchtab nav https://example.com 2>/dev/null | jq -r '"  导航到：\(.url)"' || echo "  导航到写作平台"

echo ""
echo "✅ 工作流 3 完成"
echo ""

# 工作流 4：数据抓取 + 截图存档
echo "📸 工作流 4: 数据抓取 + 截图存档"
echo "------------------------------"

echo ""
echo "步骤 1: 抓取网页内容..."
opencli web read https://example.com 2>/dev/null | head -5 || echo "  读取网页"

echo ""
echo "步骤 2: 使用 PinchTab 截图..."
pinchtab screenshot -o /tmp/workflow-example.png 2>/dev/null && echo "  截图保存：/tmp/workflow-example.png" || echo "  截图"

echo ""
echo "步骤 3: 导出为 PDF..."
# pinchtab pdf --tab <tabId> -o /tmp/workflow-example.pdf 2>/dev/null && echo "  PDF 保存：/tmp/workflow-example.pdf" || echo "  导出 PDF"
echo "  (需要指定 tabId)"

echo ""
echo "✅ 工作流 4 完成"
echo ""

echo "===================================="
echo "🎉 所有工作流示例执行完成！"
echo ""
echo "💡 提示："
echo "  - opencli 适合快速抓取公开数据"
echo "  - PinchTab 适合需要交互的场景"
echo "  - 两者结合可实现复杂自动化任务"
echo ""
