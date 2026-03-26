#!/usr/bin/env python3
# competitor-analysis.py - 一键竞品分析
# 用法：python3 competitor-analysis.py --product "产品名" --competitors "竞品 1，竞品 2"

import argparse
import json
from datetime import datetime

def generate_competitor_matrix(product, competitors):
    """生成竞品对比矩阵"""
    
    matrix = {
        "generated_at": datetime.now().isoformat(),
        "product": product,
        "competitors": competitors,
        "comparison": {
            "功能对比": {},
            "价格对比": {},
            "优势劣势": {}
        }
    }
    
    # 功能对比模板
    features = [
        "核心功能 1",
        "核心功能 2",
        "核心功能 3",
        "用户体验",
        "价格",
        "集成能力"
    ]
    
    print("=" * 80)
    print("🔍 竞品分析报告")
    print("=" * 80)
    print(f"产品：{product}")
    print(f"竞品：{', '.join(competitors)}")
    print(f"日期：{datetime.now().strftime('%Y-%m-%d')}")
    print("")
    
    # 生成功能对比表
    print("## 功能对比矩阵")
    print("")
    
    # 表头
    header = f"| 功能 | {product} | " + " | ".join(competitors) + " |"
    print(header)
    print("|" + "-" * 15 + "|" + "-" * 15 + "|" + "|".join(["-" * 15] * len(competitors)) + "|")
    
    # 功能行（示例）
    for feature in features:
        row = f"| {feature} | ✅ | " + " | ".join(["⚠️"] * len(competitors)) + " |"
        print(row)
    
    print("")
    
    # 生成 SWOT 分析
    print("## SWOT 分析")
    print("")
    
    print(f"### {product} - 优势 (Strengths)")
    print("- [ ] [填写你的核心优势]")
    print("- [ ] [填写你的核心优势]")
    print("")
    
    print(f"### {product} - 劣势 (Weaknesses)")
    print("- [ ] [填写你的劣势]")
    print("- [ ] [填写你的劣势]")
    print("")
    
    print(f"### 市场机会 (Opportunities)")
    print("- [ ] [填写市场机会]")
    print("- [ ] [填写市场机会]")
    print("")
    
    print(f"### 市场威胁 (Threats)")
    print("- [ ] [填写市场威胁]")
    print("- [ ] [填写市场威胁]")
    print("")
    
    # 生成差异化建议
    print("## 差异化建议")
    print("")
    print("基于竞品分析，建议聚焦以下差异化：")
    print("")
    print("1. **[差异化 1]**: [描述]")
    print("2. **[差异化 2]**: [描述]")
    print("3. **[差异化 3]**: [描述]")
    print("")
    
    # 输出 Markdown
    markdown_output = f"""# 竞品分析报告

**产品**: {product}  
**竞品**: {', '.join(competitors)}  
**日期**: {datetime.now().strftime('%Y-%m-%d')}

---

## 功能对比矩阵

{header}
|{"|" + "-" * 15 + "|" + "|".join(["-" * 15] * (len(competitors) + 1))}|
"""
    
    for feature in features:
        markdown_output += f"| {feature} | ✅ | " + " | ".join(["⚠️"] * len(competitors)) + " |\n"
    
    markdown_output += f"""
---

## SWOT 分析

### {product} - 优势 (Strengths)
- [ ] [填写你的核心优势]

### {product} - 劣势 (Weaknesses)
- [ ] [填写你的劣势]

### 市场机会 (Opportunities)
- [ ] [填写市场机会]

### 市场威胁 (Threats)
- [ ] [填写市场威胁]

---

## 差异化建议

1. **[差异化 1]**: [描述]
2. **[差异化 2]**: [描述]
3. **[差异化 3]**: [描述]

---

*报告生成时间：{datetime.now().isoformat()}*
"""
    
    # 保存文件
    output_file = f"docs/competitor-analysis-{datetime.now().strftime('%Y%m%d')}.md"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(markdown_output)
    
    print(f"✅ 报告已保存到：{output_file}")
    print("")
    print("=" * 80)
    print("🔜 下一步")
    print("=" * 80)
    print("1. 使用 firecrawl-search 收集竞品信息")
    print("2. 填充上述模板中的 [待填写] 内容")
    print("3. 将分析结果整合到 PRD 的'竞争格局'部分")

def main():
    parser = argparse.ArgumentParser(description='一键生成竞品分析模板')
    parser.add_argument('--product', type=str, required=True, help='你的产品名称')
    parser.add_argument('--competitors', type=str, required=True, help='竞品列表，用逗号分隔')
    
    args = parser.parse_args()
    
    competitors = [c.strip() for c in args.competitors.split(',')]
    
    generate_competitor_matrix(args.product, competitors)

if __name__ == "__main__":
    main()
