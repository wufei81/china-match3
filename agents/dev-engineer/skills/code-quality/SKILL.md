# Code Quality Skill - 代码质量技能

**版本**: 1.0
**创建日期**: 2026-03-26
**触发词**: "代码质量", "代码审查", "重构", "代码规范", "clean code", "code review", "refactoring"

---

## 🎯 技能概述

为开发工程师智能体提供代码质量提升能力，包括代码审查清单、重构技巧、代码规范、Clean Code 原则。帮助从"能跑的代码"升级为"高质量代码"。

---

## 📊 核心功能

### 1. 代码审查清单

**目的**: 系统化代码审查，避免遗漏关键问题

#### 通用审查清单

```markdown
## 代码审查清单

### 功能正确性
- [ ] 代码实现符合需求
- [ ] 边界条件处理正确
- [ ] 错误处理完整
- [ ] 无逻辑错误

### 代码质量
- [ ] 函数职责单一 (SRP)
- [ ] 函数长度合理 (<50 行)
- [ ] 变量命名清晰
- [ ] 无重复代码 (DRY)
- [ ] 注释恰当 (解释 Why 而非 What)

### 安全性
- [ ] 输入验证完整
- [ ] 无 SQL 注入风险
- [ ] 无 XSS 风险
- [ ] 敏感数据不记录日志
- [ ] 权限校验正确

### 性能
- [ ] 无 N+1 查询
- [ ] 循环内无低效操作
- [ ] 资源正确释放
- [ ] 缓存使用合理

### 可测试性
- [ ] 单元测试覆盖
- [ ] 测试用例清晰
- [ ] Mock 使用合理
- [ ] 测试覆盖边界条件

### 可维护性
- [ ] 依赖最小化
- [ ] 配置外部化
- [ ] 日志完整可追踪
- [ ] 无硬编码
```

#### 前端专项审查清单

| 类别 | 检查项 |
|------|-------|
| **React** | 组件职责单一、避免过度渲染、正确使用 Hooks |
| **性能** | 图片优化、懒加载、代码分割 |
| **安全** | XSS 防护、CSP、依赖安全 |
| **可访问性** | ARIA 标签、键盘导航、对比度 |
| **样式** | 响应式、浏览器兼容、CSS 规范 |

#### 后端专项审查清单

| 类别 | 检查项 |
|------|-------|
| **API 设计** | RESTful 规范、版本控制、错误码统一 |
| **数据库** | 索引优化、事务使用、连接池配置 |
| **安全** | 认证授权、输入验证、速率限制 |
| **日志** | 结构化日志、敏感信息脱敏、日志级别 |
| **配置** | 环境分离、密钥管理、特性开关 |

---

### 2. 重构技巧

**目的**: 改善代码结构，不改变外部行为

#### 重构识别信号

| 信号 | 描述 | 重构方法 |
|------|------|---------|
| **重复代码** | 相同代码出现多次 | 提取函数/类 |
| **过长函数** | 函数超过 50 行 | 提取函数 |
| **过大类** | 类超过 500 行 | 提取类 |
| **过长参数列表** | 参数超过 5 个 | 参数对象 |
| **发散式变化** | 一个原因改多个类 | 移动方法/内联 |
| **霰弹式修改** | 一个修改改多个类 | 移动方法 |
| **依恋情结** | 函数访问他类数据 | 移动方法 |
| **数据泥团** | 经常一起出现的数据 | 提取类 |
| **基本类型偏执** | 过度使用基本类型 | 提取值对象 |
| **switch 语句** | 冗长 switch/case | 多态替换 |

#### 重构手法速查

```markdown
## 重构手法

### 组成函数提取 (Extract Function)
**场景**: 函数过长，职责不单一

**Before**:
```javascript
function processOrder(order) {
  // 计算总价 (50 行)
  // 验证库存 (30 行)
  // 创建订单记录 (40 行)
  // 发送邮件 (20 行)
}
```

**After**:
```javascript
function processOrder(order) {
  const total = calculateTotal(order);
  validateInventory(order);
  const record = createOrderRecord(order, total);
  sendConfirmationEmail(record);
}
```

### 类提取 (Extract Class)
**场景**: 类过大，职责不单一

**Before**:
```javascript
class User {
  // 用户数据
  // 用户验证
  // 用户通知
  // 用户报表 (500+ 行)
}
```

**After**:
```javascript
class User {
  // 用户数据 + 基本操作
}

class UserValidator {
  // 验证逻辑
}

class UserNotifier {
  // 通知逻辑
}
```

### 参数对象 (Introduce Parameter Object)
**场景**: 函数参数过多

**Before**:
```javascript
function createEvent(name, date, location, capacity, price, currency) {
}
```

**After**:
```javascript
function createEvent(eventConfig) {
  // eventConfig: { name, date, location, capacity, price, currency }
}
```

### 以多态取代条件 (Replace Conditional with Polymorphism)
**场景**: 冗长的 switch/case

**Before**:
```javascript
function getPaymentType(type) {
  switch(type) {
    case 'credit': return new CreditPayment();
    case 'paypal': return new PaypalPayment();
    case 'crypto': return new CryptoPayment();
  }
}
```

**After**:
```javascript
// 使用工厂模式 + 多态
const payment = PaymentFactory.create(type);
```
```

#### 重构优先级矩阵

```
                影响范围
            小 ←────────→ 大
          ┌─────────┬─────────┐
       高 │ 立即重构 │ 计划重构 │
  复      │ (技术债)│ (大改动)│
  杂   ──┼─────────┼─────────┤
  度      │ 可选重构 │ 避免重构 │
          │ (代码味)│ (风险高)│
          └─────────┴─────────┘
```

---

### 3. Clean Code 原则

**目的**: 编写可读、可维护、可测试的代码

#### 命名原则

| 原则 | 说明 | 示例 |
|------|------|------|
| **意图清晰** | 名字表达用途 | `daysSinceCreation` 而非 `d` |
| **可搜索** | 避免魔术数字 | `MAX_RETRY = 3` 而非 `if (x === 3)` |
| **有意义** | 避免废话 | `User` 而非 `UserDataInfo` |
| **可发音** | 能读出来 | `generationTimestamp` 而非 `genymdhms` |
| **一致性** | 同一概念统一命名 | `get/fetch/retrieve` 选一个 |

#### 函数原则

| 原则 | 说明 |
|------|------|
| **短小** | 理想<20 行，最大<50 行 |
| **单一职责** | 只做一件事 |
| **一个抽象层级** | 不要混用不同层级 |
| **参数少** | 理想 0-2 个，最多 5 个 |
| **无副作用** | 函数名要诚实 |

#### 注释原则

| 原则 | 说明 | 示例 |
|------|------|------|
| **解释 Why** | 不解释 What | `// 兼容旧版本 API` |
| **避免废话** | 不重复代码 | ❌ `// 获取用户` `getUser()` |
| **TODO 说明** | TODO 要完整 | `// TODO: 性能优化 - 使用缓存` |
| **警告注释** | 重要警告要醒目 | `// WARNING: 此方法非线程安全` |

#### 错误处理原则

```javascript
// ✅ 使用异常而非返回码
try {
  const result = riskyOperation();
} catch (error) {
  logger.error('Operation failed', { error, context });
  throw new BusinessError('OPERATION_FAILED', error);
}

// ✅ 不要返回 null
function findUser(id) {
  return user || null; // ❌
  return user; // ✅ 返回 Optional 或抛出异常
}

// ✅ 使用 Try-Catch-Finally 清理资源
async function fetchData() {
  const conn = await getConnection();
  try {
    return await conn.query(sql);
  } finally {
    await conn.release(); // 总是执行
  }
}
```

---

### 4. 代码度量标准

**目的**: 量化代码质量，持续改进

#### 核心度量指标

| 指标 | 目标值 | 说明 |
|------|-------|------|
| **代码覆盖率** | ≥80% | 单元测试覆盖比例 |
| **圈复杂度** | ≤10 | 函数复杂度 (分支数) |
| **重复率** | ≤5% | 重复代码比例 |
| **技术债务比** | ≤5% | 修复时间/开发时间 |
| **代码异味数** | 0 | 严重代码问题数 |
| **构建成功率** | ≥95% | CI 构建成功比例 |

#### 代码质量看板模板

```markdown
## 代码质量看板 - [项目名称]

### 核心指标
| 指标 | 当前值 | 目标值 | 趋势 |
|------|-------|-------|------|
| 代码覆盖率 | 75% | ≥80% | ↑ |
| 圈复杂度 (avg) | 8 | ≤10 | → |
| 重复率 | 3% | ≤5% | → |
| 技术债务 | 2.1% | ≤5% | ↓ |
| 代码异味 | 5 | 0 | ↓ |

### 待改进项
| 文件 | 问题 | 优先级 | 预计工时 |
|------|------|-------|---------|
| auth.ts | 圈复杂度 25 | P0 | 4h |
| user.service.ts | 重复代码 | P1 | 2h |

### 改进计划
- [ ] 重构 auth.ts (本周)
- [ ] 提取公共函数 (下周)
- [ ] 补充单元测试 (持续)
```

---

## 🔧 使用示例

### 示例 1: 代码审查

**输入**: "帮我审查这段代码"

**输出**:
```markdown
## 代码审查报告

### ✅ 优点
- 函数命名清晰
- 错误处理完整
- 有单元测试

### ⚠️ 需改进
1. **函数过长** (80 行) → 建议拆分为 3 个函数
2. **重复代码** → 提取公共逻辑
3. **缺少输入验证** → 添加参数校验

### ❌ 严重问题
1. **SQL 注入风险** → 改用参数化查询
2. **敏感信息日志** → 移除密码日志

### 建议优先级
P0: 修复安全问题
P1: 重构长函数
P2: 提取重复代码
```

### 示例 2: 重构建议

**输入**: "这个类 800 行，怎么重构"

**输出**:
```markdown
## 重构建议

### 问题分析
- 当前 800 行，违反单一职责
- 包含 5 个不同职责

### 拆分方案
1. **UserAuth** (150 行) - 认证逻辑
2. **UserProfile** (200 行) - 用户资料
3. **UserNotification** (180 行) - 通知
4. **UserAnalytics** (170 行) - 分析
5. **User** (100 行) - 核心模型

### 重构步骤
1. 先补测试 (保护网)
2. 提取 UserAuth
3. 提取 UserProfile
4. 继续提取其他
5. 最后清理 User 类
```

---

## 📋 输出规范

1. **具体可操作**: 审查意见要具体到行号和修改建议
2. **优先级明确**: P0/P1/P2 分级
3. **正向反馈**: 先肯定优点，再指出问题
4. **持续改进**: 定期回顾质量指标

---

## ⚠️ 注意事项

- ⛔ 审查对事不对人
- ⛔ 重构前先补测试
- ⛔ 不要过度优化 (YAGNI)
- ✅ 小步快跑，持续改进

---

## 🔗 相关技能

- `api-tester` - API 测试
- `performance-optimization` - 性能优化 (待创建)
- `security-coding` - 安全编码 (待创建)

---

**最后更新**: 2026-03-26
**维护者**: DevEngineer
