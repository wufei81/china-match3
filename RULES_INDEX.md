# 📋 规则文档索引 (Rules Index)

> **版本**: 1.0 **创建日期**: 2026-03-20 **目的**: 统一规则文档导航，避免重复查找

---

## 🎯 规则体系层级

```
Level 1: 核心规则 (唯一来源)
    ↓ 引用
Level 2: 角色规范 (角色特定)
    ↓ 引用
Level 3: 快速参考 (会话启动)
    ↓ 引用
Level 4: 执行模板 (项目级)
```

---

## 📚 Level 1: 核心规则 (唯一来源)

### memory/CORE_RULES.md

**位置**: `/home/wufei/.openclaw/workspace/memory/CORE_RULES.md`

**内容**:

- ⛔ 三条红线 + 安全基线
- 🎯 6 阶段开发流程 (英文)
- 📋 5 个质量门禁
- 🔧 必备模板清单
- 🚨 违规处理

**特点**:

- ✅ **唯一来源** - 所有规则以此为准
- ✅ **全局共享** - 所有智能体读同一份
- ✅ **持久化** - memory 系统存储
- ✅ **支持检索** - 语义搜索

**更新原则**: 规则变更只改此处

---

## 📚 Level 2: 角色规范 (9 个文件)

### agents/product-manager/AGENTS.md

**内容**: Phase 0 需求澄清 + PRD 标准 + WorkPackages **特定职责**: AC E2E 可验证 + 5 点需求明确

### agents/architect/AGENTS.md

**内容**: Phase 1-3 架构设计 + 自验证 + tech-leader 评审 **特定职责**: 字段级合同 + SECURITY_CHECKLIST Phase 1

### agents/tech-leader/AGENTS.md

**内容**: 架构评审 + 代码审查 + 6 阶段监督 **特定职责**: 安全评审签字 + 流程合规监督

### agents/dev-engineer/AGENTS.md

**内容**: 完整 Phase 0-6 + E2E 自验证 + VALIDATION_LOG **特定职责**: 6 阶段执行 + 开发者 E2E 测试

### agents/qa-engineer/AGENTS.md

**内容**: Phase 5 验证 + 交付前检查 + 独立 E2E **特定职责**: VALIDATION_LOG 验证 + QA 独立测试

### agents/devops-engineer/AGENTS.md

**内容**: Phase 5 部署 + 10 大类检查 + 发布评审 **特定职责**: DEPLOYMENT_READINESS + 发布否决权

### agents/ai-orchestrator/AGENTS.md

**内容**: 流程监督 + 自动初始化 + 进度追踪 **特定职责**: 项目自动初始化 + 5 门禁验证

### agents/project-manager/AGENTS.md

**内容**: 整体进度 + ProjectPackages + 风险管理 **特定职责**: 任务分配 + 里程碑追踪

### agents/ui-ux-designer/AGENTS.md

**内容**: Phase 0-5 设计 + 令牌/状态 + 技术评审 **特定职责**: 设计令牌代码化 + 所有状态定义

**更新原则**: 仅更新角色特定流程，核心规则引用 Level 1

---

## 📚 Level 3: 快速参考 (9 个文件)

### agents/\*/BOOTSTRAP.md

**位置**: `agents/<agent>/BOOTSTRAP.md`

**内容**:

- 🧠 会话启动自动读取
- ⛔ 核心规则链接 (引用 Level 1)
- 🎯 角色关键职责 (3-5 点)
- ✅ 快速检查清单
- 📚 完整文档链接

**特点**:

- ✅ 简洁 (快速加载)
- ✅ 链接到完整规则
- ✅ 每次会话必读

**更新原则**: 仅更新快速检查清单，规则引用 Level 1

---

## 📚 Level 4: 执行模板 (项目级)

### 项目模板文件

**位置**: `<project>/docs/*.md`

**文件清单**:

- `CODEBASE_INDEX.md` - 代码库索引
- `VALIDATION_LOG.md` - 验证日志
- `TASK_TRACKER.md` - 任务追踪
- `ERROR_LOG.md` - 错误记录
- `SECURITY_CHECKLIST.md` - 安全检查
- `CODE_REVIEW_CHECKLIST.md` - 代码审查
- `INTEGRATION_TEST_PLAN.md` - 集成测试
- `DEPLOYMENT_READINESS.md` - 部署就绪
- `DEVELOPMENT_PROCESS_CHECKLIST.md` - 6 阶段流程

**特点**:

- ✅ 项目级执行
- ✅ 填写式检查
- ✅ 可追溯

**更新原则**: 模板变更需同步更新所有项目 (或下次初始化时)

---

## 📚 其他重要文档

### 协作协议

**位置**: `/home/wufei/.openclaw/workspace/COLLABORATION_PROTOCOL.md` **内容**: 完整协作流程 + 5 门禁 + 4 清单 + 6 阶段

### 6 阶段详解 (中文)

**位置**: `/home/wufei/.openclaw/workspace/DEVELOPMENT_PROCESS_CHECKLIST.md` **内容**: 6 阶段详细流程 (中文版本)

### 英文规则摘要

**位置**: `/home/wufei/.openclaw/workspace/ENGLISH_RULES_SUMMARY.md` **内容**: 6 阶段流程 (英文版本)

### 自动初始化方案

**位置**: `/home/wufei/.openclaw/workspace/AUTO_INIT_PLAN.md` **内容**: 自动检测 + 自动初始化流程

### 开发者 E2E 方案

**位置**: `/home/wufei/.openclaw/workspace/DEVELOPER_E2E_SELF_VERIFICATION.md` **内容**: dev-engineer E2E 自验证 +
qa-engineer 独立验证

### P0+P1 优化总结

**位置**: `/home/wufei/.openclaw/workspace/P0_P1_OPTIMIZATION_COMPLETE.md` **内容**: P0+P1 优先级优化完成总结

---

## 🔄 更新流程

### 核心规则变更

```
1. 更新 memory/CORE_RULES.md
   ↓
2. 更新版本号和日期
   ↓
3. 通知所有智能体 (通过 ai-orchestrator)
   ↓
4. 更新项目模板 (下次初始化时同步)
```

### 角色规范变更

```
1. 更新 agents/<agent>/AGENTS.md
   ↓
2. 确保引用 CORE_RULES.md (不复制)
   ↓
3. 更新相关 BOOTSTRAP.md
   ↓
4. 测试流程是否生效
```

### 快速参考变更

```
1. 更新 agents/<agent>/BOOTSTRAP.md
   ↓
2. 确保链接到最新 CORE_RULES.md
   ↓
3. 保持简洁 (仅关键 3-5 点)
   ↓
4. 验证会话启动读取正常
```

---

## 📊 文档维护责任

| 文档类型          | 维护者                        | 更新频率        |
| ----------------- | ----------------------------- | --------------- |
| **CORE_RULES.md** | tech-leader + ai-orchestrator | 低 (规则稳定)   |
| **AGENTS.md**     | 各智能体 + tech-leader        | 中 (流程优化时) |
| **BOOTSTRAP.md**  | 各智能体                      | 低 (引用为主)   |
| **项目模板**      | tech-leader                   | 低 (模板稳定)   |
| **其他文档**      | ai-orchestrator               | 中 (持续改进)   |

---

## 🎯 快速导航

### 按角色查找

| 角色            | AGENTS.md                                | BOOTSTRAP.md                                |
| --------------- | ---------------------------------------- | ------------------------------------------- |
| product-manager | [链接](agents/product-manager/AGENTS.md) | [链接](agents/product-manager/BOOTSTRAP.md) |
| architect       | [链接](agents/architect/AGENTS.md)       | [链接](agents/architect/BOOTSTRAP.md)       |
| tech-leader     | [链接](agents/tech-leader/AGENTS.md)     | [链接](agents/tech-leader/BOOTSTRAP.md)     |
| dev-engineer    | [链接](agents/dev-engineer/AGENTS.md)    | [链接](agents/dev-engineer/BOOTSTRAP.md)    |
| qa-engineer     | [链接](agents/qa-engineer/AGENTS.md)     | [链接](agents/qa-engineer/BOOTSTRAP.md)     |
| devops-engineer | [链接](agents/devops-engineer/AGENTS.md) | [链接](agents/devops-engineer/BOOTSTRAP.md) |
| ai-orchestrator | [链接](agents/ai-orchestrator/AGENTS.md) | [链接](agents/ai-orchestrator/BOOTSTRAP.md) |
| project-manager | [链接](agents/project-manager/AGENTS.md) | [链接](agents/project-manager/BOOTSTRAP.md) |
| ui-ux-designer  | [链接](agents/ui-ux-designer/AGENTS.md)  | [链接](agents/ui-ux-designer/BOOTSTRAP.md)  |

### 按用途查找

| 用途           | 文档                                                                     |
| -------------- | ------------------------------------------------------------------------ |
| **核心规则**   | [memory/CORE_RULES.md](memory/CORE_RULES.md)                             |
| **完整流程**   | [COLLABORATION_PROTOCOL.md](COLLABORATION_PROTOCOL.md)                   |
| **6 阶段详解** | [DEVELOPMENT_PROCESS_CHECKLIST.md](DEVELOPMENT_PROCESS_CHECKLIST.md)     |
| **英文规则**   | [ENGLISH_RULES_SUMMARY.md](ENGLISH_RULES_SUMMARY.md)                     |
| **自动初始化** | [AUTO_INIT_PLAN.md](AUTO_INIT_PLAN.md)                                   |
| **开发者 E2E** | [DEVELOPER_E2E_SELF_VERIFICATION.md](DEVELOPER_E2E_SELF_VERIFICATION.md) |
| **优化总结**   | [P0_P1_OPTIMIZATION_COMPLETE.md](P0_P1_OPTIMIZATION_COMPLETE.md)         |

---

**版本**: 1.0 **最后更新**: 2026-03-20 **维护者**: ai-orchestrator **下次审查**: 首个试点项目完成后
