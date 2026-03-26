#!/bin/bash

# 📊 Check Project Status
# 用途：检查项目初始化状态和进度

set -e

PROJECT_NAME=${1:-$(basename $(pwd))}
PROJECT_DIR="/home/wufei/.openclaw/workspace/$PROJECT_NAME"

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${BLUE}╔════════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║   Project Status: $PROJECT_NAME${NC}"
echo -e "${BLUE}╚════════════════════════════════════════════════════════╝${NC}"
echo ""

# 检查项目目录
if [ ! -d "$PROJECT_DIR" ]; then
    echo -e "${RED}❌ 项目目录不存在：$PROJECT_DIR${NC}"
    echo ""
    echo -e "${YELLOW}建议：运行自动初始化${NC}"
    echo "  cd /home/wufei/.openclaw/workspace"
    echo "  ./auto-init-if-needed.sh $PROJECT_NAME"
    exit 1
fi

echo -e "${GREEN}✓ 项目目录存在${NC}"
echo ""

# 检查关键文件
echo -e "${YELLOW}[1/3] 检查必要文件...${NC}"

REQUIRED_FILES=(
    "PROJECT_CONFIG.md:项目配置"
    "QUICK_REFERENCE.md:快速参考"
    "docs/CORE_RULES.md:核心规则"
    "docs/CODEBASE_INDEX.md:代码索引"
    "docs/VALIDATION_LOG.md:验证日志"
    "docs/TASK_TRACKER.md:任务追踪"
    "docs/SECURITY_CHECKLIST.md:安全检查"
    "docs/CODE_REVIEW_CHECKLIST.md:代码审查"
    "docs/INTEGRATION_TEST_PLAN.md:集成测试"
    "docs/DEPLOYMENT_READINESS.md:部署检查"
    "docs/DEVELOPMENT_PROCESS_CHECKLIST.md:开发流程"
)

MISSING_COUNT=0

for item in "${REQUIRED_FILES[@]}"; do
    IFS=':' read -r file desc <<< "$item"
    if [ -f "$PROJECT_DIR/$file" ]; then
        echo -e "${GREEN}  ✓ $desc${NC}"
    else
        echo -e "${RED}  ✗ $desc (缺失)${NC}"
        ((MISSING_COUNT++))
    fi
done

echo ""

if [ $MISSING_COUNT -gt 0 ]; then
    echo -e "${RED}❌ 缺失 $MISSING_COUNT 个文件${NC}"
    echo ""
    echo -e "${YELLOW}建议：运行自动初始化补全${NC}"
    echo "  cd /home/wufei/.openclaw/workspace"
    echo "  ./auto-init-if-needed.sh $PROJECT_NAME"
    exit 1
else
    echo -e "${GREEN}✅ 所有必要文件存在${NC}"
fi

echo ""

# 检查 Git 状态
echo -e "${YELLOW}[2/3] 检查 Git 状态...${NC}"

if [ -d "$PROJECT_DIR/.git" ]; then
    echo -e "${GREEN}  ✓ Git 仓库已初始化${NC}"

    cd "$PROJECT_DIR"

    # 检查是否有未提交的更改
    if ! git diff --quiet 2>/dev/null; then
        echo -e "${YELLOW}  ⚠ 有未提交的更改${NC}"
    else
        echo -e "${GREEN}  ✓ 工作区干净${NC}"
    fi

    # 最近提交
    LAST_COMMIT=$(git log -1 --format="%h %s" 2>/dev/null || echo "无提交")
    echo -e "  最近提交：$LAST_COMMIT"
else
    echo -e "${YELLOW}  ⚠ Git 仓库未初始化${NC}"
    echo -e "${YELLOW}  建议：cd $PROJECT_DIR && git init${NC}"
fi

echo ""

# 检查项目进度
echo -e "${YELLOW}[3/3] 检查项目进度...${NC}"

if [ -f "$PROJECT_DIR/docs/TASK_TRACKER.md" ]; then
    echo -e "${GREEN}  ✓ 任务追踪文件存在${NC}"

    # 简单统计
    if command -v grep &> /dev/null; then
        DONE_COUNT=$(grep -c "✅" "$PROJECT_DIR/docs/TASK_TRACKER.md" 2>/dev/null || echo "0")
        IN_PROGRESS_COUNT=$(grep -c "🟡" "$PROJECT_DIR/docs/TASK_TRACKER.md" 2>/dev/null || echo "0")
        PENDING_COUNT=$(grep -c "⏳" "$PROJECT_DIR/docs/TASK_TRACKER.md" 2>/dev/null || echo "0")

        echo -e "  任务统计："
        echo -e "    ${GREEN}已完成：$DONE_COUNT${NC}"
        echo -e "    ${YELLOW}进行中：$IN_PROGRESS_COUNT${NC}"
        echo -e "    ${BLUE}待开始：$PENDING_COUNT${NC}"
    fi
else
    echo -e "${YELLOW}  ⚠ 任务追踪文件不存在${NC}"
    echo -e "${YELLOW}  建议：ai-orchestrator 会创建${NC}"
fi

echo ""
echo -e "${BLUE}╔════════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║   项目状态总结${NC}"
echo -e "${BLUE}╚════════════════════════════════════════════════════════╝${NC}"
echo ""

if [ $MISSING_COUNT -eq 0 ]; then
    echo -e "${GREEN}✅ 项目已完全初始化，可以开始开发！${NC}"
else
    echo -e "${RED}❌ 项目未完全初始化，需要补全 $MISSING_COUNT 个文件${NC}"
    echo ""
    echo -e "${YELLOW}运行以下命令自动补全：${NC}"
    echo "  cd /home/wufei/.openclaw/workspace"
    echo "  ./auto-init-if-needed.sh $PROJECT_NAME"
fi

echo ""
