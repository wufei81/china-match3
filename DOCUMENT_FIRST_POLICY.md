# 文档先行原则 (Document-First Policy)

> **版本**: 1.0 | **生效日期**: 2026-04-03 | **适用范围**: 所有产研智能体

**核心原则**: 所有产品研发工作必须 **文档先行** —— 文档由产研智能体协同确认之后，再进行具体的设计、开发、测试工作。

---

## 1. 为什么需要文档先行？

| 问题 | 文档先行的解法 |
| --- | --- |
| 需求理解不一致 | PRD/FSD 多方评审，对齐认知 |
| 技术方案返工 | 架构文档 + 技术评审，提前暴露风险 |
| 测试覆盖不足 | 测试计划基于需求文档，AC 可追溯 |
| 交付物与预期不符 | 文档签字为门禁，无文档不开发 |

---

## 2. 文档层级与责任矩阵

### 2.1 产品文档链

| 文档 | 主责智能体 | 协作智能体 | 批准人 | 输出阶段 |
| --- | --- | --- | --- | --- |
| **BRD** (商业需求) | `product-manager-qwen` | `strategist`, `analyst` | 人类/`strategist` | 立项 |
| **MRD** (市场需求) | `product-manager-glm` | `analyst`, `strategist` | `product-manager-qwen` | 立项后 |
| **PRD** (产品需求) | `product-manager-qwen` | `product-manager-glm`, `product-manager-kimi` | `tech-leader` + 人类 | 需求冻结 |
| **FSD** (功能规格) | `product-manager-glm` | `architect`, `ui-ux-designer-qwen` | `product-manager-qwen` | 设计前 |

### 2.2 技术文档链

| 文档 | 主责智能体 | 协作智能体 | 批准人 | 输出阶段 |
| --- | --- | --- | --- | --- |
| **架构文档** | `architect` | `tech-leader`, `dev-engineer-*` | `tech-leader` | FSD 后 |
| **API 契约** (OpenAPI) | `architect` | `dev-engineer-*` | `tech-leader` | 架构后 |
| **数据模型** (DDL/ERD) | `architect` | `dev-engineer-*` | `tech-leader` | 架构后 |
| **测试计划** | `qa-engineer` | `product-manager-qwen`, `dev-engineer-*` | `tech-leader` | 开发前 |

### 2.3 设计文档链

| 文档 | 主责智能体 | 协作智能体 | 批准人 | 输出阶段 |
| --- | --- | --- | --- | --- |
| **UI 规范** | `ui-ux-designer-qwen` | `product-manager-glm` | `product-manager-qwen` | FSD 后 |
| **交互原型** | `ui-ux-designer-kimi` | `product-manager-glm` | `product-manager-qwen` | UI 规范后 |

---

## 3. 协同确认流程

### Phase 1: 文档起草 (隔离上下文)

```
→ 主责智能体独立撰写文档
→ 不参考其他智能体方案 (避免锚定效应)
→ 输出完整草案
```

### Phase 2: 多方评审 (公开辩论)

```
→ 所有协作智能体阅读草案
→ 每个智能体必须提出:
  - ✅ 认可的部分
  - ⚠️ 疑虑/风险点
  - ❌ 反对意见 + 理由
→ 主责智能体回应/修改
→ 允许被说服、修改立场
```

### Phase 3: 融合收敛

```
→ 提取各方案最优部分
→ 解决冲突点 (明确记录决策理由)
→ 输出最终版文档
→ 批准人签字
```

### Phase 4: 文档冻结

```
→ 文档存入 `docs/` 或项目仓库
→ 版本号 + 日期 + 签字记录
→ 后续变更需走变更流程
```

---

## 4. 门禁规则 (不可违背)

| 阶段 | 门禁条件 | 执行检查 |
| --- | --- | --- |
| **需求 → 设计** | PRD + FSD 已评审签字 | `ai-orchestrator` 检查 |
| **设计 → 开发** | 架构文档 + API 契约 + 数据模型 已评审签字 | `tech-leader` 检查 |
| **开发 → 测试** | 测试计划已评审 + 开发自验通过 | `qa-engineer` 检查 |
| **测试 → 发布** | E2E 测试通过 + 所有文档归档 | `devops-engineer` 检查 |

**违反处理**:
- 无文档进入下一阶段 → `project-manager` 记录为 P0 风险
- 文档未签字即开发 → `tech-leader` 有权叫停
- 变更未走流程 → 所有智能体有责任提醒

---

## 5. 文档模板索引

| 文档 | 模板路径 |
| --- | --- |
| PRD | `@workspace/templates/PRD.template.md` |
| FSD | `@workspace/templates/FSD.template.md` |
| 架构文档 | `@workspace/templates/ARCHITECTURE.template.md` |
| API 契约 | `@workspace/templates/API_SPEC.template.md` |
| 测试计划 | `@workspace/templates/TEST_PLAN.template.md` |

---

## 6. 各智能体职责速查

| 智能体 | 文档先行职责 |
| --- | --- |
| `product-manager-*` | 确保 PRD/FSD 完整、可验证、多方评审 |
| `architect` | 确保技术文档覆盖所有功能点、可落地 |
| `tech-leader` | 批准技术文档、检查门禁、叫停违规 |
| `dev-engineer-*` | 无文档不开发、开发前阅读并理解文档 |
| `qa-engineer` | 基于文档编写测试用例、追溯 AC |
| `ui-ux-designer-*` | 基于 FSD 输出设计文档 |
| `project-manager` | 跟踪文档进度、记录风险 |
| `ai-orchestrator` | 协调全链路执行文档先行、检查门禁 |
| `devops-engineer` | 发布前检查文档归档 |

---

## 7. 例外情况

**仅限以下场景可跳过完整文档流程**:

| 场景 | 简化要求 | 批准人 |
| --- | --- | --- |
| P0 紧急修复 | 简要记录问题 + 方案 (≥200 字) | `tech-leader` |
| 微小优化 (≤1h) | PR/Commit Message 说明 | `tech-leader` |
| 探索性实验 | 实验记录文档 | `architect` |

**原则**: 例外需 **事后补文档** (48 小时内)

---

## 8. 执行检查清单

每个智能体在开始工作前，必须自检:

- [ ] 所需文档是否已完成？
- [ ] 文档是否经过评审签字？
- [ ] 我是否已阅读并理解文档？
- [ ] 我的工作是否可追溯到文档中的需求/设计？

**无文档 = 不开始**

---

> 📌 **本政策为产研智能体共识，写入各智能体 AGENTS.md 作为核心约束**
