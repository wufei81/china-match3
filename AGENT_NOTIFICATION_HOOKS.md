# 智能体间通知钩子配置

**版本**: 1.0  
**创建日期**: 2026-03-26  
**目标**: 实现智能体间自动通知，减少等待时间

---

## 🎯 通知规则

### DevEngineer → QAEngineer
```json
{
  "trigger": "VALIDATION_LOG.md 创建或更新",
  "condition": "所有检查项通过",
  "action": "通知 QAEngineer 测试就绪",
  "message": "📢 DevEngineer: 登录模块开发完成，E2E 自验证通过，请 QAEngineer 测试"
}
```

### QAEngineer → DevOpsEngineer
```json
{
  "trigger": "INTEGRATION_TEST_PLAN.md 更新",
  "condition": "E2E 测试 100% 通过",
  "action": "通知 DevOpsEngineer 部署就绪",
  "message": "📢 QAEngineer: 登录模块测试通过，P0/P1 AC 全覆盖，请 DevOpsEngineer 部署"
}
```

### Architect → TechLeader
```json
{
  "trigger": "架构文档创建或更新",
  "condition": "架构设计完成",
  "action": "通知 TechLeader 评审就绪",
  "message": "📢 Architect: IM 系统架构设计完成，请 TechLeader 评审"
}
```

### DevEngineer → Architect
```json
{
  "trigger": "CODEBASE_INDEX.md 更新",
  "condition": "新增重要模块或 API",
  "action": "通知 Architect 代码对齐",
  "message": "📢 DevEngineer: 登录模块实现完成，已更新 CODEBASE_INDEX，请 Architect 确认对齐架构"
}
```

---

## 🔧 钩子配置

### hooks.json 配置
```json
{
  "PostToolUse": [
    {
      "name": "notify-qa-on-validation",
      "matcher": "tool == \"Write\" && file_path includes \"VALIDATION_LOG.md\"",
      "hooks": [{
        "type": "command",
        "command": "#!/bin/bash\n# DevEngineer 完成，通知 QAEngineer\necho \"📢 [AUTO-NOTIFY] DevEngineer → QAEngineer\"\necho \"   任务：$(basename $(dirname $file_path))\"\necho \"   状态：开发完成，E2E 自验证通过\"\necho \"   时间：$(date '+%Y-%m-%d %H:%M:%S')\"\necho \"   请 QAEngineer 开始测试\"\n"
      }]
    },
    {
      "name": "notify-devops-on-test-pass",
      "matcher": "tool == \"Write\" && file_path includes \"INTEGRATION_TEST_PLAN.md\"",
      "hooks": [{
        "type": "command",
        "command": "#!/bin/bash\n# QAEngineer 通过，通知 DevOpsEngineer\necho \"📢 [AUTO-NOTIFY] QAEngineer → DevOpsEngineer\"\necho \"   任务：$(basename $(dirname $file_path))\"\necho \"   状态：E2E 测试 100% 通过\"\necho \"   时间：$(date '+%Y-%m-%d %H:%M:%S')\"\necho \"   请 DevOpsEngineer 准备部署\"\n"
      }]
    },
    {
      "name": "notify-techlead-on-arch",
      "matcher": "tool == \"Write\" && file_path includes \"ARCH_\" && file_path includes \".md\"",
      "hooks": [{
        "type": "command",
        "command": "#!/bin/bash\n# Architect 完成，通知 TechLeader\necho \"📢 [AUTO-NOTIFY] Architect → TechLeader\"\necho \"   任务：$(basename $file_path)\"\necho \"   状态：架构设计完成\"\necho \"   时间：$(date '+%Y-%m-%d %H:%M:%S')\"\necho \"   请 TechLeader 评审\"\n"
      }]
    },
    {
      "name": "notify-arch-on-codebase-update",
      "matcher": "tool == \"Write\" && file_path includes \"CODEBASE_INDEX.md\"",
      "hooks": [{
        "type": "command",
        "command": "#!/bin/bash\n# DevEngineer 更新代码索引，通知 Architect\necho \"📢 [AUTO-NOTIFY] DevEngineer → Architect\"\necho \"   任务：CODEBASE_INDEX 更新\"\necho \"   状态：代码实现完成，已更新索引\"\necho \"   时间：$(date '+%Y-%m-%d %H:%M:%S')\"\necho \"   请 Architect 确认对齐架构\"\n"
      }]
    }
  ],
  "SessionEnd": [
    {
      "name": "auto-learn-pattern",
      "hooks": [{
        "type": "command",
        "command": "/learn"
      }]
    }
  ]
}
```

---

## 📢 通知示例

### DevEngineer → QAEngineer
```
📢 [AUTO-NOTIFY] DevEngineer → QAEngineer
   任务：auth-module
   状态：开发完成，E2E 自验证通过
   时间：2026-03-26 19:30:00
   请 QAEngineer 开始测试
   
   ✅ npm run lint → PASSED
   ✅ npm run test → PASSED (85%)
   ✅ npm run build → PASSED
   ✅ E2E 测试 → 通过
```

### QAEngineer → DevOpsEngineer
```
📢 [AUTO-NOTIFY] QAEngineer → DevOpsEngineer
   任务：auth-module
   状态：E2E 测试 100% 通过
   时间：2026-03-26 20:00:00
   请 DevOpsEngineer 准备部署
   
   ✅ E2E 测试 → 100% 通过
   ✅ P0 AC → 100% 覆盖
   ✅ P1 AC → 95% 覆盖
   ✅ 性能测试 → 通过
   ✅ 安全测试 → 通过
```

### Architect → TechLeader
```
📢 [AUTO-NOTIFY] Architect → TechLeader
   任务：ARCH_IM_System_v1.0.md
   状态：架构设计完成
   时间：2026-03-26 15:00:00
   请 TechLeader 评审
   
   ✅ API Schema → 字段级定义
   ✅ DDL → 完整
   ✅ 一致性策略 → 明确
   ✅ 安全评审 → Phase 1 完成
```

---

## 🔗 集成到 STATE.md

### 通知状态追踪
```markdown
## 通知状态

| 时间 | 发送方 | 接收方 | 任务 | 状态 |
|------|-------|-------|------|------|
| 19:30 | DevEngineer | QAEngineer | auth-module | ✅ 已通知 |
| 20:00 | QAEngineer | DevOpsEngineer | auth-module | ✅ 已通知 |
| 15:00 | Architect | TechLeader | IM 架构 | ✅ 已通知 |
```

---

## 🚀 实施步骤

### Step 1: 更新 hooks.json (10 分钟)
```bash
# 复制上面的钩子配置到 ~/.claude/settings.json
# 或者添加到项目级 .claude/settings.json
```

### Step 2: 测试通知 (10 分钟)
```bash
# 创建测试文件
echo "测试" > /tmp/test-validation.md

# 验证钩子触发
# 应该看到通知输出
```

### Step 3: 集成到工作流 (10 分钟)
```bash
# 每个智能体在 AGENTS.md 中添加通知说明
# 示例：DevEngineer 完成开发后自动触发通知
```

---

**维护者**: AI Orchestrator  
**最后更新**: 2026-03-26  
**版本**: 1.0
