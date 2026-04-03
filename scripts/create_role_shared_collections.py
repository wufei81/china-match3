#!/usr/bin/env python3
"""
创建角色专属共享记忆集合

为 17 个产研智能体的各个角色团队创建专属记忆集合：
- 研发系 (2 Dev): dev_shared_*
- 设计系 (2 UI): ui_shared_*
- 架构师 + 技术负责人：arch_tech_shared_*
- QA: qa_shared_*
- DevOps: devops_shared_*
- 项目经理：pm_mgr_shared_*
"""

from qdrant_client import QdrantClient
from qdrant_client import models

QDRANT_HOST = "localhost"
QDRANT_PORT = 6333

# 角色专属集合定义
ROLE_COLLECTIONS = [
    # ========== 研发系专属 (2 Dev) ==========
    {
        "name": "dev_shared_patterns",
        "description": "研发代码模式、最佳实践、重构经验",
        "vector_size": 384,
        "indexes": ["project_id", "pattern_type", "dev_agent", "language", "tags"],
        "access": ["dev-engineer-qwen", "dev-engineer-glm"]
    },
    {
        "name": "dev_shared_code_reviews",
        "description": "代码审查记录、常见问题、修复方案",
        "vector_size": 384,
        "indexes": ["project_id", "review_type", "dev_agent", "severity", "created_at"],
        "access": ["dev-engineer-qwen", "dev-engineer-glm"]
    },
    {
        "name": "dev_shared_api_implementations",
        "description": "API 实现细节、接口对齐记录",
        "vector_size": 384,
        "indexes": ["project_id", "api_path", "dev_agent", "status", "tags"],
        "access": ["dev-engineer-qwen", "dev-engineer-glm"]
    },
    
    # ========== 设计系专属 (2 UI) ==========
    {
        "name": "ui_shared_design_tokens",
        "description": "设计令牌、颜色方案、字体配对",
        "vector_size": 384,
        "indexes": ["project_id", "token_type", "ui_agent", "category", "tags"],
        "access": ["ui-ux-designer-qwen", "ui-ux-designer-kimi"]
    },
    {
        "name": "ui_shared_prototypes",
        "description": "交互原型、用户旅程、状态流转",
        "vector_size": 384,
        "indexes": ["project_id", "prototype_type", "ui_agent", "user_flow", "tags"],
        "access": ["ui-ux-designer-qwen", "ui-ux-designer-kimi"]
    },
    {
        "name": "ui_shared_design_reviews",
        "description": "设计评审记录、反馈、修改方案",
        "vector_size": 384,
        "indexes": ["project_id", "review_type", "ui_agent", "feedback_type", "created_at"],
        "access": ["ui-ux-designer-qwen", "ui-ux-designer-kimi"]
    },
    
    # ========== 架构师 + 技术负责人专属 ==========
    {
        "name": "arch_tech_shared_decisions",
        "description": "架构决策记录 (ADR)、技术选型、权衡分析",
        "vector_size": 384,
        "indexes": ["project_id", "decision_type", "agent", "impact_level", "created_at"],
        "access": ["architect", "tech-leader"]
    },
    {
        "name": "arch_tech_shared_security",
        "description": "安全评审记录、威胁模型、安全基线",
        "vector_size": 384,
        "indexes": ["project_id", "security_type", "agent", "risk_level", "tags"],
        "access": ["architect", "tech-leader"]
    },
    {
        "name": "arch_tech_shared_contracts",
        "description": "API 契约、数据模型、接口规范",
        "vector_size": 384,
        "indexes": ["project_id", "contract_type", "agent", "service", "version"],
        "access": ["architect", "tech-leader"]
    },
    
    # ========== QA 专属 ==========
    {
        "name": "qa_shared_test_cases",
        "description": "测试用例库、AC 追溯矩阵",
        "vector_size": 384,
        "indexes": ["project_id", "test_type", "ac_id", "priority", "tags"],
        "access": ["qa-engineer"]
    },
    {
        "name": "qa_shared_bug_reports",
        "description": "Bug 报告、复现步骤、修复验证",
        "vector_size": 384,
        "indexes": ["project_id", "bug_severity", "module", "status", "created_at"],
        "access": ["qa-engineer"]
    },
    {
        "name": "qa_shared_quality_gates",
        "description": "质量门禁检查清单、通过记录",
        "vector_size": 384,
        "indexes": ["project_id", "gate_name", "status", "agent", "created_at"],
        "access": ["qa-engineer"]
    },
    
    # ========== DevOps 专属 ==========
    {
        "name": "devops_shared_infra",
        "description": "基础设施配置、IaC 模板、部署拓扑",
        "vector_size": 384,
        "indexes": ["project_id", "infra_type", "environment", "agent", "tags"],
        "access": ["devops-engineer"]
    },
    {
        "name": "devops_shared_pipelines",
        "description": "CI/CD 流水线配置、构建记录、发布历史",
        "vector_size": 384,
        "indexes": ["project_id", "pipeline_type", "status", "agent", "created_at"],
        "access": ["devops-engineer"]
    },
    {
        "name": "devops_shared_monitoring",
        "description": "监控配置、告警规则、SLO/SLI",
        "vector_size": 384,
        "indexes": ["project_id", "monitor_type", "service", "threshold", "tags"],
        "access": ["devops-engineer"]
    },
    
    # ========== 项目经理专属 ==========
    {
        "name": "pm_mgr_shared_milestones",
        "description": "里程碑跟踪、进度记录、交付物",
        "vector_size": 384,
        "indexes": ["project_id", "milestone_name", "status", "due_date", "owner"],
        "access": ["project-manager"]
    },
    {
        "name": "pm_mgr_shared_risks",
        "description": "风险登记册、风险缓解计划",
        "vector_size": 384,
        "indexes": ["project_id", "risk_type", "severity", "status", "owner"],
        "access": ["project-manager"]
    },
    {
        "name": "pm_mgr_shared_stakeholders",
        "description": "干系人信息、沟通记录、期望管理",
        "vector_size": 384,
        "indexes": ["project_id", "stakeholder_type", "influence_level", "tags"],
        "access": ["project-manager"]
    },
]

def create_collections():
    """创建所有角色专属集合"""
    client = QdrantClient(host=QDRANT_HOST, port=QDRANT_PORT)
    
    print(f"🔗 连接到 Qdrant ({QDRANT_HOST}:{QDRANT_PORT})...")
    print()
    
    stats = {"created": 0, "exists": 0, "failed": 0}
    
    for collection in ROLE_COLLECTIONS:
        collection_name = collection["name"]
        vector_size = collection["vector_size"]
        
        try:
            # 检查集合是否已存在
            existing_collections = client.get_collections().collections
            if any(c.name == collection_name for c in existing_collections):
                print(f"⚠️  集合 '{collection_name}' 已存在，跳过创建")
                stats["exists"] += 1
                continue
            
            # 创建集合
            client.create_collection(
                collection_name=collection_name,
                vectors_config=models.VectorParams(
                    size=vector_size,
                    distance=models.Distance.COSINE
                ),
            )
            print(f"✅ 集合 '{collection_name}' 创建成功")
            stats["created"] += 1
            
            # 创建 payload 索引
            for field_name in collection["indexes"]:
                client.create_payload_index(
                    collection_name=collection_name,
                    field_name=field_name,
                    field_schema=models.PayloadSchemaType.KEYWORD
                )
                print(f"   └─ 索引 '{field_name}' 创建成功")
            
            # 打印访问权限
            access_list = ", ".join(collection["access"])
            print(f"   └─ 访问权限：{access_list}")
            
        except Exception as e:
            print(f"❌ 集合 '{collection_name}' 创建失败：{e}")
            stats["failed"] += 1
    
    print()
    print("="*60)
    print(f"📊 角色专属集合创建完成!")
    print(f"   新建：{stats['created']} 个")
    print(f"   已存在：{stats['exists']} 个")
    print(f"   失败：{stats['failed']} 个")
    print("="*60)

def test_collections():
    """测试集合是否可用"""
    client = QdrantClient(host=QDRANT_HOST, port=QDRANT_PORT)
    
    print("\n🧪 测试集合可用性...")
    print()
    
    # 按角色分组显示
    roles = {
        "研发系 (2 Dev)": ["dev_shared_patterns", "dev_shared_code_reviews", "dev_shared_api_implementations"],
        "设计系 (2 UI)": ["ui_shared_design_tokens", "ui_shared_prototypes", "ui_shared_design_reviews"],
        "架构 + 技术": ["arch_tech_shared_decisions", "arch_tech_shared_security", "arch_tech_shared_contracts"],
        "QA": ["qa_shared_test_cases", "qa_shared_bug_reports", "qa_shared_quality_gates"],
        "DevOps": ["devops_shared_infra", "devops_shared_pipelines", "devops_shared_monitoring"],
        "项目经理": ["pm_mgr_shared_milestones", "pm_mgr_shared_risks", "pm_mgr_shared_stakeholders"],
    }
    
    for role_name, collection_names in roles.items():
        print(f"📁 {role_name}")
        for collection_name in collection_names:
            try:
                info = client.get_collection(collection_name)
                print(f"   ✅ '{collection_name}': {info.points_count} 条记录")
            except Exception as e:
                print(f"   ❌ '{collection_name}': {e}")
        print()

def print_summary():
    """打印完整总结"""
    print("="*60)
    print("🧠 角色专属共享记忆配置总结")
    print("="*60)
    print()
    
    # 按角色分组打印
    roles = {
        "研发系 (2 Dev)": {
            "collections": ["dev_shared_patterns", "dev_shared_code_reviews", "dev_shared_api_implementations"],
            "agents": ["dev-engineer-qwen", "dev-engineer-glm"],
            "purpose": "代码模式、审查记录、API 实现对齐"
        },
        "设计系 (2 UI)": {
            "collections": ["ui_shared_design_tokens", "ui_shared_prototypes", "ui_shared_design_reviews"],
            "agents": ["ui-ux-designer-qwen", "ui-ux-designer-kimi"],
            "purpose": "设计令牌、交互原型、评审反馈"
        },
        "架构 + 技术": {
            "collections": ["arch_tech_shared_decisions", "arch_tech_shared_security", "arch_tech_shared_contracts"],
            "agents": ["architect", "tech-leader"],
            "purpose": "架构决策、安全评审、API 契约"
        },
        "QA": {
            "collections": ["qa_shared_test_cases", "qa_shared_bug_reports", "qa_shared_quality_gates"],
            "agents": ["qa-engineer"],
            "purpose": "测试用例、Bug 跟踪、质量门禁"
        },
        "DevOps": {
            "collections": ["devops_shared_infra", "devops_shared_pipelines", "devops_shared_monitoring"],
            "agents": ["devops-engineer"],
            "purpose": "基础设施、CI/CD、监控告警"
        },
        "项目经理": {
            "collections": ["pm_mgr_shared_milestones", "pm_mgr_shared_risks", "pm_mgr_shared_stakeholders"],
            "agents": ["project-manager"],
            "purpose": "里程碑跟踪、风险管理、干系人"
        },
        "产品经理 (3 PM)": {
            "collections": ["pm_shared_decisions", "pm_shared_research", "pm_shared_prd_templates"],
            "agents": ["product-manager-qwen", "product-manager-glm", "product-manager-kimi"],
            "purpose": "产品决策、用户研究、PRD 模板 (已存在)"
        },
        "商业团队": {
            "collections": ["claw-team-memos"],
            "agents": ["strategist", "scout", "analyst"],
            "purpose": "情报简报、数据报告、战略报告 (已存在)"
        },
    }
    
    for role_name, info in roles.items():
        print(f"📌 {role_name}")
        print(f"   智能体：{', '.join(info['agents'])}")
        print(f"   用途：{info['purpose']}")
        print(f"   集合:")
        for col in info["collections"]:
            print(f"     - {col}")
        print()
    
    print("="*60)
    print("✅ 所有角色专属记忆配置完成!")
    print("="*60)

if __name__ == "__main__":
    print("="*60)
    print("🧠 创建角色专属共享记忆集合")
    print("="*60)
    print()
    
    create_collections()
    test_collections()
    print_summary()
    
    print("\n" + "="*60)
    print("🎉 全部设置完成!")
    print("="*60)
