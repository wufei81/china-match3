#!/bin/bash
# 每日备份脚本

set -e

BACKUP_DIR="/backup/$(date +%Y%m%d)"
mkdir -p $BACKUP_DIR

echo "🔄 开始备份..."

# 备份代码
echo "备份代码..."
cd /home/wufei/.openclaw/workspace
git bundle create $BACKUP_DIR/code.bundle --all

# 备份配置
echo "备份配置..."
cp -r ~/.claude $BACKUP_DIR/ 2>/dev/null || true
cp /home/wufei/.openclaw/workspace/.env $BACKUP_DIR/ 2>/dev/null || true

# 备份记忆
echo "备份记忆..."
cp -r /home/wufei/.openclaw/workspace/shared-memory $BACKUP_DIR/ 2>/dev/null || true
cp -r /home/wufei/.openclaw/workspace/shared-skills $BACKUP_DIR/ 2>/dev/null || true

# 压缩备份
echo "压缩备份..."
cd /backup
tar -czf $(date +%Y%m%d).tar.gz $(date +%Y%m%d)

# 清理旧备份 (保留 30 天)
echo "清理旧备份..."
find /backup -name "*.tar.gz" -mtime +30 -delete

echo "✅ 备份完成：/backup/$(date +%Y%m%d).tar.gz"
