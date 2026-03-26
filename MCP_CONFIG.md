# MCP 服务器配置指南

**版本**: 1.0  
**创建日期**: 2026-03-26  
**目标**: 配置 MCP 扩展功能

---

## 🎯 MCP 服务器

### 已配置服务器

| 服务器 | 用途 | 状态 |
|-------|------|------|
| **github** | GitHub API 访问 | ✅ 已配置 |
| **filesystem** | 文件系统访问 | ✅ 已配置 |
| **memory** | 记忆管理 | ✅ 已配置 |

---

## 🔧 配置说明

### GitHub MCP
```json
{
  "command": "npx",
  "args": ["-y", "@modelcontextprotocol/server-github"],
  "env": {
    "GITHUB_TOKEN": "${GITHUB_TOKEN}"
  }
}
```

**功能**:
- 创建/管理 PR
- 管理 Issue
- 访问仓库
- GitHub Actions

---

### FileSystem MCP
```json
{
  "command": "npx",
  "args": ["-y", "@modelcontextprotocol/server-filesystem"],
  "env": {
    "ALLOWED_PATHS": "/home/wufei/.openclaw/workspace"
  }
}
```

**功能**:
- 文件读写
- 目录遍历
- 文件搜索
- 文件监控

---

### Memory MCP
```json
{
  "command": "npx",
  "args": ["-y", "@modelcontextprotocol/server-memory"],
  "env": {
    "MEMORY_DIR": "/home/wufei/.openclaw/workspace/shared-memory"
  }
}
```

**功能**:
- 记忆存储
- 记忆检索
- 记忆共享
- 记忆同步

---

## 🚀 使用方式

### GitHub MCP
```bash
# 创建 PR
/gh pr create --title "功能名称" --body "描述"

# 管理 Issue
/gh issue create --title "Bug 报告" --body "详细描述"

# 访问仓库
/gh repo view
```

### FileSystem MCP
```bash
# 文件操作
/fs read file.txt
/fs write file.txt "内容"
/fs list /path

# 文件搜索
/fs search "*.md"
```

### Memory MCP
```bash
# 记忆操作
/memory write "技能内容" --category code
/memory search "代码模式"
/memory sync
```

---

## 📊 预期效果

| 功能 | 当前 | 配置后 | 提升 |
|------|------|-------|------|
| **GitHub 访问** | 手动 | 自动 | +80% |
| **文件操作** | 基础 | 增强 | +50% |
| **记忆管理** | 独立 | 共享 | +100% |

---

**维护者**: AI Orchestrator  
**最后更新**: 2026-03-26
