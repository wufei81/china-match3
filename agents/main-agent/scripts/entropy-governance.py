#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🧬 熵治理系统 (Entropy Governance System)

基于 capability-evolver 理念的文档自动维护系统
- 检测过时文档
- 发现配置漂移
- 生成修复建议并执行
- Agent 自动维护文档

Author: Y9000P
Version: 1.0.0
"""

import os
import sys
import json
import hashlib
import subprocess
import argparse
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple, Any
from dataclasses import dataclass, field, asdict
from enum import Enum
import re


# ============================================================================
# 配置常量
# ============================================================================

class EntropyLevel(Enum):
    """熵值等级"""
    LOW = "low"           # 文档健康
    MEDIUM = "medium"     # 需要关注
    HIGH = "high"         # 需要修复
    CRITICAL = "critical" # 严重过时/漂移


class ActionType(Enum):
    """修复动作类型"""
    UPDATE = "update"           # 更新内容
    ARCHIVE = "archive"         # 归档
    DELETE = "delete"           # 删除
    MERGE = "merge"             # 合并
    SPLIT = "split"             # 拆分
    RESTRUCTURE = "restructure" # 重构


@dataclass
class DocumentInfo:
    """文档信息"""
    path: str
    name: str
    size: int
    created_at: str
    modified_at: str
    last_accessed: str
    content_hash: str
    word_count: int
    line_count: int
    entropy_level: EntropyLevel = EntropyLevel.LOW
    issues: List[str] = field(default_factory=list)
    suggestions: List[str] = field(default_factory=list)


@dataclass
class ConfigDrift:
    """配置漂移信息"""
    config_file: str
    expected_value: Any
    actual_value: Any
    drift_type: str
    severity: str
    suggestion: str


@dataclass
class GovernanceReport:
    """治理报告"""
    timestamp: str
    total_docs: int
    healthy_docs: int
    outdated_docs: int
    critical_docs: int
    config_drifts: List[ConfigDrift]
    actions_taken: List[Dict]
    summary: str


# ============================================================================
# 核心类：熵治理引擎
# ============================================================================

class EntropyGovernor:
    """熵治理引擎"""
    
    def __init__(self, workspace_root: str, config_file: Optional[str] = None):
        self.workspace_root = Path(workspace_root)
        self.config_file = config_file or self.workspace_root / ".entropy-config.json"
        self.config = self._load_config()
        self.report_data = {
            "timestamp": datetime.now().isoformat(),
            "documents": [],
            "drifts": [],
            "actions": []
        }
        
    def _load_config(self) -> Dict:
        """加载配置文件"""
        default_config = {
            "max_age_days": 90,              # 文档最大年龄（天）
            "check_interval_days": 7,        # 检查间隔（天）
            "auto_fix": False,               # 是否自动修复
            "backup_before_fix": True,       # 修复前备份
            "ignored_patterns": [            # 忽略的模式
                "*.log", "*.tmp", "*.cache",
                ".git/*", "node_modules/*",
                "__pycache__/*", "*.pyc"
            ],
            "critical_paths": [              # 关键路径（优先检查）
                "docs/", "config/", "skills/",
                "MEMORY.md", "IDENTITY.md",
                "SOUL.md", "AGENTS.md"
            ],
            "entropy_thresholds": {          # 熵值阈值
                "low": 0.3,
                "medium": 0.6,
                "high": 0.8
            },
            "content_freshness": {           # 内容新鲜度规则
                "min_update_ratio": 0.1,     # 最小更新比例
                "stale_keywords": [          # 过时关键词
                    "TODO", "FIXME", "XXX",
                    "deprecated", "obsolete"
                ]
            }
        }
        
        if self.config_file.exists():
            try:
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    user_config = json.load(f)
                    default_config.update(user_config)
            except Exception as e:
                print(f"⚠️ 配置文件加载失败：{e}")
        
        return default_config
    
    def _save_config(self):
        """保存配置文件"""
        with open(self.config_file, 'w', encoding='utf-8') as f:
            json.dump(self.config, f, indent=2, ensure_ascii=False)
    
    def _compute_hash(self, content: str) -> str:
        """计算内容哈希"""
        return hashlib.sha256(content.encode('utf-8')).hexdigest()
    
    def _get_file_stats(self, file_path: Path) -> Optional[DocumentInfo]:
        """获取文件统计信息"""
        try:
            stat = file_path.stat()
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            lines = content.split('\n')
            words = content.split()
            
            return DocumentInfo(
                path=str(file_path),
                name=file_path.name,
                size=stat.st_size,
                created_at=datetime.fromtimestamp(stat.st_ctime).isoformat(),
                modified_at=datetime.fromtimestamp(stat.st_mtime).isoformat(),
                last_accessed=datetime.fromtimestamp(stat.st_atime).isoformat(),
                content_hash=self._compute_hash(content),
                word_count=len(words),
                line_count=len(lines)
            )
        except Exception as e:
            print(f"⚠️ 读取文件失败 {file_path}: {e}")
            return None
    
    def _should_ignore(self, file_path: Path) -> bool:
        """检查文件是否应被忽略"""
        path_str = str(file_path)
        for pattern in self.config["ignored_patterns"]:
            if pattern.endswith('*'):
                if path_str.endswith(pattern[:-1]):
                    return True
            elif pattern in path_str:
                return True
        return False
    
    def _calculate_entropy(self, doc: DocumentInfo) -> EntropyLevel:
        """计算文档熵值"""
        entropy_score = 0.0
        issues = []
        suggestions = []
        
        # 1. 时间熵：基于最后修改时间
        modified_date = datetime.fromisoformat(doc.modified_at)
        age_days = (datetime.now() - modified_date).days
        
        if age_days > self.config["max_age_days"]:
            entropy_score += 0.4
            issues.append(f"文档已超过 {age_days} 天未更新（阈值：{self.config['max_age_days']} 天）")
            suggestions.append(f"审查文档内容，更新过时信息")
        elif age_days > self.config["max_age_days"] * 0.7:
            entropy_score += 0.2
            issues.append(f"文档接近更新期限（{age_days}/{self.config['max_age_days']} 天）")
            suggestions.append("考虑安排审查计划")
        
        # 2. 内容熵：检查过时关键词
        try:
            with open(doc.path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read().lower()
            
            stale_keywords = self.config["content_freshness"]["stale_keywords"]
            found_keywords = [kw for kw in stale_keywords if kw.lower() in content]
            
            if found_keywords:
                entropy_score += 0.3 * min(len(found_keywords) / 5, 1.0)
                issues.append(f"发现过时标记：{', '.join(found_keywords[:5])}")
                suggestions.append("移除或解决这些标记")
        except Exception:
            pass
        
        # 3. 访问熵：基于最后访问时间
        accessed_date = datetime.fromisoformat(doc.last_accessed)
        days_since_access = (datetime.now() - accessed_date).days
        
        if days_since_access > 180:
            entropy_score += 0.2
            issues.append(f"文档已超过 {days_since_access} 天未被访问")
            suggestions.append("考虑归档或删除")
        
        # 4. 大小熵：异常大小的文档
        if doc.size > 1024 * 1024:  # > 1MB
            entropy_score += 0.1
            issues.append("文档过大（> 1MB）")
            suggestions.append("考虑拆分文档")
        elif doc.size < 50 and doc.line_count < 5:
            entropy_score += 0.1
            issues.append("文档过小，可能为空或占位符")
            suggestions.append("补充内容或删除")
        
        # 5. 关键路径加权
        for critical_path in self.config["critical_paths"]:
            if critical_path in doc.path:
                entropy_score *= 1.2  # 关键文档熵值加权
                break
        
        # 确定熵等级
        thresholds = self.config["entropy_thresholds"]
        if entropy_score >= thresholds["high"]:
            entropy_level = EntropyLevel.CRITICAL
        elif entropy_score >= thresholds["medium"]:
            entropy_level = EntropyLevel.HIGH
        elif entropy_score >= thresholds["low"]:
            entropy_level = EntropyLevel.MEDIUM
        else:
            entropy_level = EntropyLevel.LOW
        
        doc.entropy_level = entropy_level
        doc.issues = issues
        doc.suggestions = suggestions
        
        return entropy_level
    
    def scan_documents(self, patterns: Optional[List[str]] = None) -> List[DocumentInfo]:
        """扫描文档"""
        print("🔍 开始扫描文档...")
        
        documents = []
        search_patterns = patterns or ["**/*.md", "**/*.py", "**/*.js", "**/*.json", "**/*.yaml", "**/*.yml"]
        
        for pattern in search_patterns:
            for file_path in self.workspace_root.glob(pattern):
                if file_path.is_file() and not self._should_ignore(file_path):
                    doc = self._get_file_stats(file_path)
                    if doc:
                        self._calculate_entropy(doc)
                        documents.append(doc)
                        self.report_data["documents"].append({
                            "path": doc.path,
                            "name": doc.name,
                            "entropy_level": doc.entropy_level.value,
                            "issues": doc.issues,
                            "suggestions": doc.suggestions
                        })
        
        print(f"✅ 扫描完成，共发现 {len(documents)} 个文档")
        return documents
    
    def detect_config_drift(self) -> List[ConfigDrift]:
        """检测配置漂移"""
        print("🔍 检测配置漂移...")
        
        drifts = []
        config_files = list(self.workspace_root.glob("**/*.json")) + \
                      list(self.workspace_root.glob("**/*.yaml")) + \
                      list(self.workspace_root.glob("**/*.yml")) + \
                      list(self.workspace_root.glob("**/.env*"))
        
        for config_file in config_files:
            if self._should_ignore(config_file):
                continue
            
            try:
                # 读取当前配置
                if config_file.suffix == '.json':
                    with open(config_file, 'r', encoding='utf-8') as f:
                        current_config = json.load(f)
                elif config_file.suffix in ['.yaml', '.yml']:
                    # 简单 YAML 解析（不依赖外部库）
                    current_config = self._parse_simple_yaml(config_file)
                elif config_file.name.startswith('.env'):
                    current_config = self._parse_env_file(config_file)
                else:
                    continue
                
                # 检查常见漂移
                drifts.extend(self._check_common_drifts(str(config_file), current_config))
                
            except Exception as e:
                print(f"⚠️ 配置文件解析失败 {config_file}: {e}")
        
        self.report_data["drifts"] = [asdict(d) for d in drifts]
        print(f"✅ 发现 {len(drifts)} 处配置漂移")
        return drifts
    
    def _parse_simple_yaml(self, file_path: Path) -> Dict:
        """简单 YAML 解析（基础支持）"""
        config = {}
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#') and ':' in line:
                        key, value = line.split(':', 1)
                        config[key.strip()] = value.strip()
        except Exception:
            pass
        return config
    
    def _parse_env_file(self, file_path: Path) -> Dict:
        """解析 .env 文件"""
        config = {}
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#') and '=' in line:
                        key, value = line.split('=', 1)
                        config[key.strip()] = value.strip().strip('"\'')
        except Exception:
            pass
        return config
    
    def _check_common_drifts(self, config_file: str, config: Dict) -> List[ConfigDrift]:
        """检查常见配置漂移"""
        drifts = []
        
        # 检查 API 密钥占位符
        for key, value in config.items():
            key_lower = key.lower()
            value_str = str(value).lower()
            
            # API 密钥检查
            if 'key' in key_lower or 'token' in key_lower or 'secret' in key_lower:
                if value_str in ['your_api_key', 'xxx', 'changeme', 'placeholder', '']:
                    drifts.append(ConfigDrift(
                        config_file=config_file,
                        expected_value="<实际 API 密钥>",
                        actual_value=value,
                        drift_type="missing_api_key",
                        severity="high",
                        suggestion=f"配置 {key} 为实际 API 密钥"
                    ))
            
            # URL 占位符检查
            if 'url' in key_lower or 'endpoint' in key_lower:
                if 'example.com' in value_str or 'localhost' in value_str:
                    drifts.append(ConfigDrift(
                        config_file=config_file,
                        expected_value="<生产环境 URL>",
                        actual_value=value,
                        drift_type="placeholder_url",
                        severity="medium",
                        suggestion=f"更新 {key} 为生产环境 URL"
                    ))
            
            # 版本检查
            if 'version' in key_lower:
                if value_str in ['0.0.1', '1.0.0', 'todo', 'tbd']:
                    drifts.append(ConfigDrift(
                        config_file=config_file,
                        expected_value="<实际版本号>",
                        actual_value=value,
                        drift_type="placeholder_version",
                        severity="low",
                        suggestion=f"更新 {key} 为实际版本号"
                    ))
        
        return drifts
    
    def generate_fix_suggestions(self, documents: List[DocumentInfo], 
                                  drifts: List[ConfigDrift]) -> List[Dict]:
        """生成修复建议"""
        suggestions = []
        
        # 文档修复建议
        for doc in documents:
            if doc.entropy_level in [EntropyLevel.HIGH, EntropyLevel.CRITICAL]:
                suggestion = {
                    "type": "document_update",
                    "target": doc.path,
                    "priority": "high" if doc.entropy_level == EntropyLevel.CRITICAL else "medium",
                    "actions": doc.suggestions,
                    "estimated_effort": "15-30 min"
                }
                suggestions.append(suggestion)
        
        # 配置漂移修复建议
        for drift in drifts:
            suggestion = {
                "type": "config_fix",
                "target": drift.config_file,
                "priority": drift.severity,
                "actions": [drift.suggestion],
                "estimated_effort": "5-10 min"
            }
            suggestions.append(suggestion)
        
        # 按优先级排序
        priority_order = {"high": 0, "medium": 1, "low": 2}
        suggestions.sort(key=lambda x: priority_order.get(x["priority"], 3))
        
        return suggestions
    
    def execute_fix(self, suggestion: Dict, auto_approve: bool = False) -> bool:
        """执行修复"""
        print(f"\n🔧 执行修复：{suggestion['type']} -> {suggestion['target']}")
        
        if not auto_approve:
            print(f"   优先级：{suggestion['priority']}")
            print(f"   建议操作：{', '.join(suggestion['actions'])}")
            response = input("   是否执行？(y/n): ").strip().lower()
            if response != 'y':
                print("   ⏭️ 跳过")
                return False
        
        try:
            if suggestion['type'] == 'document_update':
                self._execute_document_fix(suggestion)
            elif suggestion['type'] == 'config_fix':
                self._execute_config_fix(suggestion)
            
            self.report_data["actions"].append({
                "timestamp": datetime.now().isoformat(),
                "suggestion": suggestion,
                "status": "completed"
            })
            print("   ✅ 修复完成")
            return True
            
        except Exception as e:
            print(f"   ❌ 修复失败：{e}")
            self.report_data["actions"].append({
                "timestamp": datetime.now().isoformat(),
                "suggestion": suggestion,
                "status": "failed",
                "error": str(e)
            })
            return False
    
    def _execute_document_fix(self, suggestion: Dict):
        """执行文档修复"""
        # 备份文档
        if self.config["backup_before_fix"]:
            backup_path = suggestion['target'] + f".backup.{datetime.now().strftime('%Y%m%d%H%M%S')}"
            subprocess.run(['cp', suggestion['target'], backup_path], check=True)
            print(f"   📦 已备份到：{backup_path}")
        
        # 添加审查标记
        with open(suggestion['target'], 'a', encoding='utf-8') as f:
            f.write(f"\n---\n🤖 熵治理审查：{datetime.now().isoformat()}\n")
            f.write(f"**待审查项**: {', '.join(suggestion['actions'])}\n")
    
    def _execute_config_fix(self, suggestion: Dict):
        """执行配置修复"""
        # 备份配置
        if self.config["backup_before_fix"]:
            backup_path = suggestion['target'] + f".backup.{datetime.now().strftime('%Y%m%d%H%M%S')}"
            subprocess.run(['cp', suggestion['target'], backup_path], check=True)
            print(f"   📦 已备份到：{backup_path}")
        
        print("   ⚠️  配置修复需要手动审查，已创建备份")
    
    def generate_report(self, output_path: Optional[str] = None) -> GovernanceReport:
        """生成治理报告"""
        docs = self.report_data["documents"]
        drifts = self.report_data["drifts"]
        
        healthy = sum(1 for d in docs if d.get('entropy_level') == EntropyLevel.LOW.value)
        outdated = sum(1 for d in docs if d.get('entropy_level') in [EntropyLevel.MEDIUM.value, EntropyLevel.HIGH.value])
        critical = sum(1 for d in docs if d.get('entropy_level') == EntropyLevel.CRITICAL.value)
        
        report = GovernanceReport(
            timestamp=datetime.now().isoformat(),
            total_docs=len(docs),
            healthy_docs=healthy,
            outdated_docs=outdated,
            critical_docs=critical,
            config_drifts=[ConfigDrift(**d) for d in drifts],
            actions_taken=self.report_data["actions"],
            summary=f"扫描 {len(docs)} 个文档，发现 {outdated + critical} 个需要关注的文档，{len(drifts)} 处配置漂移"
        )
        
        # 保存报告
        report_path = output_path or self.workspace_root / "governance" / f"entropy-report-{datetime.now().strftime('%Y%m%d')}.json"
        Path(report_path).parent.mkdir(parents=True, exist_ok=True)
        
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(asdict(report), f, indent=2, ensure_ascii=False)
        
        print(f"\n📊 治理报告已保存：{report_path}")
        return report
    
    def run_full_governance(self, auto_fix: bool = False, 
                            output_report: Optional[str] = None) -> GovernanceReport:
        """运行完整治理流程"""
        print("=" * 60)
        print("🧬 熵治理系统 v1.0.0")
        print("=" * 60)
        
        # 1. 扫描文档
        documents = self.scan_documents()
        
        # 2. 检测配置漂移
        drifts = self.detect_config_drift()
        
        # 3. 生成修复建议
        suggestions = self.generate_fix_suggestions(documents, drifts)
        
        print(f"\n💡 生成 {len(suggestions)} 条修复建议")
        
        # 4. 执行修复
        if auto_fix and suggestions:
            print("\n🚀 自动修复模式已启用")
            for suggestion in suggestions:
                self.execute_fix(suggestion, auto_approve=True)
        elif suggestions:
            print("\n📋 修复建议列表:")
            for i, s in enumerate(suggestions, 1):
                print(f"  {i}. [{s['priority'].upper()}] {s['type']} -> {s['target']}")
            
            response = input("\n是否执行修复？(y/n): ").strip().lower()
            if response == 'y':
                for suggestion in suggestions:
                    self.execute_fix(suggestion, auto_approve=False)
        
        # 5. 生成报告
        report = self.generate_report(output_report)
        
        # 打印摘要
        print("\n" + "=" * 60)
        print("📈 治理摘要")
        print("=" * 60)
        print(f"  总文档数：{report.total_docs}")
        print(f"  健康文档：{report.healthy_docs} ✅")
        print(f"  需关注：{report.outdated_docs} ⚠️")
        print(f"  严重问题：{report.critical_docs} 🚨")
        print(f"  配置漂移：{len(report.config_drifts)}")
        print(f"  已执行修复：{len(report.actions_taken)}")
        print("=" * 60)
        
        return report


# ============================================================================
# 命令行接口
# ============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="🧬 熵治理系统 - 文档自动维护工具",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  # 扫描并生成报告
  python entropy-governance.py scan

  # 自动修复所有问题
  python entropy-governance.py fix --auto

  # 仅检测配置漂移
  python entropy-governance.py drift

  # 生成详细报告
  python entropy-governance.py report --output ./governance/report.json
        """
    )
    
    parser.add_argument('command', choices=['scan', 'fix', 'drift', 'report', 'full'],
                       help='执行命令')
    parser.add_argument('--workspace', '-w', default='/home/wufei/.openclaw/workspace/agents/main-agent',
                       help='工作区根目录')
    parser.add_argument('--config', '-c', help='配置文件路径')
    parser.add_argument('--auto', '-a', action='store_true',
                       help='自动修复（无需确认）')
    parser.add_argument('--output', '-o', help='报告输出路径')
    parser.add_argument('--verbose', '-v', action='store_true',
                       help='详细输出')
    
    args = parser.parse_args()
    
    governor = EntropyGovernor(args.workspace, args.config)
    
    if args.command == 'scan':
        docs = governor.scan_documents()
        print(f"\n发现 {len(docs)} 个文档")
        
    elif args.command == 'fix':
        docs = governor.scan_documents()
        drifts = governor.detect_config_drift()
        suggestions = governor.generate_fix_suggestions(docs, drifts)
        
        for suggestion in suggestions:
            governor.execute_fix(suggestion, auto_approve=args.auto)
            
    elif args.command == 'drift':
        drifts = governor.detect_config_drift()
        for drift in drifts:
            print(f"\n📍 {drift.config_file}")
            print(f"   类型：{drift.drift_type}")
            print(f"   严重性：{drift.severity}")
            print(f"   建议：{drift.suggestion}")
            
    elif args.command == 'report':
        governor.scan_documents()
        governor.detect_config_drift()
        report = governor.generate_report(args.output)
        print(f"\n{report.summary}")
        
    elif args.command == 'full':
        governor.run_full_governance(auto_fix=args.auto, output_report=args.output)


if __name__ == '__main__':
    main()
