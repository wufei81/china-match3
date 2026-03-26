#!/bin/bash
# 安全加固脚本

echo "🛡️ 开始安全加固..."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# 1. 修复文件权限
echo "1. 修复敏感文件权限..."
chmod 600 ~/.claude/.env 2>/dev/null && echo "  ✅ ~/.claude/.env 权限已修复"
chmod 600 /home/wufei/.openclaw/workspace/.env 2>/dev/null && echo "  ✅ /workspace/.env 权限已修复"
chmod 600 /home/wufei/.openclaw/workspace/.claude/*.json 2>/dev/null && echo "  ✅ .claude/*.json 权限已修复"
echo ""

# 2. 创建安全日志目录
echo "2. 创建安全日志..."
mkdir -p /home/wufei/.openclaw/workspace/logs
touch /home/wufei/.openclaw/workspace/logs/security.log
chmod 640 /home/wufei/.openclaw/workspace/logs/security.log
echo "  ✅ 安全日志已创建"
echo ""

# 3. 配置输出过滤规则
echo "3. 配置输出过滤..."
cat > /home/wufei/.openclaw/workspace/security-filter-rules.txt << 'EOF'
# 输出内容过滤规则
# 敏感词过滤
password
secret
token
api_key
private_key

# 隐私数据过滤
身份证号
银行卡号
手机号
邮箱

# 有害内容过滤
暴力
违法
恶意
EOF
echo "  ✅ 过滤规则已配置"
echo ""

# 4. Token 轮换提醒
echo "4. 配置 Token 轮换提醒..."
(crontab -l 2>/dev/null; echo "0 0 1 */3 * echo 'Token 轮换提醒' >> /home/wufei/.openclaw/workspace/logs/token-rotation.log") | crontab -
echo "  ✅ Token 轮换提醒已配置 (每 90 天)"
echo ""

# 5. 备份加密配置
echo "5. 配置备份加密..."
cat >> /home/wufei/.openclaw/workspace/scripts/backup-daily.sh << 'EOF'

# 加密备份
if command -v gpg &> /dev/null; then
  gpg --symmetric --cipher-algo AES256 --batch --passphrase-file ~/.backup-passphrase $BACKUP_DIR.tar.gz
  rm -f $BACKUP_DIR.tar.gz
  echo "✅ 备份已加密"
fi
EOF
echo "  ✅ 备份加密已配置"
echo ""

# 总结
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✅ 安全加固完成"
echo ""
echo "已实施:"
echo "  ✅ 文件权限修复"
echo "  ✅ 安全日志创建"
echo "  ✅ 输出过滤配置"
echo "  ✅ Token 轮换提醒"
echo "  ✅ 备份加密配置"
echo ""
echo "建议:"
echo "  - 启用 GitHub 双因素认证"
echo "  - 配置网络隔离"
echo "  - 定期安全审计"
