# 🚀 新项目初始化指南

> **重要**: 所有新项目必须完成此流程才能开始开发任务

---

## 🎯 为什么需要初始化？

**问题**: 之前优化的规则（6 阶段流程、安全检查清单、代码审查等）如果新项目启动时忘了用，等于零。

**解决**: 通过自动化脚本 + 强制检查，确保规则自动应用到每个新项目。

---

## 📋 初始化流程 (3 步完成)

### Step 1: 运行初始化脚本

```bash
cd /home/wufei/.openclaw/workspace
./init-project.sh <项目名称>
```

**示例**:

```bash
./init-project.sh im-system
```

**脚本会自动完成**:

- ✅ 创建项目目录结构
- ✅ 复制所有 10 个模板文件到项目/docs/
- ✅ 创建 PROJECT_CONFIG.md (项目配置)
- ✅ 创建 QUICK_REFERENCE.md (快速参考)
- ✅ 创建 .gitignore
- ✅ 初始化 Git 仓库

---

### Step 2: 填写项目配置

编辑 `<项目>/PROJECT_CONFIG.md`:

```markdown
## 基本信息

- **项目名称**: im-system
- **创建日期**: 2026-03-20
- **项目负责人**: [填写]
- **技术栈**: Python/FastAPI + React/TypeScript
```

---

### Step 3: 完成启动检查清单

编辑 `<项目>/PROJECT_STARTUP_CHECKLIST.md`:

```markdown
## 🚨 项目初始化检查 (HARD GATE)

### 1. 项目结构检查

- [x] 项目目录已创建
- [x] PROJECT_CONFIG.md 存在
- [x] QUICK_REFERENCE.md 存在 ...

### 2. 模板文件检查

- [x] CODEBASE_INDEX.md
- [x] VALIDATION_LOG.md ...

### 3. 团队流程培训

- [x] product-manager 已阅读 AGENTS.md
- [x] dev-engineer 已阅读 6 阶段流程 ...

## ✅ 初始化完成确认

- [x] 通过 - 所有检查项完成，允许开始 Phase 1

### 签字确认

| 角色            | 签字 | 日期       |
| --------------- | ---- | ---------- |
| ai-orchestrator | auto | 2026-03-20 |
```

**完成此检查清单后，才能开始第一个任务！**

---

## 🤖 智能体自动检查

**ai-orchestrator 会在第一个任务前自动验证**:

```markdown
## 10. 🚨 Project Initialization Check (MANDATORY - FIRST ACTION)

**Before any task execution, verify project has been properly initialized**:

### Initialization Checklist (MUST complete before Phase 1):

| Check                    | What to Verify                     | Action if Missing |
| ------------------------ | ---------------------------------- | ----------------- |
| PROJECT_CONFIG.md exists | Project root has config file       | ⛔ STOP           |
| 9 templates copied       | All template files in project/docs | ⛔ STOP           |

...
```

**如果未初始化**:

1. ⛔ ai-orchestrator 会**停止**所有任务
2. ✅ 通知用户："Project not initialized. Run `./init-project.sh <name>` first."
3. ✅ 等待用户完成初始化
4. ✅ 重新验证后才允许继续

---

## 📁 初始化后的项目结构

```
<project>/
├── PROJECT_CONFIG.md              # 项目配置（必须填写）
├── QUICK_REFERENCE.md             # 快速参考（团队必读）
├── PROJECT_STARTUP_CHECKLIST.md   # 启动检查（必须完成）
├── .gitignore                     # Git 忽略文件
├── .git/                          # Git 仓库
├── docs/                          # 所有模板文件
│   ├── CODEBASE_INDEX.md
│   ├── VALIDATION_LOG.md
│   ├── TASK_TRACKER.md
│   ├── ERROR_LOG.md
│   ├── SECURITY_CHECKLIST.md
│   ├── CODE_REVIEW_CHECKLIST.md
│   ├── INTEGRATION_TEST_PLAN.md
│   ├── DEPLOYMENT_READINESS.md
│   └── DEVELOPMENT_PROCESS_CHECKLIST.md
├── src/                           # 源代码
└── tests/                         # 测试代码
```

---

## ✅ 初始化完成标志

完成以下所有项，才算初始化完成：

- [ ] `./init-project.sh` 执行成功
- [ ] `PROJECT_CONFIG.md` 已填写
- [ ] `PROJECT_STARTUP_CHECKLIST.md` 所有检查项通过
- [ ] 所有 10 个模板文件在 `docs/` 目录
- [ ] ai-orchestrator 验证通过
- [ ] 团队（智能体）了解流程

**完成标志**: `PROJECT_STARTUP_CHECKLIST.md` 中 "初始化完成确认" 章节全部打勾

---

## 🚨 常见错误

### 错误 1: 忘记初始化直接开始

**现象**: ai-orchestrator 拒绝执行任务

**解决**:

```bash
./init-project.sh <项目名称>
# 然后填写 PROJECT_STARTUP_CHECKLIST.md
```

---

### 错误 2: 模板文件缺失

**现象**: 某些检查清单找不到

**解决**:

```bash
# 手动复制缺失的模板
cp /home/wufei/.openclaw/workspace/<模板名>.template.md <项目>/docs/<模板名>.md
```

---

### 错误 3: 智能体不了解流程

**现象**: dev-engineer 直接开始写代码（跳过 Phase 0-3）

**解决**:

1. 提醒 dev-engineer 阅读 `AGENTS.md` 第 2 节 (6 阶段流程)
2. 提醒 tech-leader 监督 Phase 0-3 完成
3. 在 TASK_TRACKER.md 记录违规

---

## 🔄 旧项目如何补初始化

如果项目已经开始但没用这些模板：

```bash
# 1. 手动创建 docs/目录
mkdir -p <项目>/docs

# 2. 复制所有模板
cp /home/wufei/.openclaw/workspace/*.template.md <项目>/docs/

# 3. 重命名（去掉.template）
cd <项目>/docs
for f in *.template.md; do mv "$f" "${f%.template.md}"; done

# 4. 补填 PROJECT_STARTUP_CHECKLIST.md
# 5. 补填已完成阶段的检查清单
```

---

## 📊 初始化检查自动化

**ai-orchestrator 会在以下时机自动检查**:

| 时机              | 检查内容                   | 不通过的处理 |
| ----------------- | -------------------------- | ------------ |
| 第一个任务前      | PROJECT_CONFIG.md + 9 模板 | ⛔ 停止任务  |
| Gate 3 (开发评审) | 6 阶段流程记录             | ⛔ 拒绝交付  |
| Gate 4 (测试评审) | VALIDATION_LOG.md          | ⛔ 拒绝测试  |
| Gate 5 (发布评审) | DEPLOYMENT_READINESS.md    | ⛔ 拒绝发布  |

---

## 🎯 核心保证

通过这套机制，确保：

1. ✅ **规则不会遗忘** - 脚本自动复制所有模板
2. ✅ **流程不会跳过** - ai-orchestrator 强制检查
3. ✅ **团队不会迷茫** - QUICK_REFERENCE.md 随时参考
4. ✅ **质量不会下降** - 5 门禁 + 4 清单 + 6 阶段强制

---

**版本**: 1.0 **最后更新**: 2026-03-20 **强制要求**: 所有新项目必须完成此初始化流程
