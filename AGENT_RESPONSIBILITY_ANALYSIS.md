# 🔍 智能体职责边界与验证机制分析

> **目的**: 识别类似 dev-engineer → qa-engineer 的职责分离场景 **分析维度**: 交付物、验证责任、角色混淆风险

---

## 📊 完整智能体交付链分析

### 交付链全景图

```
product-manager
    ↓ (PRD + AC)
    ├─→ architect ──→ tech-leader (评审)
    ├─→ ui-ux-designer
    │       ↓ (设计交付物)
    │   dev-engineer
    │       ↓ (开发交付物 + E2E 自验证)
    │   qa-engineer
    │       ↓ (测试报告)
    │   devops-engineer
    │       ↓ (部署完成)
    └─→ project-manager (整体进度)
            ↓
        ai-orchestrator (全流程监督)
```

---

## 🎯 已优化的场景

### ✅ dev-engineer → qa-engineer (已完成)

| 方面         | 之前             | 现在                      |
| ------------ | ---------------- | ------------------------- |
| **交付物**   | 代码 + 口头说明  | 代码 + VALIDATION_LOG.md  |
| **验证责任** | 模糊 (qa 全负责) | 清晰 (dev 自证 + qa 独立) |
| **拒绝机制** | 无               | qa 可拒绝不完整交付       |
| **职责分离** | dev 给自己打分   | dev 证明能用，qa 证明好用 |

**核心原则**: 执行者不自证清白 ✅

---

## 🔍 待优化的场景

### 场景 1: product-manager → architect/dev-engineer

**当前问题**:

| 问题                 | 表现                            | 风险              |
| -------------------- | ------------------------------- | ----------------- |
| **PRD 质量无自验证** | product-manager 写完直接交付    | AC 模糊、需求遗漏 |
| **无预评审机制**     | architect/dev-engineer 直接接收 | 返工率高          |
| **职责不清**         | product-manager 既写 PRD 又验收 | 自己给自己打分    |

**建议优化**:

```markdown
### product-manager 交付前自验证 (新增)

**必须完成才能交付**:

- [ ] AC 是 Gherkin 格式 (Given-When-Then)
- [ ] 包含数据结构草稿
- [ ] 包含 API 契约草稿
- [ ] 5 个关键点明确 (功能目标/触发方式/输入输出/失败行为/质量要求)
- [ ] WorkPackages 表格完整

### architect/dev-engineer 预评审 (新增)

**接收前验证**:

- [ ] PRD 完整性检查
- [ ] AC 可验证性检查
- [ ] 数据结构合理性检查
- [ ] API 契约清晰度检查

**如不完整 → 拒绝接收，返回 product-manager 补充**
```

---

### 场景 2: architect → dev-engineer

**当前问题**:

| 问题                     | 表现                      | 风险           |
| ------------------------ | ------------------------- | -------------- |
| **架构文档无自验证**     | architect 写完直接交付    | 字段级定义缺失 |
| **tech-leader 评审后置** | dev-engineer 开始后才评审 | 返工、停工等待 |
| **职责不清**             | architect 既设计又验收    | 缺少独立审查   |

**建议优化**:

```markdown
### architect 交付前自验证 (新增)

**必须完成才能交付**:

- [ ] API Schema 字段级定义 (类型/必填/错误码)
- [ ] DDL 完整 (表/索引/外键)
- [ ] 一致性策略明确
- [ ] 错误与重试语义定义
- [ ] SECURITY_CHECKLIST.md Phase 1 完成

### tech-leader 评审 (强制门禁)

**评审通过后 dev-engineer 才能开始**:

- [ ] 字段级合同验证
- [ ] DDL 审查
- [ ] 安全评审签字
- [ ] 记录到 TASK_TRACKER.md

**如不通过 → 打回 architect 重新设计**
```

---

### 场景 3: ui-ux-designer → dev-engineer

**当前问题**:

| 问题                 | 表现                        | 风险                       |
| -------------------- | --------------------------- | -------------------------- |
| **设计规范无自验证** | ui-ux-designer 直接交付     | 状态定义缺失、令牌不代码化 |
| **无开发可行性验证** | dev-engineer 实现时发现问题 | 返工、设计变更             |
| **职责不清**         | designer 既设计又验收       | 缺少技术视角审查           |

**建议优化**:

```markdown
### ui-ux-designer 交付前自验证 (新增)

**必须完成才能交付**:

- [ ] 设计令牌代码化 (可映射到 CSS/Tailwind)
- [ ] 所有状态定义 (default/hover/focus/loading/error/empty)
- [ ] 响应式断点明确
- [ ] 无障碍合规 (WCAG 2.1 AA 对比度)
- [ ] DesignDeliverables 表格完整

### dev-engineer 技术评审 (新增)

**接收前验证**:

- [ ] 设计令牌可实现
- [ ] 状态定义完整
- [ ] 响应式策略清晰
- [ ] 与现有组件库兼容

**如不完整 → 拒绝接收，返回 designer 补充**
```

---

### 场景 4: qa-engineer → devops-engineer

**当前问题**:

| 问题                 | 表现                     | 风险                   |
| -------------------- | ------------------------ | ---------------------- |
| **测试报告无自验证** | qa-engineer 直接交付     | E2E 覆盖不全、性能未测 |
| **发布标准模糊**     | devops-engineer 难以判断 | 带病发布风险           |
| **职责不清**         | qa 既测试又推荐发布      | 缺少独立审查           |

**建议优化**:

```markdown
### qa-engineer 交付前自验证 (新增)

**必须完成才能交付**:

- [ ] E2E 测试 100% 通过 (真实 API)
- [ ] P0 AC 全覆盖
- [ ] P1 AC 覆盖率 ≥90%
- [ ] 性能测试通过 (响应时间达标)
- [ ] 安全测试通过 (无 P0/P1 漏洞)
- [ ] INTEGRATION_TEST_PLAN.md 完整

### devops-engineer 发布评审 (新增)

**接收前验证**:

- [ ] 测试报告完整性
- [ ] E2E 通过率 100%
- [ ] 无 P0 Bug
- [ ] P1 Bug 修复率 ≥90%
- [ ] DEPLOYMENT_READINESS.md 签字

**如不完整 → 拒绝发布，返回 qa-engineer 补充**
```

---

### 场景 5: devops-engineer → 用户/生产环境

**当前问题**:

| 问题                 | 表现                     | 风险               |
| -------------------- | ------------------------ | ------------------ |
| **部署检查无自验证** | devops-engineer 直接部署 | 配置遗漏、监控缺失 |
| **无独立验证**       | 自己部署自己验收         | 缺少审查           |
| **回滚责任不清**     | 出问题时推诿             | 响应慢             |

**建议优化**:

```markdown
### devops-engineer 部署前自验证 (新增)

**必须完成才能部署**:

- [ ] DEPLOYMENT_READINESS.md 10 大类检查完成
- [ ] E2E 测试通过验证
- [ ] 密钥管理检查 (无硬编码)
- [ ] 监控告警配置完成
- [ ] 备份执行完成
- [ ] 回滚流程测试通过

### ai-orchestrator / tech-leader 发布审批 (新增)

**审批通过后才能生产部署**:

- [ ] 部署检查完整性
- [ ] 测试报告审查
- [ ] 安全评审
- [ ] 签字确认

**如不完整 → 拒绝部署，返回 devops-engineer 补充**
```

---

## 📊 完整职责分离矩阵

| 交付环节     | 执行者          | 自验证责任    | 验证者                        | 验证责任   | 否决权    |
| ------------ | --------------- | ------------- | ----------------------------- | ---------- | --------- |
| **PRD 交付** | product-manager | PRD 完整性    | architect + dev-engineer      | 可评审性   | ✅ 可拒绝 |
| **架构交付** | architect       | 字段级定义    | tech-leader                   | 安全评审   | ✅ 可拒绝 |
| **设计交付** | ui-ux-designer  | 令牌/状态完整 | dev-engineer                  | 技术可行性 | ✅ 可拒绝 |
| **开发交付** | dev-engineer    | E2E 自验证    | qa-engineer                   | 独立验证   | ✅ 可拒绝 |
| **测试交付** | qa-engineer     | 测试完整性    | devops-engineer               | 发布就绪   | ✅ 可拒绝 |
| **部署执行** | devops-engineer | 部署检查      | ai-orchestrator + tech-leader | 发布审批   | ✅ 可拒绝 |

---

## 🎯 优先级排序

### P0 (立即实施)

| 场景                              | 理由                                    | 影响                    |
| --------------------------------- | --------------------------------------- | ----------------------- |
| **architect → dev-engineer**      | 当前已有 tech-leader 评审，需强化自验证 | 高 (架构错误返工成本高) |
| **qa-engineer → devops-engineer** | 防止带病发布                            | 高 (发布风险)           |

### P1 (近期实施)

| 场景                                | 理由         | 影响              |
| ----------------------------------- | ------------ | ----------------- |
| **product-manager → architect/dev** | 减少需求返工 | 中 (需求模糊常见) |
| **ui-ux-designer → dev-engineer**   | 减少设计返工 | 中 (设计变更频繁) |

### P2 (长期优化)

| 场景                       | 理由         | 影响              |
| -------------------------- | ------------ | ----------------- |
| **devops-engineer → 生产** | 降低发布风险 | 低 (已有检查清单) |

---

## 📋 实施建议

### 阶段 1: 强化已有流程 (P0)

**architect 自验证**:

- 更新 `architect/AGENTS.md`
- 更新 `ARCHITECTURE_DELIVERABLES.template.md` (如需要)
- 明确 tech-leader 评审门禁

**qa-engineer 自验证**:

- 更新 `qa-engineer/AGENTS.md` (已部分完成)
- 更新 `INTEGRATION_TEST_PLAN.template.md`
- 明确 devops-engineer 发布评审

### 阶段 2: 新增验证流程 (P1)

**product-manager 自验证**:

- 更新 `product-manager/AGENTS.md`
- 新增 `PRD_CHECKLIST.template.md`
- 明确 architect/dev-engineer 预评审

**ui-ux-designer 自验证**:

- 更新 `ui-ux-designer/AGENTS.md`
- 更新 `DESIGN_DELIVERABLES.template.md`
- 明确 dev-engineer 技术评审

### 阶段 3: 完善发布流程 (P2)

**devops-engineer 自验证**:

- 更新 `devops-engineer/AGENTS.md` (已部分完成)
- 明确 ai-orchestrator/tech-leader 审批

---

## 🚀 预期效果

| 指标             | 当前  | 优化后 (预期) |
| ---------------- | ----- | ------------- |
| **需求返工率**   | 35%   | <15%          |
| **架构返工率**   | 25%   | <10%          |
| **设计返工率**   | 30%   | <15%          |
| **开发返工率**   | 40%   | <15%          |
| **发布失败率**   | 20%   | <5%           |
| **整体交付周期** | 10 天 | 6 天          |

---

## ✅ 总结

**核心原则**: 执行者不自证清白，交付必须验证，验证者有否决权

**已优化**: dev-engineer → qa-engineer ✅

**待优化**:

- P0: architect → dev-engineer (tech-leader 评审)
- P0: qa-engineer → devops-engineer (发布评审)
- P1: product-manager → architect/dev (需求评审)
- P1: ui-ux-designer → dev-engineer (设计评审)
- P2: devops-engineer → 生产 (发布审批)

**实施策略**: 分阶段、优先级驱动、逐步完善

---

**版本**: 1.0 **分析日期**: 2026-03-20 **维护者**: ai-orchestrator
