# ⏰ 熵治理定时任务配置

## Cron 任务详情

**任务 ID**: `4538aa31-ac01-460b-83ad-a2dd3ebc5ee9`  
**任务名称**: 熵治理 - 每周自动执行  
**状态**: ✅ 已启用

---

## 执行时间

| 配置项 | 值 | 说明 |
|--------|-----|------|
| Cron 表达式 | `0 3 * * 0` | 每周日凌晨 3 点 |
| 时区 | Asia/Shanghai | 北京时间 |
| 下次执行 | 2026-04-05 03:00:00 | 本周日 |

---

## 执行内容

```bash
python3 /home/wufei/.openclaw/workspace/agents/main-agent/scripts/entropy-governance.py full --auto \
  --output /home/wufei/.openclaw/workspace/agents/main-agent/governance/entropy-report-$(date +%Y%m%d).json
```

### 治理流程

1. 🔍 **扫描文档** - 检查工作区所有文档
2. 📊 **计算熵值** - 评估文档健康度
3. 🎯 **检测漂移** - 发现配置问题
4. 🔧 **自动修复** - 执行修复建议（自动模式）
5. 📈 **生成报告** - 输出 JSON 格式报告

---

## 报告位置

```
/home/wufei/.openclaw/workspace/agents/main-agent/governance/entropy-report-YYYYMMDD.json
```

报告保留策略：**30 天自动清理**

---

## 管理命令

### 查看任务状态
```bash
openclaw cron list
```

### 查看任务历史
```bash
openclaw cron runs --jobId 4538aa31-ac01-460b-83ad-a2dd3ebc5ee9
```

### 手动触发执行
```bash
openclaw cron run --jobId 4538aa31-ac01-460b-83ad-a2dd3ebc5ee9
```

### 暂停任务
```bash
openclaw cron update --jobId 4538aa31-ac01-460b-83ad-a2dd3ebc5ee9 --patch '{"enabled": false}'
```

### 删除任务
```bash
openclaw cron remove --jobId 4538aa31-ac01-460b-83ad-a2dd3ebc5ee9
```

---

## 日志查看

执行日志位置：
```
/home/wufei/.openclaw/workspace/agents/main-agent/governance/entropy-cron.log
```

查看最新日志：
```bash
tail -50 /home/wufei/.openclaw/workspace/agents/main-agent/governance/entropy-cron.log
```

---

## 通知方式

任务执行完成后会通过 OpenClaw 系统事件通知，内容包括：
- ✅ 执行状态（成功/失败）
- 📊 治理摘要（文档数、问题数）
- 📁 报告路径

---

## 修改执行时间

### 改为每天凌晨 3 点
```bash
openclaw cron update --jobId 4538aa31-ac01-460b-83ad-a2dd3ebc5ee9 \
  --patch '{"schedule": {"kind": "cron", "expr": "0 3 * * *", "tz": "Asia/Shanghai"}}'
```

### 改为每月 1 号凌晨 3 点
```bash
openclaw cron update --jobId 4538aa31-ac01-460b-83ad-a2dd3ebc5ee9 \
  --patch '{"schedule": {"kind": "cron", "expr": "0 3 1 * *", "tz": "Asia/Shanghai"}}'
```

---

## 注意事项

1. **首次执行**: 任务已配置，将在下一个周日凌晨 3 点自动执行
2. **手动测试**: 可随时运行 `openclaw cron run --jobId <ID>` 测试
3. **报告清理**: 30 天前的报告会自动删除，避免占用空间
4. **备份安全**: 所有修复操作前都会自动备份文件

---

**🤖 Y9000P 说**: 定时任务已设置！每周日凌晨 3 点，熵治理系统会自动起来干活，你只需要周一早上看报告就行。☕

**🔜 Next you can**:
1. 运行 `openclaw cron list` 查看所有定时任务
2. 运行 `openclaw cron run --jobId 4538aa31-ac01-460b-83ad-a2dd3ebc5ee9` 手动测试一次
3. 下周一查看治理报告
