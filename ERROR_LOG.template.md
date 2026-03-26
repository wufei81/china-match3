# ERROR_LOG.md

> **维护说明**:
>
> - 填写者：**任何智能体** (遇到错误时立即记录)
> - 用途：错误追踪 + 自动恢复机制 (对标 Cursor 的错误重试)
> - 原则：谁遇到谁记录，谁修复谁更新

---

## 🔴 错误记录模板

### Error #001 - [YYYY-MM-DD HH:mm]

**发现者**: [智能体名称，如：dev-engineer] **文件**: `src/path/to/file.ts` **错误类型**:
[编译错误/运行时错误/测试失败/API 错误] **严重性**: 🔴 P0 (阻塞) / 🟡 P1 (重要) / 🔵 P2 (次要)

---

#### 错误详情

```bash
# 错误输出 (完整堆栈/日志)
TypeError: Cannot read property 'passwordHash' of null
    at login (/app/src/auth/login.ts:23:15)
    at processTicksAndRejections (node:internal/process/task_queues:95:5)
```

---

#### 触发场景

```bash
# 复现步骤 (命令/API 调用/操作)
curl -X POST http://localhost:3000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"nonexistent@example.com","password":"123456"}'
```

**前置条件**:

- 数据库中存在用户：test@example.com
- 请求邮箱：nonexistent@example.com (不存在)

---

#### 根因分析

**假设**: `findUserByEmail()` 返回 `null` 时，代码直接访问了 `user.passwordHash` 导致空指针

**验证方法**:

```typescript
// 问题代码 (第 23 行)
const user = await findUserByEmail(email);
if (!valid) throw new AuthError("INVALID_PASSWORD"); // ❌ user 可能为 null

// 修复后
const user = await findUserByEmail(email);
if (!user) throw new AuthError("USER_NOT_FOUND"); // ✅ 先检查 null
const valid = await bcrypt.compare(password, user.passwordHash);
if (!valid) throw new AuthError("INVALID_PASSWORD");
```

---

#### 修复尝试

**Attempt #1** - [YYYY-MM-DD HH:mm]

- **方案**: 添加 null 检查
- **代码变更**:
  ```diff
  - const valid = await bcrypt.compare(password, user.passwordHash);
  + if (!user) throw new AuthError('USER_NOT_FOUND');
  + const valid = await bcrypt.compare(password, user.passwordHash);
  ```
- **结果**: ✅ 修复成功 / ❌ 仍然失败 (见 Attempt #2)

**Attempt #2** - [YYYY-MM-DD HH:mm] (如需要)

- **方案**: [描述第二种尝试]
- **结果**: ✅ / ❌

**Attempt #3** - [YYYY-MM-DD HH:mm] (如需要)

- **方案**: [描述第三种尝试]
- **结果**: ✅ / ❌

---

#### 升级处理

如果 3 次尝试后仍未修复：

**已通知**:

- [ ] tech-leader (技术评审)
- [ ] ai-orchestrator (任务协调)
- [ ] architect (架构变更)

**升级原因**: [说明为什么需要人工干预]

**后续计划**: [描述下一步行动]

---

#### 经验教训

**记录到 self-improving-agent**: [是/否] **关键学习**: [一句话总结，如："访问外部数据前必须先检查 null"]

---

## 📊 错误统计

| 日期       | 错误数 | P0  | P1  | P2  | 平均修复时间 |
| ---------- | ------ | --- | --- | --- | ------------ |
| 2026-03-20 | 1      | 0   | 1   | 0   | 15 分钟      |

---

## 📝 历史错误记录

| Error # | 日期       | 文件     | 类型   | 严重性 | 状态     | 修复者       |
| ------- | ---------- | -------- | ------ | ------ | -------- | ------------ |
| #001    | 2026-03-20 | login.ts | 运行时 | P1     | ✅ Fixed | dev-engineer |

---

## 🔄 错误恢复流程

```
发现错误
   ↓
记录到 ERROR_LOG.md
   ↓
分析根因
   ↓
尝试修复 (最多 3 次)
   ↓
成功？→ 更新 VALIDATION_LOG.md → 继续交付
   ↓
失败？→ 升级到 tech-leader + ai-orchestrator
```

---

**使用说明**:

1. 遇到错误立即记录 (不要等)
2. 填写完整信息 (便于后续分析)
3. 每次修复尝试都要记录
4. 3 次失败后必须升级
5. 修复后更新 `VALIDATION_LOG.md` 和 `CODEBASE_INDEX.md` (如需要)
