# 智能体超时配置说明

**更新时间:** 2026-03-21 13:35 **更新人:** MobileAgent

---

## ⚙️ **超时配置**

### **默认超时时间**

- **之前:** 5 分钟 (300 秒)
- **现在:** 10 分钟 (600 秒)

### **特殊配置**

- **dev-engineer:** 15 分钟 (900 秒) - 代码实现需要更多时间
- **qa-engineer:** 20 分钟 (1200 秒) - 完整测试套件编写需要充足时间 ⭐

### **适用场景**

- 数据模型设计 (architect) - 10 分钟
- 测试用例编写 (qa-engineer) - **20 分钟** ⭐
- 代码实现 (dev-engineer) - 15 分钟
- 架构设计 (tech-leader) - 10 分钟
- 文档编写 (technical-writer) - 10 分钟

---

## 📋 **超时调整原因**

**问题分析:**

1. architect 设计数据模型需要：
   - 查看项目结构
   - 分析现有代码
   - 设计多个关联表
   - 编写 Pydantic 模型
   - 创建文档

2. qa-engineer 编写测试需要：
   - 了解项目结构
   - 参考现有测试风格
   - 编写 20+ 个测试用例
   - 覆盖多种场景

**5 分钟不够用，调整为 10 分钟。**

---

## 🎯 **使用建议**

### **何时使用默认超时 (10 分钟)**

- 复杂数据模型设计 (architect)
- 完整测试套件编写 (qa-engineer)
- 架构设计文档 (tech-leader)

### **何时使用 dev-engineer 超时 (15 分钟)**

- 多文件代码实现
- API 端点开发
- 数据库集成
- 功能模块开发

### **何时使用 qa-engineer 超时 (20 分钟)**

- 完整测试套件编写
- 集成测试开发
- 性能测试编写
- 测试覆盖率>80% 要求

### **何时手动调整超时**

- 超复杂任务 → 20-30 分钟
- 简单任务 → 3-5 分钟
- 探索性任务 → 根据情况调整

---

## 📝 **代码示例**

```python
# 默认超时 (10 分钟)
sessions_spawn(
    agentId="architect",
    task="设计复杂的数据模型",
    timeoutSeconds=600  # 10 分钟
)

# dev-engineer 专用超时 (15 分钟)
sessions_spawn(
    agentId="dev-engineer",
    task="完整功能实现",
    timeoutSeconds=900  # 15 分钟
)

# qa-engineer 专用超时 (20 分钟) ⭐
sessions_spawn(
    agentId="qa-engineer",
    task="编写完整测试套件",
    timeoutSeconds=1200  # 20 分钟
)

# 超长任务 (30 分钟)
sessions_spawn(
    agentId="qa-engineer",
    task="集成测试 + 性能测试",
    timeoutSeconds=1800  # 30 分钟
)

# 简单任务 (3-5 分钟)
sessions_spawn(
    agentId="tech-leader",
    task="代码审查",
    timeoutSeconds=300  # 5 分钟
)
```

```

---

## ⚠️ **注意事项**

1. **不要无限延长超时** - 如果 10 分钟不够，考虑拆分任务
2. **监控进度** - 每 2-3 分钟检查一次进度
3. **及时接手** - 如果超时，主动接手完成任务
4. **记录原因** - 在 HEARTBEAT.md 或会话日志中记录超时原因

---

## 📊 **超时统计**

| 智能体 | 任务类型 | 原超时 | 新超时 | 状态 |
|--------|----------|--------|--------|------|
| architect | 数据模型设计 | 5min | 10min | ✅ |
| **qa-engineer** | **完整测试套件** | **5min** | **20min** | ✅ ⭐⭐ |
| **dev-engineer** | **代码实现** | **5min** | **15min** | ✅ ⭐ |
| tech-leader | 代码审查 | 5min | 10min | ✅ |
| project-manager | 进度跟踪 | 5min | 10min | ✅ |

---

**生效时间:** 立即生效
**适用范围:** 所有通过 `sessions_spawn` 创建的子任务
```
