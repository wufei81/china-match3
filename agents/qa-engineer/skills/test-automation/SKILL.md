# Test Automation Skill - 测试自动化技能

**版本**: 1.0
**创建日期**: 2026-03-26
**触发词**: "测试自动化", "自动化框架", "E2E 测试", "测试脚本", "test automation", "E2E", "test framework"

---

## 🎯 技能概述

为 QA 工程师智能体提供测试自动化能力，包括自动化测试框架设计、E2E 测试脚本、持续集成、测试报告。帮助从"手动测试"升级为"自动化测试"。

---

## 📊 核心功能

### 1. 自动化测试框架设计

**目的**: 构建可维护、可扩展的自动化测试体系

#### 测试金字塔

```
        /\
       /  \
      / E2E \      10% (UI 测试)
     /--------\
    /Integration\   30% (API 测试)
   /------------\
  /   Unit Tests   \ 60% (单元测试)
 /------------------\
```

#### 框架选型对比

| 框架 | 语言 | 适用场景 | 优点 | 缺点 |
|------|------|---------|------|------|
| **Playwright** | TS/Python | E2E 测试 | 跨浏览器、自动等待 | 较新、生态待完善 |
| **Cypress** | JS | 前端测试 | 易用、调试友好 | 仅支持 Chrome 系 |
| **Selenium** | 多语言 | 通用 E2E | 成熟、生态完善 | 配置复杂、慢 |
| **Jest** | JS | 单元测试 | 快速、内置断言 | 仅支持 JS |
| **Pytest** | Python | 通用测试 | 插件丰富、简洁 | Python 生态 |
| **TestNG** | Java | 企业测试 | 功能强大 | 配置复杂 |

#### 框架设计模板

```markdown
## 自动化测试框架设计

### 技术选型
- **E2E 测试**: Playwright + TypeScript
- **API 测试**: Supertest + Jest
- **单元测试**: Jest + Testing Library
- **报告**: Allure Report
- **CI 集成**: GitHub Actions

### 目录结构
```
tests/
├── e2e/              # E2E 测试
│   ├── fixtures/     # 测试数据
│   ├── pages/        # Page Objects
│   └── specs/        # 测试用例
├── integration/      # 集成测试
│   └── api/          # API 测试
├── unit/             # 单元测试
│   └── components/   # 组件测试
├── utils/            # 工具函数
│   ├── test-data.ts  # 测试数据生成
│   └── helpers.ts    # 辅助函数
└── config/           # 配置文件
    ├── test.env      # 测试环境配置
    └── playwright.config.ts
```

### 核心能力
- **Page Object 模式**: 封装页面操作
- **数据驱动**: 测试数据与逻辑分离
- **自动重试**: 失败自动重试机制
- **并行执行**: 支持多浏览器并行
- **截图录像**: 失败自动截图
```

---

### 2. E2E 测试脚本

**目的**: 编写稳定、可维护的 E2E 测试

#### Playwright 最佳实践

```typescript
// Page Object 模式
class LoginPage {
  constructor(private page: Page) {}

  async goto() {
    await this.page.goto('/login');
  }

  async fillEmail(email: string) {
    await this.page.fill('[data-testid=email]', email);
  }

  async fillPassword(password: string) {
    await this.page.fill('[data-testid=password]', password);
  }

  async submit() {
    await this.page.click('[data-testid=submit]');
  }

  async login(email: string, password: string) {
    await this.goto();
    await this.fillEmail(email);
    await this.fillPassword(password);
    await this.submit();
  }
}

// 测试用例
test.describe('Login Flow', () => {
  let loginPage: LoginPage;

  test.beforeEach(async ({ page }) => {
    loginPage = new LoginPage(page);
  });

  test('should login successfully with valid credentials', async ({ page }) => {
    await loginPage.login('user@example.com', 'password123');
    
    await expect(page).toHaveURL('/dashboard');
    await expect(page.locator('[data-testid=user-name]'))
      .toHaveText('John Doe');
  });

  test('should show error with invalid credentials', async ({ page }) => {
    await loginPage.login('wrong@example.com', 'wrong');
    
    await expect(page.locator('[data-testid=error]'))
      .toHaveText('Invalid email or password');
  });
});
```

#### 测试数据管理

```typescript
// 测试数据工厂
class TestDataFactory {
  static createUser(overrides = {}) {
    return {
      email: `user_${Date.now()}@example.com`,
      password: 'Password123!',
      name: 'Test User',
      ...overrides
    };
  }

  static createProduct(overrides = {}) {
    return {
      name: `Product_${Date.now()}`,
      price: 99.99,
      stock: 100,
      ...overrides
    };
  }
}

// 测试夹具 (Fixtures)
const test = base.extend<{
  testData: { user: User; product: Product };
}>({
  testData: async ({}, use) => {
    const user = TestDataFactory.createUser();
    const product = TestDataFactory.createProduct();
    
    await use({ user, product });
    
    // 清理
    await cleanupTestData(user, product);
  }
});
```

---

### 3. API 测试

**目的**: 验证 API 功能、性能、安全性

#### API 测试模板

```typescript
// API 测试示例
describe('User API', () => {
  const API_BASE = '/api/v1';
  
  describe('POST /users', () => {
    it('should create user with valid data', async () => {
      const userData = TestDataFactory.createUser();
      
      const response = await request.post(`${API_BASE}/users`, {
        data: userData
      });
      
      expect(response.status).toBe(201);
      expect(response.body).toHaveProperty('id');
      expect(response.body.email).toBe(userData.email);
    });

    it('should return 400 with invalid email', async () => {
      const response = await request.post(`${API_BASE}/users`, {
        data: { email: 'invalid', password: 'Password123!' }
      });
      
      expect(response.status).toBe(400);
      expect(response.body.error).toHaveProperty('code', 'INVALID_EMAIL');
    });

    it('should return 409 with duplicate email', async () => {
      const userData = TestDataFactory.createUser();
      await createUser(userData); // 先创建
      
      const response = await request.post(`${API_BASE}/users`, {
        data: userData
      });
      
      expect(response.status).toBe(409);
      expect(response.body.error.code).toBe('EMAIL_EXISTS');
    });
  });
});
```

#### API 测试检查清单

| 测试类型 | 检查项 |
|---------|-------|
| **功能测试** | 正常流程、边界条件、错误处理 |
| **性能测试** | 响应时间、吞吐量、并发 |
| **安全测试** | 认证、授权、注入防护 |
| **兼容性** | 向后兼容、版本管理 |

---

### 4. 持续集成

**目的**: 自动化测试执行，快速反馈

#### CI/CD 配置示例

```yaml
# GitHub Actions
name: Test Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    
    services:
      postgres:
        image: postgres:14
        env:
          POSTGRES_PASSWORD: test
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
    
    steps:
      - uses: actions/checkout@v3
      
      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'
          cache: 'npm'
      
      - name: Install dependencies
        run: npm ci
      
      - name: Lint
        run: npm run lint
      
      - name: Unit Tests
        run: npm run test:unit
        env:
          CI: true
      
      - name: Build
        run: npm run build
      
      - name: E2E Tests
        run: npm run test:e2e
        env:
          DATABASE_URL: postgresql://postgres:test@localhost:5432/test
          CI: true
      
      - name: Upload Test Report
        uses: actions/upload-artifact@v3
        if: always()
        with:
          name: test-report
          path: test-results/
```

#### 测试报告

```markdown
## 测试执行报告

### 执行摘要
| 指标 | 数值 |
|------|------|
| 总用例数 | 150 |
| 通过 | 148 (98.7%) |
| 失败 | 2 (1.3%) |
| 跳过 | 0 |
| 执行时间 | 12m 34s |

### 失败用例
| 用例 | 错误信息 | 严重性 |
|------|---------|-------|
| login_invalid_email | Expected 400, got 500 | P0 |
| create_product_no_stock | Assertion failed | P1 |

### 覆盖率
| 类型 | 覆盖率 | 目标 |
|------|-------|------|
| 行覆盖率 | 85% | ≥80% |
| 分支覆盖率 | 78% | ≥70% |
| 函数覆盖率 | 90% | ≥85% |
```

---

## 🔧 使用示例

### 示例 1: 设计测试框架

**输入**: "帮我们设计自动化测试框架"

**输出**:
```markdown
## 自动化测试框架设计

### 技术栈
- **E2E**: Playwright + TypeScript
- **API**: Jest + Supertest
- **报告**: Allure

### 目录结构
tests/
├── e2e/
│   ├── pages/      # Page Objects
│   └── specs/      # 测试用例
├── integration/
│   └── api/        # API 测试
└── utils/          # 工具函数

### CI 集成
- GitHub Actions
- 每次 PR 自动执行
- 失败阻止合并
```

### 示例 2: 编写 E2E 测试

**输入**: "写一个登录流程的 E2E 测试"

**输出**:
```typescript
test('should complete login flow', async ({ page }) => {
  const loginPage = new LoginPage(page);
  
  await loginPage.login('user@example.com', 'password123');
  
  await expect(page).toHaveURL('/dashboard');
  await expect(page.locator('[data-testid=user-name]'))
    .toHaveText('John Doe');
});
```

---

## 📋 输出规范

1. **可维护**: Page Object 模式，代码复用
2. **稳定**: 自动等待，避免硬编码延迟
3. **可追溯**: 测试与需求/AC 对应
4. **可报告**: 清晰的测试报告

---

## ⚠️ 注意事项

- ⛔ 避免测试间依赖 (每个测试独立)
- ⛔ 避免硬编码延迟 (使用自动等待)
- ⛔ 测试数据要清理
- ✅ 测试也要 Code Review

---

## 🔗 相关技能

- `performance-testing` - 性能测试
- `security-testing` - 安全测试
- `test-data-management` - 测试数据管理

---

**最后更新**: 2026-03-26
**维护者**: QAEngineer
