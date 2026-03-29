---
name: opencli
description:
  AI 驱动的网站 CLI 工具，把 65+ 网站变成命令行。支持知乎、B 站、微博、小红书、抖音、京东、GitHub 等。Use when user
  needs to fetch data from websites, browse social media, search content, or automate web interactions via CLI.
---

# opencli Skill

## 核心能力

opencli 是一个 AI 驱动的 CLI 工具，可以把任何网站变成命令行工具。内置 **392 个命令**，覆盖 **65 个网站**。

## 快速开始

### 安装状态检查

```bash
# 检查 opencli 是否已安装
opencli --version

# 查看可用命令列表
opencli list
```

### 常用命令

#### 中文内容平台

```bash
# 知乎
opencli zhihu hot              # 知乎热榜
opencli zhihu search "AI 工具"  # 搜索话题
opencli zhihu question "https://www.zhihu.com/question/xxx"  # 问题详情

# B 站
opencli bilibili hot           # 热门视频
opencli bilibili search "教程"  # 搜索视频
opencli bilibili user "UID"    # 用户投稿

# 微博
opencli weibo hot              # 微博热搜
opencli weibo search "话题"     # 搜索微博
opencli weibo feed             # 关注的时间线

# 小红书
opencli xiaohongshu search "好物推荐"  # 搜索笔记
opencli xiaohongshu comments "笔记 ID"  # 获取评论

# 抖音
opencli douyin videos          # 作品列表
opencli douyin profile         # 账号信息

# 什么值得买
opencli smzdm search "iPhone"  # 搜索好价
```

#### 开发相关

```bash
# GitHub (自动安装)
opencli gh repo list
opencli gh issue list

# Vercel (自动安装)
opencli vercel deploy
opencli vercel logs

# HackerNews
opencli hackernews top         # 热门话题
opencli hackernews new         # 最新提交

# Stack Overflow
opencli stackoverflow hot      # 热门问题
opencli stackoverflow search "python error"  # 搜索
```

#### 新闻资讯

```bash
# 36 氪
opencli 36kr hot               # 热榜
opencli 36kr news              # 最新资讯

# 新浪财经
opencli sinafinance news       # 7x24 小时快讯
opencli sinafinance stock "sh600519"  # 股票行情

# BBC
opencli bbc news               # 新闻头条

# Bloomberg
opencli bloomberg markets      # 市场新闻
```

#### 视频/音乐

```bash
# YouTube
opencli youtube search "tutorial"  # 搜索视频
opencli youtube video "视频 ID"    # 视频详情
opencli youtube transcript "视频 ID"  # 字幕

# 小宇宙播客
opencli xiaoyuzhou podcast "播客 ID"  # 播客详情
opencli xiaoyuzhou episode "单集 ID"  # 单集详情

# Apple Podcasts
opencli apple-podcasts search "AI"  # 搜索播客
opencli apple-podcasts top          # 热门榜单
```

#### 购物

```bash
# 京东
opencli jd item "https://item.jd.com/xxx.html"  # 商品详情

# 淘宝/天猫
# 需要通过 web read 间接访问

# 什么值得买
opencli smzdm search "折扣"  # 搜索好价
```

#### 通用网页读取

```bash
# 任何网页转 Markdown
opencli web read "https://example.com/article"
```

## 命令分类

### 按访问方式

- **public** - 无需登录，直接访问
- **cookie** - 需要浏览器登录态
- **ui** - 需要桌面应用（ChatGPT Desktop、Cursor 等）
- **intercept** - 通过拦截网络请求获取数据

### 按功能

- **搜索** - `search` 命令
- **热门** - `hot` / `top` / `trending` 命令
- **详情** - `detail` / `info` / `profile` 命令
- **列表** - `list` / `feed` / `timeline` 命令
- **下载** - `download` 命令

## 使用场景

### 信息收集

- 收集竞品动态（知乎、微博、小红书）
- 跟踪行业新闻（36 氪、Bloomberg、HackerNews）
- 监控品牌提及（搜索命令）

### 内容创作

- 找选题灵感（热榜命令）
- 收集素材（搜索 + 详情命令）
- 分析爆款内容（评论、点赞数据）

### 开发辅助

- 查技术文档（web read）
- 搜解决方案（Stack Overflow）
- 管理 GitHub 项目

### 数据分析

- 抓取公开数据（public 命令）
- 导出为 JSON/Markdown（`-f json` 参数）
- 批量处理（循环调用）

## 输出格式

大多数命令支持格式参数：

```bash
# 默认人类可读格式
opencli zhihu hot

# JSON 格式（便于程序处理）
opencli zhihu hot -f json

# 简洁模式
opencli zhihu hot --compact
```

## 注意事项

### Cookie 依赖

需要登录的命令（标记为 `cookie`）依赖浏览器登录态：

1. 确保已在浏览器登录对应网站
2. opencli 会复用浏览器会话
3. 某些网站可能需要定期重新登录

### 反爬限制

- 部分网站有频率限制
- 避免短时间内大量请求
- 建议使用 `public` 命令优先

### 错误处理

```bash
# 诊断工具
opencli doctor  # 检查浏览器连接状态

# 详细日志
opencli zhihu hot --verbose
```

## 扩展能力

### 一键生成 CLI

可以把任意网站变成 CLI：

```bash
opencli generate https://example.com
```

### 录制 API

从浏览器会话录制 API 调用：

```bash
opencli record https://example.com
```

### 插件系统

安装第三方插件：

```bash
opencli plugin install <plugin-name>
```

## 故障排查

### 常见问题

**命令不工作**

```bash
# 1. 检查版本
opencli --version

# 2. 检查浏览器连接
opencli doctor

# 3. 查看详细错误
opencli <command> --verbose
```

**需要登录**

- 在浏览器中登录对应网站
- 确保浏览器完全关闭前不要操作
- 某些网站需要保持浏览器运行

**输出为空**

- 检查网站是否需要登录
- 尝试 `--verbose` 查看请求详情
- 可能是网站结构变化，需要更新 opencli

## 相关资源

- 完整命令列表：`opencli list`
- GitHub: https://github.com/jackwener/opencli
- 扩展下载：https://github.com/jackwener/opencli/releases
