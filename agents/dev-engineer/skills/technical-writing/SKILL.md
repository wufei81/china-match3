# Technical Writing Skill - 技术文档技能

**版本**: 1.0
**创建日期**: 2026-03-26
**触发词**: "技术文档", "RFC", "设计文档", "API 文档", "technical writing", "RFC", "documentation", "API docs"

---

## 🎯 技能概述

为开发工程师智能体提供技术文档写作能力，包括 RFC 撰写、设计文档、API 文档、技术博客。帮助从"代码工人"升级为"知识传播者"。

---

## 📊 核心功能

### 1. RFC (Request for Comments) 撰写

**目的**: 规范技术方案讨论流程，收集反馈达成共识

#### RFC 结构

```markdown
# RFC-XXX: [标题]

## 状态
[草稿 | 评审中 | 已接受 | 已拒绝 | 已废弃]

## 摘要
[200 字以内概述 RFC 内容]

## 动机
[为什么要做这个改动？解决什么问题？]

## 目标
- [ ] 目标 1
- [ ] 目标 2
- [ ] 目标 3

## 非目标
[明确说明不包含什么]

## 方案详述

### 方案设计
[详细技术方案，包括架构图、流程图、数据模型等]

### 技术选型
| 选项 | 优点 | 缺点 | 选择理由 |
|------|------|------|---------|
| 方案 A | | | |
| 方案 B | | | ✅ 推荐 |

### 接口设计
[API 设计、数据结构]

### 兼容性
[向后兼容性、迁移策略]

## 实施计划
| 阶段 | 内容 | 时间 | 负责人 |
|------|------|------|-------|
| Phase 1 | | | |
| Phase 2 | | | |

## 风险与缓解
| 风险 | 影响 | 概率 | 缓解措施 |
|------|------|------|---------|
| [风险 1] | | | |
| [风险 2] | | | |

## 替代方案
[考虑过的其他方案及为什么不选]

## 相关问题
[链接到相关的 issue、讨论]

## 参考
[相关文档、论文、博客]
```

#### RFC 评审流程

```
1. 起草 (作者)
   ↓
2. 预审 (核心成员)
   ↓
3. 公开评审 (全员，7 天)
   ↓
4. 修改完善
   ↓
5. 决策 (技术委员会)
   ↓
6. 实施/归档
```

---

### 2. 设计文档撰写

**目的**: 记录设计决策，便于后续开发和维护

#### 设计文档模板

```markdown
# [功能名称] 设计文档

## 概述
### 背景
[业务背景、问题陈述]

### 范围
**In Scope**:
- [包含的功能]

**Out of Scope**:
- [不包含的功能]

## 需求
### 功能需求
| ID | 需求 | 优先级 |
|----|------|-------|
| FR-1 | | P0 |
| FR-2 | | P0 |

### 非功能需求
| 类型 | 要求 |
|------|------|
| 性能 | P99 < 500ms |
| 可用性 | 99.9% |
| 安全 | 符合安全规范 |

## 架构设计
### 系统上下文
```mermaid
[系统上下文图]
```

### 核心流程
```mermaid
[流程图/时序图]
```

### 数据模型
```mermaid
[ER 图]
```

## 详细设计
### 模块划分
| 模块 | 职责 | 接口 |
|------|------|------|
| [模块 A] | | |
| [模块 B] | | |

### API 设计
```yaml
# OpenAPI 规范
paths:
  /api/resource:
    post:
      summary: Create resource
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                field1:
                  type: string
```

### 数据库设计
```sql
CREATE TABLE table_name (
  id BIGINT PRIMARY KEY,
  field1 VARCHAR(255),
  created_at TIMESTAMP
);
```

## 实施计划
### 任务分解
| 任务 | 工时 | 依赖 | 负责人 |
|------|------|------|-------|
| [任务 1] | 3d | - | |
| [任务 2] | 2d | 任务 1 | |

### 里程碑
| 时间 | 里程碑 | 交付物 |
|------|-------|-------|
| [日期] | [里程碑] | |

## 测试策略
### 测试类型
- [ ] 单元测试
- [ ] 集成测试
- [ ] E2E 测试
- [ ] 性能测试

### 测试用例
| 用例 | 输入 | 预期输出 |
|------|------|---------|
| | | |

## 监控与告警
### 核心指标
| 指标 | 告警阈值 |
|------|---------|
| | |

### 日志
[关键日志点]

## 运维
### 部署
[部署步骤、回滚方案]

### 配置
[配置项说明]

## 附录
### 术语表
| 术语 | 定义 |
|------|------|
| | |

### 参考
[相关链接]
```

---

### 3. API 文档撰写

**目的**: 清晰描述 API 用法，降低集成成本

#### API 文档标准

```markdown
# API 文档 - [API 名称]

## 概述
[API 用途、适用场景]

## 认证
[认证方式、Token 获取]

## 基础 URL
```
Production: https://api.example.com/v1
Staging: https://staging-api.example.com/v1
```

## 通用约定
### 请求格式
```json
{
  "field1": "value",
  "field2": 123
}
```

### 响应格式
```json
{
  "data": {},
  "error": null,
  "meta": {
    "request_id": "xxx",
    "timestamp": "2026-03-26T13:30:00Z"
  }
}
```

### 错误码
| 错误码 | 含义 | 处理建议 |
|-------|------|---------|
| 400 | 请求参数错误 | 检查参数 |
| 401 | 未认证 | 检查 Token |
| 403 | 无权限 | 检查权限 |
| 404 | 资源不存在 | 检查资源 ID |
| 500 | 服务器错误 | 联系支持 |

## 接口详情

### [接口名称]
[接口描述]

**请求**
```http
POST /api/resource
Content-Type: application/json
Authorization: Bearer {token}

{
  "field1": "value"
}
```

**响应**
```json
{
  "data": {
    "id": "123",
    "field1": "value"
  }
}
```

**错误响应**
```json
{
  "error": {
    "code": "INVALID_PARAM",
    "message": "field1 is required",
    "details": []
  }
}
```

**代码示例**
```javascript
// JavaScript
const response = await fetch('/api/resource', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Authorization': `Bearer ${token}`
  },
  body: JSON.stringify({ field1: 'value' })
});
const data = await response.json();
```

```python
# Python
import requests

response = requests.post(
    'https://api.example.com/api/resource',
    headers={'Authorization': f'Bearer {token}'},
    json={'field1': 'value'}
)
data = response.json()
```

**限流**
- 速率限制：100 次/分钟
- 配额：10000 次/天
```

---

### 4. 技术博客撰写

**目的**: 分享技术经验，建立个人/团队技术品牌

#### 技术博客结构

```markdown
# [吸引人的标题]

## 引言
[背景介绍、问题引出、文章价值]

## 问题描述
[具体问题、痛点、影响]

## 解决方案
[方案介绍、为什么选择这个方案]

## 实施过程
### 步骤 1: [步骤名称]
[详细说明、代码示例]

### 步骤 2: [步骤名称]
[详细说明、代码示例]

## 结果与收益
[量化结果、经验总结]

## 踩坑记录
[遇到的问题、如何解决的]

## 最佳实践
[总结的建议、注意事项]

## 参考资源
[相关链接、进一步阅读]

## 关于作者
[简介、联系方式]
```

#### 写作技巧

| 技巧 | 说明 |
|------|------|
| **标题吸引人** | 具体、有数字、有收益 |
| **结构清晰** | 小标题、列表、代码块 |
| **代码示例** | 完整、可运行、有注释 |
| **图表辅助** | 架构图、流程图、对比表 |
| **量化结果** | 性能提升 X%、成本降低 Y% |

---

## 🔧 使用示例

### 示例 1: 撰写 RFC

**输入**: "帮我们写一个引入 GraphQL 的 RFC"

**输出**:
```markdown
# RFC-001: 引入 GraphQL API

## 摘要
建议在项目中引入 GraphQL 作为 REST API 的补充，解决过度获取和获取不足问题。

## 动机
- 当前 REST API 存在过度获取问题
- 移动端需要多次请求
- 前端需要灵活查询

## 目标
- [ ] 减少 API 请求次数
- [ ] 减少数据传输量
- [ ] 提高前端开发效率

## 方案
### 技术选型
| 方案 | 优点 | 缺点 |
|------|------|------|
| Apollo | 生态完善 | 较重 |
| Relay | Facebook 背书 | 学习曲线陡 |
| 原生 GraphQL | 轻量 | 需要自建 |

推荐：Apollo (生态完善，社区活跃)

### Schema 设计
```graphql
type Query {
  user(id: ID!): User
  posts(authorId: ID, limit: Int): [Post]
}
```

## 实施计划
- Phase 1: 试点项目 (2 周)
- Phase 2: 核心业务 (4 周)
- Phase 3: 全面推广 (持续)
```

### 示例 2: API 文档

**输入**: "写一个用户登录 API 文档"

**输出**:
```markdown
# 用户登录 API

## 概述
用户登录接口，支持账号密码登录。

## 请求
```http
POST /api/v1/auth/login
Content-Type: application/json

{
  "username": "user@example.com",
  "password": "password123"
}
```

## 响应
**成功 (200)**
```json
{
  "data": {
    "token": "eyJhbGciOiJIUzI1NiIs...",
    "expires_in": 3600,
    "user": {
      "id": "123",
      "username": "user@example.com"
    }
  }
}
```

**失败 (401)**
```json
{
  "error": {
    "code": "INVALID_CREDENTIALS",
    "message": "用户名或密码错误"
  }
}
```
```

---

## 📋 输出规范

1. **结构清晰**: 使用标准模板
2. **示例完整**: 提供可运行的代码示例
3. **版本管理**: 文档版本与代码版本对应
4. **定期更新**: 文档与实际保持一致

---

## ⚠️ 注意事项

- ⛔ 文档不是写完就结束，要持续维护
- ⛔ 避免过度技术术语，考虑读者背景
- ⛔ 代码示例要测试，确保可运行
- ✅ 文档也是代码，需要 Code Review

---

## 🔗 相关技能

- `code-quality` - 代码质量
- `system-design` - 系统设计
- `api-governance` - API 治理 (待创建)

---

**最后更新**: 2026-03-26
**维护者**: DevEngineer
