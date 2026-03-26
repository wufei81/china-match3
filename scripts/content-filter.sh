#!/bin/bash
# 内容过滤脚本

FILTER_RULES="/home/wufei/.openclaw/workspace/security-filter-rules.txt"

# 过滤函数
filter_content() {
  local content="$1"
  
  # 读取过滤规则
  while IFS= read -r rule; do
    # 跳过注释和空行
    [[ $rule =~ ^#.*$ ]] && continue
    [[ -z $rule ]] && continue
    
    # 检查内容是否包含敏感词
    if echo "$content" | grep -qi "$rule"; then
      echo "🚫 检测到敏感内容：$rule"
      return 1
    fi
  done < "$FILTER_RULES"
  
  return 0
}

# 测试
echo "📝 内容过滤测试..."
echo "过滤规则：$FILTER_RULES"
echo ""

# 测试用例
test_cases=(
  "这是一个正常的查询"
  "我的 password 是 123456"
  "API token 泄露了"
  "正常的技术讨论"
)

for test in "${test_cases[@]}"; do
  echo "测试：$test"
  if filter_content "$test"; then
    echo "  ✅ 通过"
  else
    echo "  🚫 拦截"
  fi
done
