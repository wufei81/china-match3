# ChatBI 临时表隔离测试方案

**版本:** 1.0 **日期:** 2026-03-20 **测试负责人:** QA Engineer **测试类型:** 功能测试、性能测试、安全测试、回归测试

---

## 1. 测试目标

验证 ChatBI 临时表隔离机制的正确性、性能、安全性和稳定性，确保：

- 多用户/多会话临时表完全隔离，无数据泄露
- 临时表创建、使用、清理功能正常
- 高并发场景下性能满足业务需求
- 无 SQL 注入、权限绕过等安全风险
- 系统升级后功能正常回归

---

## 2. 测试范围

### 2.1 测试对象

- 临时表创建接口
- 临时表读写操作
- 临时表隔离机制（会话级/用户级）
- 临时表自动清理机制
- 临时表元数据管理

### 2.2 不测试范围

- 底层数据库引擎内部实现
- 非临时表相关的业务功能

---

## 3. 测试环境

| 环境项     | 配置要求                               |
| ---------- | -------------------------------------- |
| 数据库     | PostgreSQL 14+ / MySQL 8+ (生产同版本) |
| 应用服务器 | 与生产配置一致                         |
| 测试数据   | 脱敏生产数据或等效模拟数据             |
| 并发工具   | JMeter / k6 / locust                   |
| 安全工具   | SQLMap / Burp Suite                    |

---

## 4. 功能测试用例

### 4.1 临时表创建 (P0)

| 用例 ID | 用例名称                 | 前置条件         | 测试步骤                                                | 预期结果                                                     | 优先级 |
| ------- | ------------------------ | ---------------- | ------------------------------------------------------- | ------------------------------------------------------------ | ------ |
| FT-001  | 单用户创建临时表         | 用户已登录       | 1. 调用创建临时表接口<br>2. 传入表名、字段定义          | 1. 返回成功<br>2. 临时表创建成功<br>3. 返回表 ID/名称        | P0     |
| FT-002  | 多用户创建同名临时表     | 用户 A、B 已登录 | 1. 用户 A 创建 temp_table<br>2. 用户 B 创建 temp_table  | 1. 两个表独立存在<br>2. 物理隔离（不同 schema 或带会话前缀） | P0     |
| FT-003  | 同一用户多会话创建临时表 | 用户登录两个会话 | 1. 会话 1 创建 temp_table<br>2. 会话 2 创建 temp_table  | 1. 两个表隔离<br>2. 会话间互不可见                           | P0     |
| FT-004  | 临时表命名冲突处理       | 已存在同名临时表 | 1. 创建已存在的临时表名                                 | 1. 返回明确错误<br>2. 或自动重命名                           | P1     |
| FT-005  | 临时表字段类型支持       | 用户已登录       | 1. 创建包含各种数据类型的临时表                         | 1. 支持 INT/VARCHAR/DATE/JSON 等                             | P1     |
| FT-006  | 临时表创建参数校验       | 用户已登录       | 1. 传入空表名<br>2. 传入非法字段类型<br>3. 传入超长表名 | 1. 返回参数错误<br>2. 不创建表                               | P1     |

### 4.2 临时表读写操作 (P0)

| 用例 ID | 用例名称       | 前置条件     | 测试步骤                                   | 预期结果                         | 优先级 |
| ------- | -------------- | ------------ | ------------------------------------------ | -------------------------------- | ------ |
| FT-010  | 临时表插入数据 | 临时表已创建 | 1. 执行 INSERT 操作                        | 1. 插入成功<br>2. 数据可查询     | P0     |
| FT-011  | 临时表查询数据 | 临时表有数据 | 1. 执行 SELECT 操作                        | 1. 返回正确数据<br>2. 与插入一致 | P0     |
| FT-012  | 临时表更新数据 | 临时表有数据 | 1. 执行 UPDATE 操作                        | 1. 更新成功<br>2. 查询验证更新   | P0     |
| FT-013  | 临时表删除数据 | 临时表有数据 | 1. 执行 DELETE 操作                        | 1. 删除成功<br>2. 查询验证删除   | P0     |
| FT-014  | 临时表批量操作 | 临时表已创建 | 1. 批量 INSERT 1000 条数据                 | 1. 全部成功<br>2. 性能可接受     | P1     |
| FT-015  | 临时表事务支持 | 临时表已创建 | 1. 开启事务<br>2. 执行操作<br>3. 提交/回滚 | 1. 事务正常<br>2. 回滚生效       | P1     |

### 4.3 临时表隔离验证 (P0 - 核心)

| 用例 ID | 用例名称         | 前置条件                   | 测试步骤                                                | 预期结果                                              | 优先级 |
| ------- | ---------------- | -------------------------- | ------------------------------------------------------- | ----------------------------------------------------- | ------ |
| FT-020  | 用户间临时表隔离 | 用户 A、B 各有临时表       | 1. 用户 A 查询自己的表<br>2. 用户 A 尝试查询用户 B 的表 | 1. 步骤 1 成功<br>2. 步骤 2 失败（表不存在/权限拒绝） | P0     |
| FT-021  | 会话间临时表隔离 | 同一用户两个会话           | 1. 会话 1 创建并插入数据<br>2. 会话 2 尝试查询          | 1. 会话 2 查不到会话 1 的表或数据                     | P0     |
| FT-022  | 临时表元数据隔离 | 多用户创建临时表           | 1. 查询系统元数据表<br>2. 检查临时表可见性              | 1. 用户只能看到自己的临时表元数据                     | P0     |
| FT-023  | 临时表索引隔离   | 用户 A、B 各有带索引临时表 | 1. 用户 A 使用索引查询<br>2. 验证不影响用户 B           | 1. 索引正常工作<br>2. 无跨用户影响                    | P2     |
| FT-024  | 临时表约束隔离   | 多用户临时表有约束         | 1. 违反约束插入数据                                     | 1. 只影响当前用户表<br>2. 其他用户不受影响            | P1     |

### 4.4 临时表清理机制 (P0)

| 用例 ID | 用例名称         | 前置条件     | 测试步骤                                       | 预期结果                              | 优先级 |
| ------- | ---------------- | ------------ | ---------------------------------------------- | ------------------------------------- | ------ |
| FT-030  | 会话结束自动清理 | 临时表已创建 | 1. 关闭数据库会话/连接                         | 1. 临时表自动删除<br>2. 元数据清理    | P0     |
| FT-031  | 用户登出清理     | 临时表已创建 | 1. 用户登出<br>2. 检查临时表                   | 1. 临时表被清理                       | P0     |
| FT-032  | 超时自动清理     | 临时表已创建 | 1. 等待超时时间（如 30 分钟）<br>2. 检查临时表 | 1. 超时后临时表自动删除               | P1     |
| FT-033  | 手动删除临时表   | 临时表已创建 | 1. 调用删除接口                                | 1. 删除成功<br>2. 无法再访问          | P1     |
| FT-034  | 异常断开清理     | 临时表已创建 | 1. 强制断开连接（kill）<br>2. 检查临时表       | 1. 临时表被清理（通过数据库会话监控） | P1     |
| FT-035  | 清理失败重试     | 清理任务异常 | 1. 模拟清理失败<br>2. 验证重试机制             | 1. 有重试机制<br>2. 最终清理成功      | P2     |

### 4.5 边界与异常测试 (P1)

| 用例 ID | 用例名称           | 前置条件     | 测试步骤                       | 预期结果                               | 优先级 |
| ------- | ------------------ | ------------ | ------------------------------ | -------------------------------------- | ------ |
| FT-040  | 临时表数量上限     | 用户已登录   | 1. 创建超过上限数量的临时表    | 1. 超出部分拒绝创建<br>2. 返回明确错误 | P1     |
| FT-041  | 临时表大小上限     | 用户已登录   | 1. 插入数据超过大小限制        | 1. 超出部分拒绝<br>2. 返回空间不足错误 | P1     |
| FT-042  | 临时表生命周期边界 | 临时表已创建 | 1. 在生命周期边界点操作        | 1. 行为符合预期                        | P2     |
| FT-043  | 并发创建临时表     | 多用户并发   | 1. 100 用户同时创建临时表      | 1. 全部成功或合理降级<br>2. 无死锁     | P1     |
| FT-044  | 数据库重启后       | 临时表已创建 | 1. 重启数据库<br>2. 检查临时表 | 1. 临时表已清理（符合预期）            | P2     |

---

## 5. 性能测试

### 5.1 性能基准指标

| 指标项         | 基准值        | 可接受值      | 测量方法             |
| -------------- | ------------- | ------------- | -------------------- |
| 临时表创建耗时 | ≤50ms         | ≤100ms        | 单次创建 P95 延迟    |
| 临时表查询耗时 | ≤100ms        | ≤200ms        | 1000 条数据查询 P95  |
| 临时表写入 TPS | ≥1000/s       | ≥500/s        | 持续写入吞吐量       |
| 临时表清理耗时 | ≤100ms        | ≤500ms        | 单次清理 P95         |
| 并发支持能力   | ≥500 并发会话 | ≥200 并发会话 | 稳定运行最大并发     |
| 临时表隔离开销 | ≤10%          | ≤20%          | 相比无隔离的性能损耗 |

### 5.2 性能测试场景

| 场景 ID | 场景名称       | 测试目标          | 并发数 | 持续时间 | 通过标准                 |
| ------- | -------------- | ----------------- | ------ | -------- | ------------------------ |
| PT-001  | 单用户基准性能 | 建立性能基线      | 1      | 5 分钟   | 达到基准指标             |
| PT-002  | 多用户并发创建 | 验证创建性能      | 100    | 10 分钟  | P95≤100ms，无错误        |
| PT-003  | 多用户并发读写 | 验证读写性能      | 200    | 30 分钟  | TPS≥500，延迟≤200ms      |
| PT-004  | 高并发隔离验证 | 验证隔离性能      | 500    | 30 分钟  | 无数据泄露，性能下降≤20% |
| PT-005  | 长时间稳定性   | 验证内存/资源泄漏 | 100    | 24 小时  | 资源稳定，无泄漏         |
| PT-006  | 清理压力测试   | 验证清理机制性能  | 100    | 1 小时   | 清理及时，无堆积         |
| PT-007  | 峰值负载测试   | 验证系统极限      | 1000   | 10 分钟  | 不崩溃，合理降级         |

### 5.3 性能测试脚本 (k6 示例)

```javascript
// temp-table-performance.js
import http from "k6/http";
import { check, sleep } from "k6";
import { Rate, Trend } from "k6/metrics";

// 自定义指标
const createSuccessRate = new Rate("create_success");
const createLatency = new Trend("create_latency_ms");
const isolationFailureRate = new Rate("isolation_failure");

export const options = {
  stages: [
    { duration: "5m", target: 100 }, // 爬坡到 100 并发
    { duration: "20m", target: 100 }, // 稳定负载
    { duration: "5m", target: 500 }, // 压力测试
    { duration: "10m", target: 500 }, // 高并发稳定
    { duration: "5m", target: 0 }, // 冷却
  ],
  thresholds: {
    create_success: ["rate>0.99"],
    create_latency_ms: ["p(95)<100"],
    isolation_failure: ["rate<0.001"],
    http_req_duration: ["p(95)<200"],
  },
};

export default function () {
  const userId = `user_${__VU}`;
  const sessionId = `session_${__VU}_${Date.now()}`;

  // 1. 创建临时表
  const createStart = Date.now();
  const createRes = http.post("http://api/chatbi/temp-table/create", {
    user_id: userId,
    session_id: sessionId,
    table_name: `temp_table_${__VU}`,
    columns: [
      { name: "id", type: "INT" },
      { name: "data", type: "VARCHAR(255)" },
    ],
  });

  const createLatencyMs = Date.now() - createStart;
  createLatency.add(createLatencyMs);

  const createOk = check(createRes, {
    "create status is 200": (r) => r.status === 200,
    "create has table_id": (r) => JSON.parse(r.body).table_id !== undefined,
  });

  createSuccessRate.add(createOk);

  if (!createOk) {
    console.error(`Create failed: ${createRes.body}`);
  }

  // 2. 插入数据
  const insertRes = http.post(`http://api/chatbi/temp-table/${createRes.json().table_id}/insert`, {
    data: Array.from({ length: 100 }, (_, i) => ({
      id: i,
      data: `test_data_${i}`,
    })),
  });

  check(insertRes, {
    "insert status is 200": (r) => r.status === 200,
  });

  // 3. 查询数据（验证隔离）
  const queryRes = http.get(`http://api/chatbi/temp-table/${createRes.json().table_id}/query`);

  check(queryRes, {
    "query status is 200": (r) => r.status === 200,
    "query returns correct data": (r) => {
      const body = JSON.parse(r.body);
      return body.rows && body.rows.length === 100;
    },
  });

  // 4. 尝试验证隔离（可选：需要跨用户测试时）
  // 尝试访问其他用户的表应该失败

  sleep(1);

  // 5. 清理临时表
  http.delete(`http://api/chatbi/temp-table/${createRes.json().table_id}`);
}
```

### 5.4 性能监控指标

| 监控项         | 采集方式   | 告警阈值        |
| -------------- | ---------- | --------------- |
| 数据库连接数   | 数据库监控 | >80% 最大连接数 |
| 临时表数量     | 元数据查询 | >10000 个       |
| 临时表占用空间 | 数据库统计 | >10GB           |
| 清理任务延迟   | 应用日志   | >5 分钟         |
| 内存使用率     | 系统监控   | >85%            |
| CPU 使用率     | 系统监控   | >80%            |

---

## 6. 安全测试

### 6.1 安全测试目标

- 验证临时表隔离机制无法被绕过
- 防止 SQL 注入攻击
- 防止权限提升和越权访问
- 防止数据泄露

### 6.2 安全测试用例

| 用例 ID | 测试类型           | 测试步骤                                            | 预期结果                              | 优先级 |
| ------- | ------------------ | --------------------------------------------------- | ------------------------------------- | ------ |
| ST-001  | SQL 注入 - 表名    | 1. 创建表时传入 `temp_table'; DROP TABLE users; --` | 1. 参数被转义或拒绝<br>2. 无 SQL 注入 | P0     |
| ST-002  | SQL 注入 - 字段名  | 1. 创建表时字段名注入恶意 SQL                       | 1. 参数被转义或拒绝                   | P0     |
| ST-003  | SQL 注入 - 查询    | 1. 查询时注入恶意 SQL                               | 1. 参数化查询，注入无效               | P0     |
| ST-004  | 越权访问 - 直接 ID | 1. 获取他人临时表 ID<br>2. 尝试访问                 | 1. 权限校验失败<br>2. 返回无权限错误  | P0     |
| ST-005  | 越权访问 - 枚举    | 1. 枚举临时表 ID<br>2. 尝试访问他人表               | 1. 无法访问他人表                     | P0     |
| ST-006  | 会话劫持           | 1. 窃取会话令牌<br>2. 尝试访问临时表                | 1. 会话验证机制有效                   | P1     |
| ST-007  | 元数据泄露         | 1. 查询系统表<br>2. 检查是否暴露他人临时表信息      | 1. 元数据隔离                         | P1     |
| ST-008  | 权限提升           | 1. 普通用户尝试管理员操作                           | 1. 权限校验拒绝                       | P0     |
| ST-009  | 批量数据泄露       | 1. 高并发请求他人数据                               | 1. 隔离机制有效                       | P0     |
| ST-010  | 临时文件泄露       | 1. 检查数据库临时文件<br>2. 验证无敏感数据残留      | 1. 临时文件安全清理                   | P2     |
| ST-011  | 日志敏感信息       | 1. 检查应用日志<br>2. 验证无敏感数据                | 1. 日志脱敏                           | P1     |
| ST-012  | 错误信息泄露       | 1. 触发各种错误<br>2. 检查错误信息                  | 1. 不暴露内部结构                     | P1     |

### 6.3 安全测试工具

```bash
# SQLMap 测试（需要授权）
sqlmap -u "http://api/chatbi/temp-table/create" \
  --data="user_id=1&table_name=test" \
  --risk=3 --level=5 \
  --output-dir=./sqlmap_results

# Burp Suite 扫描
# 1. 配置代理指向测试环境
# 2. 遍历所有临时表接口
# 3. 运行主动扫描

# 自定义隔离验证脚本
python3 verify_isolation.py \
  --users 10 \
  --iterations 100 \
  --api-base http://test-api/chatbi
```

### 6.4 安全验证脚本 (Python 示例)

```python
#!/usr/bin/env python3
"""
临时表隔离安全验证脚本
验证多用户场景下无法访问他人临时表
"""

import requests
import concurrent.futures
import random
import string

API_BASE = "http://test-api/chatbi"

def create_user_session():
    """创建用户会话"""
    user_id = f"test_user_{''.join(random.choices(string.ascii_lowercase, k=8))}"
    resp = requests.post(f"{API_BASE}/auth/login", json={"user_id": user_id})
    resp.raise_for_status()
    return user_id, resp.json()["token"]

def create_temp_table(token, table_name):
    """创建临时表"""
    headers = {"Authorization": f"Bearer {token}"}
    resp = requests.post(
        f"{API_BASE}/temp-table/create",
        headers=headers,
        json={
            "table_name": table_name,
            "columns": [{"name": "id", "type": "INT"}]
        }
    )
    resp.raise_for_status()
    return resp.json()["table_id"]

def insert_data(token, table_id, data):
    """插入数据"""
    headers = {"Authorization": f"Bearer {token}"}
    resp = requests.post(
        f"{API_BASE}/temp-table/{table_id}/insert",
        headers=headers,
        json={"data": data}
    )
    return resp.status_code == 200

def query_table(token, table_id):
    """查询表数据"""
    headers = {"Authorization": f"Bearer {token}"}
    resp = requests.get(
        f"{API_BASE}/temp-table/{table_id}/query",
        headers=headers
    )
    return resp.status_code, resp.json()

def attempt_unauthorized_access(victim_token, victim_table_id):
    """尝试未授权访问"""
    # 创建攻击者会话
    attacker_id, attacker_token = create_user_session()

    # 尝试访问受害者临时表
    status, data = query_table(attacker_token, victim_table_id)

    # 应该失败
    if status == 200:
        print(f"❌ 安全漏洞：攻击者可访问受害者表 {victim_table_id}")
        return False
    elif status in [403, 404]:
        print(f"✅ 隔离有效：访问被拒绝 (status={status})")
        return True
    else:
        print(f"⚠️  意外响应：status={status}")
        return None

def main():
    print("=" * 60)
    print("ChatBI 临时表隔离安全验证")
    print("=" * 60)

    users = []
    tables = []

    # 创建多个用户和临时表
    print("\n[1] 创建测试用户和临时表...")
    for i in range(10):
        user_id, token = create_user_session()
        table_id = create_temp_table(token, f"temp_{i}")
        insert_data(token, table_id, [{"id": i, "secret": f"secret_{i}"}])
        users.append((user_id, token))
        tables.append((table_id, token))
        print(f"  ✓ 用户 {i}: table_id={table_id}")

    # 尝试验证隔离
    print("\n[2] 执行隔离验证测试...")
    success_count = 0
    fail_count = 0

    for i, (table_id, victim_token) in enumerate(tables):
        print(f"\n测试表 {i} ({table_id}):")
        result = attempt_unauthorized_access(victim_token, table_id)
        if result is True:
            success_count += 1
        elif result is False:
            fail_count += 1

    # 汇总结果
    print("\n" + "=" * 60)
    print(f"测试结果：{success_count} 通过，{fail_count} 失败")
    if fail_count > 0:
        print("❌ 安全验证未通过！存在数据泄露风险！")
        return 1
    else:
        print("✅ 安全验证通过！隔离机制有效！")
        return 0

if __name__ == "__main__":
    exit(main())
```

---

## 7. 回归测试

### 7.1 回归测试范围

| 触发场景   | 回归范围                    | 执行方式      |
| ---------- | --------------------------- | ------------- |
| 代码变更   | 功能测试全量 + 相关性能测试 | 自动化        |
| 数据库升级 | 功能测试全量 + 性能基准     | 自动化 + 手动 |
| 配置变更   | 功能测试 P0 + 隔离验证      | 自动化        |
| 紧急修复   | 修复相关用例 + P0 核心用例  | 自动化        |
| 定期回归   | 全量测试套件                | 自动化        |

### 7.2 回归测试用例集

#### P0 核心回归用例（必执行）

| 用例 ID | 用例名称             | 自动化 | 执行时间 |
| ------- | -------------------- | ------ | -------- |
| FT-001  | 单用户创建临时表     | ✅     | 1s       |
| FT-002  | 多用户创建同名临时表 | ✅     | 2s       |
| FT-010  | 临时表插入数据       | ✅     | 1s       |
| FT-011  | 临时表查询数据       | ✅     | 1s       |
| FT-020  | 用户间临时表隔离     | ✅     | 3s       |
| FT-021  | 会话间临时表隔离     | ✅     | 3s       |
| FT-030  | 会话结束自动清理     | ✅     | 5s       |
| ST-004  | 越权访问 - 直接 ID   | ✅     | 2s       |

#### P1 重要回归用例（建议执行）

| 用例 ID | 用例名称           | 自动化  | 执行时间 |
| ------- | ------------------ | ------- | -------- |
| FT-004  | 临时表命名冲突处理 | ✅      | 1s       |
| FT-014  | 临时表批量操作     | ✅      | 10s      |
| FT-032  | 超时自动清理       | ⚠️ 手动 | 30min    |
| FT-043  | 并发创建临时表     | ✅      | 30s      |
| ST-001  | SQL 注入 - 表名    | ✅      | 2s       |
| ST-005  | 越权访问 - 枚举    | ✅      | 10s      |

### 7.3 回归测试自动化脚本

```yaml
# regression-test.yml - GitHub Actions 示例
name: ChatBI Temp Table Regression Test

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]
  schedule:
    - cron: "0 2 * * *" # 每天凌晨 2 点

jobs:
  regression-test:
    runs-on: ubuntu-latest

    services:
      postgres:
        image: postgres:14
        env:
          POSTGRES_PASSWORD: test123
        options: >-
          --health-cmd pg_isready --health-interval 10s --health-timeout 5s --health-retries 5
        ports:
          - 5432:5432

    steps:
      - uses: actions/checkout@v3

      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: "18"

      - name: Install dependencies
        run: npm ci

      - name: Run P0 Regression Tests
        run: npm run test:regression:p0
        env:
          DATABASE_URL: postgres://postgres:test123@localhost:5432/test
          API_BASE_URL: http://localhost:3000

      - name: Run Security Tests
        run: npm run test:security

      - name: Run Performance Baseline
        run: npm run test:perf:baseline
        continue-on-error: true # 性能测试失败不阻塞

      - name: Upload Test Results
        uses: actions/upload-artifact@v3
        if: always()
        with:
          name: test-results
          path: test-results/
```

### 7.4 回归测试执行计划

| 测试类型     | 执行频率 | 预计时长 | 负责人    |
| ------------ | -------- | -------- | --------- |
| P0 核心回归  | 每次提交 | 5 分钟   | 自动化    |
| P1 重要回归  | 每日夜间 | 30 分钟  | 自动化    |
| 全量功能回归 | 每周     | 4 小时   | 自动化    |
| 性能基准回归 | 每周     | 2 小时   | 自动化    |
| 安全回归     | 每周     | 1 小时   | 自动化    |
| 手工探索测试 | 每迭代   | 4 小时   | QA 工程师 |

---

## 8. 测试执行计划

### 8.1 测试阶段

| 阶段   | 时间    | 测试类型         | 通过标准          |
| ------ | ------- | ---------------- | ----------------- |
| 阶段 1 | Day 1-2 | 功能测试 (P0)    | P0 用例 100% 通过 |
| 阶段 2 | Day 3   | 功能测试 (P1/P2) | P1 用例 95% 通过  |
| 阶段 3 | Day 4   | 性能测试         | 达到性能基准      |
| 阶段 4 | Day 5   | 安全测试         | 无 P0 安全问题    |
| 阶段 5 | Day 6   | 回归测试         | 全量回归通过      |
| 阶段 6 | Day 7   | 问题修复验证     | 所有缺陷关闭      |

### 8.2 资源需求

| 资源       | 数量         | 用途            |
| ---------- | ------------ | --------------- |
| 测试环境   | 1 套         | 独立测试环境    |
| 数据库实例 | 2 个         | 功能 + 性能隔离 |
| 测试账号   | 100+         | 并发测试        |
| 测试数据   | 脱敏生产数据 | 真实场景模拟    |

### 8.3 风险与应对

| 风险           | 影响 | 概率 | 应对措施             |
| -------------- | ---- | ---- | -------------------- |
| 测试环境不稳定 | 高   | 中   | 准备备用环境         |
| 性能不达标     | 高   | 中   | 提前性能调优         |
| 安全漏洞       | 高   | 低   | 安全优先，修复后上线 |
| 测试时间不足   | 中   | 中   | 优先级排序，P0 优先  |

---

## 9. 验收标准

### 9.1 功能验收

- [ ] P0 测试用例 100% 通过
- [ ] P1 测试用例 ≥95% 通过
- [ ] 所有缺陷已修复或已评估风险

### 9.2 性能验收

- [ ] 临时表创建 P95 延迟 ≤100ms
- [ ] 并发支持 ≥200 会话
- [ ] 无内存泄漏（24 小时稳定性测试）

### 9.3 安全验收

- [ ] 无 P0 级别安全漏洞
- [ ] 隔离机制验证通过
- [ ] SQL 注入测试通过

### 9.4 回归验收

- [ ] 自动化回归测试 100% 通过
- [ ] 性能基线无显著退化（≤10%）

---

## 10. 交付物

| 交付物     | 说明           | 交付时间 |
| ---------- | -------------- | -------- |
| 测试计划   | 本文档         | Day 1    |
| 测试用例   | Excel/TestRail | Day 2    |
| 自动化脚本 | GitHub 仓库    | Day 3    |
| 测试报告   | 包含结果和分析 | Day 7    |
| 缺陷报告   | JIRA/Bug 列表  | 持续     |
| 性能报告   | 性能测试结果   | Day 4    |
| 安全报告   | 安全测试结果   | Day 5    |

---

## 附录

### A. 术语表

- **临时表**: 会话级或用户级的临时数据存储表
- **隔离**: 多用户/多会话间临时表互不可见、互不影响
- **P0/P1/P2**: 缺陷/用例优先级，P0 为最高

### B. 参考文档

- PRD: ChatBI 临时表功能需求
- 设计文档: 临时表隔离技术方案
- API 文档: 临时表接口定义

### C. 联系方式

- QA 负责人: [待填写]
- 开发负责人: [待填写]
- 产品负责人: [待填写]

---

**文档版本历史:**

| 版本 | 日期       | 作者        | 变更说明 |
| ---- | ---------- | ----------- | -------- |
| 1.0  | 2026-03-20 | QA Engineer | 初始版本 |
