# System Design Skill - 系统设计技能

**版本**: 1.0
**创建日期**: 2026-03-26
**触发词**: "系统设计", "设计模式", "DDD", "架构模式", "system design", "design pattern", "domain driven design"

---

## 🎯 技能概述

为开发工程师智能体提供系统设计能力，包括设计模式、领域驱动设计 (DDD)、架构模式、设计原则。帮助从"模块实现"升级为"系统设计"。

---

## 📊 核心功能

### 1. 设计模式应用

**目的**: 使用经过验证的设计模式解决常见问题

#### GoF 设计模式分类

| 类型 | 模式 | 用途 |
|------|------|------|
| **创建型** | Factory, Builder, Singleton, Prototype, Abstract Factory | 对象创建 |
| **结构型** | Adapter, Bridge, Composite, Decorator, Facade, Flyweight, Proxy | 类/对象组合 |
| **行为型** | Chain of Responsibility, Command, Interpreter, Iterator, Mediator, Memento, Observer, State, Strategy, Template Method, Visitor | 对象协作 |

#### 常用模式速查

```markdown
## 设计模式速查

### Singleton (单例)
**场景**: 全局唯一实例 (配置、连接池)

**实现**:
```typescript
class Database {
  private static instance: Database;
  
  private constructor() {}
  
  static getInstance(): Database {
    if (!Database.instance) {
      Database.instance = new Database();
    }
    return Database.instance;
  }
}
```

### Factory (工厂)
**场景**: 对象创建逻辑复杂

**实现**:
```typescript
interface Button { render(): void; }
class WindowsButton implements Button { render() { /* Windows 风格 */ } }
class MacButton implements Button { render() { /* Mac 风格 */ } }

class ButtonFactory {
  static createButton(os: string): Button {
    if (os === 'windows') return new WindowsButton();
    return new MacButton();
  }
}
```

### Observer (观察者)
**场景**: 对象间一对多依赖

**实现**:
```typescript
class Subject {
  private observers: Observer[] = [];
  
  attach(observer: Observer) { this.observers.push(observer); }
  notify() { this.observers.forEach(o => o.update()); }
}
```

### Strategy (策略)
**场景**: 多种算法可互换

**实现**:
```typescript
interface PaymentStrategy {
  pay(amount: number): void;
}

class CreditCardPayment implements PaymentStrategy {
  pay(amount: number) { /* 信用卡支付 */ }
}

class PayPalPayment implements PaymentStrategy {
  pay(amount: number) { /* PayPal 支付 */ }
}

// 使用
class ShoppingCart {
  constructor(private strategy: PaymentStrategy) {}
  checkout(amount: number) { this.strategy.pay(amount); }
}
```
```

#### 模式选择指南

| 问题 | 推荐模式 |
|------|---------|
| 创建复杂对象 | Builder |
| 需要对象池 | Singleton + Factory |
| 对象依赖通知 | Observer |
| 算法频繁切换 | Strategy |
| 接口不兼容 | Adapter |
| 需要控制访问 | Proxy |
| 复杂对象结构 | Composite |

---

### 2. 领域驱动设计 (DDD)

**目的**: 基于业务领域设计软件结构

#### DDD 核心概念

```
┌─────────────────────────────────────────┐
│          战略设计 (Strategic)           │
│  实体 | 值对象 | 聚合根 | 领域事件 | 限界上下文  │
├─────────────────────────────────────────┤
│          战术设计 (Tactical)            │
│   仓库 | 工厂 | 领域服务 | 应用服务          │
└─────────────────────────────────────────┘
```

#### DDD 分层架构

```markdown
## DDD 分层架构

### 四层架构
```
┌─────────────────────────────────┐
│     用户接口层 (Interfaces)      │  Controller, DTO, View
├─────────────────────────────────┤
│       应用层 (Application)       │  应用服务，编排业务流程
├─────────────────────────────────┤
│       领域层 (Domain)           │  实体、值对象、聚合根、领域服务
├─────────────────────────────────┤
│     基础设施层 (Infrastructure)  │  数据库、消息队列、外部服务
└─────────────────────────────────┘
```

### 各层职责
| 层级 | 职责 | 依赖方向 |
|------|------|---------|
| 用户接口 | 处理用户请求 | → 应用层 |
| 应用层 | 业务流程编排 | → 领域层 |
| 领域层 | 核心业务逻辑 | 无依赖 |
| 基础设施 | 技术实现 | → 被依赖 |
```

#### 领域建模示例

```typescript
// 实体 (Entity) - 有唯一标识
class Order {
  constructor(
    public id: OrderId,
    public customerId: CustomerId,
    private items: OrderItem[],
    public status: OrderStatus,
    private createdAt: Date
  ) {}
  
  // 业务行为
  addItem(product: Product, quantity: number) {
    // 业务规则验证
    if (this.status !== OrderStatus.DRAFT) {
      throw new Error('Cannot modify completed order');
    }
    this.items.push(new OrderItem(product, quantity));
  }
  
  // 领域事件
  getDomainEvents(): DomainEvent[] {
    return this.domainEvents;
  }
}

// 值对象 (Value Object) - 无标识，不可变
class Money {
  constructor(
    public amount: number,
    public currency: string
  ) {
    Object.freeze(this); // 不可变
  }
  
  add(other: Money): Money {
    if (this.currency !== other.currency) {
      throw new Error('Currency mismatch');
    }
    return new Money(this.amount + other.amount, this.currency);
  }
}

// 聚合根 (Aggregate Root)
class OrderAggregate {
  constructor(
    public order: Order,
    private payments: Payment[],
    private shipments: Shipment[]
  ) {}
  
  // 保证一致性边界
  completePayment(paymentId: PaymentId) {
    const payment = this.payments.find(p => p.id === paymentId);
    payment.markAsCompleted();
    this.order.status = OrderStatus.PAID;
  }
}

// 仓库接口 (Repository Interface)
interface OrderRepository {
  findById(id: OrderId): Promise<OrderAggregate | null>;
  save(aggregate: OrderAggregate): Promise<void>;
}
```

---

### 3. 架构模式

**目的**: 选择合适的架构模式组织代码

#### 常见架构模式

| 模式 | 描述 | 适用场景 |
|------|------|---------|
| **分层架构** | 按职责分层 | 传统企业应用 |
| **整洁架构** | 依赖向内 | 复杂业务系统 |
| **六边形架构** | 端口适配器 | 多外部系统 |
| **CQRS** | 读写分离 | 高并发读 |
| **事件溯源** | 状态=事件累加 | 审计要求高 |
| **微内核** | 核心 + 插件 | 可扩展系统 |

#### 整洁架构示例

```markdown
## 整洁架构

### 架构结构
```
        ┌─────────────────┐
        │   Frameworks    │  React, Spring, Express
        ├─────────────────┤
        │   Interface     │  Controllers, Views
        ├─────────────────┤
        │   Application   │  Use Cases, Services
        ├─────────────────┤
        │     Domain      │  Entities, Business Rules
        └─────────────────┘
           依赖方向 ↑
```

### 代码组织
```
src/
├── domain/           # 领域层 (无依赖)
│   ├── entities/
│   ├── value-objects/
│   ├── repositories/
│   └── services/
├── application/      # 应用层 (依赖领域)
│   ├── use-cases/
│   ├── dtos/
│   └── interfaces/
├── interface/        # 接口层 (依赖应用)
│   ├── controllers/
│   ├── views/
│   └── middleware/
└── infrastructure/   # 基础设施 (实现领域接口)
    ├── database/
    ├── external/
    └── config/
```
```

---

### 4. 设计原则

**目的**: 遵循设计原则，提高代码质量

#### SOLID 原则

| 原则 | 描述 | 示例 |
|------|------|------|
| **SRP** 单一职责 | 一个类只做一件事 | 分离业务逻辑和数据访问 |
| **OCP** 开闭原则 | 对扩展开放，对修改关闭 | 使用接口/抽象类 |
| **LSP** 里氏替换 | 子类可替换父类 | 不违反父类行为 |
| **ISP** 接口隔离 | 接口要小而专 | 多个专用接口优于一个大接口 |
| **DIP** 依赖倒置 | 依赖抽象不依赖具体 | 依赖接口，注入实现 |

#### 其他原则

| 原则 | 描述 |
|------|------|
| **DRY** | Don't Repeat Yourself - 避免重复 |
| **KISS** | Keep It Simple, Stupid - 保持简单 |
| **YAGNI** | You Aren't Gonna Need It - 不要过度设计 |
| **LOD** | Law of Demeter - 最少知识原则 |

---

## 🔧 使用示例

### 示例 1: 选择设计模式

**输入**: "设计一个支持多种支付方式的系统"

**输出**:
```markdown
## 设计方案

### 推荐模式：Strategy + Factory

**理由**:
- Strategy: 多种支付算法可互换
- Factory: 根据类型创建支付策略

### 实现
```typescript
// 策略接口
interface PaymentStrategy {
  pay(amount: number): Promise<PaymentResult>;
}

// 具体策略
class CreditCardPayment implements PaymentStrategy {
  async pay(amount: number) { /* 信用卡支付逻辑 */ }
}

class AlipayPayment implements PaymentStrategy {
  async pay(amount: number) { /* 支付宝逻辑 */ }
}

// 工厂
class PaymentFactory {
  static createStrategy(type: string): PaymentStrategy {
    switch(type) {
      case 'credit': return new CreditCardPayment();
      case 'alipay': return new AlipayPayment();
      default: throw new Error('Unknown payment type');
    }
  }
}

// 使用
class OrderService {
  async checkout(orderId: string, type: string) {
    const strategy = PaymentFactory.createStrategy(type);
    await strategy.pay(order.amount);
  }
}
```
```

### 示例 2: DDD 建模

**输入**: "用 DDD 设计电商订单系统"

**输出**:
```markdown
## DDD 设计 - 订单系统

### 限界上下文
- **订单上下文**: Order, OrderItem, OrderStatus
- **支付上下文**: Payment, PaymentMethod
- **物流上下文**: Shipment, TrackingInfo

### 聚合根
**OrderAggregate**:
- Order (聚合根)
- OrderItem[] (实体)
- Money (值对象)
- Address (值对象)

### 领域服务
- OrderPricingService: 计算订单价格
- OrderValidationService: 订单验证

### 仓库接口
- OrderRepository: 订单持久化
- PaymentRepository: 支付记录
```

---

## 📋 输出规范

1. **模式适用**: 选择适合场景的模式
2. **代码示例**: 提供可运行的代码示例
3. **权衡分析**: 说明优缺点和适用场景
4. **可演进**: 设计考虑未来扩展

---

## ⚠️ 注意事项

- ⛔ 不要为了模式而模式 (过度设计)
- ⛔ DDD 不是银弹，简单场景用简单设计
- ⛔ 先理解业务，再选择模式
- ✅ 模式是工具，不是目标

---

## 🔗 相关技能

- `code-quality` - 代码质量
- `security-coding` - 安全编码
- `api-governance` - API 治理 (待创建)

---

**最后更新**: 2026-03-26
**维护者**: DevEngineer
