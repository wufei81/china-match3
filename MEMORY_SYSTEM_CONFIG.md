# 记忆系统配置指南

**版本**: 1.0  
**创建日期**: 2026-03-26  
**目标**: 配置智能体记忆共享机制

---

## 🎯 记忆系统架构

### 当前状态
- ✅ memory-qdrant 已安装 (向量记忆)
- ✅ memory-setup 已安装 (记忆管理)
- ⚠️ 记忆未共享 (各智能体独立)

### 目标状态
- ✅ 共享记忆库
- ✅ 经验自动同步
- ✅ 技能自动学习

---

## 🔧 配置步骤

### Step 1: 配置共享记忆目录
```bash
# 创建共享记忆目录
mkdir -p /home/wufei/.openclaw/workspace/shared-memory

# 设置权限
chmod 755 /home/wufei/.openclaw/workspace/shared-memory
```

### Step 2: 配置 Qdrant 向量数据库
```bash
# 检查 Qdrant 是否运行
docker ps | grep qdrant

# 如未运行，启动 Qdrant
docker run -d -p 6333:6333 -p 6334:6334 \
  --name qdrant \
  qdrant/qdrant
```

### Step 3: 配置记忆共享
```json
// ~/.claude/memory-config.json
{
  "provider": "qdrant",
  "qdrant": {
    "url": "http://localhost:6333",
    "collection": "shared-memory"
  },
  "shared": {
    "enabled": true,
    "directory": "/home/wufei/.openclaw/workspace/shared-memory"
  }
}
```

### Step 4: 配置自动同步
```bash
# 添加到 crontab
# 每小时同步记忆
0 * * * * rsync -av /home/wufei/.openclaw/workspace/agents/*/memory/ /home/wufei/.openclaw/workspace/shared-memory/
```

---

## 📊 记忆分类

### 短期记忆
- 会话上下文
- 当前任务状态
- 临时变量

### 长期记忆
- 技能模式
- 项目经验
- 最佳实践

### 共享记忆
- 代码模式
- 测试模式
- 架构模式
- 安全模式

---

## 🚀 使用方式

### 写入记忆
```bash
# 手动写入
/memory write "登录模块最佳实践" --category code-patterns

# 自动写入 (会话结束)
/memory auto-save
```

### 读取记忆
```bash
# 搜索记忆
/memory search "登录模块"

# 列出所有记忆
/memory list
```

### 同步记忆
```bash
# 同步到共享目录
/memory sync

# 从共享目录加载
/memory load
```

---

## 📈 预期效果

| 指标 | 当前 | 配置后 | 提升 |
|------|------|-------|------|
| **记忆共享** | 0% | 100% | +100% |
| **经验复用** | 独立 | 共享 | +100% |
| **学习效率** | 基准 | +50% | +50% |

---

**维护者**: AI Orchestrator  
**最后更新**: 2026-03-26
