# 🚀 OpenClaw 快捷命令配置

> **用途**: 添加快捷命令到 shell，实现自动初始化

---

## 📦 安装快捷命令

### 方法 1: 添加到 bashrc（推荐）

```bash
# 添加到 ~/.bashrc
cat >> ~/.bashrc << 'EOF'

# OpenClaw 快捷命令
alias oc-init='cd /home/wufei/.openclaw/workspace && ./auto-init-if-needed.sh'
alias oc-new='cd /home/wufei/.openclaw/workspace && ./init-project.sh'
alias oc-status='cd /home/wufei/.openclaw/workspace && ./check-project-status.sh'

# 自动初始化函数
oc-auto() {
    cd /home/wufei/.openclaw/workspace
    ./auto-init-if-needed.sh "$1"
}
EOF

# 使配置生效
source ~/.bashrc
```

### 方法 2: 添加到 zshrc

```bash
# 如果使用 zsh，添加到 ~/.zshrc
cat >> ~/.zshrc << 'EOF'

# OpenClaw 快捷命令
alias oc-init='cd /home/wufei/.openclaw/workspace && ./auto-init-if-needed.sh'
alias oc-new='cd /home/wufei/.openclaw/workspace && ./init-project.sh'

oc-auto() {
    cd /home/wufei/.openclaw/workspace
    ./auto-init-if-needed.sh "$1"
}
EOF

source ~/.zshrc
```

---

## 🎯 使用方式

### 自动初始化（推荐）

```bash
# 在项目目录下执行
cd my-new-project
oc-init

# 或指定项目名称
oc-init my-project
```

### 手动初始化

```bash
oc-new my-project
```

### 检查项目状态

```bash
oc-status my-project
```

---

## 🤖 完全自动化（无需手动命令）

### 方案：在 AGENTS.md 中配置自动执行

**ai-orchestrator** 会在检测到新项目时自动执行：

```bash
cd /home/wufei/.openclaw/workspace
./auto-init-if-needed.sh <project-name>
```

**用户完全不需要手动执行！**

---

## 📋 自动化流程

```
用户：帮我创建一个新的 IM 项目
  ↓
ai-orchestrator: 检测项目是否存在
  ↓
未存在 → 自动执行 ./auto-init-if-needed.sh im-system
  ↓
自动创建目录 + 复制模板 + 初始化 Git
  ↓
✅ 回复用户：项目已自动初始化完成
  ↓
开始执行开发任务
```

---

## 🔧 自定义配置

### 跳过自动初始化

如果用户想手动控制，可以在任务中说明：

```
"创建新项目，但不要自动初始化"
```

ai-orchestrator 会：

- ⛔ 不执行 auto-init-if-needed.sh
- ✅ 仅创建基本目录
- ⚠️ 提醒用户手动初始化

### 强制重新初始化

```bash
oc-init my-project --force
```

会覆盖现有文件（会先备份）

---

## 📊 快捷命令列表

| 命令        | 功能              | 示例                   |
| ----------- | ----------------- | ---------------------- |
| `oc-init`   | 自动检测 + 初始化 | `oc-init my-project`   |
| `oc-new`    | 强制新建项目      | `oc-new my-project`    |
| `oc-status` | 检查项目状态      | `oc-status my-project` |
| `oc-auto`   | 智能初始化函数    | `oc-auto my-project`   |

---

## 🎯 推荐配置

**最简单的方式**（推荐）：

什么都不用做！ai-orchestrator 会自动检测和初始化。

**如果习惯用命令行**：

```bash
# 添加到 ~/.bashrc
alias oc-init='cd /home/wufei/.openclaw/workspace && ./auto-init-if-needed.sh'
```

然后用：

```bash
oc-init my-project
```

---

**版本**: 1.0 **最后更新**: 2026-03-20
