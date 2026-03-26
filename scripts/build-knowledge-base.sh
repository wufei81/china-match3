#!/bin/bash
# 构建知识库脚本

echo "📚 开始构建知识库..."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# 1. 创建知识库目录
echo "1. 创建知识库目录..."
mkdir -p /home/wufei/.openclaw/workspace/knowledge-base/{product,technology,development,operations}
mkdir -p /home/wufei/.openclaw/workspace/knowledge-base/product/{requirements,business-analysis,user-research}
mkdir -p /home/wufei/.openclaw/workspace/knowledge-base/technology/{architecture,design-patterns,security}
mkdir -p /home/wufei/.openclaw/workspace/knowledge-base/development/{coding-standards,testing,performance}
mkdir -p /home/wufei/.openclaw/workspace/knowledge-base/operations/{cicd,monitoring,backup}
echo "  ✅ 知识库目录已创建"
echo ""

# 2. 导入现有技能文档
echo "2. 导入现有技能文档..."
cd /home/wufei/.openclaw/workspace
for agent_dir in agents/*/skills/*/; do
  if [ -d "$agent_dir" ]; then
    agent_name=$(echo $agent_dir | cut -d'/' -f2)
    skill_name=$(echo $agent_dir | cut -d'/' -f4)
    
    case $agent_name in
      product-manager)
        cp -r $agent_dir knowledge-base/product/ 2>/dev/null && echo "  ✅ 导入产品知识：$skill_name"
        ;;
      architect|tech-leader)
        cp -r $agent_dir knowledge-base/technology/ 2>/dev/null && echo "  ✅ 导入技术知识：$skill_name"
        ;;
      dev-engineer)
        cp -r $agent_dir knowledge-base/development/ 2>/dev/null && echo "  ✅ 导入开发知识：$skill_name"
        ;;
      qa-engineer|devops-engineer)
        cp -r $agent_dir knowledge-base/operations/ 2>/dev/null && echo "  ✅ 导入运维知识：$skill_name"
        ;;
    esac
  fi
done
echo ""

# 3. 统计知识库
echo "3. 统计知识库..."
TOTAL_DOCS=$(find knowledge-base -name "*.md" 2>/dev/null | wc -l)
TOTAL_SIZE=$(du -sh knowledge-base 2>/dev/null | cut -f1)
echo "  文档总数：$TOTAL_DOCS"
echo "  总大小：$TOTAL_SIZE"
echo ""

# 4. 生成知识索引
echo "4. 生成知识索引..."
cat > knowledge-base/INDEX.md << EOF
# 知识库索引

**最后更新**: $(date +%Y-%m-%d)

## 分类
- [产品管理](product/)
- [技术架构](technology/)
- [开发实践](development/)
- [运维实践](operations/)

## 统计
- 文档总数：$TOTAL_DOCS
- 总大小：$TOTAL_SIZE
EOF
echo "  ✅ 知识索引已生成"
echo ""

# 总结
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✅ 知识库构建完成"
echo ""
echo "知识库位置：/home/wufei/.openclaw/workspace/knowledge-base/"
echo "文档总数：$TOTAL_DOCS"
echo "总大小：$TOTAL_SIZE"
