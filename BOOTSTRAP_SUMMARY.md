# 📋 9 个智能体 BOOTSTRAP.md 完成总结

> **版本**: 1.0 **完成日期**: 2026-03-20 **目的**: 每次会话启动时自动读取规则

---

## ✅ 已创建的 BOOTSTRAP.md 文件

| 智能体              | 文件位置                              | 核心职责              | 关键内容                         |
| ------------------- | ------------------------------------- | --------------------- | -------------------------------- |
| **product-manager** | `agents/product-manager/BOOTSTRAP.md` | 需求澄清              | Phase 0 的 5 个关键点 + PRD 标准 |
| **architect**       | `agents/architect/BOOTSTRAP.md`       | 架构设计              | Phase 1-3 + 安全评审 Gate 2      |
| **tech-leader**     | `agents/tech-leader/BOOTSTRAP.md`     | 架构守门人 + 流程监督 | 安全评审 + 代码审查 + 6 阶段监督 |
| **dev-engineer**    | `agents/dev-engineer/BOOTSTRAP.md`    | 6 阶段流程执行        | 完整 Phase 0-6 + 禁止跳步        |
| **qa-engineer**     | `agents/qa-engineer/BOOTSTRAP.md`     | 质量守门人 + 流程验证 | VALIDATION_LOG 验证 + E2E 测试   |
| **devops-engineer** | `agents/devops-engineer/BOOTSTRAP.md` | 发布守门人            | 10 大类部署检查                  |
| **ai-orchestrator** | `agents/ai-orchestrator/BOOTSTRAP.md` | 总协调 + 自动初始化   | 项目自动检测 + 流程追踪          |
| **project-manager** | `agents/project-manager/BOOTSTRAP.md` | 整体进度管理          | ProjectPackages + 风险管理       |
| **ui-ux-designer**  | `agents/ui-ux-designer/BOOTSTRAP.md`  | UI/UX 设计            | 设计需求澄清 + 设计规范          |

---

## 🎯 每个 BOOTSTRAP.md 的核心结构

### 统一结构

```markdown
# BOOTSTRAP.md - <agent> 会话启动自动执行

## 🧠 会话启动自动读取

(列出自动读取的文件)

## ⛔ 三条红线/核心职责

(该智能体的核心规则)

## 🎯 核心阶段/流程

(该智能体负责的主要阶段)

## 📋 交付物标准

(必须包含的文档/检查清单)

## 🔒 安全检查

(该智能体负责的安全检查)

## 🚨 项目初始化检查

(验证项目已初始化)

## 📚 完整文档位置

(相关文档链接)

## 🎯 快速检查清单

(每次任务前确认)
```

---

## 🤖 OpenClaw 原生机制

### 自动读取时机

**每次新会话启动时**:

1. ✅ OpenClaw 自动读取 `BOOTSTRAP.md`
2. ✅ 智能体读取 `memory/CORE_RULES.md`
3. ✅ 智能体读取各自 `AGENTS.md`
4. ✅ 开始执行用户任务

### 无需额外配置

**这是 OpenClaw 的原生机制**:

- 无需修改 Gateway 配置
- 无需添加 Hook 脚本
- 无需手动执行命令

---

## 📊 覆盖的核心规则

### 所有智能体共同遵守

| 规则               | 覆盖智能体                           |
| ------------------ | ------------------------------------ |
| **三条红线**       | 所有 9 个                            |
| **安全基线**       | 所有 9 个                            |
| **项目初始化检查** | 所有 9 个                            |
| **6 阶段流程**     | dev-engineer (完整), 其他 (相关阶段) |

### 智能体特定规则

| 智能体          | 特定规则               |
| --------------- | ---------------------- |
| product-manager | Phase 0 的 5 个关键点  |
| architect       | 字段级合同定义         |
| tech-leader     | 安全评审 + 代码审查    |
| dev-engineer    | 完整 6 阶段 + 禁止跳步 |
| qa-engineer     | VALIDATION_LOG 验证    |
| devops-engineer | 10 大类部署检查        |
| ai-orchestrator | 自动初始化 + 流程追踪  |
| project-manager | ProjectPackages        |
| ui-ux-designer  | 设计规范 + 无障碍      |

---

## 🚀 工作流程

### 完整流程

```
新会话启动
  ↓
OpenClaw 自动读取 BOOTSTRAP.md (原生机制)
  ↓
智能体读取 memory/CORE_RULES.md
  ↓
智能体读取 AGENTS.md
  ↓
ai-orchestrator 检测项目状态
  ↓
未初始化 → 自动执行 auto-init-if-needed.sh
  ↓
开始执行用户任务
```

### 每个智能体的启动流程

```
智能体启动
  ↓
读取 BOOTSTRAP.md (自动)
  ↓
读取 CORE_RULES.md (按 AGENTS.md 要求)
  ↓
读取 AGENTS.md (角色规范)
  ↓
检查 TASK_TRACKER.md (项目状态)
  ↓
验证项目初始化 (如未初始化 → 通知 ai-orchestrator)
  ↓
开始执行任务
```

---

## 📋 验证方法

### 测试自动读取

```bash
# 启动新会话
/new

# 问智能体
"What do you read on session start?"

# 期望回答
- BOOTSTRAP.md (auto-read by OpenClaw)
- memory/CORE_RULES.md (per AGENTS.md)
- AGENTS.md (role specification)
```

### 测试规则遵守

```bash
# 对 dev-engineer 说
"Add a login API endpoint"

# 期望行为
- 不直接写代码
- 提出 Phase 0 的 5 个问题
- 说明需要需求澄清
```

---

## 🎯 核心优势

| 优势                 | 说明                     |
| -------------------- | ------------------------ |
| ✅ **OpenClaw 原生** | 无需额外配置，自动读取   |
| ✅ **每次会话必读**  | 不会遗漏，不会忘记       |
| ✅ **角色定制化**    | 每个智能体有针对性的规则 |
| ✅ **简洁快速**      | 摘要版本，快速加载       |
| ✅ **完整引用**      | 链接到完整文档           |

---

## 📚 相关文档

| 文档                               | 用途                  |
| ---------------------------------- | --------------------- |
| `memory/CORE_RULES.md`             | 持久化核心规则 (完整) |
| `DEVELOPMENT_PROCESS_CHECKLIST.md` | 6 阶段流程详解        |
| `ENGLISH_RULES_SUMMARY.md`         | 英文规则摘要          |
| `AUTO_INIT_PLAN.md`                | 自动初始化方案        |
| `COLLABORATION_PROTOCOL.md`        | 完整协作协议          |

---

## ✅ 完成检查清单

- [x] product-manager/BOOTSTRAP.md 创建
- [x] architect/BOOTSTRAP.md 创建
- [x] tech-leader/BOOTSTRAP.md 创建
- [x] dev-engineer/BOOTSTRAP.md 创建
- [x] qa-engineer/BOOTSTRAP.md 创建
- [x] devops-engineer/BOOTSTRAP.md 创建
- [x] ai-orchestrator/BOOTSTRAP.md 创建
- [x] project-manager/BOOTSTRAP.md 创建
- [x] ui-ux-designer/BOOTSTRAP.md 创建
- [x] 所有文件包含统一结构
- [x] 所有文件包含角色特定规则
- [x] 所有文件包含项目初始化检查
- [x] 所有文件包含快速检查清单

---

## 🎯 总结

**9 个智能体的 BOOTSTRAP.md 全部完成！**

现在：

- ✅ 每次会话启动自动读取
- ✅ 每个智能体清楚自己的职责
- ✅ 核心规则不会遗忘
- ✅ 6 阶段流程强制执行
- ✅ 安全红线时刻牢记

**用户完全无感知，一切自动进行！** 🤖

---

**版本**: 1.0 **最后更新**: 2026-03-20 **维护者**: ai-orchestrator
