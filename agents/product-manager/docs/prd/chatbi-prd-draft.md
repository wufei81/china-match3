# PRD: ChatBI - AI 驱动的商业智能分析系统

**文档 ID**: PRD-ChatBI-2026-001  
**版本**: v1.0  
**创建日期**: 2026-03-26  
**状态**: Draft  
**保密级别**: 内部公开

---

## 🧠 生成说明

**生成模式**: 自主多步推理 (Autonomous Multi-Step Reasoning)  
**输入**: ChatBI 产品需求（自然语言查询 + 自动可视化 + 智能洞察）

**推理过程摘要**:

| 阶段 | 推理内容 | 置信度 |
|------|----------|--------|
| 1. 问题发现 | 业务人员不会 SQL，数据获取依赖分析师 | 85% |
| 2. 用户分析 | 业务分析师/运营/管理层，日常需要数据报表 | 80% |
| 3. 指标定义 | 响应时间<3s，准确率>95%，NPS>40 | 90% |
| 4. 范围界定 | MVP 聚焦 NL2SQL+ 可视化，砍掉复杂功能 | 75% |
| 5. 约束识别 | 支持多数据源，私有部署，安全合规 | 85% |
| 6. 优先级 | P0: 自然语言查询，P1: 智能洞察 | 80% |

**关键假设**:
- ⚠️ 目标用户 100-500 人企业 — 基于常见 BI 使用场景
- ⚠️ 6 周 MVP — 基于 NL2SQL 技术成熟度
- ⚠️ 私有部署 — 基于数据安全考量

---

## 1. 问题陈述

### 1.1 核心问题
企业业务人员需要数据洞察，但不会 SQL，每次取数都要找分析师，效率低下。

**用户原话**:
> "我就想知道上周销售额，要在钉钉上问数据分析师，等半天才给我回复"

### 1.2 Why Now（紧迫性）

| 因素 | 说明 | 置信度 |
|------|------|--------|
| AI 成熟 | NL2SQL 技术已成熟，准确率>95% | 90% |
| 效率需求 | 业务决策需要实时数据支持 | 85% |
| 成本压力 | 数据分析师人力成本高 | 75% |

**如果不解决会怎样**:
- 业务决策延迟，错失市场机会
- 数据分析师沦为"取数工具人"
- 业务人员满意度低

### 1.3 现有解决方案

| 方案类型 | 具体方案 | 缺点 |
|----------|----------|------|
| 传统 BI | Tableau/PowerBI | 学习成本高，需要培训 |
| 自建 | 内部开发 | 周期长，维护成本高 |
| 人工 | 找数据分析师 | 效率低，响应慢 |
| 维持现状 | Excel 手动统计 | 易出错，时效性差 |

---

## 2. 目标与成功指标

### 2.1 业务目标
- [ ] 3 个月内覆盖 80% 业务人员
- [ ] 日均活跃用户达到 100+
- [ ] 数据分析师取数需求减少 70%

### 2.2 成功指标（KPI）

| 指标类型 | 指标名称 | 当前基线 | 目标值 | 测量方法 | 时间窗口 |
|----------|----------|----------|--------|----------|----------|
| 性能 | 查询响应时间 (P95) | N/A | <3s | APM 监控 | 持续 |
| 质量 | NL2SQL 准确率 | N/A | >95% | 抽样验证 | 每周 |
| 用户满意度 | NPS | N/A | >40 | 季度调研 | 季度 |
| 效率 | 数据分析师取数需求 | 100% | -70% | 工单统计 | 3 个月 |

### 2.3 非目标
- [ ] 不做数据仓库（集成现有数仓）
- [ ] 不做 ETL 工具（使用现有数据）
- [ ] 不做开放平台（v1 不考虑第三方集成）

---

## 3. 用户与市场

### 3.1 目标用户画像

| 属性 | 描述 |
|------|------|
| 用户类型 | 业务分析师/运营人员/管理层 |
| 企业规模 | 100-500 人中小企业 |
| 使用场景 | 日常数据查询、报表生成、经营分析 |
| 核心需求 | 快速、准确、易用 |
| 痛点 | 不会 SQL、等数据慢、报表制作繁琐 |

### 3.2 用户故事

| ID | 用户角色 | 想要... | 以便... | 优先级 |
|----|----------|---------|---------|--------|
| US-001 | 运营人员 | 用自然语言查询销售额 | 快速获取日报数据 | P0 |
| US-002 | 管理层 | 查看经营分析图表 | 辅助决策 | P0 |
| US-003 | 业务分析师 | 自动生成周报 | 减少重复劳动 | P0 |
| US-004 | 运营人员 | 下钻分析数据异常 | 定位问题原因 | P1 |
| US-005 | 管理层 | 智能洞察推荐 | 发现业务机会 | P1 |

### 3.3 竞争格局

| 竞品 | 优势 | 劣势 | 我们的差异化 |
|------|------|------|--------------|
| Tableau | 功能强大，生态好 | 学习成本高，贵 | 自然语言，零学习成本 |
| PowerBI | 微软生态，便宜 | 需要 DAX，复杂 | 对话式，更简单 |
| 帆软 | 本土化好 | 传统 BI，不够智能 | AI 驱动，更智能 |
| 自建 | 定制化 | 周期长，维护难 | 开箱即用 |

---

## 4. 范围定义

### 4.1 In Scope（v1.0 MVP）

| 功能模块 | 功能描述 | 优先级 | 验收标准摘要 |
|----------|----------|--------|--------------|
| 自然语言查询 | 用户输入问题，自动转 SQL 查询 | P0 | 准确率>95%，响应<3s |
| 自动可视化 | 根据查询结果自动推荐图表类型 | P0 | 支持柱状图/折线图/饼图 |
| 数据报告 | 自动生成日报/周报 | P0 | 支持定时发送 |
| 多数据源 | 支持 MySQL/PostgreSQL/ClickHouse | P0 | 一键切换数据源 |
| 权限管理 | 行级/列级数据权限控制 | P0 | 不同角色看到不同数据 |

### 4.2 Out of Scope（本次不做）

| 功能 | 排除原因 | 可能 reconsider 的时间 |
|------|----------|----------------------|
| 数据仓库 | 聚焦查询层，不做存储 | v2.0 |
| ETL 工具 | 使用现有数据管道 | 暂不考虑 |
| 预测分析 | MVP 聚焦描述性分析 | v2.0 |
| 移动端 APP | 先用 Web/H5 | v2.0 |

### 4.3 Future Considerations（v2.0+）
- [ ] 预测分析（销量预测、趋势预测）
- [ ] 异常检测（自动发现数据异常）
- [ ] 移动端 APP
- [ ] 开放平台（第三方集成）

---

## 5. 功能需求详情

### 5.1 功能：自然语言查询

**功能 ID**: FEAT-001

**优先级**: P0

**功能描述**:
用户输入自然语言问题，系统自动转换为 SQL 查询并返回结果。

**用户流程**:
```
用户输入"上周销售额是多少" → 
NL2SQL 引擎解析 → 
生成 SQL 查询 → 
执行查询 → 
返回结果
```

**验收标准**（Gherkin）:
```gherkin
Feature: 自然语言查询

Scenario: 查询销售额
  Given 用户有数据权限
  When 用户输入"上周销售额是多少"
  Then 系统在 3 秒内返回结果
  And 结果准确无误

Scenario: 模糊查询
  Given 用户输入不完整
  When 用户输入"销售额"
  Then 系统提示补充时间范围
  And 提供建议问题

Scenario: 无权限查询
  Given 用户无某表权限
  When 用户查询敏感数据
  Then 系统提示无权限
  And 不暴露表结构
```

**NL2SQL 准确率要求**:
- 简单查询（单表）: >98%
- 中等查询（2-3 表关联）: >95%
- 复杂查询（4+ 表）: >90%

---

## 6. 数据结构草稿

### 6.1 核心表

```sql
-- 查询历史表
CREATE TABLE query_history (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  user_id BIGINT NOT NULL,
  natural_language TEXT NOT NULL,
  generated_sql TEXT,
  execution_time_ms INT,
  result_count INT,
  feedback ENUM('good', 'bad'),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  INDEX idx_user (user_id),
  INDEX idx_created (created_at)
);

-- 数据源配置表
CREATE TABLE data_sources (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(100) NOT NULL,
  type ENUM('mysql', 'postgresql', 'clickhouse'),
  host VARCHAR(200),
  port INT,
  database_name VARCHAR(100),
  encrypted_credentials TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 权限配置表
CREATE TABLE data_permissions (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  role_id BIGINT NOT NULL,
  table_name VARCHAR(100),
  column_policy JSON, -- 列级权限
  row_filter JSON,    -- 行级过滤
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### 6.2 数据表映射

```sql
-- 业务表映射（示例：销售表）
CREATE TABLE sales_fact (
  date DATE,
  product_id BIGINT,
  region_id BIGINT,
  sales_amount DECIMAL(10,2),
  quantity INT,
  -- 更多字段...
);
```

---

## 7. API 契约草稿

### 7.1 查询 API

```yaml
POST /api/v1/query
Content-Type: application/json
Authorization: Bearer {token}

Request:
{
  "question": "上周销售额是多少",
  "data_source_id": 1,
  "limit": 100
}

Response (200 OK):
{
  "query_id": "q_123",
  "sql": "SELECT SUM(sales_amount) FROM sales_fact WHERE date >= '2026-03-18'",
  "data": [
    {"sum": 1234567.89}
  ],
  "execution_time_ms": 250,
  "chart_suggestion": "card"
}

Response (400 Bad Request):
{
  "error": "invalid_question",
  "message": "问题不明确，请补充时间范围",
  "suggestions": ["上周销售额是多少", "上月销售额是多少"]
}

Response (403 Forbidden):
{
  "error": "permission_denied",
  "message": "您无权访问该表"
}
```

### 7.2 可视化 API

```yaml
POST /api/v1/visualize
Content-Type: application/json

Request:
{
  "query_id": "q_123",
  "chart_type": "line",  // line/bar/pie/card/table
  "options": {
    "x_axis": "date",
    "y_axis": "sales_amount"
  }
}

Response (200 OK):
{
  "chart_config": {
    "type": "line",
    "data": {...},
    "options": {...}
  },
  "image_url": "/charts/q_123.png"
}
```

### 7.3 报告 API

```yaml
POST /api/v1/reports
Content-Type: application/json

Request:
{
  "name": "销售日报",
  "queries": ["q_123", "q_124"],
  "schedule": "0 9 * * *",  // 每天 9 点
  "recipients": ["user@company.com"]
}

Response (201 Created):
{
  "report_id": "r_001",
  "next_run": "2026-03-27T09:00:00Z"
}
```

---

## 8. 非功能需求

### 8.1 性能要求

| 指标 | 要求 | 测量条件 |
|------|------|----------|
| 查询响应时间 (P95) | <3s | 简单查询 |
| 查询响应时间 (P95) | <10s | 复杂查询 |
| 并发用户数 | 100 | 同时在线 |
| NL2SQL 准确率 | >95% | 抽样验证 |

### 8.2 安全要求

- [ ] 认证方式：SSO（企业微信/钉钉/OAuth）
- [ ] 数据加密：TLS 1.3 传输加密
- [ ] 权限控制：行级/列级数据权限
- [ ] 审计日志：所有查询操作可追溯
- [ ] 数据脱敏：敏感字段自动脱敏

### 8.3 部署要求

- [ ] 部署方式：私有化部署（Docker/K8s）
- [ ] 资源需求：4 核 8G 起
- [ ] 高可用：支持集群部署
- [ ] 备份恢复：支持数据备份

---

## 9. 时间线与里程碑

### 9.1 项目计划

| 阶段 | 周次 | 交付物 | 负责人 |
|------|------|--------|--------|
| 需求评审 | Week 1 | PRD 定稿 | 产品经理 |
| 技术设计 | Week 2 | 架构文档 | 技术负责人 |
| NL2SQL 开发 | Week 3-4 | 核心引擎 | 后端团队 |
| 前端开发 | Week 3-5 | 用户界面 | 前端团队 |
| 集成测试 | Week 6 | 测试报告 | 测试团队 |
| MVP 发布 | Week 6 | 可运行版本 | 全体 |
| 公测迭代 | Week 7-9 | 优化改进 | 全体 |
| GA 发布 | Week 10 | 正式发布 | 全体 |

### 9.2 WorkPackages

| Agent | Input | Output | Acceptance |
|-------|-------|--------|------------|
| ui-ux-designer | P0 功能列表 | Figma 设计稿 | 设计覆盖所有 P0 功能 |
| architect | PRD+API 草稿 | 架构文档+DDL | 字段级契约明确，支持多数据源 |
| dev-engineer | 架构 + 设计 | 可运行代码+ 单元测试 | E2E 测试通过，准确率>95% |
| qa-engineer | PRD AC | 测试用例+E2E 测试 | AC 覆盖 100%，性能达标 |
| devops-engineer | 架构拓扑 | 部署脚本 + 监控 | 一键部署，监控告警就绪 |

---

## 10. 风险评估

| 风险 ID | 风险描述 | 可能性 | 影响 | 风险等级 | 缓解措施 |
|---------|----------|--------|------|----------|----------|
| R-001 | NL2SQL 准确率不达标 | 中 | 高 | 🟡 | 前期技术验证，准备规则兜底 |
| R-002 | 复杂查询性能差 | 中 | 中 | 🟡 | 查询优化，缓存热点查询 |
| R-003 | 数据安全问题 | 低 | 高 | 🟡 | 行级权限，审计日志 |
| R-004 | 用户接受度低 | 低 | 中 | 🟢 | 早期用户参与，快速迭代 |

---

## ⚠️ 需要确认的事项

| 编号 | 假设内容 | 推理依据 | 建议确认方式 |
|------|----------|----------|--------------|
| A1 | 目标用户 100-500 人企业 | 基于常见 BI 使用场景 | 与销售团队确认 |
| A2 | 6 周 MVP 周期 | 基于 NL2SQL 技术成熟度 | 与研发团队确认 |
| A3 | 私有部署为主 | 基于数据安全考量 | 与客户确认 |
| A4 | 准确率>95% 可行 | 基于业界 NL2SQL 水平 | 技术验证 |

---

## ❓ 开放问题

| 问题 ID | 问题描述 | 影响范围 | 建议负责人 |
|---------|----------|----------|------------|
| Q-001 | 支持哪些数据源（除 MySQL/PG/CH 外）？ | 技术选型 | 技术负责人 |
| Q-002 | 是否需要支持实时数据？ | 架构设计 | 技术负责人 |
| Q-003 | 预算范围是多少？ | 技术选型 | 财务/发起人 |
| Q-004 | 是否需要与现有 BI 集成？ | 功能范围 | 产品经理 |

---

**文档状态**: Draft | **最后更新**: 2026-03-26 | **维护者**: product-manager

---

## 📋 下一步建议

1. ✅ 确认上述假设（A1-A4）
2. ✅ 回答开放问题（Q-001~Q-004）
3. ✅ 与干系人评审 PRD
4. ✅ 进入技术设计阶段
5. ✅ 调用 WorkPackages 生成脚本分解任务

