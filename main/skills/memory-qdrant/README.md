# openclaw-memory-chroma

OpenClaw 本地语义记忆插件，基于 **Python ChromaDB** + **Node.js 桥接** 实现持久化向量存储。

## 架构

```
┌─────────────┐     stdin/stdout      ┌──────────────────┐
│  Node.js    │ ◄──────────────────► │  Python ChromaDB │
│  插件桥接   │     JSON-RPC 风格     │  PersistentClient│
└─────────────┘                       └──────────────────┘
       │                                      │
       ▼                                      ▼
┌─────────────┐                       ┌──────────────────┐
│ 内存模式    │                       │  SQLite 文件存储  │
│ (自动降级)  │                       │ (~/.openclaw/    │
└─────────────┘                       │  memory/chroma.db)│
                                      └──────────────────┘
```

## 特性

- 🧠 **本地语义搜索** - Transformers.js 本地生成 embeddings
- 💾 **持久化存储** - ChromaDB SQLite 后端，重启数据不丢失
- 🔄 **自动降级** - ChromaDB 不可用时自动切换到内存模式
- ⚡ **异步桥接** - Node.js 非阻塞调用 Python 进程
- 🎯 **智能召回** - 对话前自动注入相关记忆

## 安装

### 1. 安装 Python ChromaDB

```bash
# Ubuntu/Debian
pip3 install chromadb --break-system-packages

# 或使用虚拟环境（推荐）
python3 -m venv ~/.venvs/chroma
source ~/.venvs/chroma/bin/activate
pip install chromadb
```

### 2. 安装 Node.js 依赖

```bash
cd ~/.openclaw/workspace/main/skills/memory-qdrant
npm install
```

### 3. 配置 OpenClaw

在 `~/.openclaw/openclaw.json` 中启用插件：

```json
{
  "plugins": {
    "entries": {
      "memory-qdrant": {
        "enabled": true,
        "config": {
          "persistPath": "~/.openclaw/memory/chroma.db",
          "autoCapture": false,
          "autoRecall": true,
          "maxMemorySize": 999999
        }
      }
    }
  }
}
```

## 配置选项

| 选项 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `persistPath` | string | `~/.openclaw/memory/chroma.db` | ChromaDB 持久化路径 |
| `autoCapture` | boolean | `false` | 自动捕获对话内容 |
| `autoRecall` | boolean | `true` | 对话前自动注入记忆 |
| `captureMaxChars` | number | `500` | 单条记忆最大字符数 |
| `maxMemorySize` | number | `1000` | 内存模式最大记忆数 |

## 使用

### AI 工具

插件提供三个工具供智能体使用：

**memory_store** - 保存记忆：
```javascript
memory_store({
  text: "用户喜欢用 Opus 处理复杂任务",
  category: "preference",
  importance: 0.8
})
// 返回：{ success: true, id: "xxx", mode: "chromadb" }
```

**memory_search** - 搜索记忆：
```javascript
memory_search({
  query: "工作流程",
  limit: 5
})
// 返回：{ success: true, count: 3, memories: [...], mode: "chromadb" }
```

**memory_forget** - 删除记忆：
```javascript
memory_forget({
  memoryId: "uuid-here"
})
// 或
memory_forget({
  query: "要删除的内容"
})
```

### 命令行

```bash
# 保存记忆
openclaw remember "吴飞喜欢喝美式咖啡"

# 搜索记忆
openclaw recall "咖啡偏好"

# 查看统计
openclaw memory-qdrant stats

# 搜索（JSON 输出）
openclaw memory-qdrant search "工作流程"
```

## 降级机制

插件会自动检测 ChromaDB 可用性：

1. **ChromaDB 可用** → 使用持久化存储
2. **Python 进程启动失败** → 自动降级到内存模式
3. **运行时错误** → 自动切换到内存模式
4. **重启后** → 自动尝试重新连接 ChromaDB

内存模式特点：
- ✅ 无需外部依赖
- ✅ 零配置
- ⚠️ 重启后数据清空

## 技术细节

### 通信协议

Node.js 与 Python 通过 stdin/stdout 进行 JSON-RPC 风格通信：

```json
// 请求
{"id": 1, "action": "store", "params": {"id": "xxx", "text": "...", "vector": [...]}}

// 响应
{"id": 1, "success": true, "id": "xxx"}
```

### 支持的动作

| Action | 参数 | 返回 |
|--------|------|------|
| `health` | - | `{ healthy: boolean, count: number }` |
| `store` | `id, text, vector, category, importance` | `{ success: boolean, id: string }` |
| `search` | `vector, limit, min_score` | `{ success: boolean, results: [...], count: number }` |
| `delete` | `id` | `{ success: boolean }` |
| `count` | - | `{ success: boolean, count: number }` |

### 依赖

- **Python**: chromadb >= 1.5.0
- **Node.js**: @xenova/transformers >= 2.17.0
- **系统**: Python 3.10+, Node.js 18+

## 故障排除

### Python 进程启动失败

```bash
# 检查 Python 版本
python3 --version  # 需要 >= 3.10

# 检查 ChromaDB 安装
python3 -c "import chromadb; print(chromadb.__version__)"

# 手动测试脚本
echo '{"action":"health"}' | python3 chroma_server.py
```

### 内存占用过高

- 调整 `maxMemorySize` 限制内存模式大小
- 定期清理旧记忆：`memory_forget({ query: "..." })`

### 搜索不准确

- 检查 embedding 模型是否正确加载
- 调整 `SIMILARITY_THRESHOLDS` 阈值
- 确保文本经过 `sanitizeInput` 清理

## 隐私与安全

- ✅ 所有数据本地存储
- ✅ 无需外部 API
- ✅ 持久化文件可备份
- ⚠️ `autoCapture` 可能记录敏感信息（默认关闭）

## 许可证

MIT
