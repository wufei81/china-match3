#!/usr/bin/env python3
# generate-workpackages.py - 从 PRD 自动生成 WorkPackages
# 用法：python3 generate-workpackages.py <PRD 文件路径>

import sys
import re
import json
from datetime import datetime

def extract_p0_features(prd_content):
    """提取 P0 功能 - 增强版（精简）"""
    features = []
    
    # 模式 1: 功能 ID + P0 + 功能名称（最精确）
    id_pattern = r'(?:FEAT-\d+)\s*\|\s*([^|]+)\s*\|\s*P0'
    matches = re.findall(id_pattern, prd_content)
    for match in matches:
        if match.strip() and len(match.strip()) > 2:
            features.append(match.strip())
    
    # 模式 2: 4.1 In Scope 表格中的 P0
    scope_pattern = r'###\s*4\.1\s+In\s+Scope.*?\|\s*([^|]+)\s*\|\s*[^|]*P0[^|]*\|'
    matches = re.findall(scope_pattern, prd_content, re.DOTALL)
    for match in matches[:5]:  # 最多 5 个
        clean = match.strip().split('\n')[0].strip()
        if clean and len(clean) > 2 and clean not in features:
            features.append(clean)
    
    # 模式 3: 5.1 功能章节标题
    func_pattern = r'###\s*5\.\d+\s+功能 [：:]\s*([^\n]+)'
    matches = re.findall(func_pattern, prd_content)
    for match in matches[:5]:
        if match.strip() and len(match.strip()) > 2 and match.strip() not in features:
            features.append(match.strip())
    
    # 如果还是没找到，使用默认 P0 功能
    if not features:
        features = [
            "自然语言查询 - FEAT-001",
            "自动可视化 - FEAT-002",
            "数据报告 - FEAT-003",
            "多数据源支持 - FEAT-004",
            "权限管理 - FEAT-005"
        ]
    
    return features[:5]  # 最多返回 5 个

def extract_api_contracts(prd_content):
    """提取 API 契约"""
    apis = []
    # 查找 API 定义
    api_pattern = r'(POST|GET|PUT|DELETE)\s+(/api/\S+)'
    matches = re.findall(api_pattern, prd_content)
    for method, path in matches:
        apis.append(f"{method} {path}")
    return apis if apis else ["API 契约待定义"]

def extract_user_stories(prd_content):
    """提取用户故事 - 增强版"""
    stories = []
    
    # 模式 1: 标准用户故事格式
    story_pattern = r'作为\s*([^，,]+)，?\s*我想要\s*([^，,]+)，?\s*以便\s*([^\n]+)'
    matches = re.findall(story_pattern, prd_content)
    for role, want, benefit in matches:
        story = f"作为{role.strip()}，我想要{want.strip()}，以便{benefit.strip()}"
        if story not in stories and len(story) > 10:
            stories.append(story)
    
    # 模式 2: 表格中的用户故事
    table_pattern = r'\|\s*(US-\d+)\s*\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|'
    matches = re.findall(table_pattern, prd_content)
    for us_id, role, want, benefit in matches:
        story = f"[{us_id}] 作为{role.strip()}，想要{want.strip()}，以便{benefit.strip()}"
        if story not in stories:
            stories.append(story)
    
    # 模式 3: 简化格式
    simple_pattern = r'(?:^|\n)\s*[-*•]\s*作为\s*([^，,]+)，?\s*想要\s*([^，,]+)'
    matches = re.findall(simple_pattern, prd_content, re.MULTILINE)
    for role, want in matches:
        story = f"作为{role.strip()}，想要{want.strip()}"
        if story not in stories and len(story) > 10:
            stories.append(story)
    
    # 如果没找到，使用默认故事
    if not stories:
        stories = [
            "作为运营人员，我想要用自然语言查询销售额，以便快速获取日报数据",
            "作为管理层，我想要查看经营分析图表，以便辅助决策",
            "作为业务分析师，我想要自动生成周报，以便减少重复劳动"
        ]
    
    return stories[:5]  # 最多返回 5 个

def extract_acceptance_criteria(prd_content):
    """提取验收标准"""
    criteria = []
    # 查找 Gherkin 格式
    gherkin_pattern = r'(Given|When|Then).*?(?:\n|$)'
    matches = re.findall(gherkin_pattern, prd_content, re.MULTILINE)
    if matches:
        criteria.append("Gherkin AC 已定义")
    else:
        criteria.append("AC 待补充 (Gherkin 格式)")
    return criteria

def extract_deployment_requirements(prd_content):
    """提取部署需求"""
    deps = []
    if "部署" in prd_content or "deploy" in prd_content.lower():
        deps.append("部署需求已识别")
    if "监控" in prd_content:
        deps.append("监控需求已识别")
    if "安全" in prd_content:
        deps.append("安全需求已识别")
    return deps if deps else ["部署需求待识别"]

def generate_workpackages(prd_file):
    """生成 WorkPackages"""
    with open(prd_file, 'r', encoding='utf-8') as f:
        prd_content = f.read()
    
    workpackages = {
        "generated_at": datetime.now().isoformat(),
        "prd_file": prd_file,
        "packages": {
            "ui-ux-designer": {
                "input": "P0 功能列表",
                "output": "设计交付物 (Figma/原型)",
                "tasks": extract_p0_features(prd_content),
                "acceptance": "设计覆盖所有 P0 功能的 AC"
            },
            "architect": {
                "input": "PRD + API 契约草稿",
                "output": "架构文档 + DDL",
                "tasks": extract_api_contracts(prd_content),
                "acceptance": "字段级契约明确，DDD 完整"
            },
            "dev-engineer": {
                "input": "架构文档 + 设计稿",
                "output": "可运行代码 + 单元测试",
                "tasks": extract_user_stories(prd_content),
                "acceptance": "E2E 测试通过，AC 覆盖 100%"
            },
            "qa-engineer": {
                "input": "PRD AC + 交付物",
                "output": "测试用例 + E2E 测试",
                "tasks": extract_acceptance_criteria(prd_content),
                "acceptance": "E2E 通过，AC 覆盖 100%"
            },
            "devops-engineer": {
                "input": "架构拓扑 + 部署需求",
                "output": "部署脚本 + 监控配置",
                "tasks": extract_deployment_requirements(prd_content),
                "acceptance": "可一键部署，监控告警就绪"
            }
        }
    }
    
    return workpackages

def print_workpackages(wps):
    """打印 WorkPackages 表格"""
    print("=" * 80)
    print("📦 WorkPackages 自动生成")
    print("=" * 80)
    print(f"生成时间：{wps['generated_at']}")
    print(f"PRD 文件：{wps['prd_file']}")
    print("")
    
    print("| Agent | Input | Output | Acceptance |")
    print("|-------|-------|--------|------------|")
    
    for agent, pkg in wps['packages'].items():
        task_count = len(pkg['tasks'])
        print(f"| {agent} | {pkg['input']} | {pkg['output']} | {pkg['acceptance']} |")
    
    print("")
    print("=" * 80)
    print("📋 详细任务列表")
    print("=" * 80)
    
    for agent, pkg in wps['packages'].items():
        print(f"\n### {agent}")
        print(f"**任务数**: {len(pkg['tasks'])}")
        for i, task in enumerate(pkg['tasks'], 1):
            print(f"  {i}. {task}")

def main():
    if len(sys.argv) < 2:
        print("用法：python3 generate-workpackages.py <PRD 文件路径>")
        print("")
        print("示例:")
        print("  python3 generate-workpackages.py examples/sample-prd-im.md")
        sys.exit(1)
    
    prd_file = sys.argv[1]
    
    try:
        workpackages = generate_workpackages(prd_file)
        print_workpackages(workpackages)
        
        # 保存为 JSON
        output_file = prd_file.replace('.md', '-workpackages.json')
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(workpackages, f, ensure_ascii=False, indent=2)
        print(f"\n✅ WorkPackages 已保存到：{output_file}")
        
    except FileNotFoundError:
        print(f"❌ 错误：文件不存在 - {prd_file}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ 错误：{e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
