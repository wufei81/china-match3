#!/bin/bash

# 🚀 OpenClaw 新项目初始化脚本
# 用途：自动复制所有模板文件 + 初始化项目结构
# 使用：./init-project.sh <项目名称>

set -e

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 检查参数
if [ -z "$1" ]; then
    echo -e "${RED}❌ 错误：请提供项目名称${NC}"
    echo "用法：./init-project.sh <项目名称>"
    echo "示例：./init-project.sh im-system"
    exit 1
fi

PROJECT_NAME=$1
PROJECT_DIR="$PROJECT_NAME"
TEMPLATES_DIR="/home/wufei/.openclaw/workspace"

echo -e "${BLUE}╔════════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║   OpenClaw 新项目初始化 - $PROJECT_NAME${NC}"
echo -e "${BLUE}╚════════════════════════════════════════════════════════╝${NC}"
echo ""

# 创建项目目录
echo -e "${YELLOW}[1/6] 创建项目目录...${NC}"
mkdir -p "$PROJECT_DIR"
mkdir -p "$PROJECT_DIR/docs"
mkdir -p "$PROJECT_DIR/src"
mkdir -p "$PROJECT_DIR/tests"
echo -e "${GREEN}✓ 项目目录已创建：$PROJECT_DIR${NC}"
echo ""

# 复制模板文件
echo -e "${YELLOW}[2/6] 复制模板文件...${NC}"
TEMPLATES=(
    "memory/CORE_RULES.md:docs/CORE_RULES.md"
    "CODEBASE_INDEX.template.md:CODEBASE_INDEX.md"
    "VALIDATION_LOG.template.md:VALIDATION_LOG.md"
    "TASK_TRACKER.template.md:TASK_TRACKER.md"
    "ERROR_LOG.template.md:ERROR_LOG.md"
    "SECURITY_CHECKLIST.template.md:SECURITY_CHECKLIST.md"
    "CODE_REVIEW_CHECKLIST.template.md:CODE_REVIEW_CHECKLIST.md"
    "INTEGRATION_TEST_PLAN.template.md:INTEGRATION_TEST_PLAN.md"
    "DEPLOYMENT_READINESS.template.md:DEPLOYMENT_READINESS.md"
    "DEVELOPMENT_PROCESS_CHECKLIST.md:DEVELOPMENT_PROCESS_CHECKLIST.md"
    "PROJECT_STARTUP_CHECKLIST.template.md:PROJECT_STARTUP_CHECKLIST.md"
)

for template in "${TEMPLATES[@]}"; do
    IFS=':' read -r src dst <<< "$template"
    if [ -f "$TEMPLATES_DIR/$src" ]; then
        cp "$TEMPLATES_DIR/$src" "$PROJECT_DIR/$dst"
        echo -e "${GREEN}  ✓ $dst${NC}"
    else
        echo -e "${RED}  ✗ $src 不存在${NC}"
    fi
done
echo ""

# 创建项目配置文件
echo -e "${YELLOW}[3/6] 创建项目配置文件...${NC}"
cat > "$PROJECT_DIR/PROJECT_CONFIG.md" << 'EOF'
# 项目配置

## 基本信息
- **项目名称**: [填写]
- **创建日期**: [自动填充]
- **项目负责人**: [填写]
- **技术栈**: [填写]

## 质量门禁 (MANDATORY)

本项目启用以下强制检查：

- [x] **5 个质量门禁** - Gate 1-5 必须全部通过
- [x] **4 个检查清单** - SECURITY/CODE_REVIEW/INTEGRATION_TEST/DEPLOYMENT
- [x] **6 阶段开发流程** - 所有开发任务必须遵循 Phase 0-6
- [x] **安全基线** - 禁止硬编码密钥/SQL 拼接/CORS 错误

## 智能体分工

| 角色 | 智能体 | 职责 |
|------|--------|------|
| 产品 | product-manager | PRD + AC |
| 架构 | architect + tech-leader | 架构设计 + 安全评审 |
| 开发 | dev-engineer | 6 阶段流程执行 |
| 测试 | qa-engineer | E2E 测试 + 流程验证 |
| 运维 | devops-engineer | 部署就绪检查 |
| 协调 | ai-orchestrator | 进度追踪 + 流程监督 |
| 管理 | project-manager | 项目整体进度 |

## 模板文件清单

所有模板已复制到 `docs/` 目录，请在相应阶段填写：

- [ ] CODEBASE_INDEX.md (dev-engineer)
- [ ] VALIDATION_LOG.md (dev-engineer, 每次交付前)
- [ ] TASK_TRACKER.md (ai-orchestrator, 每 2-3 分钟)
- [ ] ERROR_LOG.md (所有智能体，遇到错误时)
- [ ] SECURITY_CHECKLIST.md (tech-leader + dev + qa)
- [ ] CODE_REVIEW_CHECKLIST.md (tech-leader, 合并前)
- [ ] INTEGRATION_TEST_PLAN.md (qa-engineer, 测试前)
- [ ] DEPLOYMENT_READINESS.md (devops-engineer, 部署前)
- [ ] DEVELOPMENT_PROCESS_CHECKLIST.md (所有智能体参考)

## 快速开始

1. 填写 PROJECT_CONFIG.md 基本信息
2. product-manager 开始撰写 PRD
3. 按照 5 门禁流程执行

---
**初始化时间**: [自动填充]
**初始化脚本版本**: 1.0
EOF

# 替换日期占位符
DATE=$(date +"%Y-%m-%d %H:%M:%S")
sed -i "s/\[自动填充\]/$DATE/g" "$PROJECT_DIR/PROJECT_CONFIG.md"

echo -e "${GREEN}✓ PROJECT_CONFIG.md 已创建${NC}"
echo ""

# 创建快速参考卡片
echo -e "${YELLOW}[4/6] 创建快速参考卡片...${NC}"
cat > "$PROJECT_DIR/QUICK_REFERENCE.md" << 'EOF'
# 🚨 快速参考 - 不可跳过！

## ⛔ 开发前必问 (Phase 0)

在开始写代码前，**必须**明确这 5 点：

1. **功能目标**：新增/修改/删除什么行为？
2. **触发方式**：从哪里调用？谁会用到？
3. **输入输出**：参数、返回结构、数据格式？
4. **失败行为**：异常/空结果/超时/权限不足时怎么表现？
5. **质量要求**：性能、可读性、兼容性、测试？

**⛔ 如果任何点不清楚 → 停止！问用户！**

---

## 📋 6 阶段流程 (必须按顺序)

```
Phase 0: 需求澄清 (5 点) → ⛔ 禁止跳过
    ↓
Phase 1: 定位入口 + 上下文 → ⛔ 禁止盲改
    ↓
Phase 2: 方案决策 (小/中/大) → ⛔ 中/大需用户确认
    ↓
Phase 3: 微设计 (子任务 A-E) → ⛔ 禁止无计划
    ↓
Phase 4: 编码 (增量) → ⛔ 禁止一次性写完
    ↓
Phase 5: 验证 (4 层) → ⛔ 禁止只跑通
    ↓
Phase 6: 对齐 (不确定时停止)
```

---

## 🔒 安全红线 (违反=打回)

- ⛔ 硬编码密钥/密码
- ⛔ SQL 字符串拼接
- ⛔ CORS * + credentials
- ⛔ 鉴权测试后门
- ⛔ 默认关闭安全配置

---

## ✅ 交付前检查 (dev-engineer)

- [ ] VALIDATION_LOG.md 已填写
- [ ] lint/test/build 全部通过
- [ ] curl 测试通过
- [ ] CODEBASE_INDEX.md 已更新
- [ ] 6 阶段流程完成记录

---

## ✅ 合并前检查 (tech-leader)

- [ ] CODE_REVIEW_CHECKLIST.md 已填写
- [ ] SECURITY_CHECKLIST.md Phase 2 已签字
- [ ] 6 阶段流程合规
- [ ] 无 P0 问题

---

## ✅ 发布前检查 (qa/devops)

- [ ] INTEGRATION_TEST_PLAN.md 完成
- [ ] SECURITY_CHECKLIST.md Phase 3 通过
- [ ] DEPLOYMENT_READINESS.md 签字
- [ ] 所有 P0/P1 Bug 修复

---

**完整文档**: 见 `docs/` 目录
EOF

echo -e "${GREEN}✓ QUICK_REFERENCE.md 已创建${NC}"
echo ""

# 创建 .gitignore
echo -e "${YELLOW}[5/6] 创建 .gitignore...${NC}"
cat > "$PROJECT_DIR/.gitignore" << 'EOF'
# 环境
.env
.env.local
.env.production
__pycache__/
*.pyc
node_modules/
dist/
build/

# IDE
.vscode/
.idea/
*.swp
*.swo

# 日志
*.log
logs/

# 临时
tmp/
temp/
*.tmp

# 敏感
*.pem
*.key
secrets/
EOF

echo -e "${GREEN}✓ .gitignore 已创建${NC}"
echo ""

# 初始化 Git 仓库 (可选)
echo -e "${YELLOW}[6/6] 初始化 Git 仓库...${NC}"
if command -v git &> /dev/null; then
    cd "$PROJECT_DIR"
    git init
    git add .
    git commit -m "chore: initial project setup with OpenClaw templates"
    echo -e "${GREEN}✓ Git 仓库已初始化${NC}"
    cd ..
else
    echo -e "${YELLOW}⚠ Git 未安装，跳过${NC}"
fi
echo ""

# 完成
echo -e "${BLUE}╔════════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║   ✅ 项目初始化完成！${NC}"
echo -e "${BLUE}╚════════════════════════════════════════════════════════╝${NC}"
echo ""
echo -e "${GREEN}项目目录:${NC} $PROJECT_DIR"
echo -e "${GREEN}模板文件:${NC} 已复制到项目目录"
echo -e "${GREEN}快速参考:${NC} $PROJECT_DIR/QUICK_REFERENCE.md"
echo -e "${GREEN}项目配置:${NC} $PROJECT_DIR/PROJECT_CONFIG.md"
echo ""
echo -e "${YELLOW}下一步:${NC}"
echo "1. cd $PROJECT_DIR"
echo "2. 编辑 PROJECT_CONFIG.md 填写基本信息"
echo "3. product-manager 开始撰写 PRD"
echo ""
echo -e "${YELLOW}重要提醒:${NC}"
echo "- 所有开发任务必须遵循 6 阶段流程"
echo "- 所有交付必须填写 VALIDATION_LOG.md"
echo "- 所有合并必须填写 CODE_REVIEW_CHECKLIST.md"
echo "- 所有部署必须填写 DEPLOYMENT_READINESS.md"
echo ""
