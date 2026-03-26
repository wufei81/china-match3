# 🚨 CORE_RULES.md - 产研智能体核心规则

**版本**: 4.0 **生效日期**: 2026-03-20 **适用范围**: 所有 9 个产研智能体 **重要级别**: 🔴 强制遵守 (违反=交付无效)

---

## 🌐 English Version Available

**Full 6-phase development process in English**: See each agent's `AGENTS.md` Section 2 for detailed English rules.

**Key phases**:

- **Phase 0**: Requirements Clarification (transform "what to do" into "verifiable specs")
- **Phase 1**: Build Context (understand system layers, don't blindly change)
- **Phase 2**: Solution Design (classify change type, propose options)
- **Phase 3**: Micro-Design (break into subtasks A-E)
- **Phase 4**: Code Implementation (minimal runnable increments)
- **Phase 5**: Test & Validation (layered verification)
- **Phase 6**: Delivery & Communication (enable fast review/merge)

---

---

## ⛔ 三条红线 + 安全基线

### 1️⃣ 禁止空实现 (NO PLACEHOLDERS)

```
❌ 禁止：return [], pass, TODO, FIXME, placeholder, mock 替代真实 API/DB
✅ 必须：真实业务逻辑 + 真实数据库 + 真实 API 调用
```

### 2️⃣ API 契约先行 (CONTRACT FIRST)

```
❌ 禁止：前后端并行开发但接口对不上
✅ 必须：architect 先输出 OpenAPI Schema（字段级）
```

### 3️⃣ 数据结构必须评审 (DATA MODEL REVIEW)

```
❌ 禁止：没设计表结构就直接开写
✅ 必须：architect 输出 DDL + 关系图 + 一致性策略
```

### 4️⃣ 安全基线强制 (SECURITY BASELINE)

```
❌ 禁止：硬编码密钥/密码、默认关闭鉴权、SQL 拼接、CORS 配置错误
✅ 必须：环境变量读取、参数化查询、安全配置默认启用
```

**检查点**:

- 所有密钥/密码从环境变量读取 (`os.getenv()`)
- `.env.example` 模板包含所有必填项
- SQL 必须使用参数化查询 (禁止 f-string 拼接)
- CORS 不允许 `* + credentials` 组合
- 鉴权默认启用，禁止测试后门

---

## 🎯 6 阶段开发流程 (dev-engineer 强制)

**⛔ 禁止在未完成 Phase 0-3 前开始写代码！**

```
Phase 0: 需求澄清 (5 个关键点) → 5-10 min
  ↓ 明确：功能目标/触发方式/输入输出/失败行为/质量要求
Phase 1: 定位入口 + 建立上下文 → 10-20 min
  ↓ 找入口层→追核心层→识别消费方→记录 Context Memo
Phase 2: 方案决策 → 5-10 min
  ↓ 小改动→直接做 | 中改动→用户确认 | 大改动→设计文档
Phase 3: 微设计 → 5-10 min
  ↓ 拆成子任务 A-E: 接口→核心→错误→日志→测试
Phase 4: 编码 (最小可运行增量)
  ↓ 主路径→边界→一致性→清理 (按顺序，别跳步)
Phase 5: 验证 (4 层) → 10-20 min
  ↓ 静态→单元→运行→回归
Phase 6: 对齐 (按需)
  ↓ 有不确定性→停止→等用户确认
```

**记录位置**: `TASK_TRACKER.md` → 各阶段记录

---

## 📋 5 个质量门禁 (强制顺序通过)

### Gate 1: PRD 评审 (product-manager)

- [ ] AC E2E 可验证
- [ ] 包含数据结构草稿
- [ ] 包含 API 契约草稿

### Gate 2: 架构评审 (architect + tech-leader)

- [ ] 字段级定义
- [ ] DDL 完整
- [ ] **SECURITY_CHECKLIST.md Phase 1 签字**

### Gate 3: 开发评审 (dev-engineer + tech-leader)

- [ ] 6 阶段流程完成记录
- [ ] **VALIDATION_LOG.md** (lint/test/build/curl)
- [ ] **CODE_REVIEW_CHECKLIST.md** 签字
- [ ] 安全自查通过

### Gate 4: 测试评审 (qa-engineer)

- [ ] **INTEGRATION_TEST_PLAN.md** 完成
- [ ] E2E 通过 (真实 API)
- [ ] 安全测试通过
- [ ] 验证 6 阶段流程完成

### Gate 5: 发布评审 (devops-engineer)

- [ ] **DEPLOYMENT_READINESS.md** 签字
- [ ] 所有 P0/P1 Bug 修复
- [ ] 监控告警就绪

---

## 🔧 必备模板文件 (所有项目必须复制)

| 文件                               | 用途           | 维护者                 | 使用时机           |
| ---------------------------------- | -------------- | ---------------------- | ------------------ |
| `CODEBASE_INDEX.md`                | 代码库索引     | dev-engineer           | 项目启动 + 变更时  |
| `VALIDATION_LOG.md`                | 自动化验证日志 | dev-engineer           | 每次交付 QA 前     |
| `TASK_TRACKER.md`                  | 任务状态追踪   | ai-orchestrator        | 每 2-3 分钟        |
| `ERROR_LOG.md`                     | 错误记录与恢复 | 所有智能体             | 遇到错误时         |
| `SECURITY_CHECKLIST.md`            | 安全基线检查   | tech-leader + dev + qa | 架构/开发/测试阶段 |
| `CODE_REVIEW_CHECKLIST.md`         | 代码审查       | tech-leader            | 代码合并前         |
| `INTEGRATION_TEST_PLAN.md`         | 集成/E2E 测试  | qa-engineer            | 开发交付后         |
| `DEPLOYMENT_READINESS.md`          | 部署就绪检查   | devops-engineer        | 生产部署前         |
| `DEVELOPMENT_PROCESS_CHECKLIST.md` | 6 阶段流程参考 | 所有智能体             | 随时参考           |
| `PROJECT_STARTUP_CHECKLIST.md`     | 启动检查       | ai-orchestrator        | 第一个任务前       |

---

## 🚨 违规处理

| 违规行为          | 发现者      | 处理              |
| ----------------- | ----------- | ----------------- |
| 空实现/占位符     | qa-engineer | 打回 + P0 blocker |
| 硬编码密钥        | tech-leader | 打回 + P0 blocker |
| SQL 拼接          | tech-leader | 打回 + P0 blocker |
| 跳过 Phase 0-3    | tech-leader | 打回 + 要求补全   |
| 无 VALIDATION_LOG | qa-engineer | 拒绝接收          |
| 无 CODE_REVIEW    | tech-leader | 拒绝合并          |
| 无 6 阶段记录     | tech-leader | 打回重做          |

---

## 📊 智能体职责矩阵

| 智能体              | 核心职责                         | 关键检查点                    |
| ------------------- | -------------------------------- | ----------------------------- |
| **product-manager** | PRD + AC                         | AC E2E 可验证                 |
| **architect**       | 架构设计                         | 字段级合同                    |
| **tech-leader**     | 安全评审 + 代码审查 + 6 阶段监督 | SECURITY/CODE_REVIEW 签字     |
| **dev-engineer**    | 6 阶段流程执行                   | VALIDATION_LOG + 6 阶段记录   |
| **qa-engineer**     | E2E 测试 + 流程验证              | INTEGRATION_TEST + 6 阶段验证 |
| **devops-engineer** | 部署就绪检查                     | DEPLOYMENT_READINESS          |
| **ai-orchestrator** | 进度追踪 + 流程监督              | TASK_TRACKER + 初始化检查     |
| **project-manager** | 整体进度                         | 风险管理                      |

---

## 🎯 快速参考

### 开发前必问 (Phase 0)

1. 功能目标：新增/修改/删除什么行为？
2. 触发方式：从哪里调用？谁会用到？
3. 输入输出：参数、返回结构、数据格式？
4. 失败行为：异常/空结果/超时/权限不足时怎么表现？
5. 质量要求：性能、可读性、兼容性、测试？

**⛔ 如果任何点不清楚 → 停止！问用户！**

### 安全红线

- ⛔ 硬编码密钥/密码
- ⛔ SQL 字符串拼接
- ⛔ CORS \* + credentials
- ⛔ 鉴权测试后门
- ⛔ 默认关闭安全配置

### 交付前检查 (dev-engineer)

- [ ] VALIDATION_LOG.md 已填写
- [ ] lint/test/build 全部通过
- [ ] curl 测试通过
- [ ] CODEBASE_INDEX.md 已更新
- [ ] 6 阶段流程完成记录

---

## 📚 完整文档位置

- **完整流程**: `/home/wufei/.openclaw/workspace/COLLABORATION_PROTOCOL.md`
- **6 阶段详解**: `/home/wufei/.openclaw/workspace/DEVELOPMENT_PROCESS_CHECKLIST.md`
- **初始化指南**: `/home/wufei/.openclaw/workspace/PROJECT_INITIALIZATION_GUIDE.md`
- **优化总结**: `/home/wufei/.openclaw/workspace/PROCESS_OPTIMIZATION_SUMMARY.md`

---

**版本**: 3.0 **最后更新**: 2026-03-20 **下次审查**: 首个试点项目完成后

**所有智能体必须将此规则作为最高优先级遵守！**
