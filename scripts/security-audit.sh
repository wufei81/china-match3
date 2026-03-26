#!/bin/bash
# 安全审计脚本

echo "🔍 开始安全审计..."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

RISK_COUNT=0
HIGH_RISK=0
MEDIUM_RISK=0

# 1. 检查文件权限
echo "1. 检查敏感文件权限..."
for file in ~/.claude/.env /home/wufei/.openclaw/workspace/.env; do
  if [ -f "$file" ]; then
    PERM=$(stat -c %a "$file" 2>/dev/null)
    if [ "$PERM" != "600" ]; then
      echo "  🟠 高风险：$file 权限为 $PERM (应为 600)"
      ((HIGH_RISK++))
    else
      echo "  ✅ $file 权限正确"
    fi
    ((RISK_COUNT++))
  fi
done
echo ""

# 2. 检查 Token 轮换
echo "2. 检查 Token 轮换..."
if [ -f "/home/wufei/.openclaw/workspace/.env" ]; then
  TOKEN_AGE=$(( ($(date +%s) - $(stat -c %Y /home/wufei/.openclaw/workspace/.env)) / 86400 ))
  if [ $TOKEN_AGE -gt 90 ]; then
    echo "  🟠 高风险：Token 已使用 $TOKEN_AGE 天 (建议 90 天轮换)"
    ((HIGH_RISK++))
  else
    echo "  ✅ Token 已使用 $TOKEN_AGE 天"
  fi
fi
echo ""

# 3. 检查备份加密
echo "3. 检查备份加密..."
if [ -d "/home/wufei/.openclaw/workspace/backups" ]; then
  ENCRYPTED=$(find /home/wufei/.openclaw/workspace/backups -name "*.gpg" 2>/dev/null | wc -l)
  TOTAL=$(find /home/wufei/.openclaw/workspace/backups -name "*.tar.gz" 2>/dev/null | wc -l)
  if [ $TOTAL -gt 0 ] && [ $ENCRYPTED -eq 0 ]; then
    echo "  🟠 高风险：备份文件未加密 ($TOTAL 个文件)"
    ((HIGH_RISK++))
  else
    echo "  ✅ 备份文件已加密或无备份"
  fi
fi
echo ""

# 4. 检查双因素认证
echo "4. 检查双因素认证..."
echo "  🟡 中风险：请手动检查 GitHub 2FA 状态"
echo "  检查地址：https://github.com/settings/security"
((MEDIUM_RISK++))
echo ""

# 5. 检查安全日志
echo "5. 检查安全日志..."
if [ ! -f "/var/log/security.log" ] && [ ! -f "/home/wufei/.openclaw/workspace/logs/security.log" ]; then
  echo "  🟡 中风险：缺少安全日志"
  ((MEDIUM_RISK++))
else
  echo "  ✅ 安全日志存在"
fi
echo ""

# 6. 检查输出过滤
echo "6. 检查 AI 输出过滤..."
echo "  🟠 高风险：缺少输出内容过滤"
((HIGH_RISK++))
echo ""

# 7. 检查网络隔离
echo "7. 检查网络隔离..."
echo "  🟡 中风险：缺少网络隔离配置"
((MEDIUM_RISK++))
echo ""

# 总结
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "安全审计完成"
echo ""
echo "风险汇总:"
echo "  总风险数：$((HIGH_RISK + MEDIUM_RISK))"
echo "  高风险：$HIGH_RISK"
echo "  中风险：$MEDIUM_RISK"
echo ""

if [ $HIGH_RISK -gt 0 ]; then
  echo "🟠 发现高风险！建议立即修复"
elif [ $MEDIUM_RISK -gt 0 ]; then
  echo "🟡 发现中风险！建议本周修复"
else
  echo "✅ 无明显风险"
fi
