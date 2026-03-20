# 🧠 向量记忆系统 - ChromaDB

本地轻量级向量数据库记忆系统，支持语义搜索。

## 架构

```
memory/
├── chroma_db/           # ChromaDB 向量数据库 (自动生成)
├── vector_memory.py     # 向量记忆管理模块
├── README.md            # 本文档
└── YYYY-MM-DD.md        # 日常记忆文件
```

## 快速开始

### 1. 添加记忆

```python
from vector_memory import VectorMemory

memory = VectorMemory()

# 添加记忆
memory.add_memory(
    "用户吴飞持有腾讯控股、阿里巴巴、小米集团等港股",
    category="investment",
    metadata={"tags": ["股票", "港股"]}
)
```

### 2. 搜索记忆

```python
# 语义搜索
results = memory.search_memories("投资持仓", n_results=5)
for r in results:
    print(f"{r['content']} (相似度：{1-r['distance']:.2%})")
```

### 3. 分类管理

```python
# 按分类搜索
investment_memories = memory.search_memories(
    "持仓",
    category="investment"
)

# 获取所有记忆
all_memories = memory.get_all_memories()

# 统计信息
stats = memory.get_stats()
print(f"总记忆数：{stats['total_memories']}")
```

## API 参考

### VectorMemory 类

| 方法 | 说明 |
|------|------|
| `add_memory(text, category, metadata)` | 添加记忆 |
| `search_memories(query, n_results, category)` | 搜索记忆 |
| `delete_memory(memory_id)` | 删除记忆 |
| `get_all_memories(category)` | 获取所有记忆 |
| `get_stats()` | 获取统计信息 |
| `export_memories(output_path)` | 导出到 JSON |

### 参数说明

**add_memory:**
- `text` (str): 记忆内容
- `category` (str): 分类标签 (general, investment, preference, schedule, etc.)
- `metadata` (dict): 额外元数据 (可选)

**search_memories:**
- `query` (str): 搜索查询 (支持自然语言)
- `n_results` (int): 返回结果数量 (默认 5)
- `category` (str): 分类过滤 (可选)

## 分类建议

| 分类 | 用途 | 示例 |
|------|------|------|
| `general` | 通用记忆 | 用户基本信息 |
| `investment` | 投资相关 | 持仓、偏好、策略 |
| `preference` | 用户偏好 | 邮件格式、通知方式 |
| `schedule` | 定时任务 | cron 任务、提醒 |
| `work` | 工作相关 | 项目、任务 |
| `personal` | 个人信息 | 联系方式、地址 |

## 语义搜索原理

使用 `all-MiniLM-L6-v2` 模型 (384 维向量) 进行文本嵌入：
- 自动下载首次运行时
- 本地缓存于 `~/.cache/chroma/`
- 支持中文语义理解
- 余弦相似度匹配

## 数据持久化

- **向量数据**: `chroma_db/` 目录
- **自动保存**: 每次添加/删除自动持久化
- **可备份**: 直接复制 `chroma_db/` 目录
- **可导出**: `export_memories("backup.json")`

## 示例脚本

```bash
# 运行演示
python3 vector_memory.py

# 查看统计
python3 -c "from vector_memory import VectorMemory; m=VectorMemory(); print(m.get_stats())"
```

## 注意事项

1. **首次运行** 会下载 embedding 模型 (~80MB)
2. **分类命名** 使用小写英文
3. **搜索语言** 支持中英文混合
4. **距离值** 越小越相似 (0=完全相同，1=完全不同)

---

*最后更新：2026-03-09*
