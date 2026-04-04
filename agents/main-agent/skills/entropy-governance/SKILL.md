---
name: entropy-governance
description: 熵治理系统 - 自动检测过时文档、配置漂移，生成修复建议并执行
tags: [governance, maintenance, automation, documentation]
permissions: [shell, read, write]
metadata:
  clawdbot:
    requires:
      bins: [python3, git]
      env: [WORKSPACE_ROOT]
    files: ["scripts/entropy-governance.py", "scripts/.entropy-config.json"]
  capabilities:
    allow:
      - execute: [python3, git, cp]
      - read: [workspace/**]
      - write: [workspace/**, governance/**]
    deny:
      - execute: ["!python3", "!git", "!cp", "!rm"]
      - network: ["*"]
  env_declarations:
    - name: WORKSPACE_ROOT
      required: false
      default: /home/wufei/.openclaw/workspace/agents/main-agent
      description: 工作区根目录
    - name: ENTROPY_AUTO_FIX
      required: false
      default: "false"
      description: 是否自动修复（true/false）
    - name: ENTROPY_REPORT_PATH
      required: false
      default: ./governance
      description: 报告输出目录
---

# 🧬 熵治理技能 (Entropy Governance Skill)

基于 `capability-evolver` 理念的文档自动维护技能，实现**文档熵值检测**、**配置漂移发现**、**自动修复建议**和**Agent 自主维护**。

## 功能特性

- 🔍 **文档扫描** - 自动扫描工作区所有文档
- 📊 **熵值计算** - 基于时间、内容、访问频率计算熵值
- 🎯 **漂移检测** - 发现配置文件中的占位符/过期值
- 💡 **智能建议** - 生成可执行的修复建议
- 🔧 **自动修复** - 支持自动/手动修复模式
- 📈 **治理报告** - 生成 JSON 格式的治理报告
- ⏰ **定时任务** - 支持 Cron 定期自动执行

## 使用方法

### 1. 基础扫描

```bash
cd /home/wufei/.openclaw/workspace/agents/main-agent/scripts
python3 entropy-governance.py scan
```

### 2. 完整治理流程

```bash
# 交互式修复
python3 entropy-governance.py full

# 自动修复（无需确认）
export ENTROPY_AUTO_FIX=true
python3 entropy-governance.py full --auto
```

### 3. 检测配置漂移

```bash
python3 entropy-governance.py drift
```

### 4. 生成治理报告

```bash
python3 entropy-governance.py report --output ./governance/entropy-report.json
```

## 熵值等级

| 等级 | 分数 | 说明 | 建议操作 |
|------|------|------|----------|
| 🟢 LOW | < 0.3 | 文档健康 | 无需操作 |
| 🟡 MEDIUM | 0.3-0.6 | 需要关注 | 安排审查 |
| 🟠 HIGH | 0.6-0.8 | 需要修复 | 优先处理 |
| 🔴 CRITICAL | > 0.8 | 严重过时 | 立即处理 |

## 配置选项

编辑 `scripts/.entropy-config.json`:

```json
{
  "max_age_days": 90,              // 文档最大年龄（天）
  "check_interval_days": 7,        // 检查间隔（天）
  "auto_fix": false,               // 是否自动修复
  "backup_before_fix": true,       // 修复前备份
  "ignored_patterns": [],          // 忽略的文件模式
  "critical_paths": [],            // 关键路径（优先检查）
  "entropy_thresholds": {          // 熵值阈值
    "low": 0.3,
    "medium": 0.6,
    "high": 0.8
  }
}
```

## 与 capability-evolver 集成

```python
# 在 evolver 流程中调用熵治理
from entropy_governance import EntropyGovernor

governor = EntropyGovernor(workspace_root)
report = governor.run_full_governance(auto_fix=False)

# 将治理报告作为进化信号
if report.critical_docs > 5:
    trigger_evolution("document_maintenance")
```

## Cron 定时任务

### 每周自动治理

```bash
# 编辑 crontab
crontab -e

# 添加任务（每周一上午 9 点）
0 9 * * 1 cd /home/wufei/.openclaw/workspace/agents/main-agent/scripts && \
  python3 entropy-governance.py full --output ./governance/weekly-report.json >> ./governance/cron.log 2>&1
```

### 使用 OpenClaw Cron

```bash
openclaw cron add \
  --schedule "0 9 * * 1" \
  --command "python3 /home/wufei/.openclaw/workspace/agents/main-agent/scripts/entropy-governance.py full"
```

## 输出文件

| 文件 | 说明 | 位置 |
|------|------|------|
| `.entropy-config.json` | 配置文件 | scripts/ |
| `entropy-report-YYYYMMDD.json` | 治理报告 | governance/ |
| `*.backup.TIMESTAMP` | 修复前备份 | 原文件同级目录 |

## 最佳实践

1. **定期执行** - 建议每周执行一次完整治理
2. **备份优先** - 始终启用 `backup_before_fix`
3. **关键文档加权** - 将核心文档加入 `critical_paths`
4. **渐进式修复** - 优先处理 CRITICAL 级别问题
5. **报告归档** - 保留历史报告用于趋势分析

## 故障排除

### 扫描速度慢
增加 `ignored_patterns`，排除不必要的目录

### 误报过多
调整 `entropy_thresholds` 阈值

### 自动修复失败
检查文件权限：`chmod -R u+w <workspace>`

---

**Author**: Y9000P  
**Version**: 1.0.0  
**License**: MIT
