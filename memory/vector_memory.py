#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ChromaDB 向量库记忆系统
本地轻量级向量存储，支持语义搜索
"""

import hashlib
import os
from datetime import datetime

import chromadb
from chromadb.config import Settings

# 配置
MEMORY_DIR = os.path.dirname(os.path.abspath(__file__))
CHROMA_DIR = os.path.join(MEMORY_DIR, "chroma_db")


class VectorMemory:
    """向量记忆管理类"""

    def __init__(self, collection_name="memories"):
        """初始化 ChromaDB 客户端"""
        # 创建持久化客户端
        self.client = chromadb.PersistentClient(path=CHROMA_DIR)

        # 获取或创建集合
        self.collection = self.client.get_or_create_collection(
            name=collection_name, metadata={"description": "用户记忆存储", "hnsw:space": "cosine"}
        )

    def add_memory(self, text: str, category: str = "general", metadata: dict = None):
        """
        添加记忆到向量库

        Args:
            text: 记忆文本内容
            category: 分类标签 (general, work, personal, etc.)
            metadata: 额外元数据
        """
        # 生成唯一 ID
        memory_id = hashlib.md5(f"{text}{datetime.now().isoformat()}".encode()).hexdigest()[:16]

        # 准备元数据
        mem_metadata = {
            "category": category,
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat(),
        }
        if metadata:
            mem_metadata.update(metadata)

        # 添加到集合
        self.collection.add(documents=[text], metadatas=[mem_metadata], ids=[memory_id])

        return memory_id

    def search_memories(self, query: str, n_results: int = 5, category: str = None):
        """
        搜索相关记忆

        Args:
            query: 搜索查询
            n_results: 返回结果数量
            category: 可选的分类过滤

        Returns:
            匹配的记忆列表
        """
        where_filter = None
        if category:
            where_filter = {"category": category}

        results = self.collection.query(
            query_texts=[query],
            n_results=n_results,
            where=where_filter,
            include=["documents", "metadatas", "distances"],
        )

        # 格式化结果
        memories = []
        if results["documents"] and results["documents"][0]:
            for i, doc in enumerate(results["documents"][0]):
                memory = {
                    "id": results["ids"][0][i],
                    "content": doc,
                    "metadata": results["metadatas"][0][i],
                    "distance": results["distances"][0][i] if results["distances"] else None,
                }
                memories.append(memory)

        return memories

    def delete_memory(self, memory_id: str):
        """删除指定记忆"""
        self.collection.delete(ids=[memory_id])

    def get_all_memories(self, category: str = None):
        """获取所有记忆"""
        where_filter = None
        if category:
            where_filter = {"category": category}

        results = self.collection.get(where=where_filter, include=["documents", "metadatas"])

        memories = []
        if results["documents"]:
            for i, doc in enumerate(results["documents"]):
                memory = {"id": results["ids"][i], "content": doc, "metadata": results["metadatas"][i]}
                memories.append(memory)

        return memories

    def get_stats(self):
        """获取记忆库统计信息"""
        count = self.collection.count()
        return {"total_memories": count, "chroma_dir": CHROMA_DIR}

    def export_memories(self, output_path: str):
        """导出所有记忆到 JSON 文件"""
        import json

        memories = self.get_all_memories()
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(memories, f, ensure_ascii=False, indent=2)
        return output_path


def demo():
    """演示用法"""
    print("🧠 ChromaDB 向量记忆系统演示\n")

    # 初始化
    memory = VectorMemory()

    # 添加示例记忆
    print("📝 添加示例记忆...")
    memory.add_memory(
        "用户吴飞持有腾讯控股、阿里巴巴、小米集团等港股，总仓位约 81%",
        category="investment",
        metadata={"tags": ["股票", "港股", "持仓"]},
    )
    memory.add_memory(
        "用户偏好 HTML 格式的晨间投顾报告，发送至 wufei81@126.com",
        category="preference",
        metadata={"tags": ["邮件", "报告", "偏好"]},
    )
    memory.add_memory(
        "每个交易日 09:00 AM 自动生成晨间投顾报告", category="schedule", metadata={"tags": ["定时任务", "报告"]}
    )

    # 搜索记忆
    print("\n🔍 搜索'投资'相关记忆...")
    results = memory.search_memories("投资", n_results=3)
    for r in results:
        print(f"  - {r['content'][:50]}... (距离：{r['distance']:.4f})")

    # 统计信息
    print("\n📊 记忆库统计:")
    stats = memory.get_stats()
    print(f"  总记忆数：{stats['total_memories']}")
    print(f"  存储路径：{stats['chroma_dir']}")

    print("\n✅ 演示完成!")


if __name__ == "__main__":
    demo()
