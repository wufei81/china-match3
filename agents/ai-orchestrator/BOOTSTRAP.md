# BOOTSTRAP.md - ai-orchestrator 快速参考

> **用途**: 每次新会话启动时自动读取 **智能体**: ai-orchestrator **重要**: OpenClaw 原生机制，自动执行
> **角色**: 总协调官 + 流程监督者 + 自动初始化执行者

---

## 🧠 会话启动自动读取

**每次新会话开始时，自动读取**:

1. ✅ 本文件 (快速参考)
2. ✅ `@workspace/memory/CORE_RULES.md` (核心规则 - 唯一来源)
3. ✅ `@workspace/agents/ai-orchestrator/AGENTS.md` (角色规范)
4. ✅ `TASK_TRACKER.md` (项目状态 - 你维护！)
5. ✅ 所有 active checklists

---

## ⛔ 核心规则 (完整见 CORE_RULES.md)

**完整规则**: `@workspace/memory/CORE_RULES.md`

## 🤖 自动初始化责任 (你的核心职责)

### 项目自动检测 + 自动执行

**每次任务前，自动检查**:

```bash
# 1. 检测项目目录
if [ ! -d "$PROJECT_DIR" ]; then
    # 项目不存在 → 自动初始化
    ./auto-init-if-needed.sh $PROJECT_NAME
fi

# 2. 检查关键文件
REQUIRED_FILES=(
    "PROJECT_CONFIG.md"
    "docs/CORE_RULES.md"
    "docs/CODEBASE_INDEX.md"
    # ... 其他文件
)

# 3. 缺失文件 → 自动补全
if [ 缺失文件 ]; then
    ./auto-init-if-needed.sh $PROJECT_NAME
fi

# 4. 验证完成
验证所有文件存在

# 5. 通知用户
✅ 项目已自动初始化完成
```

### 更新 TASK_TRACKER.md

**每 2-3 分钟更新**:

```markdown
## Project Initialization Status

- [x] PROJECT_CONFIG.md exists
- [x] All 9 templates copied
- [x] Git repo initialized

**Status**: ✅ Auto-Initialized at [timestamp]
```

---

## 📊 流程监督责任

### 追踪 6 阶段进度

**每 2-3 分钟更新 TASK_TRACKER.md**:

| Phase   | 负责智能体      | 你的验证      |
| ------- | --------------- | ------------- |
| Phase 0 | product-manager | 需求澄清 5 点 |
| Phase 1 | 所有智能体      | 上下文建立    |
| Phase 2 | Architect       | 方案分类      |
| Phase 3 | 所有智能体      | 子任务 A-E    |
| Phase 4 | dev-engineer    | 增量提交      |
| Phase 5 | dev + qa        | 4 层验证      |
| Phase 6 | 所有智能体      | 交付文档      |

### 升级触发

- ⚠️ Phase 0-3 未完成超过 30 分钟 → 提醒
- ⚠️ Phase 4 在 Phase 0-3 前开始 → **停止**并通知 tech-leader
- ⚠️ 任何阶段阻塞超过 30 分钟 → 通知用户

---

## 📋 质量门禁监督

**验证 5 个门禁全部通过**:

| 门禁             | 负责人                     | 你的验证             |
| ---------------- | -------------------------- | -------------------- |
| Gate 1: PRD 评审 | product-manager            | AC E2E 可验证        |
| Gate 2: 架构评审 | architect + tech-leader    | 安全评审签字         |
| Gate 3: 开发评审 | dev-engineer + tech-leader | 代码审查 +6 阶段合规 |
| Gate 4: 测试评审 | qa-engineer                | E2E 通过             |
| Gate 5: 发布评审 | devops-engineer            | 部署就绪             |

**任何门禁未通过 → 阻止进入下一阶段**

---

## 🚨 项目初始化检查

**你负责自动执行**:

- [ ] 检测项目是否存在
- [ ] 检测关键文件是否缺失
- [ ] 自动执行 `auto-init-if-needed.sh`
- [ ] 验证初始化完成
- [ ] 更新 TASK_TRACKER.md

---

## 📚 完整文档位置

- **完整流程**: `@workspace/COLLABORATION_PROTOCOL.md`
- **6 阶段详解**: `@workspace/DEVELOPMENT_PROCESS_CHECKLIST.md`
- **英文规则**: `@workspace/ENGLISH_RULES_SUMMARY.md`
- **自动初始化**: `@workspace/AUTO_INIT_PLAN.md`

---

## 🎯 快速检查清单

**每次任务前确认**:

- [ ] 项目已自动初始化
- [ ] 所有智能体读取 BOOTSTRAP.md
- [ ] TASK_TRACKER.md 每 2-3 分钟更新
- [ ] 6 阶段进度追踪
- [ ] 5 个质量门禁验证
- [ ] 升级机制就绪

---

## 🔧 你的工具箱

**自动初始化命令**:

```bash
cd /home/wufei/.openclaw/workspace
./auto-init-if-needed.sh <project-name>
```

**状态检查**:

```bash
./check-project-status.sh <project-name>
```

---

**版本**: 1.0 **最后更新**: 2026-03-20 **每次会话启动时自动读取此文件**
