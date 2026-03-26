# 🧠 智能体记忆系统说明

> **目的**: 将核心规则持久化到记忆系统，确保所有智能体每次会话都会主动读取

---

## 📁 记忆文件结构

```
/home/wufei/.openclaw/workspace/memory/
├── CORE_RULES.md              # 核心规则 (所有智能体必读)
├── README.md                  # 记忆系统说明
├── vector_memory.py           # 向量记忆实现
└── chroma_db/                 # 向量数据库
```

---

## 📋 CORE_RULES.md 内容

**位置**: `/home/wufei/.openclaw/workspace/memory/CORE_RULES.md`

**包含内容**:

1. ⛔ 三条红线 + 安全基线
2. 🎯 6 阶段开发流程
3. 📋 5 个质量门禁
4. 🔧 必备模板文件清单
5. 🚨 违规处理
6. 📊 智能体职责矩阵
7. 🎯 快速参考

**重要级别**: 🔴 强制遵守 (违反=交付无效)

---

## 🤖 智能体读取责任

### 所有智能体 (MANDATORY)

**每次会话开始时** (在 AGENTS.md 第 2 节已添加):

```markdown
### 🧠 Every Session Start (MANDATORY)

**Before any task**:

1. Read `@workspace/memory/CORE_RULES.md` (core rules)
2. Read `@workspace/agents/<agent-name>/AGENTS.md` (this file)
3. Read `TASK_TRACKER.md` (project status)
4. Check `PROJECT_STARTUP_CHECKLIST.md` (initialization status)
```

### 各智能体额外读取

| 智能体              | 额外读取文件                            |
| ------------------- | --------------------------------------- |
| **tech-leader**     | `SECURITY_CHECKLIST.md` (current phase) |
| **dev-engineer**    | `DEVELOPMENT_PROCESS_CHECKLIST.md`      |
| **qa-engineer**     | `INTEGRATION_TEST_PLAN.md`              |
| **devops-engineer** | `DEPLOYMENT_READINESS.md`               |
| **ai-orchestrator** | 所有 active checklists                  |

---

## 🚀 项目初始化时的复制

**init-project.sh** 会自动复制：

```bash
# 复制 CORE_RULES.md 到项目 docs/目录
cp /home/wufei/.openclaw/workspace/memory/CORE_RULES.md <project>/docs/CORE_RULES.md
```

**项目中的位置**: `<project>/docs/CORE_RULES.md`

**用途**: 项目团队成员随时参考

---

## 📊 记忆系统 vs 文件模板

| 类型           | 位置                   | 用途               | 更新频率            |
| -------------- | ---------------------- | ------------------ | ------------------- |
| **记忆文件**   | `memory/CORE_RULES.md` | 智能体每次会话必读 | 低 (规则稳定)       |
| **项目模板**   | `docs/*.md`            | 项目执行记录       | 高 (每次任务更新)   |
| **智能体规范** | `agents/*/AGENTS.md`   | 角色特定职责       | 中 (流程优化时更新) |

---

## 🎯 为什么放在记忆系统？

### 优势

1. ✅ **持久化** - 不会因项目删除而丢失
2. ✅ **全局共享** - 所有智能体/项目共用一份
3. ✅ **强制读取** - AGENTS.md 明确规定每次会话必读
4. ✅ **版本控制** - 集中管理，易于更新
5. ✅ **语义检索** - 可通过 memory_search 快速定位

### 与文件模板的配合

```
记忆系统 (memory/CORE_RULES.md)
    ↓ 每次会话读取
智能体 AGENTS.md
    ↓ 指导行为
项目模板 (docs/*.md)
    ↓ 填写记录
质量门禁 (5 Gates)
```

---

## 🔄 更新流程

当规则需要更新时：

1. **更新** `memory/CORE_RULES.md`
2. **更新版本**号 (顶部)
3. **更新** `PROCESS_OPTIMIZATION_SUMMARY.md`
4. **通知** 所有智能体 (通过 ai-orchestrator)
5. **更新** 各项目 `docs/CORE_RULES.md` (下次初始化时自动同步)

---

## 📝 智能体记忆读取示例

### dev-engineer 读取流程

```markdown
## 2. Operating Protocol

### 🧠 Every Session Start (MANDATORY)

**Before any task**:

1. Read `@workspace/memory/CORE_RULES.md` (core rules) → 了解 3 条红线 +6 阶段流程
2. Read `@workspace/agents/dev-engineer/AGENTS.md` → 了解具体职责
3. Read `TASK_TRACKER.md` → 了解当前进度
4. Check `PROJECT_STARTUP_CHECKLIST.md` → 确认项目已初始化
5. Review `DEVELOPMENT_PROCESS_CHECKLIST.md` → 温习 6 阶段细节

### 🛑 PHASE 0: REQUIREMENTS CLARIFICATION

→ 开始执行任务
```

---

## 🎯 核心保证

通过记忆系统 +AGENTS.md 强制读取，确保：

1. ✅ **规则不会遗忘** - 每次会话必读
2. ✅ **新智能体快速上手** - 读取 CORE_RULES.md 即可了解全流程
3. ✅ **规则一致性** - 所有智能体遵守同一份规则
4. ✅ **易于更新** - 改一处，所有智能体生效

---

**版本**: 1.0 **最后更新**: 2026-03-20 **维护者**: ai-orchestrator + tech-leader
