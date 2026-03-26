# BOOTSTRAP.md - 会话启动自动执行

> **用途**: 每次新会话启动时自动读取和执行 **重要**: 这是 OpenClaw 的原生机制，无需额外配置

---

## 🧠 会话启动时自动读取

**每次新会话开始时，智能体会自动**:

1. ✅ 读取 `BOOTSTRAP.md` (本文件)
2. ✅ 读取 `SOUL.md` (身份定义)
3. ✅ 读取 `IDENTITY.md` (角色规范)
4. ✅ 读取 `memory/CORE_RULES.md` (核心规则)

---

## 🚀 项目初始化自动执行

**如果检测到新项目，自动执行**:

```bash
# 自动检测并初始化
cd /home/wufei/.openclaw/workspace
./auto-init-if-needed.sh <project-name>
```

**然后继续执行用户任务**。

---

## 📋 核心规则快速参考

**所有智能体必须遵守**:

### ⛔ 三条红线

1. 禁止空实现 (NO PLACEHOLDERS)
2. API 契约先行 (CONTRACT FIRST)
3. 数据结构必须评审 (DATA MODEL REVIEW)
4. 安全基线强制 (SECURITY BASELINE)

### 🎯 6 阶段开发流程

- Phase 0: 需求澄清 (5 个关键点)
- Phase 1: 定位入口 + 建立上下文
- Phase 2: 方案决策 (小/中/大改动分类)
- Phase 3: 微设计 (子任务 A-E)
- Phase 4: 编码 (最小可运行增量)
- Phase 5: 验证 (4 层验证)
- Phase 6: 对齐 (不确定性时停止)

### 📋 5 个质量门禁

- Gate 1: PRD 评审
- Gate 2: 架构评审 + 安全评审
- Gate 3: 开发评审 + 代码审查
- Gate 4: 测试评审 + E2E
- Gate 5: 发布评审 + 部署检查

---

## 📁 必备模板文件

所有项目必须有以下文件：

| 文件                            | 用途       |
| ------------------------------- | ---------- |
| `docs/CORE_RULES.md`            | 核心规则   |
| `docs/CODEBASE_INDEX.md`        | 代码库索引 |
| `docs/VALIDATION_LOG.md`        | 验证日志   |
| `docs/TASK_TRACKER.md`          | 任务追踪   |
| `docs/SECURITY_CHECKLIST.md`    | 安全检查   |
| `docs/CODE_REVIEW_CHECKLIST.md` | 代码审查   |
| `docs/INTEGRATION_TEST_PLAN.md` | 集成测试   |
| `docs/DEPLOYMENT_READINESS.md`  | 部署检查   |

---

## 🤖 智能体职责

| 智能体          | 核心职责                         |
| --------------- | -------------------------------- |
| product-manager | PRD + AC (E2E 可验证)            |
| architect       | 架构设计 + API 合同              |
| tech-leader     | 安全评审 + 代码审查 + 6 阶段监督 |
| dev-engineer    | 6 阶段流程执行                   |
| qa-engineer     | E2E 测试 + 流程验证              |
| devops-engineer | 部署就绪检查                     |
| ai-orchestrator | 进度追踪 + 流程监督 + 自动初始化 |
| project-manager | 整体进度                         |

---

## 🎯 快速检查清单

**每次任务前自动确认**:

- [ ] 项目已初始化 (PROJECT_CONFIG.md 存在)
- [ ] 所有模板文件在 docs/目录
- [ ] 6 阶段流程理解
- [ ] 质量门禁清楚
- [ ] 安全红线牢记

---

## 📚 完整文档

- **完整流程**: `COLLABORATION_PROTOCOL.md`
- **6 阶段详解**: `DEVELOPMENT_PROCESS_CHECKLIST.md`
- **英文规则**: `ENGLISH_RULES_SUMMARY.md`
- **自动初始化**: `AUTO_INIT_PLAN.md`

---

**版本**: 1.0 **最后更新**: 2026-03-20 **所有智能体每次会话启动时自动读取此文件**
