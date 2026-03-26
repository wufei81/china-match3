# OpenClaw 向量记忆集成指南

## 在 OpenClaw 中使用向量记忆

### 方法 1: Python 脚本调用

在你的 OpenClaw 技能或脚本中：

```python
import sys
sys.path.insert(0, '/home/wufei/.openclaw/workspace/memory')
from vector_memory import VectorMemory

# 初始化
memory = VectorMemory()

# 添加记忆
memory.add_memory(
    "用户喜欢幽默风格的对话",
    category="preference",
    metadata={"tags": ["对话风格", "偏好"]}
)

# 搜索记忆
results = memory.search_memories("用户偏好", n_results=3)
for r in results:
    print(r['content'])
```

### 方法 2: 命令行工具

```bash
# 添加记忆
python3 /home/wufei/.openclaw/workspace/memory/memory_cli.py add "用户 timezone 是 Asia/Shanghai" -c preference

# 搜索记忆
python3 /home/wufei/.openclaw/workspace/memory/memory_cli.py search "时区"

# 列出所有记忆
python3 /home/wufei/.openclaw/workspace/memory/memory_cli.py list

# 查看统计
python3 /home/wufei/.openclaw/workspace/memory/memory_cli.py stats

# 导出备份
python3 /home/wufei/.openclaw/workspace/memory/memory_cli.py export backup.json
```

### 方法 3: OpenClaw exec 工具

在 OpenClaw 会话中：

```
exec: python3 /home/wufei/.openclaw/workspace/memory/memory_cli.py add "新记忆内容" -c general
```

## 自动化集成建议

### 心跳检查时记录

在 HEARTBEAT.md 中添加：

```markdown
# 向量记忆自动备份

- 时间：每周五 18:00
- 任务：导出记忆备份到 memory/backups/
```

### 会话结束时保存

在会话结束前自动保存重要上下文：

```python
memory.add_memory(
    f"2026-03-09 会话摘要：完成了 ChromaDB 向量记忆系统搭建",
    category="session",
    metadata={"date": "2026-03-09", "type": "summary"}
)
```

## 与现有 Markdown 记忆配合

**向量记忆** (ChromaDB):

- ✅ 语义搜索
- ✅ 模糊匹配
- ✅ 自动关联
- ❌ 不可直接阅读

**Markdown 记忆** (文件):

- ✅ 人类可读
- ✅ 可直接编辑
- ✅ 版本控制友好
- ❌ 无语义搜索

**最佳实践**: 两者结合使用

- 向量记忆：快速检索、上下文关联
- Markdown 文件：长期存储、人工维护

## 示例工作流

```
1. 用户对话 → 提取关键信息
2. 添加到向量记忆 (语义搜索)
3. 同时记录到 memory/YYYY-MM-DD.md (人类可读)
4. 定期导出备份
```

## 性能优化

- **批量添加**: 一次添加多条记忆时，批量操作更高效
- **分类过滤**: 搜索时指定分类可加速
- **定期清理**: 删除过期或不相关的记忆

---

_创建时间：2026-03-09_
