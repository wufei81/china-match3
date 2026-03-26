# 🚀 Session Auto-Initialization

> **目标**: 每次会话启动时自动读取规则 + 自动初始化项目

---

## 🎯 实现方式

### 方式 1: BOOTSTRAP.md (已实现 ✅)

**位置**: `/home/wufei/.openclaw/workspace/BOOTSTRAP.md`

**机制**: OpenClaw 原生支持 - 每次新会话启动时**自动读取**

**内容**:

- 核心规则摘要
- 6 阶段流程
- 5 个质量门禁
- 必备模板清单
- 智能体职责

**优点**:

- ✅ OpenClaw 原生机制
- ✅ 无需额外配置
- ✅ 每次会话必读

---

### 方式 2: memory/CORE_RULES.md (已实现 ✅)

**位置**: `/home/wufei/.openclaw/workspace/memory/CORE_RULES.md`

**机制**: 所有智能体 AGENTS.md 第 2 节规定"每次会话开始必读"

**内容**:

- 三条红线 + 安全基线
- 6 阶段开发流程
- 5 个质量门禁
- 模板文件清单
- 违规处理

**优点**:

- ✅ 持久化记忆
- ✅ 全局共享
- ✅ 语义检索支持

---

### 方式 3: 会话启动钩子 (推荐增强)

**创建**: `~/.openclaw/session-init.sh`

```bash
#!/bin/bash

# Session Initialization Hook
# 每次新会话启动时自动执行

# 1. 读取核心规则
cat /home/wufei/.openclaw/workspace/memory/CORE_RULES.md

# 2. 检测项目是否需要初始化
PROJECT_DIR=$(pwd)
if [ ! -f "$PROJECT_DIR/PROJECT_CONFIG.md" ]; then
    echo "⚠️  Project not initialized. Auto-initializing..."
    /home/wufei/.openclaw/workspace/auto-init-if-needed.sh
fi

# 3. 显示快速参考
echo ""
echo "📋 Quick Reference:"
echo "- Phase 0: Requirements Clarification (5 questions)"
echo "- Phase 1-6: Development Process"
echo "- Gates 1-5: Quality Checkpoints"
echo ""
```

**配置**: 在 Gateway 配置中引用

---

### 方式 4: Agent 配置级别自动读取

**修改**: 每个智能体的 AGENTS.md 第 1 节

```markdown
## 1. Core Identity

### 🧠 Automatic Reading (Session Start)

**Every session automatically reads**:

1. `/home/wufei/.openclaw/workspace/BOOTSTRAP.md`
2. `/home/wufei/.openclaw/workspace/memory/CORE_RULES.md`
3. `/home/wufei/.openclaw/workspace/agents/<agent>/AGENTS.md`

**This happens BEFORE any task execution.**
```

---

## 📊 方案对比

| 方案                     | 自动程度       | 实现难度          | 推荐度     |
| ------------------------ | -------------- | ----------------- | ---------- |
| **BOOTSTRAP.md**         | 100% 自动      | ✅ 已完成         | ⭐⭐⭐⭐⭐ |
| **memory/CORE_RULES.md** | 依赖 AGENTS.md | ✅ 已完成         | ⭐⭐⭐⭐⭐ |
| **Session Hook**         | 100% 自动      | 🟡 需配置 Gateway | ⭐⭐⭐⭐   |
| **Agent 配置**           | 依赖自觉       | ✅ 已完成         | ⭐⭐⭐⭐   |

---

## ✅ 当前实现状态

### 已实现 (无需额外配置)

- [x] `BOOTSTRAP.md` - 会话启动自动读取
- [x] `memory/CORE_RULES.md` - 持久化记忆
- [x] `agents/*/AGENTS.md` - 规定每次会话必读
- [x] `auto-init-if-needed.sh` - 自动检测 + 初始化

### 工作流程

```
新会话启动
  ↓
OpenClaw 自动读取 BOOTSTRAP.md
  ↓
智能体读取 memory/CORE_RULES.md (按 AGENTS.md 要求)
  ↓
检测项目是否初始化
  ↓
未初始化 → 自动执行 auto-init-if-needed.sh
  ↓
开始执行用户任务
```

---

## 🎯 最佳实践

### 推荐配置 (当前已实现)

**什么都不用做！** 已经自动了：

1. ✅ BOOTSTRAP.md 每次会话自动读
2. ✅ memory/CORE_RULES.md 智能体必读
3. ✅ auto-init-if-needed.sh 自动检测执行

### 可选增强

如果想更激进，可以：

**添加 Session Hook**:

```bash
# ~/.openclaw/session-init.sh
cat /home/wufei/.openclaw/workspace/memory/CORE_RULES.md
```

**修改 Gateway 配置**:

```json
{
  "session": {
    "initScript": "~/.openclaw/session-init.sh"
  }
}
```

---

## 📋 验证方法

### 测试自动读取

```bash
# 1. 启动新会话
/new

# 2. 问智能体
"What are the 3 red lines?"

# 3. 期望回答
- No placeholders
- Contract first
- Data model review
- Security baseline

# 4. 证明读取了 CORE_RULES.md
```

### 测试自动初始化

```bash
# 1. 创建新目录
mkdir test-project
cd test-project

# 2. 对智能体说
"Create a new IM project"

# 3. 期望行为
- 自动检测项目未初始化
- 自动执行 auto-init-if-needed.sh
- 回复：项目已自动初始化完成
```

---

## 🎯 总结

**当前方案已经是最优解**:

1. ✅ **BOOTSTRAP.md** - OpenClaw 原生，每次会话必读
2. ✅ **memory/CORE_RULES.md** - 持久化，所有智能体共享
3. ✅ **agents/AGENTS.md** - 明确规定每次会话必读
4. ✅ **auto-init-if-needed.sh** - 自动检测 + 初始化

**无需额外配置！** 已经全自动了 🤖

---

**版本**: 1.0 **最后更新**: 2026-03-20 **维护者**: ai-orchestrator
