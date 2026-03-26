# VALIDATION_LOG.md

> **维护说明**:
>
> - 填写者：`dev-engineer` (每次声称"开发完成"前)
> - 审核者：`qa-engineer` (看到此日志才接受交付)
> - 用途：自动化验证钩子，确保代码质量（对标 Cursor 的自动 lint/test/build）
> - **重要**: 必须包含开发者 E2E 自验证，QA 看到此日志才接受交付

---

## 📋 Pre-Delivery Validation

### Task: [填写任务名称，如：Auth Module Implementation]

### Agent: dev-engineer

### Timestamp: [ISO 8601 格式，如：2026-03-20T14:30:00+08:00]

### Commit Hash: [Git commit ID，如：abc123f]

---

### ✅ 检查清单

#### 静态检查 (Static Checks)

- [ ] `npm run lint` → **PASSED** (0 errors)
- [ ] `npm run test` → **PASSED** (覆盖率 ≥80%)
- [ ] `npm run build` → **PASSED** (无编译错误)
- [ ] `CODEBASE_INDEX.md` 已更新 (如有新增文件/API)

#### 🔴 开发者 E2E 自验证 (Developer E2E Self-Verification) - MANDATORY

- [ ] `curl http://localhost:3000/health` → **200 OK**
- [ ] 关键 API 测试通过 (附 curl 命令 + 响应)
- [ ] 主路径端到端测试通过 (Smoke Test - 完整用户流程)
- [ ] 错误分支测试通过 (Wrong password, missing fields, etc.)
- [ ] 前端集成测试通过 (如适用 - 页面能调用 API，Token 存储，跳转等)

**⛔ 任何一项失败 → 不能交付 QA！**

---

### 📊 测试输出

#### Lint 结果

```bash
$ npm run lint
> eslint src/ --ext .ts

[在此粘贴完整输出]
✓ 0 problems

# 或如果有警告/错误：
✖ 3 problems (1 error, 2 warnings)
# → 如果有 error，不能交付！
```

#### 单元测试结果

```bash
$ npm run test
> jest --coverage

[在此粘贴完整输出]
PASS  src/auth/login.test.ts
  login()
    ✓ should return JWT on valid credentials (15ms)
    ✓ should throw AuthError on invalid password (8ms)
    ✓ should handle null user gracefully (5ms)

PASS  src/auth/jwt.test.ts
  generateJWT()
    ✓ should return valid token (10ms)
  verifyJWT()
    ✓ should throw on expired token (7ms)

Test Suites: 2 passed, 2 total
Tests:       5 passed, 5 total
Snapshots:   0 total
Time:        2.3s

----------|---------|----------|---------|---------|-------------------
File      | % Stmts | % Branch | % Funcs | % Lines | Uncovered Line #s
----------|---------|----------|---------|---------|-------------------
All files |   85.42 |    78.26 |   90.00 |   86.11 |
 login.ts |   92.31 |    85.71 |     100 |   91.67 | 23
 jwt.ts   |   78.57 |    70.83 |      80 |   80.65 | 45-48
----------|---------|----------|---------|---------|-------------------

# 要求：总覆盖率 ≥80%，关键模块 ≥90%
```

#### 构建结果

```bash
$ npm run build
> tsc --project tsconfig.json

[在此粘贴完整输出]
✓ Build completed in 3.2s
Output: dist/

# 或如果有编译错误：
src/auth/login.ts(23,5): error TS2322: Type 'null' is not assignable to type 'string'
# → 如果有 error，不能交付！
```

---

### 🔴 开发者 E2E 自验证 (Developer E2E Self-Verification)

**这是交付 QA 前的强制验证，必须全部通过！**

#### 1. 主路径端到端测试 (Smoke Test)

**场景**: [描述完整的用户流程，如：用户登录 → 查看首页 → 退出]

```bash
# Step 1: 登录
curl -X POST http://localhost:3000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","password":"Password123!"}'

# Expected: {"token":"...","expiresIn":3600}
# Actual: [粘贴实际响应]
# Result: ✅ PASS / ❌ FAIL

# Step 2: 使用 Token 访问受保护资源
curl -H "Authorization: Bearer [token]" http://localhost:3000/api/user/me

# Expected: {"id":"...","email":"test@example.com"}
# Actual: [粘贴实际响应]
# Result: ✅ PASS / ❌ FAIL

# Step 3: 前端集成验证 (如适用)
- [ ] 登录页面能调用 API
- [ ] Token 正确存储 (localStorage/cookie)
- [ ] 成功跳转到首页
- [ ] 用户信息显示正确
```

#### 2. 错误分支测试

**场景**: [描述错误场景，如：密码错误/用户不存在/字段缺失]

```bash
# Test: 密码错误
curl -X POST http://localhost:3000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","password":"wrongpassword"}'

# Expected: {"error":"INVALID_PASSWORD","message":"密码错误"}
# Actual: [粘贴实际响应]
# Result: ✅ PASS / ❌ FAIL

# Test: 字段缺失
curl -X POST http://localhost:3000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com"}'

# Expected: {"error":"VALIDATION_ERROR","message":"密码不能为空"}
# Actual: [粘贴实际响应]
# Result: ✅ PASS / ❌ FAIL
```

#### 3. 健康检查

```bash
curl http://localhost:3000/health

# Expected: {"status":"ok","timestamp":"..."}
# Actual: [粘贴实际响应]
# Result: ✅ PASS / ❌ FAIL
```

---

### 🔧 手动 API 测试

#### Test 1: Login API - 成功场景

```bash
# Request
curl -X POST http://localhost:3000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","password":"123456"}'

# Expected Response
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "expiresIn": 3600
}

# Actual Response
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "expiresIn": 3600
}

# Result: ✅ PASS (token 格式正确，expiresIn 符合预期)
```

#### Test 2: Login API - 密码错误

```bash
# Request
curl -X POST http://localhost:3000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","password":"wrongpassword"}'

# Expected Response
{
  "error": "INVALID_PASSWORD",
  "message": "密码错误"
}

# Actual Response
{
  "error": "INVALID_PASSWORD",
  "message": "密码错误"
}

# Result: ✅ PASS (错误码和消息匹配)
```

#### Test 3: Login API - 用户不存在

```bash
# Request
curl -X POST http://localhost:3000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"nonexistent@example.com","password":"123456"}'

# Expected Response
{
  "error": "USER_NOT_FOUND",
  "message": "用户不存在"
}

# Actual Response
{
  "error": "USER_NOT_FOUND",
  "message": "用户不存在"
}

# Result: ✅ PASS
```

#### Test 4: Health Check

```bash
# Request
curl http://localhost:3000/health

# Expected Response
{"status":"ok","timestamp":"2026-03-20T14:30:00.000Z"}

# Actual Response
{"status":"ok","timestamp":"2026-03-20T14:30:00.000Z"}

# Result: ✅ PASS
```

---

### 📁 交付物清单

- [ ] 源代码文件列表：
  - `src/auth/login.ts`
  - `src/auth/jwt.ts`
  - `src/db/user.ts`
  - `src/api/v1/auth.ts`

- [ ] 测试文件列表：
  - `src/auth/login.test.ts`
  - `src/auth/jwt.test.ts`

- [ ] 文档更新：
  - [x] `CODEBASE_INDEX.md` 已更新
  - [ ] `README.md` 已更新 (如需要)

- [ ] 数据库迁移：
  - [x] `migrations/001_create_users.sql` 已创建并执行

---

### ⚠️ 已知问题

| 问题描述 | 严重性 | 临时方案 | 计划修复时间 |
| -------- | ------ | -------- | ------------ |
| 无       | -      | -        | -            |

---

### 🎯 结论

- [x] **所有检查项通过，可以交付 QA**
- [ ] 存在失败项，需要修复 (见 `ERROR_LOG.md`)

**交付声明**: 本人确认以上测试全部通过，代码符合 PRD AC 和架构合同要求，无 placeholder/硬编码/已知严重 bug。

**签名**: dev-engineer **时间**: 2026-03-20T14:30:00+08:00

---

## 📝 历史验证记录

| 日期       | 任务        | 结果    | 审核者      |
| ---------- | ----------- | ------- | ----------- |
| 2026-03-20 | Auth Module | ✅ PASS | qa-engineer |

---

**使用说明**:

1. 复制此模板到新的验证记录区块
2. 填写所有检查项和输出
3. 如有失败项，先修复并记录到 `ERROR_LOG.md`
4. 全部通过后，通知 `qa-engineer` 进行 E2E 测试
