# opencli 快速命令参考

## 📱 中文社交平台

### 知乎

```bash
opencli zhihu hot                          # 热榜
opencli zhihu search "关键词"               # 搜索
opencli zhihu question "问题 URL"           # 问题详情
opencli zhihu download "文章 URL"           # 导出 Markdown
```

### B 站

```bash
opencli bilibili hot                       # 热门视频
opencli bilibili search "关键词"            # 搜索视频
opencli bilibili user "UID"                # 用户投稿
opencli bilibili comments "视频 ID"         # 评论
opencli bilibili ranking                   # 排行榜
```

### 微博

```bash
opencli weibo hot                          # 热搜榜
opencli weibo search "话题"                 # 搜索微博
opencli weibo feed                         # 关注时间线
opencli weibo comments "微博 ID"            # 评论
```

### 小红书

```bash
opencli xiaohongshu search "关键词"         # 搜索笔记
opencli xiaohongshu comments "笔记 ID"      # 评论
opencli xiaohongshu download "笔记 ID"      # 下载图片/视频
opencli xiaohongshu feed                   # 推荐 Feed
```

### 抖音

```bash
opencli douyin videos                      # 作品列表
opencli douyin profile                     # 账号信息
opencli douyin stats "作品 ID"              # 作品数据
opencli douyin hashtag "话题"               # 话题列表
```

### 即刻

```bash
opencli jike feed                          # 首页动态
opencli jike search "关键词"                # 搜索
opencli jike topic "话题 ID"                # 话题帖子
opencli jike user "用户 ID"                 # 用户动态
```

## 📰 新闻资讯

### 36 氪

```bash
opencli 36kr hot                           # 热榜
opencli 36kr news                          # 最新资讯
opencli 36kr search "关键词"                # 搜索
opencli 36kr article "文章 URL"            # 文章详情
```

### 新浪财经

```bash
opencli sinafinance news                   # 7x24 快讯
opencli sinafinance stock "sh600519"       # A 股行情
opencli sinafinance stock "hk00700"        # 港股行情
opencli sinafinance stock "usAAPL"         # 美股行情
```

### V2EX

```bash
opencli v2ex hot                           # 热门话题
opencli v2ex latest                        # 最新话题
opencli v2ex daily                         # 每日签到
opencli v2ex node "节点名"                  # 节点话题
```

### HackerNews

```bash
opencli hackernews top                     # 热门
opencli hackernews new                     # 最新
opencli hackernews ask                     # Ask HN
opencli hackernews search "关键词"          # 搜索
```

## 💻 开发工具

### GitHub

```bash
opencli gh repo list                       # 仓库列表
opencli gh issue list                      # Issues
opencli gh pr list                         # Pull Requests
opencli gh release list                    #  Releases
```

### Stack Overflow

```bash
opencli stackoverflow hot                  # 热门问题
opencli stackoverflow search "错误信息"     # 搜索
opencli stackoverflow unanswered           # 未回答问题
opencli stackoverflow bounties             # 悬赏问题
```

### Vercel

```bash
opencli vercel deploy                      # 部署项目
opencli vercel logs                        # 查看日志
opencli vercel ls                          # 项目列表
```

### Cursor/Codex

```bash
opencli cursor ask "问题"                  # 询问 AI
opencli cursor read                        # 读取对话
opencli cursor export                      # 导出对话
opencli codex ask "问题"                   # 询问 Codex
```

## 🛒 电商购物

### 京东

```bash
opencli jd item "商品 URL"                 # 商品详情
```

### 什么值得买

```bash
opencli smzdm search "商品名"              # 搜索好价
```

### 雪球

```bash
opencli xueqiu hot                         # 热门动态
opencli xueqiu stock "股票代码"             # 股票行情
opencli xueqiu watchlist                   # 自选股
opencli xueqiu search "股票名"              # 搜索股票
```

## 🎵 视频音乐

### YouTube

```bash
opencli youtube search "关键词"             # 搜索视频
opencli youtube video "视频 ID"            # 视频详情
opencli youtube transcript "视频 ID"       # 字幕
opencli youtube comments "视频 ID"         # 评论
opencli youtube channel "频道 ID"          # 频道信息
```

### 小宇宙

```bash
opencli xiaoyuzhou podcast "播客 ID"       # 播客详情
opencli xiaoyuzhou episode "单集 ID"       # 单集详情
```

### Apple Podcasts

```bash
opencli apple-podcasts search "关键词"     # 搜索播客
opencli apple-podcasts top                 # 热门榜单
opencli apple-podcasts episodes "播客 ID"  # 单集列表
```

### 豆瓣

```bash
opencli douban movie-hot                   # 电影热榜
opencli douban book-hot                    # 图书热榜
opencli douban top250                      # Top250
opencli douban search "电影名"              # 搜索
opencli douban subject "豆瓣 ID"           # 详情
```

## 🌐 通用工具

### 网页读取

```bash
opencli web read "任意 URL"                # 网页转 Markdown
```

### 搜索

```bash
opencli google search "关键词"             # Google 搜索
opencli google news                        # Google 新闻
opencli google trends                      # Google 趋势
```

### 百科

```bash
opencli wikipedia search "关键词"          # 搜索
opencli wikipedia summary "词条"           # 摘要
opencli wikipedia trending                 # 热门词条
opencli wikipedia random                   # 随机文章
```

### 字典

```bash
opencli dictionary search "单词"           # 查单词
opencli dictionary synonyms "单词"         # 同义词
opencli dictionary examples "单词"         # 例句
```

## 📊 金融数据

### Barchart（美股期权）

```bash
opencli barchart quote "AAPL"             # 股票行情
opencli barchart options "AAPL"           # 期权链
opencli barchart flow                      # 期权异动
opencli barchart greeks                    # 期权希腊值
```

### Yahoo Finance

```bash
opencli yahoo-finance quote "AAPL"        # 股票行情
```

## 🔍 使用技巧

### 输出格式

```bash
# JSON 格式（便于程序处理）
opencli zhihu hot -f json

# 简洁模式
opencli zhihu hot --compact

# 详细模式
opencli zhihu hot --verbose
```

### 诊断工具

```bash
opencli doctor                            # 检查浏览器连接
opencli list                              # 查看所有命令
```

### 一键生成

```bash
opencli generate https://example.com      # 把网站变成 CLI
opencli record https://example.com        # 录制 API 调用
```
