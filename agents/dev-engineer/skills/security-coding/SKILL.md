# Security Coding Skill - 安全编码技能

**版本**: 1.0
**创建日期**: 2026-03-26
**触发词**: "安全编码", "安全开发", "漏洞预防", "secure coding", "OWASP", "security"

---

## 🎯 技能概述

为开发工程师智能体提供安全编码能力，包括安全编码规范、常见漏洞预防、输入验证、安全 API 设计。帮助将安全内置于代码层面，而非事后修补。

---

## 📊 核心功能

### 1. 安全编码规范

**目的**: 编写安全代码，预防常见漏洞

#### 通用安全编码原则

| 原则 | 描述 | 示例 |
|------|------|------|
| **验证所有输入** | 不信任任何外部输入 | 参数验证、类型检查 |
| **最小权限** | 使用最低必要权限 | DB 只读账号、文件权限 |
| **防御性编程** | 假设会出错 | 异常处理、边界检查 |
| **安全默认值** | 默认配置是安全的 | 默认拒绝、默认加密 |
| **不泄露敏感信息** | 错误信息不暴露细节 | 通用错误消息 |

#### 语言特定安全规范

**Node.js 安全编码**:
```javascript
// ✅ 参数化查询 (防 SQL 注入)
const user = await db.query(
  'SELECT * FROM users WHERE id = $1',
  [userId]
);

// ✅ 路径清理 (防路径遍历)
const safePath = path.join(baseDir, path.normalize(userPath));
if (!safePath.startsWith(baseDir)) {
  throw new Error('Invalid path');
}

// ✅ 安全随机数
const token = crypto.randomBytes(32).toString('hex');

// ❌ 不安全：Math.random()
const token = Math.random().toString(); // 可预测
```

**Python 安全编码**:
```python
# ✅ 参数化查询
cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))

# ✅ 安全命令执行
subprocess.run(['ls', '-la'], shell=False)  # 不用 shell

# ✅ 安全反序列化
import json
data = json.loads(user_input)  # 不用 pickle
```

---

### 2. 输入验证

**目的**: 防止恶意输入导致的安全漏洞

#### 输入验证策略

| 策略 | 描述 | 适用场景 |
|------|------|---------|
| **白名单** | 只允许已知安全值 | 枚举值、固定选项 |
| **黑名单** | 拒绝已知危险值 | 特殊字符过滤 |
| **类型检查** | 验证数据类型 | 数字、布尔值 |
| **范围检查** | 验证数值范围 | 年龄、金额 |
| **长度限制** | 限制输入长度 | 用户名、密码 |

#### 输入验证模板

```javascript
// ✅ 完整输入验证示例
const userSchema = Joi.object({
  username: Joi.string()
    .alphanum()
    .min(3)
    .max(30)
    .required(),
  
  email: Joi.string()
    .email()
    .required(),
  
  password: Joi.string()
    .min(8)
    .pattern(/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)/)
    .required(),
  
  age: Joi.number()
    .min(0)
    .max(150),
  
  role: Joi.string()
    .valid('user', 'admin') // 白名单
    .default('user')
});

// 使用
const { error, value } = userSchema.validate(req.body);
if (error) {
  return res.status(400).json({ error: 'Invalid input' });
}
```

#### XSS 防护

```javascript
// ✅ 输出编码
function escapeHtml(text) {
  const map = {
    '&': '&amp;',
    '<': '&lt;',
    '>': '&gt;',
    '"': '&quot;',
    "'": '&#039;'
  };
  return text.replace(/[&<>"']/g, m => map[m]);
}

// ✅ React 自动转义
<div>{userInput}</div> // 安全

// ❌ 危险： dangerouslySetInnerHTML
<div dangerouslySetInnerHTML={{__html: userInput}} /> // XSS 风险
```

---

### 3. 认证与授权

**目的**: 实现安全的身份验证和访问控制

#### 认证安全

```javascript
// ✅ 密码存储
const bcrypt = require('bcrypt');
const saltRounds = 12;

// 哈希密码
const hash = await bcrypt.hash(password, saltRounds);

// 验证密码
const match = await bcrypt.compare(password, hash);

// ✅ Token 管理
const jwt = require('jsonwebtoken');

// 签发 Token
const token = jwt.sign(
  { userId: user.id, role: user.role },
  process.env.JWT_SECRET,
  { expiresIn: '1h' }
);

// 验证 Token
try {
  const decoded = jwt.verify(token, process.env.JWT_SECRET);
} catch (err) {
  // Token 无效或过期
}

// ✅ 防暴力破解
const rateLimit = require('express-rate-limit');

const loginLimiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 分钟
  max: 5, // 最多 5 次
  message: 'Too many login attempts'
});
```

#### 授权检查

```javascript
// ✅ 服务端权限校验 (每接口)
async function deleteUser(req, res) {
  const userId = req.params.id;
  const currentUser = req.user;
  
  // 权限检查
  if (currentUser.role !== 'admin' && currentUser.id !== userId) {
    return res.status(403).json({ error: 'Forbidden' });
  }
  
  // 执行删除
  await db.users.delete(userId);
}

// ✅ 资源级授权
async function getOrder(req, res) {
  const orderId = req.params.id;
  const userId = req.user.id;
  
  // 确保用户只能访问自己的订单
  const order = await db.orders.findOne({
    where: { id: orderId, userId } // 关键：加上 userId
  });
  
  if (!order) {
    return res.status(404).json({ error: 'Not found' });
  }
}
```

---

### 4. 数据安全

**目的**: 保护敏感数据的机密性和完整性

#### 数据加密

```javascript
// ✅ 传输加密 (HTTPS/TLS)
// 配置强制 HTTPS
app.use((req, res, next) => {
  if (!req.secure) {
    return res.redirect(`https://${req.headers.host}${req.url}`);
  }
  next();
});

// ✅ 敏感数据加密存储
const crypto = require('crypto');

function encrypt(text, key) {
  const iv = crypto.randomBytes(16);
  const cipher = crypto.createCipheriv('aes-256-gcm', key, iv);
  let encrypted = cipher.update(text, 'utf8', 'hex');
  encrypted += cipher.final('hex');
  return {
    iv: iv.toString('hex'),
    encrypted,
    authTag: cipher.getAuthTag().toString('hex')
  };
}

// ✅ 日志脱敏
function sanitizeLog(data) {
  const sensitive = ['password', 'token', 'secret', 'creditCard'];
  const sanitized = { ...data };
  sensitive.forEach(key => {
    if (sanitized[key]) {
      sanitized[key] = '***REDACTED***';
    }
  });
  return sanitized;
}
```

#### SQL 注入防护

| 风险等级 | 代码示例 | 修复方案 |
|---------|---------|---------|
| 🔴 高危 | `db.query("SELECT * FROM users WHERE id=" + userId)` | 参数化查询 |
| 🟠 中危 | `db.query("SELECT * FROM users WHERE name='" + name + "'")` | ORM/参数化 |
| 🟢 低危 | 使用 ORM 但动态表名 | 白名单验证表名 |

---

### 5. 安全 API 设计

**目的**: 设计安全的 API 接口

#### API 安全清单

```markdown
## API 安全设计清单

### 认证
- [ ] 所有接口需要认证 (公开接口明确标注)
- [ ] Token 有合理过期时间
- [ ] Token 吊销机制
- [ ] 支持 Token 刷新

### 授权
- [ ] 每接口权限校验
- [ ] 资源级访问控制
- [ ] 水平越权防护
- [ ] 垂直越权防护

### 输入
- [ ] 参数验证 (类型、范围、格式)
- [ ] 请求体大小限制
- [ ] 文件上传安全 (类型、大小、扫描)
- [ ] 防重放攻击 (nonce/timestamp)

### 输出
- [ ] 错误信息不泄露细节
- [ ] 敏感数据脱敏
- [ ] 统一错误格式
- [ ] 分页限制 (防数据泄露)

### 速率限制
- [ ] 每用户/每 IP 限流
- [ ] 每接口限流
- [ ] 全局限流

### 审计
- [ ] 关键操作日志
- [ ] 登录日志
- [ ] 数据变更日志
- [ ] 异常行为检测
```

#### 安全响应头

```javascript
// ✅ 安全响应头配置
app.use((req, res, next) => {
  // 防止 XSS
  res.setHeader('X-Content-Type-Options', 'nosniff');
  res.setHeader('X-Frame-Options', 'DENY');
  res.setHeader('X-XSS-Protection', '1; mode=block');
  
  // 内容安全策略
  res.setHeader('Content-Security-Policy', 
    "default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'");
  
  // HSTS
  res.setHeader('Strict-Transport-Security', 
    'max-age=31536000; includeSubDomains');
  
  next();
});
```

---

## 🔧 使用示例

### 示例 1: 安全代码审查

**输入**: "审查这段登录代码的安全性"

**输出**:
```markdown
## 安全审查报告

### ✅ 符合项
- 使用 bcrypt 哈希密码
- 有速率限制

### ⚠️ 需改进
1. **错误信息过细** → 改为通用错误
2. **缺少登录日志** → 添加审计日志
3. **Token 无过期** → 设置合理过期时间

### ❌ 严重问题
1. **密码明文日志** → 立即移除
2. **无 HTTPS 强制** → 添加重定向

### 修复建议 (优先级)
P0: 移除密码日志，强制 HTTPS
P1: 通用错误消息，添加登录日志
P2: Token 过期策略
```

### 示例 2: 安全 API 设计

**输入**: "设计一个安全的文件上传 API"

**输出**:
```markdown
## 安全文件上传 API 设计

### 安全措施
1. **认证**: JWT Token 验证
2. **授权**: 仅登录用户可上传
3. **文件类型**: 白名单 (jpg, png, pdf)
4. **文件大小**: 限制 10MB
5. **文件名**: 随机生成，不信任用户输入
6. **病毒扫描**: 上传后扫描
7. **存储**: 独立存储服务器，不可执行

### 代码示例
```javascript
const upload = multer({
  storage: multer.diskStorage({
    filename: (req, file, cb) => {
      // 随机文件名
      cb(null, crypto.randomBytes(16).toString('hex'));
    }
  }),
  fileFilter: (req, file, cb) => {
    // 白名单验证
    const allowed = ['image/jpeg', 'image/png', 'application/pdf'];
    cb(null, allowed.includes(file.mimetype));
  },
  limits: {
    fileSize: 10 * 1024 * 1024 // 10MB
  }
});
```
```

---

## 📋 输出规范

1. **防御性**: 假设输入都是恶意的
2. **最小权限**: 只授予必要权限
3. **纵深防御**: 多层防护措施
4. **可审计**: 所有安全事件可追溯

---

## ⚠️ 注意事项

- ⛔ 不要自己发明加密算法
- ⛔ 不要在前端存储敏感信息
- ⛔ 不要信任客户端验证
- ✅ 定期安全培训和代码审计

---

## 🔗 相关技能

- `code-quality` - 代码质量
- `security-architecture` - 安全架构 (Architect)
- `api-tester` - API 测试

---

**最后更新**: 2026-03-26
**维护者**: DevEngineer
