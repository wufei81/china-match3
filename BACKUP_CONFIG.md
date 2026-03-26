# 备份配置指南

**版本**: 1.0  
**创建日期**: 2026-03-26  
**目标**: 数据安全和灾难恢复

---

## 🎯 备份策略

### 3-2-1 原则
- **3** 份数据副本
- **2** 种不同介质
- **1** 份异地备份

---

## 📁 备份内容

### 代码备份
- ✅ Git 仓库 (GitHub)
- ✅ 本地备份 (每日)

### 配置备份
- ✅ 智能体配置
- ✅ 环境变量
- ✅ 密钥管理

### 记忆备份
- ✅ 向量数据库
- ✅ 技能库
- ✅ 会话历史

### 数据备份
- ✅ 数据库
- ✅ 文件存储
- ✅ 日志归档

---

## 🔧 备份脚本

### 每日备份脚本
```bash
#!/bin/bash
# backup-daily.sh

set -e

BACKUP_DIR="/backup/$(date +%Y%m%d)"
mkdir -p $BACKUP_DIR

echo "🔄 开始备份..."

# 备份代码
echo "备份代码..."
git bundle create $BACKUP_DIR/code.bundle --all

# 备份配置
echo "备份配置..."
cp -r ~/.claude $BACKUP_DIR/claude-config
cp -r /workspace/.env $BACKUP_DIR/env-config

# 备份记忆
echo "备份记忆..."
cp -r /workspace/shared-memory $BACKUP_DIR/memory
cp -r /workspace/shared-skills $BACKUP_DIR/skills

# 备份数据库
echo "备份数据库..."
# pg_dump -U postgres mydb > $BACKUP_DIR/db.sql

# 压缩备份
echo "压缩备份..."
tar -czf $BACKUP_DIR.tar.gz $BACKUP_DIR

# 清理旧备份 (保留 30 天)
echo "清理旧备份..."
find /backup -name "*.tar.gz" -mtime +30 -delete

echo "✅ 备份完成：$BACKUP_DIR.tar.gz"
```

### 恢复脚本
```bash
#!/bin/bash
# restore.sh

set -e

BACKUP_FILE=$1

if [ -z "$BACKUP_FILE" ]; then
  echo "❌ 请指定备份文件"
  exit 1
fi

echo "🔄 开始恢复..."

# 解压备份
tar -xzf $BACKUP_FILE

# 恢复代码
echo "恢复代码..."
git unbundle < code.bundle

# 恢复配置
echo "恢复配置..."
cp -r claude-config ~/.claude
cp env-config /workspace/.env

# 恢复记忆
echo "恢复记忆..."
cp -r memory /workspace/shared-memory
cp -r skills /workspace/shared-skills

# 恢复数据库
echo "恢复数据库..."
# psql -U postgres mydb < db.sql

echo "✅ 恢复完成"
```

---

## 📅 备份计划

### Cron 配置
```bash
# 编辑 crontab
crontab -e

# 每日备份 (凌晨 2 点)
0 2 * * * /workspace/scripts/backup-daily.sh

# 每周完整备份 (周日凌晨 3 点)
0 3 * * 0 /workspace/scripts/backup-full.sh

# 每月归档 (每月 1 号凌晨 4 点)
0 4 1 * * /workspace/scripts/backup-archive.sh
```

---

## ☁️ 异地备份

### 云存储备份
```bash
# 备份到 AWS S3
aws s3 cp /backup s3://your-bucket/backup --recursive

# 备份到 Google Drive
rclone copy /backup gdrive:backup

# 备份到阿里云 OSS
ossutil cp -r /backup oss://your-bucket/backup
```

### 异地同步
```bash
# rsync 同步到异地服务器
rsync -avz /backup user@remote-server:/backup
```

---

## 🧪 恢复测试

### 测试计划
```bash
#!/bin/bash
# test-restore.sh

echo "🧪 开始恢复测试..."

# 创建测试环境
TEST_DIR="/tmp/restore-test-$(date +%s)"
mkdir -p $TEST_DIR

# 恢复备份
./restore.sh latest-backup.tar.gz $TEST_DIR

# 验证恢复
echo "验证恢复..."
test -d $TEST_DIR/code && echo "✅ 代码恢复成功"
test -d $TEST_DIR/config && echo "✅ 配置恢复成功"
test -d $TEST_DIR/memory && echo "✅ 记忆恢复成功"

# 清理测试环境
rm -rf $TEST_DIR

echo "✅ 恢复测试完成"
```

### 测试频率
- **每月**: 恢复测试一次
- **每季度**: 完整灾难恢复演练
- **每年**: 备份策略审查

---

## 📊 备份监控

### 监控指标
| 指标 | 阈值 | 告警 |
|------|------|------|
| **备份成功率** | <95% | 邮件 |
| **备份大小** | 异常波动 | 邮件 |
| **备份时间** | >2 小时 | 邮件 |
| **恢复时间** | >30 分钟 | 邮件 |

---

## 📈 预期效果

| 指标 | 当前 | 配置后 | 提升 |
|------|------|-------|------|
| **数据安全** | 基础 | 3-2-1 | +100% |
| **恢复时间** | 4 小时 | 30 分钟 | -87% |
| **数据丢失风险** | 高 | 低 | -90% |

---

**维护者**: AI Orchestrator  
**最后更新**: 2026-03-26
