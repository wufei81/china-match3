# 🎯 P1 优化方案 - AGENTS.md 去重

> **版本**: 1.0 **日期**: 2026-03-20 **目标**: 减少 AGENTS.md 重复内容，聚焦角色特定规范

---

## 📊 当前状态分析

### 文件体积统计

| 智能体              | 行数      | 字符数     | 重复度估计   |
| ------------------- | --------- | ---------- | ------------ |
| **dev-engineer**    | 449       | ~35KB      | 🔴 高 (60%)  |
| **ai-orchestrator** | 381       | ~30KB      | 🔴 高 (55%)  |
| **tech-leader**     | 228       | ~18KB      | 🟡 中 (45%)  |
| **qa-engineer**     | 292       | ~23KB      | 🔴 高 (50%)  |
| **ui-ux-designer**  | 193       | ~15KB      | 🟡 中 (40%)  |
| **devops-engineer** | 136       | ~11KB      | 🟡 中 (35%)  |
| **product-manager** | 136       | ~11KB      | 🟡 中 (35%)  |
| **architect**       | 134       | ~10KB      | 🟡 中 (35%)  |
| **project-manager** | 120       | ~9KB       | 🟡 中 (30%)  |
| **mobile-agent**    | 51        | ~4KB       | 🟢 低 (10%)  |
| **总计**            | **2,120** | **~166KB** | **平均 45%** |

---

## 🔍 识别的重复内容

### 重复 1: 核心规则引用

**出现位置**: 所有 9 个 AGENTS.md 第 2 节

**当前**:

```markdown
### 🧠 Every Session Start (MANDATORY)

**Before any task**:

1. Read `@workspace/memory/CORE_RULES.md` (core rules)
2. Read `@workspace/agents/<agent>/AGENTS.md` (this file) ...
```

**优化**:

```markdown
### 🧠 Every Session Start (MANDATORY)

**自动读取**:

1. `@workspace/memory/CORE_RULES.md` (核心规则 - 唯一来源)
2. 本文件 (角色规范)
3. `TASK_TRACKER.md` (项目状态)

**快速参考**: `@workspace/agents/<agent>/BOOTSTRAP.md`
```

**收益**: 减少 30% 重复

---

### 重复 2: 6 阶段流程详解

**出现位置**: dev-engineer, architect, qa-engineer 等

**当前**: 每个文件都有完整 6 阶段说明

**优化**:

```markdown
## 🎯 6 阶段开发流程

**完整流程**: `@workspace/DEVELOPMENT_PROCESS_CHECKLIST.md`

**你的关键阶段**:

- Phase 0: 需求澄清 (5 点)
- Phase 4: 编码 (增量)
- Phase 5: 验证 (4 层)
```

**收益**: 减少 50% 重复

---

### 重复 3: 自验证检查清单

**出现位置**: 所有 9 个 AGENTS.md

**当前**: 每个文件都有完整检查清单

**优化**:

```markdown
### 🔴 PRE-DELIVERY SELF-VERIFICATION

**完整清单**: `@workspace/VALIDATION_LOG.template.md`

**你的关键检查**:

- [ ] 单元测试通过
- [ ] API 集成测试通过
- [ ] 主路径冒烟测试通过
```

**收益**: 减少 40% 重复

---

### 重复 4: 质量门禁说明

**出现位置**: 所有 9 个 AGENTS.md

**当前**: 每个文件都有 5 个门禁详解

**优化**:

```markdown
## 📋 质量门禁

**完整门禁**: `@workspace/COLLABORATION_PROTOCOL.md`

**你的关键门禁**:

- Gate 2: 架构评审 (architect)
- Gate 3: 开发评审 (dev-engineer)
- Gate 4: 测试评审 (qa-engineer)
```

**收益**: 减少 60% 重复

---

## 🎯 优化策略

### 策略 1: 引用模式

**原则**: 核心规则、流程、清单都引用，仅保留角色特定内容

**示例**:

```markdown
## 核心规则

**唯一来源**: `@workspace/memory/CORE_RULES.md`

**你的 3 条关键规则**:

1. [角色特定规则 1]
2. [角色特定规则 2]
3. [角色特定规则 3]
```

---

### 策略 2: 分层结构

**Level 1**: CORE_RULES.md (唯一来源) **Level 2**: AGENTS.md (角色特定) **Level 3**: BOOTSTRAP.md (快速参考)

**AGENTS.md 内容**:

- ✅ 角色特定职责
- ✅ 角色特定流程
- ✅ 角色特定检查清单
- ❌ 不复制核心规则
- ❌ 不复制通用流程

---

### 策略 3: 标准化章节

**标准结构**:

```markdown
# AGENTS.md - <agent>

## 0. Delivery Priority

[引用 CORE_RULES.md + 角色特定优先级]

## 1. Core Identity

[角色定位 + 核心使命 + 边界]

## 2. Operating Protocol

[引用 CORE_RULES.md + 角色特定流程]

## 3. Output Specifications

[角色特定交付物标准]

## 4. Toolchains

[角色特定工具链]

## 5. Example

[角色特定示例]

## 6. 🚨 Collaboration Protocol

[引用 COLLABORATION_PROTOCOL.md + 角色特定责任]
```

---

## 📋 优化实施计划

### Phase 1: 高重复文件 (P1-1)

**目标**: dev-engineer, ai-orchestrator, qa-engineer, tech-leader

**预计收益**: 减少 50% 体积

**实施步骤**:

1. 识别重复内容 (核心规则、6 阶段、门禁)
2. 替换为引用
3. 保留角色特定内容
4. 验证功能正常

---

### Phase 2: 中重复文件 (P1-2)

**目标**: ui-ux-designer, devops-engineer, product-manager, architect

**预计收益**: 减少 40% 体积

**实施步骤**: 同 Phase 1

---

### Phase 3: 低重复文件 (P1-3)

**目标**: project-manager, mobile-agent

**预计收益**: 减少 20% 体积

**实施步骤**: 同 Phase 1

---

## 📊 预期收益

### 文件体积对比

| 智能体              | 优化前       | 优化后        | 减少     |
| ------------------- | ------------ | ------------- | -------- |
| **dev-engineer**    | 449 行       | ~225 行       | -50%     |
| **ai-orchestrator** | 381 行       | ~190 行       | -50%     |
| **tech-leader**     | 228 行       | ~125 行       | -45%     |
| **qa-engineer**     | 292 行       | ~146 行       | -50%     |
| **ui-ux-designer**  | 193 行       | ~116 行       | -40%     |
| **devops-engineer** | 136 行       | ~88 行        | -35%     |
| **product-manager** | 136 行       | ~88 行        | -35%     |
| **architect**       | 134 行       | ~87 行        | -35%     |
| **project-manager** | 120 行       | ~96 行        | -20%     |
| **总计**            | **2,120 行** | **~1,161 行** | **-45%** |

---

### 维护成本对比

| 指标             | 优化前  | 优化后         | 改善 |
| ---------------- | ------- | -------------- | ---- |
| **平均文件体积** | 213 行  | 116 行         | -45% |
| **重复内容**     | 45%     | <10%           | -78% |
| **更新工作量**   | 改 9 处 | 改 1 处 + 引用 | -89% |
| **阅读时间**     | 30 分钟 | 15 分钟        | -50% |

---

## 🎯 保持的原则

### 不优化的内容

| 内容               | 原因               |
| ------------------ | ------------------ |
| **角色特定流程**   | 必须详细，不能引用 |
| **自验证检查清单** | 执行层，需完整     |
| **评审门禁要求**   | 强制责任，需明确   |
| **工具链说明**     | 角色特定，需详细   |
| **示例**           | 角色特定，需具体   |

### 优化的内容

| 内容             | 优化方式                              |
| ---------------- | ------------------------------------- |
| **核心规则**     | 引用 CORE_RULES.md                    |
| **6 阶段流程**   | 引用 DEVELOPMENT_PROCESS_CHECKLIST.md |
| **质量门禁**     | 引用 COLLABORATION_PROTOCOL.md        |
| **通用检查清单** | 引用模板文件                          |
| **会话启动说明** | 标准化 + 引用                         |

---

## 📋 实施检查清单

### P1-1: 高重复文件

- [ ] dev-engineer/AGENTS.md 去重
- [ ] ai-orchestrator/AGENTS.md 去重
- [ ] qa-engineer/AGENTS.md 去重
- [ ] tech-leader/AGENTS.md 去重

### P1-2: 中重复文件

- [ ] ui-ux-designer/AGENTS.md 去重
- [ ] devops-engineer/AGENTS.md 去重
- [ ] product-manager/AGENTS.md 去重
- [ ] architect/AGENTS.md 去重

### P1-3: 低重复文件

- [ ] project-manager/AGENTS.md 去重
- [ ] mobile-agent/AGENTS.md (可选)

---

## 🚀 实施建议

### 推荐方式：分阶段实施

**阶段 1**: 优化 dev-engineer (最大文件)

- 收益最高 (-50%)
- 风险可控 (保持角色特定内容)
- 可作为模板

**阶段 2**: 优化其他高重复文件

- 应用阶段 1 经验
- 批量优化

**阶段 3**: 优化中低重复文件

- 选择性优化
- 保持可读性

---

### 替代方式：一次性重构

**优点**:

- 快速完成
- 统一标准

**缺点**:

- 风险较高
- 测试工作量大

**建议**: 分阶段实施 (更稳妥)

---

## 📈 成功标准

### 量化指标

| 指标               | 目标值 |
| ------------------ | ------ |
| **总体积减少**     | ≥40%   |
| **重复内容减少**   | ≥70%   |
| **维护成本降低**   | ≥80%   |
| **规则执行力保持** | 100%   |

### 质化指标

| 指标           | 目标状态 |
| -------------- | -------- |
| **可读性**     | 更清晰   |
| **易维护性**   | 更容易   |
| **角色清晰度** | 不降低   |
| **智能体遵守** | 不降低   |

---

## 🎯 结论

### 推荐方案

**分阶段实施 P1 优化**:

1. ✅ 保持多层注入 (确保遵守)
2. ✅ 引用核心规则 (减少重复)
3. ✅ 聚焦角色特定 (保持清晰)
4. ✅ 标准化结构 (易于维护)

### 预期收益

- **文件体积**: -45% (2,120 行 → 1,161 行)
- **重复内容**: -78% (45% → <10%)
- **维护成本**: -89% (改 9 处 → 改 1 处)
- **阅读时间**: -50% (30 分钟 → 15 分钟)

### 风险可控

- ✅ 保持规则执行力
- ✅ 保持角色清晰度
- ✅ 保持智能体遵守度
- ✅ 渐进式优化 (可随时回滚)

---

**版本**: 1.0 **日期**: 2026-03-20 **维护者**: ai-orchestrator **建议**: 分阶段实施，从 dev-engineer 开始

**准备好开始 P1 优化了吗？** 🤖
