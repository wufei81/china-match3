# 🧬 熵治理系统 (Entropy Governance System)

基于 `capability-evolver` 理念的文档自动维护系统，实现**文档熵值检测**、**配置漂移发现**、**自动修复建议**和**Agent 自主维护**。

## 📋 功能特性

| 功能 | 说明 | 状态 |
|------|------|------|
| 文档扫描 | 自动扫描工作区所有文档 | ✅ |
| 熵值计算 | 基于时间、内容、访问频率计算熵值 | ✅ |
| 配置漂移检测 | 发现配置文件中的占位符/过期值 | ✅ |
| 修复建议生成 | 智能生成可执行的修复建议 | ✅ |
| 自动修复 | 支持自动/手动修复模式 | ✅ |
| 治理报告 | 生成 JSON 格式的治理报告 | ✅ |
| Cron 定时任务 | 支持定期自动执行 | ✅ |

## 🚀 快速开始

### 1. 基础扫描

```bash
cd /home/wufei/.openclaw/workspace/agents/main-agent/scripts
python3 entropy-governance.py scan
```

### 2. 检测配置漂移

```bash
python3 entropy-governance.py drift
```

### 3. 完整治理流程

```bash
# 交互式修复
python3 entropy-governance.py full

# 自动修复（无需确认）
python3 entropy-governance.py full --auto
```

### 4. 生成治理报告

```bash
python3 entropy-governance.py report --output ./governance/entropy-report.json
```

## 📖 命令行参数

```bash
python3 entropy-governance.py --help

命令:
  scan    - 扫描文档并计算熵值
  drift   - 仅检测配置漂移
  fix     - 执行修复
  report  - 生成治理报告
  full    - 完整治理流程

参数:
  --workspace, -w  工作区根目录（默认：当前 agent 目录）
  --config, -c     配置文件路径
  --auto, -a       自动修复（无需确认）
  --output, -o     报告输出路径
  --verbose, -v    详细输出
```

## ⚙️ 配置文件

配置文件 `.entropy-config.json` 支持以下选项：

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
  },
  "content_freshness": {           // 内容新鲜度规则
    "stale_keywords": ["TODO", "FIXME", "XXX"]
  }
}
```

## 📊 熵值等级

| 等级 | 分数 | 说明 | 建议操作 |
|------|------|------|----------|
| 🟢 LOW | < 0.3 | 文档健康 | 无需操作 |
| 🟡 MEDIUM | 0.3-0.6 | 需要关注 | 安排审查 |
| 🟠 HIGH | 0.6-0.8 | 需要修复 | 优先处理 |
| 🔴 CRITICAL | > 0.8 | 严重过时 | 立即处理 |

## 🔍 熵值计算因子

1. **时间熵** (40%) - 基于最后修改时间
2. **内容熵** (30%) - 检测过时关键词（TODO/FIXME 等）
3. **访问熵** (20%) - 基于最后访问时间
4. **大小熵** (10%) - 异常大小的文档

## 🛠️ 配置漂移检测

自动检测以下类型的配置漂移：

| 漂移类型 | 检测内容 | 严重性 |
|----------|----------|--------|
| `missing_api_key` | API 密钥占位符 | 🔴 High |
| `placeholder_url` | 示例 URL（example.com/localhost） | 🟡 Medium |
| `placeholder_version` | 占位版本号（0.0.1/TBD） | 🟢 Low |

## 📅 Cron 定时任务

### 添加每周治理任务

```bash
# 编辑 crontab
crontab -e

# 添加任务（每周一上午 9 点执行）
0 9 * * 1 cd /home/wufei/.openclaw/workspace/agents/main-agent/scripts && python3 entropy-governance.py full --output ./governance/weekly-report.json >> ./governance/cron.log 2>&1
```

### 使用 OpenClaw Cron

```bash
# 通过 OpenClaw cron 添加
openclaw cron add --schedule "0 9 * * 1" \
  --command "python3 /home/wufei/.openclaw/workspace/agents/main-agent/scripts/entropy-governance.py full"
```

## 📁 输出文件

| 文件 | 说明 | 位置 |
|------|------|------|
| `.entropy-config.json` | 配置文件 | scripts/ |
| `entropy-report-YYYYMMDD.json` | 治理报告 | governance/ |
| `*.backup.TIMESTAMP` | 修复前备份 | 原文件同级目录 |
| `cron.log` | Cron 执行日志 | governance/ |

## 🔧 集成示例

### 1. 与 capability-evolver 集成

```python
# 在 evolver 的 evolve 流程中调用熵治理
from entropy_governance import EntropyGovernor

governor = EntropyGovernor(workspace_root)
report = governor.run_full_governance(auto_fix=False)

# 将治理报告作为进化信号
if report.critical_docs > 5:
    trigger_evolution("document_maintenance")
```

### 2. 与 OpenClaw Agent 集成

```python
# 在 agent 启动时检查熵值
@agent.on_startup
async def check_entropy():
    governor = EntropyGovernor(agent.workspace)
    report = governor.generate_report()
    
    if report.critical_docs > 0:
        await agent.notify(f"🚨 发现 {report.critical_docs} 个严重过时的文档")
```

### 3. 与 Feishu 通知集成

```python
# 发送治理报告到飞书
def send_feishu_report(report: GovernanceReport):
    webhook = os.environ.get("FEISHU_WEBHOOK")
    
    message = {
        "msg_type": "interactive",
        "card": {
            "header": {
                "title": f"🧬 熵治理报告 - {report.timestamp}",
                "template": "blue"
            },
            "elements": [
                {"tag": "div", "text": {"content": report.summary}},
                {"tag": "div", "text": {"content": f"健康文档：{report.healthy_docs} ✅"}},
                {"tag": "div", "text": {"content": f"需关注：{report.outdated_docs} ⚠️"}},
                {"tag": "div", "text": {"content": f"严重问题：{report.critical_docs} 🚨"}}
            ]
        }
    }
    
    requests.post(webhook, json=message)
```

## 🎯 最佳实践

1. **定期执行** - 建议每周执行一次完整治理
2. **备份优先** - 始终启用 `backup_before_fix`
3. **关键文档加权** - 将核心文档加入 `critical_paths`
4. **渐进式修复** - 优先处理 CRITICAL 级别问题
5. **报告归档** - 保留历史报告用于趋势分析

## 📈 治理报告示例

```json
{
  "timestamp": "2026-04-04T15:30:00",
  "total_docs": 156,
  "healthy_docs": 142,
  "outdated_docs": 11,
  "critical_docs": 3,
  "config_drifts": [
    {
      "config_file": ".env",
      "expected_value": "<实际 API 密钥>",
      "actual_value": "your_api_key",
      "drift_type": "missing_api_key",
      "severity": "high",
      "suggestion": "配置 API_KEY 为实际 API 密钥"
    }
  ],
  "actions_taken": [],
  "summary": "扫描 156 个文档，发现 14 个需要关注的文档，1 处配置漂移"
}
```

## 🐛 故障排除

### 问题：扫描速度慢

**解决**: 增加 `ignored_patterns`，排除不必要的目录

```json
"ignored_patterns": [
  "node_modules/*",
  ".git/*",
  "*.log",
  "build/*",
  "dist/*"
]
```

### 问题：误报过多

**解决**: 调整 `entropy_thresholds` 阈值

```json
"entropy_thresholds": {
  "low": 0.2,
  "medium": 0.5,
  "high": 0.7
}
```

### 问题：自动修复失败

**解决**: 检查文件权限，确保有写入权限

```bash
chmod -R u+w /home/wufei/.openclaw/workspace/agents/main-agent
```

## 📝 更新日志

### v1.0.0 (2026-04-04)
- ✅ 初始版本发布
- ✅ 文档熵值计算
- ✅ 配置漂移检测
- ✅ 修复建议生成
- ✅ 治理报告输出
- ✅ Cron 定时任务支持

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

---

**👉 Plain English**: 这个系统就像一个文档管家，定期检查你的文件是否过时、配置是否正确，然后告诉你该修什么、怎么修。你只需要喝茶看报告就行。☕

**🔜 Next you can**:
1. 运行 `python3 entropy-governance.py scan` 试试扫描效果
2. 配置 Cron 定时任务实现自动治理
3. 集成到 capability-evolver 的进化流程中
