# 测试修复记录 - 2026-03-27

**修复人**: DevEngineer  
**时间**: 09:15-09:30  
**状态**: 🟡 部分修复

---

## ✅ 已修复

### Patch 路径问题

**修复内容**:
```bash
# 批量替换 patch 路径
app.api.v1.auth.crud.* → app.crud.*
app.api.v1.auth.get_settings → app.config.get_settings
app.api.v1.auth.get_login_attempt_manager → app.auth.login_attempts.get_login_attempt_manager
```

**文件**: `tests/unit/test_api_auth.py`

**结果**: Patch 路径错误已修复

---

## ⚠️ 遗留问题 (代码 bug)

### 1. 缺少 mcp 模块

**错误**: `ModuleNotFoundError: No module named 'mcp'`

**测试**: `test_login_success`

**修复**: 需要安装 mcp 模块或移除导入

---

### 2. bcrypt 版本不兼容

**错误**: `module 'bcrypt' has no attribute 'CheckError'`

**测试**: `test_login_wrong_password`

**原因**: bcrypt 4.0+ 移除了 `CheckError`

**修复**:
```python
# 修复前
except bcrypt.CheckError:

# 修复后
except (ValueError, TypeError):
```

**文件**: `app/auth/security.py`

---

### 3. 异步函数未 await

**错误**: `'coroutine' object has no attribute 'first'`

**测试**: `test_login_account_locked`

**原因**: 数据库查询未 await

**修复**: 添加 await 关键字

---

### 4. CSRF cookie 未设置

**错误**: `AssertionError: 'csrf_token' not in ['access_token', 'refresh_token']`

**测试**: `test_login_sets_cookies`

**原因**: CSRF cookie 设置逻辑缺失

**修复**: 在 login 函数中添加 CSRF cookie 设置

---

### 5. Token 解码错误

**错误**: `Invalid header string: 'utf-8' codec can't decode byte 0x8a`

**测试**: `test_refresh_token_invalid`

**原因**: 测试生成的 token 格式不正确

**修复**: 使用正确的 token 生成方法

---

## 📋 建议修复计划

**优先级**: P1  
**预计工时**: 30 分钟  
**负责人**: DevEngineer

| 问题 | 难度 | 工时 | 优先级 |
|------|------|------|--------|
| bcrypt 版本 | 低 | 5 分钟 | P0 |
| 异步函数 await | 低 | 5 分钟 | P0 |
| CSRF cookie | 中 | 10 分钟 | P1 |
| Token 解码 | 中 | 10 分钟 | P1 |
| mcp 模块 | 低 | 5 分钟 | P2 |

---

**记录时间**: 2026-03-27 09:30  
**下次修复**: Day 7 上午
