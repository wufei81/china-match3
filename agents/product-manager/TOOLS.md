# TOOLS.md - 产品经理快速参考

> **完整工具链**: 见 `AGENTS.md` Section 4 | **工作目录**: `~/.openclaw/workspace/agents/product-manager/`

---

## 🔍 Firecrawl 搜索 (首选)

**API Key**: `FIRECRAWL_API_KEY` (已在 ~/.bashrc 配置)

| 操作         | 命令                                                                               |
| ------------ | ---------------------------------------------------------------------------------- |
| **竞品调研** | `python3 skills/firecrawl-search/scripts/search.py "竞品 功能分析" --limit 10`     |
| **用户研究** | `python3 skills/firecrawl-search/scripts/search.py "用户痛点 行业报告" --limit 10` |
| **最佳实践** | `python3 skills/firecrawl-search/scripts/scrape.py "URL"`                          |
| **行业趋势** | `python3 skills/firecrawl-search/scripts/crawl.py "行业网站" --max-pages 20`       |

**备用**: `web_search` (firecrawl 不可用时)

---

## 📋 核心技能触发词

| 技能                 | 触发词                          | 说明                 |
| -------------------- | ------------------------------- | -------------------- |
| **phy-prd-writer**   | `write PRD`, `/prd`, `自主生成` | 双模式 PRD 创建      |
| **diagram**          | -                               | 流程图/时序图/架构图 |
| **firecrawl-search** | -                               | 竞品/市场调研        |
| **summarize**        | -                               | URL/文件摘要         |
| **document-pro**     | -                               | PDF/DOCX 处理        |

---

## 📁 模板路径

| 模板           | 路径                        | 用途              |
| -------------- | --------------------------- | ----------------- |
| **PRD 完整版** | `templates/PRD-Template.md` | 大项目/跨团队协作 |
| **PRD 轻量版** | `templates/PRD-Lite-MVP.md` | MVP/小功能迭代    |

---

## 🎯 注意事项

1. **PRD 模式**: 默认自主多步推理模式
2. **假设标记**: 推断内容必须标记 ⚠️ + 置信度
3. **数据驱动**: 关键决策需有数据支撑

---

**版本**: 2.0 (快速参考) | **最后更新**: 2026-03-26
