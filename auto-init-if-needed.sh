#!/bin/bash

# 🚀 Auto-Initialize Project if Needed
# 用途：智能检测项目是否需要初始化，如需则自动执行
# 使用：./auto-init-if-needed.sh [项目名称]

set -e

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

# 获取项目名称（参数或当前目录）
if [ -n "$1" ]; then
    PROJECT_NAME=$1
else
    PROJECT_NAME=$(basename $(pwd))
fi

PROJECT_DIR="/home/wufei/.openclaw/workspace/$PROJECT_NAME"
INIT_SCRIPT="/home/wufei/.openclaw/workspace/init-project.sh"

echo -e "${BLUE}╔════════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║   OpenClaw Auto-Initialization Check${NC}"
echo -e "${BLUE}╚════════════════════════════════════════════════════════╝${NC}"
echo ""

# 检查项目是否已存在
if [ ! -d "$PROJECT_DIR" ]; then
    echo -e "${YELLOW}[检测] 项目目录不存在：$PROJECT_DIR${NC}"
    echo -e "${YELLOW}[操作] 创建新项目并初始化...${NC}"
    echo ""

    # 执行初始化脚本
    cd /home/wufei/.openclaw/workspace
    ./init-project.sh "$PROJECT_NAME"

    echo ""
    echo -e "${GREEN}✅ 新项目已自动初始化完成！${NC}"
    exit 0
fi

# 检查关键文件是否存在
echo -e "${YELLOW}[检测] 检查项目初始化状态...${NC}"

REQUIRED_FILES=(
    "$PROJECT_DIR/PROJECT_CONFIG.md"
    "$PROJECT_DIR/docs/CORE_RULES.md"
    "$PROJECT_DIR/docs/CODEBASE_INDEX.md"
    "$PROJECT_DIR/docs/VALIDATION_LOG.md"
    "$PROJECT_DIR/docs/SECURITY_CHECKLIST.md"
)

MISSING_FILES=()

for file in "${REQUIRED_FILES[@]}"; do
    if [ ! -f "$file" ]; then
        MISSING_FILES+=("$file")
    fi
done

if [ ${#MISSING_FILES[@]} -eq 0 ]; then
    echo -e "${GREEN}✓ 项目已初始化，所有必要文件存在${NC}"
    echo ""
    echo -e "${GREEN}✅ 项目就绪，可以开始开发！${NC}"
    exit 0
else
    echo -e "${RED}✗ 发现 ${#MISSING_FILES[@]} 个缺失文件:${NC}"
    for file in "${MISSING_FILES[@]}"; do
        echo -e "${RED}  - $file${NC}"
    done
    echo ""

    # 询问是否自动修复
    echo -e "${YELLOW}[操作] 是否自动补全缺失文件？(Y/n)${NC}"
    read -r response

    if [[ "$response" =~ ^[Yy]$ ]] || [[ -z "$response" ]]; then
        echo ""
        echo -e "${YELLOW}[操作] 执行初始化脚本补全文件...${NC}"
        echo ""

        cd /home/wufei/.openclaw/workspace
        ./init-project.sh "$PROJECT_NAME"

        echo ""
        echo -e "${GREEN}✅ 项目已自动修复完成！${NC}"
        exit 0
    else
        echo ""
        echo -e "${YELLOW}[提示] 可以手动复制缺失文件:${NC}"
        echo "  cd $PROJECT_DIR"
        echo "  cp /home/wufei/.openclaw/workspace/memory/CORE_RULES.md docs/"
        echo "  # ... 复制其他缺失文件"
        exit 1
    fi
fi
