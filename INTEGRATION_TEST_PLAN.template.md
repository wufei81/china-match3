# INTEGRATION_TEST_PLAN.md

> **维护说明**:
>
> - 填写者：`qa-engineer` (主导) + `dev-engineer` (协助)
> - 用途：集成测试和 E2E 测试计划与执行记录
> - 时机：开发交付后，发布前

---

## 📋 测试计划信息

| 字段                     | 值                                          |
| ------------------------ | ------------------------------------------- |
| 项目名称                 |                                             |
| 测试负责人 (qa-engineer) |                                             |
| 测试开始日期             |                                             |
| 测试环境                 | ⬜ Development / ⬜ Staging / ⬜ Production |
| 测试版本                 | Git Commit: **\_\_\_**                      |
| 参考文档                 | PRD: **_ ARCH: _** API: \_\_\_              |

---

## 🎯 测试范围

### P0 功能 (必须测试)

| 功能 ID | 功能名称         | 优先级 | 测试类型  | 状态 |
| ------- | ---------------- | ------ | --------- | ---- |
| F001    | 用户登录         | P0     | E2E + API | ⬜   |
| F002    | 用户注册         | P0     | E2E + API | ⬜   |
| F003    | [核心业务功能 1] | P0     | E2E + API | ⬜   |
| F004    | [核心业务功能 2] | P0     | E2E + API | ⬜   |

### P1 功能 (重要)

| 功能 ID | 功能名称     | 优先级 | 测试类型 | 状态 |
| ------- | ------------ | ------ | -------- | ---- |
| F101    | 用户信息更新 | P1     | API      | ⬜   |
| F102    | 数据查询     | P1     | API      | ⬜   |
| F103    | [重要功能 1] | P1     | API      | ⬜   |

### P2 功能 (可选)

| 功能 ID | 功能名称    | 优先级 | 测试类型    | 状态 |
| ------- | ----------- | ------ | ----------- | ---- |
| F201    | UI 细节优化 | P2     | UI          | ⬜   |
| F202    | 性能优化    | P2     | Performance | ⬜   |

---

## 🔬 API 测试用例

### 1. 认证模块

#### Test 1.1: 用户登录 - 成功场景

```yaml
测试 ID: API-AUTH-001
功能：用户登录
优先级：P0
前置条件：
  - 用户已注册：test@example.com / Password123!
测试步骤:
  1. POST /api/auth/login
  2. Body: {"email": "test@example.com", "password": "Password123!"}
预期结果:
  - 状态码：200 OK
  - 响应体包含：token (JWT), expiresIn
  - token 格式正确 (三段式)
实际结果:
  - 状态码：___
  - 响应体：___
测试状态：⬜ Pass / ⬜ Fail / ⬜ Blocked
```

#### Test 1.2: 用户登录 - 密码错误

```yaml
测试 ID: API-AUTH-002
功能：用户登录 - 错误处理
优先级：P0
前置条件：用户已注册
测试步骤:
  1. POST /api/auth/login
  2. Body: {"email": "test@example.com", "password": "wrongpassword"}
预期结果:
  - 状态码：401 Unauthorized
  - 错误码：INVALID_PASSWORD
  - 错误消息清晰
实际结果:
  - 状态码：___
  - 响应体：___
测试状态：⬜ Pass / ⬜ Fail / ⬜ Blocked
```

#### Test 1.3: 用户登录 - 用户不存在

```yaml
测试 ID: API-AUTH-003
功能：用户登录 - 错误处理
优先级：P0
前置条件：无
测试步骤:
  1. POST /api/auth/login
  2. Body: {"email": "nonexistent@example.com", "password": "Password123!"}
预期结果:
  - 状态码：404 Not Found
  - 错误码：USER_NOT_FOUND
实际结果:
  - 状态码：___
  - 响应体：___
测试状态：⬜ Pass / ⬜ Fail / ⬜ Blocked
```

#### Test 1.4: 无 Token 访问受保护 API

```yaml
测试 ID: API-AUTH-004
功能：鉴权验证
优先级：P0
前置条件：无
测试步骤:
  1. GET /api/user/me (无 Authorization header)
预期结果:
  - 状态码：401 Unauthorized
  - 错误码：TOKEN_REQUIRED
实际结果:
  - 状态码：___
  - 响应体：___
测试状态：⬜ Pass / ⬜ Fail / ⬜ Blocked
```

#### Test 1.5: 无效 Token 访问

```yaml
测试 ID: API-AUTH-005
功能：鉴权验证
优先级：P0
前置条件：无
测试步骤:
  1. GET /api/user/me
  2. Authorization: Bearer invalid_token_xyz
预期结果:
  - 状态码：401 Unauthorized
  - 错误码：TOKEN_INVALID
实际结果:
  - 状态码：___
  - 响应体：___
测试状态：⬜ Pass / ⬜ Fail / ⬜ Blocked
```

---

### 2. 数据库模块

#### Test 2.1: SQL 注入防护 - 表名注入

```yaml
测试 ID: API-DB-001
功能：SQL 注入防护
优先级：P0
前置条件：用户已登录
测试步骤:
  1. POST /api/database/query
  2. Body: {"sql": "SELECT * FROM users; DROP TABLE users;--"}
预期结果:
  - 状态码：400 Bad Request
  - 错误码：SQL_INJECTION_DETECTED
  - 或：仅执行 SELECT，DROP 被拦截
实际结果:
  - 状态码：___
  - 响应体：___
测试状态：⬜ Pass / ⬜ Fail / ⬜ Blocked
```

#### Test 2.2: SQL 注入防护 - 特殊字符

```yaml
测试 ID: API-DB-002
功能：SQL 注入防护
优先级：P0
前置条件：用户已登录
测试步骤:
  1. POST /api/database/query
  2. Body: {"sql": "SELECT * FROM users WHERE name = '' OR '1'='1'"}
预期结果:
  - 状态码：400 Bad Request
  - 或：返回单条记录（参数化转义）
实际结果:
  - 状态码：___
  - 响应体：___
测试状态：⬜ Pass / ⬜ Fail / ⬜ Blocked
```

#### Test 2.3: 越权访问 - 访问他人数据

```yaml
测试 ID: API-DB-003
功能：权限验证
优先级：P0
前置条件：用户 A 和用户 B 已登录
测试步骤:
  1. 用户 A 请求：GET /api/data/{用户 B 的 ID}
预期结果:
  - 状态码：403 Forbidden
  - 错误码：ACCESS_DENIED
实际结果:
  - 状态码：___
  - 响应体：___
测试状态：⬜ Pass / ⬜ Fail / ⬜ Blocked
```

---

### 3. CORS 测试

#### Test 3.1: 跨域请求 - 允许的域名

```yaml
测试 ID: API-CORS-001
功能：CORS 配置
优先级：P1
前置条件：无
测试步骤:
  1. 从 https://allowed-domain.com 发起跨域请求
  2. 带凭据 (Cookie/Authorization)
预期结果:
  - Access-Control-Allow-Origin: https://allowed-domain.com
  - Access-Control-Allow-Credentials: true
实际结果:
  - Access-Control-Allow-Origin: ___
  - Access-Control-Allow-Credentials: ___
测试状态：⬜ Pass / ⬜ Fail / ⬜ Blocked
```

#### Test 3.2: 跨域请求 - 未允许的域名

```yaml
测试 ID: API-CORS-002
功能：CORS 配置
优先级：P1
前置条件：无
测试步骤:
  1. 从 https://malicious-site.com 发起跨域请求
预期结果:
  - Access-Control-Allow-Origin: 不存在或不匹配
实际结果:
  - Access-Control-Allow-Origin: ___
测试状态：⬜ Pass / ⬜ Fail / ⬜ Blocked
```

---

## 🎭 E2E 测试用例

### E2E Test 1: 用户注册 → 登录 → 访问受保护资源

```yaml
测试 ID: E2E-001
功能：完整用户流程
优先级：P0
前置条件：无
测试步骤:
  1. 访问注册页面
  2. 填写注册表单 (email, password)
  3. 提交注册
  4. 验证注册成功提示
  5. 访问登录页面
  6. 使用刚注册的账号登录
  7. 验证登录成功（跳转到首页/显示用户信息）
  8. 访问受保护 API (/api/user/me)
  9. 验证返回正确的用户信息
预期结果:
  - 所有步骤成功
  - 无错误提示
  - 数据一致性正确
实际结果:
  - 步骤 1-9: ⬜ Pass / ⬜ Fail
  - 截图/录屏：___
测试状态：⬜ Pass / ⬜ Fail / ⬜ Blocked
```

### E2E Test 2: 错误流程 - 登录失败后重试

```yaml
测试 ID: E2E-002
功能：错误处理
优先级：P1
前置条件：用户已注册
测试步骤:
  1. 访问登录页面
  2. 输入错误密码
  3. 提交登录
  4. 验证错误提示显示
  5. 输入正确密码
  6. 提交登录
  7. 验证登录成功
预期结果:
  - 步骤 4 显示清晰的错误消息
  - 步骤 7 登录成功
  - 无状态混乱
实际结果:
  - 步骤 1-7: ⬜ Pass / ⬜ Fail
测试状态：⬜ Pass / ⬜ Fail / ⬜ Blocked
```

---

## 🔒 安全测试用例

### Security Test 1: 敏感信息泄露

```yaml
测试 ID: SEC-001
功能：信息安全
优先级：P0
测试步骤:
  1. 检查所有 API 响应
  2. 检查日志输出
  3. 检查前端源码
预期结果:
  - 无明文密码
  - 无完整信用卡号
  - 无明文密钥
  - 无数据库连接字符串
实际结果:
  - API 响应：⬜ 清洁 / ⬜ 有泄露
  - 日志：⬜ 清洁 / ⬜ 有泄露
  - 前端：⬜ 清洁 / ⬜ 有泄露
测试状态：⬜ Pass / ⬜ Fail / ⬜ Blocked
```

### Security Test 2: 暴力破解防护

```yaml
测试 ID: SEC-002
功能：暴力破解防护
优先级：P1
测试步骤:
  1. 连续 10 次登录失败（同一账号）
  2. 观察是否有速率限制/账号锁定
预期结果:
  - 第 N 次失败后触发限制
  - 或：需要验证码
  - 或：账号临时锁定
实际结果:
  - 触发限制：第___次
  - 限制方式：___
测试状态：⬜ Pass / ⬜ Fail / ⬜ Blocked
```

---

## 📊 测试结果汇总

### 测试执行统计

| 测试类型 | 总数   | Pass   | Fail   | Blocked | 通过率  |
| -------- | ------ | ------ | ------ | ------- | ------- |
| API 测试 | \_\_\_ | \_\_\_ | \_\_\_ | \_\_\_  | \_\_\_% |
| E2E 测试 | \_\_\_ | \_\_\_ | \_\_\_ | \_\_\_  | \_\_\_% |
| 安全测试 | \_\_\_ | \_\_\_ | \_\_\_ | \_\_\_  | \_\_\_% |
| **总计** | \_\_\_ | \_\_\_ | \_\_\_ | \_\_\_  | \_\_\_% |

### P0 问题列表 (必须修复)

| 问题 ID | 测试 ID | 问题描述 | 严重性 | 状态               |
| ------- | ------- | -------- | ------ | ------------------ |
| BUG-001 |         |          | P0     | ⬜ Open / ⬜ Fixed |
| BUG-002 |         |          | P0     | ⬜ Open / ⬜ Fixed |

### P1 问题列表 (重要)

| 问题 ID | 测试 ID | 问题描述 | 严重性 | 状态               |
| ------- | ------- | -------- | ------ | ------------------ |
| BUG-101 |         |          | P1     | ⬜ Open / ⬜ Fixed |

---

## ✅ 发布决策

### 发布标准检查

- [ ] 所有 P0 测试用例 Pass
- [ ] 所有 P1 测试用例 Pass 或 有临时方案
- [ ] P0 Bug 全部修复
- [ ] P1 Bug 修复率 ≥90%
- [ ] SECURITY_CHECKLIST.md 全部通过
- [ ] VALIDATION_LOG.md 完整
- [ ] CODE_REVIEW_CHECKLIST.md 已签字

### 发布结论

- [ ] **批准发布** - 所有标准满足
- [ ] **条件批准** - 有***个 P1 问题，限期***前修复
- [ ] **拒绝发布** - 存在 P0 问题或 P1 问题超标

**qa-engineer 签字**: ******\_\_\_****** **日期**: ******\_\_\_******

**tech-leader 确认**: ******\_\_\_****** **日期**: ******\_\_\_******

---

## 📝 缺陷记录

| Bug ID | 发现日期 | 测试用例 | 描述 | 严重性   | 状态                          | 修复日期 |
| ------ | -------- | -------- | ---- | -------- | ----------------------------- | -------- |
|        |          |          |      | P0/P1/P2 | ⬜ Open ⬜ Fixed ⬜ Won't Fix |          |

---

**模板版本**: 1.0 **最后更新**: 2026-03-20 **使用说明**:
qa-engineer 必须在 E2E 测试前制定此计划，测试完成后填写结果并签字
