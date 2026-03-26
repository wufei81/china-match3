# 自动质量检查配置

**版本**: 1.0  
**创建日期**: 2026-03-26  
**目标**: 自动化质量门禁，减少人工检查

---

## 🎯 质量门禁自动化

### Gate 1: PRD 评审自动化
```json
{
  "check": "PRD 完整性",
  "rules": [
    "AC 必须是 Gherkin 格式",
    "必须包含数据结构草稿",
    "必须包含 API 契约草稿",
    "必须有时间估算（分钟）"
  ],
  "auto_check": true,
  "tool": "NLP + 规则引擎"
}
```

### Gate 2: 架构评审自动化
```json
{
  "check": "架构完整性",
  "rules": [
    "API Schema 字段级定义",
    "DDL 完整（表/索引/外键）",
    "一致性策略明确",
    "安全评审 Phase 1 完成"
  ],
  "auto_check": true,
  "tool": "OpenAPI Validator + SQL Validator"
}
```

### Gate 3: 开发评审自动化
```json
{
  "check": "开发质量",
  "rules": [
    "npm run lint → 0 errors",
    "npm run test → coverage ≥80%",
    "npm run build → 0 errors",
    "VALIDATION_LOG.md 完整"
  ],
  "auto_check": true,
  "tool": "CI/CD Pipeline"
}
```

### Gate 4: 测试评审自动化
```json
{
  "check": "测试覆盖",
  "rules": [
    "E2E 使用真实 API",
    "P0 AC 100% 覆盖",
    "P1 AC ≥90% 覆盖",
    "异常场景覆盖"
  ],
  "auto_check": true,
  "tool": "Test Coverage Analyzer"
}
```

### Gate 5: 部署评审自动化
```json
{
  "check": "部署就绪",
  "rules": [
    "E2E 测试通过",
    "无硬编码密钥",
    "健康检查端点配置",
    "监控告警配置",
    "回滚流程测试"
  ],
  "auto_check": true,
  "tool": "Security Scanner + Health Check"
}
```

---

## 🔧 自动化实现

### CI/CD 质量门禁脚本
```bash
#!/bin/bash
# quality-gate.sh

set -e

echo "🔍 运行质量门禁检查..."

# Gate 3: 开发质量检查
echo "Gate 3: 开发质量检查"
npm run lint
if [ $? -ne 0 ]; then
  echo "❌ Lint 失败"
  exit 1
fi
echo "✅ Lint 通过"

npm run test -- --coverage
if [ $? -ne 0 ]; then
  echo "❌ 测试失败"
  exit 1
fi
echo "✅ 测试通过"

# 检查覆盖率
COVERAGE=$(cat coverage/coverage-summary.json | jq '.total.lines.pct')
if (( $(echo "$COVERAGE < 80" | bc -l) )); then
  echo "❌ 覆盖率不足：${COVERAGE}% < 80%"
  exit 1
fi
echo "✅ 覆盖率通过：${COVERAGE}%"

npm run build
if [ $? -ne 0 ]; then
  echo "❌ 构建失败"
  exit 1
fi
echo "✅ 构建通过"

echo "✅ Gate 3 通过"

# Gate 5: 安全检查
echo "Gate 5: 安全检查"
# 检查硬编码密钥
if grep -r "password.*=" src/ --include="*.ts" --include="*.js"; then
  echo "❌ 发现硬编码密码"
  exit 1
fi
echo "✅ 无硬编码密钥"

# 检查健康检查端点
if ! grep -r "/health" src/ --include="*.ts" --include="*.js"; then
  echo "❌ 缺少健康检查端点"
  exit 1
fi
echo "✅ 健康检查端点配置"

echo "✅ 所有质量门禁通过"
```

### GitHub Actions 配置
```yaml
name: Quality Gates

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  quality-gate:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v3
      
      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'
          cache: 'npm'
      
      - name: Install dependencies
        run: npm ci
      
      - name: Gate 3 - Lint
        run: npm run lint
      
      - name: Gate 3 - Test
        run: npm run test -- --coverage
      
      - name: Gate 3 - Check Coverage
        run: |
          COVERAGE=$(cat coverage/coverage-summary.json | jq '.total.lines.pct')
          if (( $(echo "$COVERAGE < 80" | bc -l) )); then
            echo "❌ Coverage ${COVERAGE}% < 80%"
            exit 1
          fi
      
      - name: Gate 3 - Build
        run: npm run build
      
      - name: Gate 5 - Security Scan
        run: |
          # 检查硬编码密钥
          if grep -r "password.*=" src/ --include="*.ts" --include="*.js"; then
            echo "❌ Hardcoded password found"
            exit 1
          fi
      
      - name: Upload Coverage
        uses: codecov/codecov-action@v3
        with:
          files: ./coverage/lcov.info
```

---

## 📊 质量看板

### 实时质量指标
```markdown
## 质量看板 - IM System

### Gate 状态
| Gate | 状态 | 检查时间 | 检查者 |
|------|------|---------|-------|
| Gate 1: PRD | ✅ 通过 | 03-21 10:00 | AI Orchestrator |
| Gate 2: 架构 | ✅ 通过 | 03-22 14:00 | TechLeader |
| Gate 3: 开发 | 🟡 进行中 | - | 自动检查 |
| Gate 4: 测试 | ⚪ 待检查 | - | - |
| Gate 5: 部署 | ⚪ 待检查 | - | - |

### 质量指标
| 指标 | 当前值 | 目标值 | 状态 |
|------|-------|-------|------|
| 代码覆盖率 | 85% | ≥80% | ✅ |
| Lint 错误 | 0 | 0 | ✅ |
| 构建状态 | 成功 | 成功 | ✅ |
| 安全问题 | 0 | 0 | ✅ |
| E2E 通过率 | - | 100% | ⚪ |
```

---

## 🚀 实施步骤

### Step 1: 创建质量检查脚本 (15 分钟)
```bash
# 创建脚本
cat > scripts/quality-gate.sh << 'EOF'
#!/bin/bash
# 复制上面的质量门禁脚本
EOF

chmod +x scripts/quality-gate.sh
```

### Step 2: 配置 CI/CD (15 分钟)
```bash
# 创建 GitHub Actions 配置
mkdir -p .github/workflows
cat > .github/workflows/quality-gates.yml << 'EOF'
# 复制上面的 GitHub Actions 配置
EOF
```

### Step 3: 集成到工作流 (10 分钟)
```bash
# 在 AGENTS.md 中添加质量门禁说明
# 每个智能体在交付前自动运行质量检查
```

---

## 🎯 预期效果

| 指标 | 当前 | 优化后 | 提升 |
|------|------|-------|------|
| **质量检查时间** | 30 分钟 | 5 分钟 | 83% ↓ |
| **人工检查** | 100% | 20% | 80% ↓ |
| **问题发现** | 后期 | 早期 | 提前 50% |
| **返工率** | 25% | 10% | 60% ↓ |

---

**维护者**: AI Orchestrator  
**最后更新**: 2026-03-26  
**版本**: 1.0
