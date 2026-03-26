#!/bin/bash
# validate-prd.sh - PRD 质量检查脚本
# 用法：./validate-prd.sh <PRD 文件路径>

set -e

PRD_FILE="${1:-}"
SCORE=0
TOTAL=10
PASSING_SCORE=8

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# 检查函数
check_section() {
    local section="$1"
    local pattern="$2"
    
    if grep -q "$pattern" "$PRD_FILE" 2>/dev/null; then
        echo -e "${GREEN}✅${NC} $section"
        ((SCORE++))
        return 0
    else
        echo -e "${RED}❌${NC} $section"
        return 1
    fi
}

# 用法说明
usage() {
    echo "用法：$0 <PRD 文件路径>"
    echo ""
    echo "示例:"
    echo "  $0 docs/prd/im-system.md"
    echo "  $0 examples/sample-prd-im.md"
    exit 1
}

# 主程序
main() {
    if [ -z "$PRD_FILE" ]; then
        usage
    fi
    
    if [ ! -f "$PRD_FILE" ]; then
        echo -e "${RED}错误：文件不存在 - $PRD_FILE${NC}"
        exit 1
    fi
    
    echo "=================================="
    echo "📋 PRD 质量检查"
    echo "=================================="
    echo "文件：$PRD_FILE"
    echo "日期：$(date +%Y-%m-%d)"
    echo ""
    
    echo "检查项目:"
    echo "----------------------------------"
    
    # 检查 10 项必须内容
    check_section "1. 背景与目标" "问题陈述\|Problem Statement\|背景与目标"
    check_section "2. 范围 (In/Out)" "In Scope\|Out of Scope\|范围"
    check_section "3. 业务流程图" "Mermaid\|流程图\|flow"
    check_section "4. 用户旅程" "用户旅程\|User Journey\|使用场景"
    check_section "5. 功能列表" "功能列表\|Feature\|P0\|P1\|P2"
    check_section "6. 数据结构" "数据结构\|Data Structure\|CREATE TABLE\|字段"
    check_section "7. API 契约" "API\|OpenAPI\|POST\|GET\|/api/"
    check_section "8. 验收标准" "验收标准\|Acceptance\|Gherkin\|Given-When-Then"
    check_section "9. 非功能需求" "非功能\|NFR\|性能\|安全\|可靠性"
    check_section "10. 迭代计划" "迭代\|Timeline\|Milestone\|排期\|周"
    
    echo ""
    echo "=================================="
    echo "📊 评分结果"
    echo "=================================="
    echo "得分：$SCORE / $TOTAL"
    
    # 计算百分比
    PERCENTAGE=$((SCORE * 100 / TOTAL))
    echo "百分比：$PERCENTAGE%"
    
    echo ""
    
    # 判断是否通过
    if [ $SCORE -ge $PASSING_SCORE ]; then
        echo -e "${GREEN}✅ 通过 - PRD 质量合格${NC}"
        
        if [ $SCORE -eq $TOTAL ]; then
            echo -e "${GREEN}🌟 完美 - 所有项目都包含！${NC}"
        fi
        exit 0
    else
        echo -e "${RED}❌ 需要改进 - 缺少 $((TOTAL - SCORE)) 项内容${NC}"
        echo ""
        echo "建议:"
        
        if [ $SCORE -lt 5 ]; then
            echo -e "${YELLOW}⚠️  PRD 完成度较低，建议补充基础内容${NC}"
        elif [ $SCORE -lt 8 ]; then
            echo -e "${YELLOW}⚠️  PRD 基本完整，建议补充缺失项${NC}"
        fi
        
        exit 1
    fi
}

# 执行主程序
main
