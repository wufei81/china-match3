# PROJECT_STARTUP_CHECKLIST.md

> **维护说明**:
>
> - 填写者：`ai-orchestrator` (主导) + `project-manager`
> - 时机：**第一个任务开始前** (硬性门禁)
> - 用途：确保新项目正确初始化，所有模板就位，团队了解流程
> - **未完成前禁止开始任何开发任务**

---

## 🚨 项目初始化检查 (HARD GATE)

**⛔ 此检查清单完成前，禁止开始 Phase 1 (需求定义)**

### 1. 项目结构检查

| 检查项                  | 预期                                        | 实际 | 状态 |
| ----------------------- | ------------------------------------------- | ---- | ---- |
| 项目目录已创建          | `/home/wufei/.openclaw/workspace/<project>` |      | ⬜   |
| PROJECT_CONFIG.md 存在  | 项目根目录                                  |      | ⬜   |
| QUICK_REFERENCE.md 存在 | 项目根目录                                  |      | ⬜   |
| docs/ 目录存在          | 项目根目录/docs/                            |      | ⬜   |
| src/ 目录存在           | 项目根目录/src/                             |      | ⬜   |
| tests/ 目录存在         | 项目根目录/tests/                           |      | ⬜   |
| .gitignore 存在         | 项目根目录                                  |      | ⬜   |
| Git 仓库初始化          | .git/ 目录                                  |      | ⬜   |

**检查命令**:

```bash
cd /home/wufei/.openclaw/workspace/<project>
ls -la
ls -la docs/
```

---

### 2. 模板文件检查

| 模板文件                         | 用途           | 状态 |
| -------------------------------- | -------------- | ---- |
| CODEBASE_INDEX.md                | 代码库索引     | ⬜   |
| VALIDATION_LOG.md                | 自动化验证日志 | ⬜   |
| TASK_TRACKER.md                  | 任务状态追踪   | ⬜   |
| ERROR_LOG.md                     | 错误记录与恢复 | ⬜   |
| SECURITY_CHECKLIST.md            | 安全基线检查   | ⬜   |
| CODE_REVIEW_CHECKLIST.md         | 代码审查       | ⬜   |
| INTEGRATION_TEST_PLAN.md         | 集成/E2E 测试  | ⬜   |
| DEPLOYMENT_READINESS.md          | 部署就绪检查   | ⬜   |
| DEVELOPMENT_PROCESS_CHECKLIST.md | 6 阶段流程参考 | ⬜   |

**检查命令**:

```bash
cd /home/wufei/.openclaw/workspace/<project>/docs
ls -la *.md
```

---

### 3. 团队流程培训

**确认所有参与智能体了解以下流程**:

| 智能体          | 必须了解的内容                   | 确认方式       | 状态 |
| --------------- | -------------------------------- | -------------- | ---- |
| product-manager | PRD 格式 + AC 要求               | 阅读 AGENTS.md | ⬜   |
| architect       | 架构评审 + 安全检查              | 阅读 AGENTS.md | ⬜   |
| tech-leader     | 安全评审 + 代码审查 + 6 阶段监督 | 阅读 AGENTS.md | ⬜   |
| dev-engineer    | 6 阶段流程 + VALIDATION_LOG      | 阅读 AGENTS.md | ⬜   |
| qa-engineer     | E2E 测试 + 流程验证              | 阅读 AGENTS.md | ⬜   |
| devops-engineer | 部署就绪检查                     | 阅读 AGENTS.md | ⬜   |
| ai-orchestrator | 进度追踪 + 流程监督              | 阅读 AGENTS.md | ⬜   |
| project-manager | 整体进度 + 风险管理              | 阅读 AGENTS.md | ⬜   |

**培训方式**:

- ✅ 各智能体阅读各自 AGENTS.md 第 6+ 章节
- ✅ 阅读 `QUICK_REFERENCE.md`
- ✅ 阅读 `DEVELOPMENT_PROCESS_CHECKLIST.md`

---

### 4. 质量门禁确认

**确认 5 个质量门禁已配置**:

| 门禁             | 负责人                     | 检查清单                              | 状态 |
| ---------------- | -------------------------- | ------------------------------------- | ---- |
| Gate 1: PRD 评审 | product-manager            | -                                     | ⬜   |
| Gate 2: 架构评审 | architect + tech-leader    | SECURITY_CHECKLIST.md Phase 1         | ⬜   |
| Gate 3: 开发评审 | dev-engineer + tech-leader | CODE_REVIEW_CHECKLIST.md + 6 阶段合规 | ⬜   |
| Gate 4: 测试评审 | qa-engineer                | INTEGRATION_TEST_PLAN.md              | ⬜   |
| Gate 5: 发布评审 | devops-engineer            | DEPLOYMENT_READINESS.md               | ⬜   |

---

### 5. 安全基线确认

**确认以下安全规则已传达**:

| 安全规则                      | 违反后果              | 状态 |
| ----------------------------- | --------------------- | ---- |
| ⛔ 禁止硬编码密钥/密码        | 立即打回 + P0 blocker | ⬜   |
| ⛔ 禁止 SQL 字符串拼接        | 立即打回 + P0 blocker | ⬜   |
| ⛔ 禁止 CORS \* + credentials | 立即打回 + P0 blocker | ⬜   |
| ⛔ 禁止鉴权测试后门           | 立即打回 + P0 blocker | ⬜   |
| ⛔ 禁止默认关闭安全配置       | 立即打回 + P0 blocker | ⬜   |

---

### 6. 沟通渠道确认

| 沟通类型 | 渠道                     | 负责人          | 状态 |
| -------- | ------------------------ | --------------- | ---- |
| 日常进度 | TASK_TRACKER.md          | ai-orchestrator | ⬜   |
| 问题升级 | 直接通知用户             | ai-orchestrator | ⬜   |
| 安全审查 | SECURITY_CHECKLIST.md    | tech-leader     | ⬜   |
| 代码审查 | CODE_REVIEW_CHECKLIST.md | tech-leader     | ⬜   |
| 测试报告 | INTEGRATION_TEST_PLAN.md | qa-engineer     | ⬜   |

---

## ✅ 初始化完成确认

### 检查结论

- [ ] **通过** - 所有检查项完成，允许开始 Phase 1
- [ ] **不通过** - 存在\_\_\_项未完成，修复后重新检查

### 签字确认

| 角色            | 签字 | 日期 |
| --------------- | ---- | ---- |
| ai-orchestrator |      |      |
| project-manager |      |      |
| tech-leader     |      |      |

---

## 📝 初始化记录

**项目名称**: **\*\***\_\_\_**\*\*** **初始化日期**: **\*\***\_\_\_**\*\*** **初始化脚本版本**: 1.0 **执行命令**:
`./init-project.sh <project-name>`

**未完成项** (如有):

```
[列出所有未完成项]
```

**备注**:

```
[其他需要记录的信息]
```

---

## 🔁 变更历史

| 日期 | 变更内容 | 变更者 |
| ---- | -------- | ------ |
|      |          |        |

---

**模板版本**: 1.0 **最后更新**: 2026-03-20 **强制要求**: 所有新项目必须完成此检查清单才能开始开发
