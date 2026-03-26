# UI/UX 布局差异分析报告

**分析日期**: 2026-03-17 **分析师**: UI/UX 专家 **参考产品**: Julius.ai **目标项目**: ChatBI
(`/home/wufei/workspace/vanna-main/frontends/analysis-chat`)

---

## 目录

1. [布局差异分析](#1-布局差异分析)
2. [浅色主题设计规范](#2-浅色主题设计规范)
3. [组件优化建议](#3-组件优化建议)
4. [实施路线图](#4-实施路线图)

---

## 1. 布局差异分析

### 1.1 整体架构对比

| 维度         | Julius.ai (参考)             | 当前 ChatBI              | 差距评估            |
| ------------ | ---------------------------- | ------------------------ | ------------------- |
| **主题**     | 浅色主题 (#FFFFFF)           | 深色主题 (#0F0F0F)       | ⚠️ 需要切换         |
| **侧边栏**   | 可折叠 + 用户信息 + 使用限制 | 固定 + 导航菜单          | ⚠️ 缺少使用限制提示 |
| **顶部栏**   | 模型选择器 + 设置按钮        | 项目选择器 + 搜索 + 用户 | ⚠️ 缺少模型选择器   |
| **主输入区** | 大型输入框 + 快捷按钮        | 基础输入框               | ⚠️ 缺少快捷操作按钮 |
| **引导入门** | 解锁进度 (2/3 步骤)          | 欢迎卡片                 | ⚠️ 缺少进度引导     |
| **数据连接** | Slack/Postgres 快捷按钮      | 无                       | ❌ 缺失             |

### 1.2 详细功能对比

#### 1.2.1 侧边栏对比

**Julius.ai 侧边栏特点:**

```
┌─────────────────┐
│ 🎯 Logo         │
│ 👤 用户信息      │
│ [+ New] 按钮    │
├─────────────────┤
│ 📝 Chats        │
│ 📓 Notebooks    │
│ 📁 Files        │
│ 🔌 Data Conn.   │
│ 🤖 Custom Agents│
├─────────────────┤
│ 📊 5 messages   │
│    left         │
│ [⬆️ Upgrade]    │
└─────────────────┘
```

**当前 ChatBI 侧边栏:**

```
┌─────────────────┐
│ 📊 数据导航     │
├─────────────────┤
│ 📊 数据表 (42)  │
│ 📈 报表         │
│ 💾 指标         │
│ 🔗 血缘         │
├─────────────────┤
│ 🕐 历史会话     │
│ - 今天          │
│ - 昨天          │
│ - 更早          │
└─────────────────┘
```

**差距分析:**

- ✅ 已有: 导航菜单、历史记录
- ❌ 缺失: 用户信息区、使用限制提示、升级入口
- ⚠️ 建议: 添加 New 按钮到顶部，添加配额显示

#### 1.2.2 主内容区对比

**Julius.ai 主内容区:**

```
┌─────────────────────────────────────┐
│ [Julius 1.1 Lite ▼]        [⚙️]    │ ← 模型选择器
├─────────────────────────────────────┤
│                                     │
│    ┌─────────────────────────┐     │
│    │ 💬 输入您的问题...      │     │ ← 大型输入框
│    │                         │     │
│    └─────────────────────────┘     │
│                                     │
│    [Connectors] [Tools] [Advanced] │ ← 快捷按钮
│                                     │
│    Start from a template ▼         │ ← 模板选择
│    [Slack] [Postgres] [+]          │ ← 数据连接
│                                     │
├─────────────────────────────────────┤
│    🎯 Unlock 2/3 steps             │ ← 进度引导
│    ✓ Connect data                  │
│    ✓ Ask a question                │
│    ○ Save a chart                  │
└─────────────────────────────────────┘
```

**当前 ChatBI 主内容区:**

```
┌─────────────────────────────────────┐
│                                     │
│    🤖 欢迎使用 ChatBI               │
│    智能数据分析助手                  │
│                                     │
│    ┌──────────┐ ┌──────────┐       │
│    │ 分析销售 │ │ 生成图表 │       │
│    └──────────┘ └──────────┘       │
│    ┌──────────┐ ┌──────────┐       │
│    │ 异常检测 │ │ 生成报告 │       │
│    └──────────┘ └──────────┘       │
│                                     │
├─────────────────────────────────────┤
│    💬 输入问题... [发送]            │ ← 基础输入框
└─────────────────────────────────────┘
```

**差距分析:**

- ❌ 缺失: 模型选择器（顶部）
- ❌ 缺失: Connectors/Tools/Advanced Reasoning 快捷按钮
- ❌ 缺失: 数据连接快捷入口 (Slack, Postgres)
- ❌ 缺失: 引导式入门进度条
- ⚠️ 建议: 扩展输入区，添加快捷操作

#### 1.2.3 配色方案对比

| 用途       | Julius.ai        | 当前 ChatBI      | 建议        |
| ---------- | ---------------- | ---------------- | ----------- |
| 主品牌色   | `#7C3AED` (紫色) | `#7C3AED` (紫色) | ✅ 保持一致 |
| 背景       | `#FFFFFF`        | `#0F0F0F`        | ⚠️ 需要切换 |
| 次背景     | `#F9FAFB`        | `#1A1A1A`        | ⚠️ 需要切换 |
| 卡片背景   | `#FFFFFF`        | `#1F1F1F`        | ⚠️ 需要切换 |
| 边框       | `#E5E7EB`        | `#2A2A2A`        | ⚠️ 需要切换 |
| 主文字     | `#111827`        | `#FFFFFF`        | ⚠️ 需要切换 |
| 次文字     | `#6B7280`        | `#9CA3AF`        | ⚠️ 可复用   |
| Hover 背景 | `#F3F4F6`        | `#1F1F1F`        | ⚠️ 需要切换 |

---

## 2. 浅色主题设计规范

### 2.1 CSS 变量定义

```css
:root {
  /* ===== 品牌色 ===== */
  --color-primary: #7c3aed;
  --color-primary-hover: #6d28d9;
  --color-primary-light: #a78bfa;
  --color-primary-surface: rgba(124, 58, 237, 0.08);

  /* ===== 背景色 ===== */
  --color-bg-base: #ffffff;
  --color-bg-subtle: #f9fafb;
  --color-bg-muted: #f3f4f6;
  --color-bg-elevated: #ffffff;
  --color-bg-sunken: #f9fafb;

  /* ===== 边框色 ===== */
  --color-border: #e5e7eb;
  --color-border-subtle: #f3f4f6;
  --color-border-strong: #d1d5db;
  --color-border-focus: #7c3aed;

  /* ===== 文字色 ===== */
  --color-text-primary: #111827;
  --color-text-secondary: #6b7280;
  --color-text-muted: #9ca3af;
  --color-text-inverse: #ffffff;

  /* ===== 状态色 ===== */
  --color-success: #10b981;
  --color-success-surface: rgba(16, 185, 129, 0.08);
  --color-warning: #f59e0b;
  --color-warning-surface: rgba(245, 158, 11, 0.08);
  --color-error: #ef4444;
  --color-error-surface: rgba(239, 68, 68, 0.08);
  --color-info: #3b82f6;
  --color-info-surface: rgba(59, 130, 246, 0.08);

  /* ===== 圆角 ===== */
  --radius-sm: 8px;
  --radius-md: 12px;
  --radius-lg: 16px;
  --radius-xl: 20px;
  --radius-full: 9999px;

  /* ===== 阴影 ===== */
  --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.05);
  --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
  --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
  --shadow-xl: 0 20px 25px -5px rgba(0, 0, 0, 0.1);
  --shadow-primary: 0 4px 14px rgba(124, 58, 237, 0.25);
}

/* 深色模式 (保留切换能力) */
.dark {
  --color-bg-base: #0f0f0f;
  --color-bg-subtle: #141414;
  --color-bg-muted: #1a1a1a;
  --color-bg-elevated: #1f1f1f;
  --color-bg-sunken: #0a0a0a;

  --color-border: #2a2a2a;
  --color-border-subtle: #1f1f1f;
  --color-border-strong: #3a3a3a;

  --color-text-primary: #ffffff;
  --color-text-secondary: #9ca3af;
  --color-text-muted: #6b7280;

  --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.3);
  --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.4);
  --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.5);
}
```

### 2.2 Tailwind 类名映射

```typescript
// tailwind.config.js 扩展配置
module.exports = {
  theme: {
    extend: {
      colors: {
        // 品牌色
        primary: {
          DEFAULT: "#7C3AED",
          hover: "#6D28D9",
          light: "#A78BFA",
          surface: "rgba(124, 58, 237, 0.08)",
        },
        // 浅色主题背景
        surface: {
          base: "#FFFFFF",
          subtle: "#F9FAFB",
          muted: "#F3F4F6",
          elevated: "#FFFFFF",
          sunken: "#F9FAFB",
        },
        // 边框
        border: {
          DEFAULT: "#E5E7EB",
          subtle: "#F3F4F6",
          strong: "#D1D5DB",
        },
        // 文字
        content: {
          primary: "#111827",
          secondary: "#6B7280",
          muted: "#9CA3AF",
        },
      },
      borderRadius: {
        sm: "8px",
        md: "12px",
        lg: "16px",
        xl: "20px",
      },
      boxShadow: {
        primary: "0 4px 14px rgba(124, 58, 237, 0.25)",
        card: "0 1px 3px rgba(0, 0, 0, 0.1), 0 1px 2px rgba(0, 0, 0, 0.06)",
      },
    },
  },
};
```

### 2.3 组件样式类映射表

| 组件         | 深色模式类                      | 浅色模式类                   | 说明     |
| ------------ | ------------------------------- | ---------------------------- | -------- |
| **页面背景** | `bg-[#0F0F0F]`                  | `bg-white`                   | 主背景   |
| **卡片背景** | `bg-[#1A1A1A]`                  | `bg-white`                   | 卡片容器 |
| **次级背景** | `bg-[#1F1F1F]`                  | `bg-gray-50`                 | 次级容器 |
| **边框**     | `border-[#2A2A2A]`              | `border-gray-200`            | 边框色   |
| **主文字**   | `text-white`                    | `text-gray-900`              | 主文字   |
| **次文字**   | `text-gray-400`                 | `text-gray-500`              | 次文字   |
| **悬停背景** | `hover:bg-[#1F1F1F]`            | `hover:bg-gray-100`          | 悬停效果 |
| **选中背景** | `bg-purple-500/20`              | `bg-purple-50`               | 选中状态 |
| **输入框**   | `bg-[#1A1A1A] border-[#2A2A2A]` | `bg-gray-50 border-gray-200` | 输入框   |
| **阴影**     | 无/自定义                       | `shadow-sm shadow-card`      | 卡片阴影 |

---

## 3. 组件优化建议

### 3.1 全局样式文件 (`style.css`)

**当前问题:**

- 默认深色主题
- 缺少浅色模式变量
- 部分硬编码颜色值

**优化方案:**

```css
/* style.css 优化版 */

/* 主题变量 */
:root {
  color-scheme: light;

  /* 浅色主题 (默认) */
  --primary: #7c3aed;
  --primary-hover: #6d28d9;
  --primary-light: #a78bfa;

  --bg-base: #ffffff;
  --bg-subtle: #f9fafb;
  --bg-muted: #f3f4f6;
  --bg-elevated: #ffffff;

  --border: #e5e7eb;
  --border-subtle: #f3f4f6;

  --text-primary: #111827;
  --text-secondary: #6b7280;
  --text-muted: #9ca3af;

  --radius-lg: 16px;
  --radius-md: 12px;
  --radius-sm: 8px;

  --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.05);
  --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
  --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
  --shadow-primary: 0 4px 14px rgba(124, 58, 237, 0.25);
}

/* 深色模式 */
.dark {
  color-scheme: dark;

  --bg-base: #0f0f0f;
  --bg-subtle: #141414;
  --bg-muted: #1a1a1a;
  --bg-elevated: #1f1f1f;

  --border: #2a2a2a;
  --border-subtle: #1f1f1f;

  --text-primary: #ffffff;
  --text-secondary: #9ca3af;
  --text-muted: #6b7280;

  --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.3);
  --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.4);
  --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.5);
}

/* 基础样式 */
body {
  background-color: var(--bg-base);
  color: var(--text-primary);
  transition:
    background-color 0.2s,
    color 0.2s;
}

/* 消息气泡 - 浅色 */
.message-user {
  background: linear-gradient(135deg, #7c3aed 0%, #6d28d9 100%);
  color: white;
  border-radius: var(--radius-lg) var(--radius-lg) 4px var(--radius-lg);
}

.message-ai {
  background: var(--bg-muted);
  color: var(--text-primary);
  border-radius: var(--radius-lg) var(--radius-lg) var(--radius-lg) 4px;
  border: 1px solid var(--border-subtle);
}

.dark .message-ai {
  background: #1f1f1f;
  border-color: #2a2a2a;
}

/* 卡片样式 - 浅色 */
.card-welcome {
  background: var(--bg-elevated);
  border: 1px solid var(--border);
  transition: all 0.3s ease;
  box-shadow: var(--shadow-sm);
}

.card-welcome:hover {
  background: var(--bg-subtle);
  border-color: var(--primary);
  transform: translateY(-2px);
  box-shadow: var(--shadow-primary);
}

/* 输入框 - 浅色 */
.input-area {
  background: var(--bg-muted);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  transition: all 0.2s ease;
}

.input-area:focus-within {
  border-color: var(--primary);
  box-shadow: 0 0 0 3px rgba(124, 58, 237, 0.1);
}

/* 按钮样式 */
.btn-primary {
  background: linear-gradient(135deg, #7c3aed 0%, #6d28d9 100%);
  color: white;
  border-radius: var(--radius-md);
  transition: all 0.2s ease;
}

.btn-primary:hover {
  transform: translateY(-1px);
  box-shadow: var(--shadow-primary);
}

.btn-secondary {
  background: var(--bg-muted);
  color: var(--text-primary);
  border: 1px solid var(--border);
  border-radius: var(--radius-md);
  transition: all 0.2s ease;
}

.btn-secondary:hover {
  background: var(--bg-subtle);
  border-color: var(--primary);
}
```

### 3.2 App.vue 组件优化

**需要修改的部分:**

```vue
<!-- 修改前 (深色硬编码) -->
<div class="h-screen flex flex-col bg-[#0F0F0F] text-white">

<!-- 修改后 (支持主题切换) -->
<div class="h-screen flex flex-col bg-white dark:bg-[#0F0F0F] text-gray-900 dark:text-white">
```

**侧边栏优化:**

```vue
<!-- 修改前 -->
<aside class="w-64 border-r border-[#2A2A2A] bg-[#0F0F0F] flex flex-col">

<!-- 修改后 -->
<aside class="w-64 border-r border-gray-200 dark:border-[#2A2A2A] bg-white dark:bg-[#0F0F0F] flex flex-col">
```

**导航项优化:**

```vue
<!-- 修改前 -->
:class="[ 'w-full flex items-center gap-3 px-3 py-2 rounded-lg text-sm transition-colors', currentPage === item.id ?
'bg-purple-500/20 text-purple-400' : 'text-gray-400 hover:bg-[#1F1F1F] hover:text-white' ]"

<!-- 修改后 -->
:class="[ 'w-full flex items-center gap-3 px-3 py-2 rounded-lg text-sm transition-colors', currentPage === item.id ?
'bg-purple-50 dark:bg-purple-500/20 text-purple-600 dark:text-purple-400' : 'text-gray-600 dark:text-gray-400
hover:bg-gray-100 dark:hover:bg-[#1F1F1F] hover:text-gray-900 dark:hover:text-white' ]"
```

**添加模型选择器 (新功能):**

```vue
<!-- 在顶部导航栏添加 -->
<div class="flex items-center gap-4">
  <!-- 模型选择器 -->
  <div class="model-selector">
    <button class="flex items-center gap-2 px-3 py-1.5 bg-gray-100 dark:bg-[#1A1A1A] rounded-lg text-sm">
      <span class="text-purple-500">●</span>
      <span>{{ currentModel }}</span>
      <svg class="w-4 h-4 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
      </svg>
    </button>
  </div>
</div>
```

**添加使用限制提示 (新功能):**

```vue
<!-- 在侧边栏底部添加 -->
<div class="p-4 border-t border-gray-200 dark:border-[#2A2A2A]">
  <div class="bg-purple-50 dark:bg-purple-500/10 rounded-xl p-3">
    <div class="flex items-center gap-2 text-sm text-purple-700 dark:text-purple-300">
      <span>📊</span>
      <span>{{ messagesLeft }} 条消息剩余</span>
    </div>
    <button class="w-full mt-2 py-2 bg-purple-500 text-white rounded-lg text-sm font-medium hover:bg-purple-600 transition-colors">
      升级 Pro
    </button>
  </div>
</div>
```

### 3.3 ChatBIInterface.vue 组件优化

**背景渐变优化:**

```css
/* 修改前 (深色渐变) */
.chatbi-container {
  background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
}

/* 修改后 (浅色渐变) */
.chatbi-container {
  background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 50%, #e2e8f0 100%);
}

.dark .chatbi-container {
  background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
}
```

**顶部导航优化:**

```css
/* 修改前 */
.top-nav {
  background: rgba(255, 255, 255, 0.05);
  backdrop-filter: blur(10px);
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

/* 修改后 */
.top-nav {
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(10px);
  border-bottom: 1px solid rgba(0, 0, 0, 0.05);
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
}

.dark .top-nav {
  background: rgba(255, 255, 255, 0.05);
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}
```

**消息气泡优化:**

```css
/* 修改前 */
.message-text {
  background: rgba(255, 255, 255, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.1);
  color: rgba(255, 255, 255, 0.9);
}

/* 修改后 */
.message-text {
  background: white;
  border: 1px solid rgba(0, 0, 0, 0.08);
  color: #1f2937;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
}

.dark .message-text {
  background: rgba(255, 255, 255, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.1);
  color: rgba(255, 255, 255, 0.9);
}
```

**指标卡片优化:**

```css
/* 修改前 */
.metric-card {
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid rgba(255, 255, 255, 0.1);
}

/* 修改后 */
.metric-card {
  background: white;
  border: 1px solid rgba(0, 0, 0, 0.08);
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
}

.dark .metric-card {
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid rgba(255, 255, 255, 0.1);
}
```

### 3.4 ChatInterface.vue 组件优化

**背景色优化:**

```vue
<!-- 修改前 -->
<div class="flex-1 flex flex-col min-h-0 bg-dark-bg">

<!-- 修改后 -->
<div class="flex-1 flex flex-col min-h-0 bg-white dark:bg-dark-bg">
```

**输入区域优化:**

```vue
<!-- 修改前 -->
<div class="flex-shrink-0 p-4 bg-dark-surface border-t border-dark-border">

<!-- 修改后 -->
<div class="flex-shrink-0 p-4 bg-gray-50 dark:bg-dark-surface border-t border-gray-200 dark:border-dark-border">
```

**输入框优化:**

```vue
<!-- 修改前 -->
<div class="relative flex items-end gap-2 bg-dark-elevated border border-dark-border rounded-2xl">

<!-- 修改后 -->
<div class="relative flex items-end gap-2 bg-white dark:bg-dark-elevated border border-gray-200 dark:border-dark-border rounded-2xl shadow-sm dark:shadow-none">
```

### 3.5 WelcomeCards.vue 组件优化

**欢迎标题优化:**

```vue
<!-- 修改前 -->
<h1 class="text-3xl font-bold text-white mb-3">

<!-- 修改后 -->
<h1 class="text-3xl font-bold text-gray-900 dark:text-white mb-3">
```

**描述文字优化:**

```vue
<!-- 修改前 -->
<p class="text-gray-400 max-w-md mx-auto">

<!-- 修改后 -->
<p class="text-gray-500 dark:text-gray-400 max-w-md mx-auto">
```

**快捷卡片优化:**

```css
/* 修改前 */
.quick-card {
  background: var(--dark-surface);
  border: 1px solid var(--dark-border);
}

/* 修改后 */
.quick-card {
  background: white;
  border: 1px solid rgba(0, 0, 0, 0.08);
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
}

.dark .quick-card {
  background: var(--dark-surface);
  border: 1px solid var(--dark-border);
}
```

### 3.6 新增组件建议

#### 3.6.1 ModelSelector.vue (新建)

```vue
<template>
  <div class="model-selector relative">
    <button
      @click="isOpen = !isOpen"
      class="flex items-center gap-2 px-3 py-1.5 bg-gray-100 dark:bg-gray-800 rounded-lg text-sm hover:bg-gray-200 dark:hover:bg-gray-700 transition-colors"
    >
      <span class="w-2 h-2 rounded-full bg-green-500"></span>
      <span class="text-gray-700 dark:text-gray-300">{{ currentModel.name }}</span>
      <svg class="w-4 h-4 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
      </svg>
    </button>

    <div
      v-if="isOpen"
      class="absolute top-full mt-2 w-48 bg-white dark:bg-gray-800 rounded-xl shadow-lg border border-gray-200 dark:border-gray-700 py-1 z-50"
    >
      <button
        v-for="model in models"
        :key="model.id"
        @click="selectModel(model)"
        :class="[
          'w-full px-3 py-2 text-left text-sm hover:bg-gray-100 dark:hover:bg-gray-700 transition-colors',
          currentModel.id === model.id ? 'text-purple-600 dark:text-purple-400' : 'text-gray-700 dark:text-gray-300',
        ]"
      >
        <div class="flex items-center gap-2">
          <span class="w-2 h-2 rounded-full" :class="model.color"></span>
          <span>{{ model.name }}</span>
        </div>
        <div class="text-xs text-gray-400 mt-0.5">{{ model.description }}</div>
      </button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";

interface Model {
  id: string;
  name: string;
  description: string;
  color: string;
}

const models: Model[] = [
  { id: "lite", name: "ChatBI Lite", description: "快速响应", color: "bg-green-500" },
  { id: "pro", name: "ChatBI Pro", description: "深度分析", color: "bg-purple-500" },
  { id: "advanced", name: "ChatBI Advanced", description: "高级推理", color: "bg-blue-500" },
];

const currentModel = ref<Model>(models[0]);
const isOpen = ref(false);

function selectModel(model: Model) {
  currentModel.value = model;
  isOpen.value = false;
}
</script>
```

#### 3.6.2 UsageIndicator.vue (新建)

```vue
<template>
  <div class="usage-indicator">
    <div class="bg-purple-50 dark:bg-purple-500/10 rounded-xl p-4">
      <div class="flex items-center justify-between mb-2">
        <span class="text-sm font-medium text-purple-700 dark:text-purple-300">使用配额</span>
        <span class="text-xs text-purple-600 dark:text-purple-400">{{ used }}/{{ total }}</span>
      </div>

      <!-- 进度条 -->
      <div class="w-full h-2 bg-purple-100 dark:bg-purple-900/30 rounded-full overflow-hidden">
        <div
          class="h-full bg-gradient-to-r from-purple-500 to-purple-600 rounded-full transition-all duration-300"
          :style="{ width: `${progress}%` }"
        ></div>
      </div>

      <div class="mt-3 flex items-center justify-between">
        <span class="text-xs text-purple-600 dark:text-purple-400"> {{ remaining }} 条消息剩余 </span>
        <button class="px-3 py-1 bg-purple-500 text-white text-xs rounded-lg hover:bg-purple-600 transition-colors">
          升级 Pro
        </button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from "vue";

const props = withDefaults(
  defineProps<{
    used?: number;
    total?: number;
  }>(),
  {
    used: 15,
    total: 20,
  },
);

const remaining = computed(() => props.total - props.used);
const progress = computed(() => (props.used / props.total) * 100);
</script>
```

#### 3.6.3 OnboardingProgress.vue (新建)

```vue
<template>
  <div
    class="onboarding-progress bg-gradient-to-r from-purple-50 to-blue-50 dark:from-purple-900/20 dark:to-blue-900/20 rounded-xl p-4 mb-4"
  >
    <div class="flex items-center justify-between mb-3">
      <span class="text-sm font-medium text-gray-700 dark:text-gray-300">解锁进度</span>
      <span class="text-xs text-purple-600 dark:text-purple-400">{{ completedSteps }}/{{ totalSteps }}</span>
    </div>

    <div class="space-y-2">
      <div v-for="(step, index) in steps" :key="step.id" class="flex items-center gap-3">
        <div
          :class="[
            'w-6 h-6 rounded-full flex items-center justify-center text-xs',
            step.completed ? 'bg-green-500 text-white' : 'bg-gray-200 dark:bg-gray-700 text-gray-400',
          ]"
        >
          <svg v-if="step.completed" class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
          </svg>
          <span v-else>{{ index + 1 }}</span>
        </div>
        <span
          :class="['text-sm', step.completed ? 'text-gray-700 dark:text-gray-300' : 'text-gray-400 dark:text-gray-500']"
        >
          {{ step.label }}
        </span>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from "vue";

interface Step {
  id: string;
  label: string;
  completed: boolean;
}

const steps: Step[] = [
  { id: "connect", label: "连接数据源", completed: true },
  { id: "ask", label: "提出第一个问题", completed: true },
  { id: "save", label: "保存图表", completed: false },
];

const completedSteps = computed(() => steps.filter((s) => s.completed).length);
const totalSteps = computed(() => steps.length);
</script>
```

#### 3.6.4 DataConnectorButtons.vue (新建)

```vue
<template>
  <div class="data-connectors">
    <div class="text-sm text-gray-500 dark:text-gray-400 mb-3">快速连接数据源</div>
    <div class="flex flex-wrap gap-2">
      <button
        v-for="connector in connectors"
        :key="connector.id"
        @click="handleConnect(connector)"
        class="flex items-center gap-2 px-3 py-2 bg-white dark:bg-gray-800 border border-gray-200 dark:border-gray-700 rounded-lg text-sm hover:border-purple-500 dark:hover:border-purple-500 transition-colors"
      >
        <span class="text-lg">{{ connector.icon }}</span>
        <span class="text-gray-700 dark:text-gray-300">{{ connector.name }}</span>
      </button>
    </div>
  </div>
</template>

<script setup lang="ts">
interface Connector {
  id: string;
  name: string;
  icon: string;
}

const connectors: Connector[] = [
  { id: "slack", name: "Slack", icon: "💬" },
  { id: "postgres", name: "PostgreSQL", icon: "🐘" },
  { id: "mysql", name: "MySQL", icon: "🐬" },
  { id: "mongodb", name: "MongoDB", icon: "🍃" },
  { id: "csv", name: "CSV", icon: "📄" },
  { id: "excel", name: "Excel", icon: "📊" },
];

const emit = defineEmits<{
  (e: "connect", connector: Connector): void;
}>();

function handleConnect(connector: Connector) {
  emit("connect", connector);
}
</script>
```

---

## 4. 实施路线图

### 4.1 优先级排序

| 优先级 | 任务                            | 预计工时 | 影响范围 |
| ------ | ------------------------------- | -------- | -------- |
| **P0** | 修改全局 CSS 变量，支持浅色主题 | 2h       | 全局     |
| **P0** | 更新 App.vue 主要组件颜色类     | 2h       | 主界面   |
| **P0** | 更新 ChatBIInterface.vue 颜色类 | 3h       | 主界面   |
| **P1** | 添加模型选择器组件              | 4h       | 顶部栏   |
| **P1** | 添加使用限制提示组件            | 2h       | 侧边栏   |
| **P1** | 添加引导式入门组件              | 3h       | 主内容   |
| **P2** | 添加数据连接快捷按钮            | 3h       | 主内容   |
| **P2** | 优化 WelcomeCards 组件样式      | 2h       | 主内容   |
| **P2** | 添加深浅主题切换过渡动画        | 2h       | 全局     |

### 4.2 实施步骤

#### 第一阶段: 主题切换 (P0)

1. 更新 `style.css`，添加完整的 CSS 变量体系
2. 确保所有组件使用变量而非硬编码颜色
3. 更新 Tailwind 配置，添加主题相关的工具类
4. 测试主题切换功能

#### 第二阶段: 功能补充 (P1)

1. 创建 `ModelSelector.vue` 组件
2. 创建 `UsageIndicator.vue` 组件
3. 创建 `OnboardingProgress.vue` 组件
4. 集成到主界面布局中

#### 第三阶段: 体验优化 (P2)

1. 创建 `DataConnectorButtons.vue` 组件
2. 优化 WelcomeCards 动画效果
3. 添加主题切换过渡动画
4. 完善响应式适配

### 4.3 验收标准

- [ ] 浅色主题默认开启
- [ ] 深浅主题切换平滑过渡
- [ ] 所有组件支持双主题
- [ ] 模型选择器正常工作
- [ ] 使用限制提示正确显示
- [ ] 引导式入门进度正确
- [ ] 数据连接按钮可点击

---

## 附录

### A. 设计资源

- **Julius.ai 参考截图**: 提供的布局描述
- **Tailwind CSS 文档**: https://tailwindcss.com/docs
- **设计规范参考**: Julius.ai 产品界面

### B. 技术栈

- **框架**: Vue 3 + TypeScript
- **样式**: Tailwind CSS + CSS Variables
- **状态管理**: Pinia
- **构建工具**: Vite

---

**报告结束**

_生成时间: 2026-03-17_
