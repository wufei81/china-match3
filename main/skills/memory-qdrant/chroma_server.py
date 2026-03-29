#!/usr/bin/env python3
"""
ChromaDB 本地持久化服务
通过 stdin/stdout 与 Node.js 通信（JSON-RPC 风格）
"""

import sys
import json
import chromadb
from chromadb.config import Settings
import os
from pathlib import Path

# ============================================================================
# 配置
# ============================================================================

DEFAULT_PERSIST_PATH = os.path.expanduser("~/.openclaw/memory/chroma.db")
COLLECTION_NAME = "openclaw_memories"
VECTOR_DIM = 384  # all-MiniLM-L6-v2

# ============================================================================
# ChromaDB 客户端
# ============================================================================

class ChromaServer:
    def __init__(self, persist_path=None):
        self.persist_path = persist_path or DEFAULT_PERSIST_PATH
        self.client = None
        self.collection = None
        self.initialized = False
        
    def initialize(self):
        """初始化 ChromaDB 持久化客户端"""
        if self.initialized:
            return True
            
        try:
            # 确保持久化目录存在
            persist_dir = os.path.dirname(self.persist_path)
            if persist_dir and not os.path.exists(persist_dir):
                os.makedirs(persist_dir, exist_ok=True)
            
            # 创建持久化客户端
            self.client = chromadb.PersistentClient(path=self.persist_path)
            
            # 获取或创建 collection
            try:
                self.collection = self.client.get_collection(name=COLLECTION_NAME)
            except Exception:
                self.collection = self.client.create_collection(
                    name=COLLECTION_NAME,
                    metadata={"hnsw:space": "cosine"}
                )
            
            self.initialized = True
            return True
        except Exception as e:
            self._log_error(f"初始化失败：{e}")
            return False
    
    def _log_error(self, msg):
        """输出错误到 stderr"""
        sys.stderr.write(f"[chroma-server] {msg}\n")
        sys.stderr.flush()
    
    def _log_info(self, msg):
        """输出信息到 stderr"""
        sys.stderr.write(f"[chroma-server] {msg}\n")
        sys.stderr.flush()
    
    def store(self, id, text, vector, category="other", importance=0.7):
        """存储记忆"""
        if not self.initialize():
            return {"success": False, "error": "初始化失败"}
        
        try:
            self.collection.upsert(
                ids=[id],
                embeddings=[vector],
                metadatas=[{
                    "text": text,
                    "category": category,
                    "importance": importance
                }]
            )
            return {"success": True, "id": id}
        except Exception as e:
            self._log_error(f"存储失败：{e}")
            return {"success": False, "error": str(e)}
    
    def search(self, vector, limit=5, min_score=0.3):
        """搜索记忆"""
        if not self.initialize():
            return {"success": False, "error": "初始化失败"}
        
        try:
            results = self.collection.query(
                query_embeddings=[vector],
                n_results=limit,
                include=["metadatas", "distances"]
            )
            
            if not results["ids"] or not results["ids"][0]:
                return {"success": True, "results": [], "count": 0}
            
            # 转换结果
            items = []
            ids = results["ids"][0]
            metadatas = results["metadatas"][0]
            distances = results["distances"][0]
            
            for i, id_ in enumerate(ids):
                distance = distances[i]
                score = 1 - distance  # 余弦距离转相似度
                
                if score >= min_score:
                    metadata = metadatas[i]
                    items.append({
                        "id": id_,
                        "text": metadata.get("text", ""),
                        "category": metadata.get("category", "other"),
                        "importance": metadata.get("importance", 0.7),
                        "score": round(score, 4)
                    })
            
            return {"success": True, "results": items, "count": len(items)}
        except Exception as e:
            self._log_error(f"搜索失败：{e}")
            return {"success": False, "error": str(e)}
    
    def delete(self, id):
        """删除记忆"""
        if not self.initialize():
            return {"success": False, "error": "初始化失败"}
        
        try:
            self.collection.delete(ids=[id])
            return {"success": True}
        except Exception as e:
            self._log_error(f"删除失败：{e}")
            return {"success": False, "error": str(e)}
    
    def count(self):
        """获取记忆数量"""
        if not self.initialize():
            return {"success": False, "error": "初始化失败"}
        
        try:
            count = self.collection.count()
            return {"success": True, "count": count}
        except Exception as e:
            self._log_error(f"计数失败：{e}")
            return {"success": False, "error": str(e)}
    
    def health(self):
        """健康检查"""
        if not self.initialize():
            return {"healthy": False, "error": "初始化失败"}
        
        try:
            count = self.collection.count()
            return {
                "healthy": True,
                "mode": "chromadb",
                "persist_path": self.persist_path,
                "count": count
            }
        except Exception as e:
            return {"healthy": False, "error": str(e)}

# ============================================================================
# 主循环
# ============================================================================

def main():
    server = ChromaServer()
    
    # 启动日志
    server._log_info(f"ChromaDB 服务启动，持久化路径：{server.persist_path}")
    
    # 读取 stdin 命令
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        
        try:
            request = json.loads(line)
            action = request.get("action")
            params = request.get("params", {})
            
            # 路由到对应方法
            if action == "health":
                result = server.health()
            elif action == "store":
                result = server.store(
                    id=params.get("id"),
                    text=params.get("text"),
                    vector=params.get("vector", []),
                    category=params.get("category", "other"),
                    importance=params.get("importance", 0.7)
                )
            elif action == "search":
                result = server.search(
                    vector=params.get("vector", []),
                    limit=params.get("limit", 5),
                    min_score=params.get("min_score", 0.3)
                )
            elif action == "delete":
                result = server.delete(id=params.get("id"))
            elif action == "count":
                result = server.count()
            else:
                result = {"success": False, "error": f"未知动作：{action}"}
            
            # 输出结果到 stdout
            print(json.dumps(result), flush=True)
            
        except json.JSONDecodeError as e:
            error_result = {"success": False, "error": f"JSON 解析错误：{e}"}
            print(json.dumps(error_result), flush=True)
        except Exception as e:
            error_result = {"success": False, "error": f"处理错误：{e}"}
            print(json.dumps(error_result), flush=True)

if __name__ == "__main__":
    main()
