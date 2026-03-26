# 🚨 COLLABORATION_PROTOCOL.md - 产研智能体协作铁律

**版本**: 2.0 | **生效日期**: 2026-03-20 | **适用范围**: 所有 9 个产研智能体
**更新说明**: 新增代码索引层 + 自动化验证钩子（对标 Cursor Agent 模式）

---

## ⛔ 三条红线（违反=交付无效）

### 1️⃣ 禁止空实现 (NO PLACEHOLDERS)

```
❌ 禁止：return [], pass, TODO, FIXME, placeholder, mock 替代真实 API/DB
✅ 必须：真实业务逻辑 + 真实数据库 + 真实 API 调用
```

**检查点**: `dev-engineer` 交付前必须自验证（curl/手动流程跑通）

---

### 2️⃣ API 契约先行 (CONTRACT FIRST)

```
❌ 禁止：前后端并行开发但接口对不上
✅ 必须：architect/tech-leader 先输出 OpenAPI Schema（字段级）
```

**检查点**: 数据结构不评审通过 → 不准写代码

---

### 3️⃣ 数据结构必须评审 (DATA MODEL REVIEW)

```
❌ 禁止：没设计表结构就直接开写
✅ 必须：architect 输出 DDL + 关系图 + 一致性策略
```

**检查点**: tech-leader 评审签字 → dev-engineer 才能实现

---

### 4️⃣ 🆕 安全基线强制 (SECURITY BASELINE) - 新增

```
❌ 禁止：硬编码密钥/密码、默认关闭鉴权、SQL 拼接、CORS 配置错误
✅ 必须：环境变量读取、参数化查询、安全配置默认启用
```

**检查点**:

- [ ] 所有密钥/密码从环境变量读取 (`os.getenv()`)
- [ ] `.env.example` 模板包含所有必填项
- [ ] SQL 必须使用参数化查询 (禁止 f-string 拼接)
- [ ] CORS 不允许 `* + credentials` 组合
- [ ] 鉴权默认启用，禁止测试后门
- [ ] `tech-leader` 安全评审签字

**违规处理**: 发现任何安全问题 → 立即停止交付 + `tech-leader` 重新评审

---

## 📋 标准协作流程 (SOP)

```
┌─────────────────────────────────────────────────────────────┐
│  Phase 1: 需求定义 (product-manager)                        │
│  → PRD + Gherkin AC (E2E 可验证) + WorkPackages              │
│  ✅ 检查：AC 是否包含数据结构草稿？                          │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│  Phase 2: 架构设计 (architect + tech-leader)                │
│  → 系统架构图 + API OpenAPI Schema + DDL + NFR              │
│  ✅ 检查：字段级定义？错误码？幂等性？                       │
│  ✅ 检查：tech-leader 评审签字                               │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│  Phase 3: UI 设计 (ui-ux-designer)                           │
│  → Design Tokens + 组件规范 + 状态表                         │
│  ✅ 检查：所有状态（loading/error/empty）？                  │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│  Phase 4: 开发实现 (dev-engineer)                           │
│  → 后端真实逻辑 + 前端真实 API 调用                            │
│  ✅ 检查：自验证通过（curl + 手动流程）？                    │
│  ✅ 检查：无 placeholder/return []/mock？                    │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│  Phase 5: 测试验证 (qa-engineer)                            │
│  → E2E 测试（真实 API）+ 集成测试 + 测试报告                   │
│  ✅ 检查：E2E 用真实 API？非 Mock？                           │
│  ✅ 检查：E2E 失败 = P0 blocker，不准进入质量验收              │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│  Phase 6: 部署运维 (devops-engineer)                        │
│  → Docker 配置 + CI/CD + 监控告警                             │
│  ✅ 检查：一键部署？监控就绪？                               │
└─────────────────────────────────────────────────────────────┘
```

---

## 🎯 各角色交付物标准

| 角色                | 交付物                       | 验收标准                   | 下游依赖                  |
| ------------------- | ---------------------------- | -------------------------- | ------------------------- |
| **product-manager** | PRD + WorkPackages           | AC E2E 可验证，无歧义      | architect, ui-ux-designer |
| **architect**       | API Schema + DDL + 架构图    | 字段级定义，错误码完整     | dev-engineer, qa-engineer |
| **tech-leader**     | 技术评审报告                 | 签字确认数据结构合理       | dev-engineer              |
| **ui-ux-designer**  | Design Tokens + 组件规范     | 所有状态定义完整           | dev-engineer              |
| **dev-engineer**    | 可运行代码 + DevDeliverables | 自验证通过，无 placeholder | qa-engineer               |
| **qa-engineer**     | E2E 测试 + 测试报告          | 真实 API 跑通，AC 全覆盖   | devops-engineer           |
| **devops-engineer** | Docker + CI/CD + 监控        | 一键部署，监控告警就绪     | project-manager           |
| **project-manager** | 项目进度报告                 | 关键路径清晰，风险暴露     | 用户                      |
| **ai-orchestrator** | 任务分发 + 进度追踪          | 每 2-3 分钟汇报一次        | 用户                      |

---

## 🔍 质量门禁 (Quality Gates)

### Gate 1: PRD 评审

- [ ] AC 是 Gherkin 格式（Given-When-Then）
- [ ] 包含数据结构草稿
- [ ] 包含 API 契约草稿
- [ ] 估算时间（分钟），含 20% buffer

### Gate 2: 架构评审

- [ ] API Schema 字段级定义（类型/必填/错误码）
- [ ] DDL 完整（表/索引/外键）
- [ ] 一致性策略明确
- [ ] tech-leader 签字

### Gate 3: 开发评审

- [ ] 无 placeholder/return []/pass
- [ ] 后端 curl 测试通过
- [ ] 前端手动流程验证通过
- [ ] Lint/Build/Test 通过

### Gate 4: 测试评审

- [ ] E2E 用真实 API（非 Mock）
- [ ] E2E 覆盖所有 P0 AC
- [ ] 异常场景测试覆盖
- [ ] 测试报告明确 Pass/Fail

---

## 📢 违规处理

| 违规类型         | 处理方式                             | 记录位置               |
| ---------------- | ------------------------------------ | ---------------------- |
| 空实现           | 打回重做 + self-improving-agent 记录 | `memory/YYYY-MM-DD.md` |
| 未评审先开发     | 停止任务 + architect 补评审          | `memory/YYYY-MM-DD.md` |
| E2E 失败强行验收 | 打回 + P0 blocker 标记               | `memory/YYYY-MM-DD.md` |
| 未自验证声称完成 | 打回 + 补充验证步骤                  | `memory/YYYY-MM-DD.md` |

---

## 🧠 持续改进

每个智能体必须在 `self-improving-agent` 技能中记录：

- 本项目遇到的坑
- 用户纠正的内容
- 发现的最佳实践

**位置**: `~/.openclaw/workspace/agents/<agent-name>/skills/self-improving-agent/LEARNINGS.md`

---

## 📦 改进 1: 代码索引层 (CODEBASE INDEX)

**目的**: 让所有智能体拥有代码级上下文（对标 Cursor Agent 的向量索引）

**创建位置**: `项目根目录/CODEBASE_INDEX.md`

**维护责任**: `dev-engineer` 创建，`architect` 审核，所有智能体可读

**结构模板**:

```markdown
# CODEBASE_INDEX.md

## 文件树
```

src/ ├── auth/ # 认证模块 │ ├── login.ts # 登录 API (POST /api/auth/login) │ └── jwt.ts # JWT 工具 ├── db/ # 数据库层 │
├── user.ts # User 模型 + DDL │ └── index.ts # 数据库连接 └── api/ # API 路由 └── v1/ # API v1

````

## API 路由表
| Method | Path | Handler | Auth | Description |
|--------|------|---------|------|-------------|
| POST | /api/auth/login | `auth/login.ts` | ❌ | 用户登录 |
| GET | /api/user/:id | `user/get.ts` | ✅ | 获取用户信息 |

## 数据模型
### User
```typescript
interface User {
  id: string;          // UUID, primary key
  email: string;       // unique, not null
  passwordHash: string; // bcrypt, not null
  createdAt: Date;     // auto-generated
}
````

## 关键函数签名

- `login(email, password) → Promise<JWT>`
- `generateJWT(user) → string`
- `findUserByEmail(email) → Promise<User|null>`

````

**更新时机**:
- 新增文件时
- API 路由变更时
- 数据模型修改时

---

## 🔧 改进 3: 自动化验证钩子 (AUTO-VALIDATION HOOKS)

**目的**: 开发交付前自动验证，缩短反馈周期（对标 Cursor 的自动 lint/test/build）

### Pre-Delivery Checklist (dev-engineer 强制)

**位置**: `项目根目录/VALIDATION_LOG.md`

**执行时机**: `dev-engineer` 声称"开发完成"前必须执行

**检查项**:
```markdown
## Pre-Delivery Validation

### Task: [任务名称]
### Agent: dev-engineer
### Timestamp: [ISO 时间戳]

- [ ] `npm run lint` → **PASSED** (附输出日志)
- [ ] `npm run test` → **PASSED** (附测试覆盖率)
- [ ] `npm run build` → **PASSED** (附构建产物路径)
- [ ] `curl http://localhost:3000/health` → **200 OK**
- [ ] 关键 API 手动测试通过 (附 curl 命令 + 响应)

### 测试输出
```bash
$ npm run lint
> eslint src/ --ext .ts
✓ 0 problems

$ npm run test
> jest --coverage
PASS  src/auth/login.test.ts
  login()
    ✓ should return JWT on valid credentials (15ms)
    ✓ should throw AuthError on invalid password (8ms)
Coverage: 85% (required: ≥80%)

$ npm run build
> tsc --project tsconfig.json
✓ Build completed in 3.2s
Output: dist/
````

### 手动测试

```bash
# Login API 测试
curl -X POST http://localhost:3000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","password":"123456"}'

# Expected: {"token":"eyJhbGc...","expiresIn":3600}
# Actual: ✅ Match
```

### 结论

- [ ] 所有检查项通过，可以交付 QA
- [ ] 存在失败项，需要修复 (见 ERROR_LOG.md)

```

### 质量门禁升级

| 门禁 | 原要求 | 新增要求 |
|------|--------|----------|
| Gate 3: 开发评审 | 自验证通过 | + lint/test/build 全部通过 + VALIDATION_LOG.md |
| Gate 4: 测试评审 | E2E 通过 | + 看到 VALIDATION_LOG.md 才接受交付 |

### 违规处理
- `dev-engineer` 未附 VALIDATION_LOG.md → `qa-engineer` 必须拒绝接收
- `qa-engineer` 在无 VALIDATION_LOG.md 情况下验收 → 双打回 + 记录违规

---

## 📋 新增模板文件

| 文件 | 用途 | 维护者 | 使用时机 |
|------|------|--------|----------|
| `CODEBASE_INDEX.md` | 代码库索引 | dev-engineer | 项目启动时创建，变更时更新 |
| `VALIDATION_LOG.md` | 自动化验证日志 | dev-engineer | 每次交付 QA 前 |
| `TASK_TRACKER.md` | 任务状态追踪 | ai-orchestrator | 每 2-3 分钟更新 |
| `ERROR_LOG.md` | 错误记录与恢复 | 所有智能体 | 遇到错误时立即记录 |
| `SECURITY_CHECKLIST.md` | 安全基线检查 | tech-leader + dev-engineer | 架构评审 + 开发完成 + 测试前 |
| `CODE_REVIEW_CHECKLIST.md` | 代码审查清单 | tech-leader | 代码合并前 |
| `INTEGRATION_TEST_PLAN.md` | 集成/E2E 测试计划 | qa-engineer | 开发交付后，发布前 |
| `DEPLOYMENT_READINESS.md` | 部署就绪检查 | devops-engineer | 生产部署前 |

---

## 🎯 完整质量门禁流程 (5 Gates + 4 Checklists + 6 Phases)

```

Phase 1: 需求定义 ↓ [Gate 1: PRD 评审] → product-manager ↓ Phase 2: 架构设计 ↓ [Gate 2: 架构评审] → architect +
tech-leader ├─ SECURITY_CHECKLIST.md Phase 1 (架构安全评审) ↓ Phase 3: UI 设计 ↓ Phase 4: 开发实现 (6 阶段流程) ├─ Phase
0: 需求澄清 (5 个关键点) ⛔ 禁止跳过 ├─ Phase 1: 定位入口 + 建立上下文 ├─ Phase 2: 方案决策 (小/中/大改动分类) ├─ Phase
3: 微设计 (子任务 A-E) ├─ Phase 4: 编码 (最小可运行增量) ├─ Phase 5: 验证 (4 层验证) ├─ Phase 6: 对齐 (不确定性时停止)
├─ CODEBASE_INDEX.md 更新 ├─ VALIDATION_LOG.md 填写 (lint/test/build/curl) ├─ SECURITY_CHECKLIST.md Phase 2
(开发安全自查) ↓ [Gate 3: 开发评审] → dev-engineer + tech-leader ├─ CODE_REVIEW_CHECKLIST.md 签字 ├─
6 阶段流程合规性检查 (tech-leader) ↓ Phase 5: 测试验证 ├─ INTEGRATION_TEST_PLAN.md 执行 ├─ SECURITY_CHECKLIST.md Phase 3
(安全测试) ↓ [Gate 4: 测试评审] → qa-engineer ├─ 验证 6 阶段流程完成 (qa-engineer) ↓ Phase 6: 部署运维 ├─
DEPLOYMENT_READINESS.md 检查 ↓ [Gate 5: 发布评审] → devops-engineer + ai-orchestrator ↓ ✅ 发布完成

```

---

## ✅ 签署确认

所有 9 个智能体必须在 AGENTS.md 中引用本协议，并承诺严格执行。

**最后更新**: 2026-03-20 13:38 (Asia/Shanghai)
```
