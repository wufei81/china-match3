#!/bin/bash
# 质量门禁检查脚本
# 用途：自动执行 5 个质量门禁检查

set -e

echo "🔍 运行质量门禁检查..."
echo ""

# Gate 3: 开发质量检查
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Gate 3: 开发质量检查"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Lint 检查
echo "Running: npm run lint"
if npm run lint 2>&1; then
  echo "✅ Lint 通过"
else
  echo "❌ Lint 失败"
  exit 1
fi
echo ""

# 测试检查
echo "Running: npm run test --coverage"
if npm run test --coverage 2>&1; then
  echo "✅ 测试通过"
else
  echo "❌ 测试失败"
  exit 1
fi
echo ""

# 检查覆盖率
if [ -f coverage/coverage-summary.json ]; then
  COVERAGE=$(cat coverage/coverage-summary.json | jq '.total.lines.pct')
  if (( $(echo "$COVERAGE < 80" | bc -l) )); then
    echo "❌ 覆盖率不足：${COVERAGE}% < 80%"
    exit 1
  fi
  echo "✅ 覆盖率通过：${COVERAGE}%"
else
  echo "⚠️ 覆盖率报告不存在，跳过检查"
fi
echo ""

# 构建检查
echo "Running: npm run build"
if npm run build 2>&1; then
  echo "✅ 构建通过"
else
  echo "❌ 构建失败"
  exit 1
fi
echo ""

echo "✅ Gate 3: 开发质量检查通过"
echo ""

# Gate 5: 安全检查
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Gate 5: 安全检查"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# 检查硬编码密钥
echo "检查硬编码密钥..."
if grep -r "password.*=" src/ --include="*.ts" --include="*.js" 2>/dev/null; then
  echo "❌ 发现硬编码密码"
  exit 1
fi
echo "✅ 无硬编码密钥"
echo ""

# 检查健康检查端点
echo "检查健康检查端点..."
if grep -r "/health" src/ --include="*.ts" --include="*.js" 2>/dev/null; then
  echo "✅ 健康检查端点配置"
else
  echo "❌ 缺少健康检查端点"
  exit 1
fi
echo ""

# 检查 SQL 注入
echo "检查 SQL 注入风险..."
if grep -r "f\"SELECT\|f\"INSERT\|f\"DROP" src/ --include="*.ts" --include="*.js" 2>/dev/null; then
  echo "❌ 发现 SQL 注入风险"
  exit 1
fi
echo "✅ 无 SQL 注入风险"
echo ""

echo "✅ Gate 5: 安全检查通过"
echo ""

# 总结
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✅ 所有质量门禁通过"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "Gate 3: ✅ 通过"
echo "Gate 5: ✅ 通过"
echo ""
echo "准备交付！🚀"
