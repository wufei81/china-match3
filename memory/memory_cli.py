#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
向量记忆命令行工具
支持添加、搜索、管理记忆
"""

import argparse
import sys
import json
from vector_memory import VectorMemory

def cmd_add(args):
    """添加记忆"""
    memory = VectorMemory()
    memory_id = memory.add_memory(
        text=args.text,
        category=args.category,
        metadata={"tags": args.tags.split(",") if args.tags else []}
    )
    print(f"✅ 记忆已添加")
    print(f"   ID: {memory_id}")
    print(f"   分类：{args.category}")
    print(f"   内容：{args.text[:60]}...")

def cmd_search(args):
    """搜索记忆"""
    memory = VectorMemory()
    results = memory.search_memories(
        query=args.query,
        n_results=args.limit,
        category=args.category
    )
    
    if not results:
        print("❌ 未找到相关记忆")
        return
    
    print(f"🔍 找到 {len(results)} 条相关记忆:\n")
    for i, r in enumerate(results, 1):
        similarity = (1 - r['distance']) * 100 if r['distance'] else 0
        print(f"{i}. [{r['metadata'].get('category', 'general')}] {r['content']}")
        print(f"   相似度：{similarity:.1f}% | 时间：{r['metadata'].get('created_at', 'N/A')[:10]}")
        if r['metadata'].get('tags'):
            print(f"   标签：{', '.join(r['metadata']['tags'])}")
        print()

def cmd_list(args):
    """列出所有记忆"""
    memory = VectorMemory()
    memories = memory.get_all_memories(category=args.category)
    
    if not memories:
        print("❌ 暂无记忆")
        return
    
    print(f"📚 共 {len(memories)} 条记忆:\n")
    for i, m in enumerate(memories, 1):
        print(f"{i}. [{m['metadata'].get('category', 'general')}] {m['content'][:50]}...")
        print(f"   ID: {m['id']} | 时间：{m['metadata'].get('created_at', 'N/A')[:10]}")
        print()

def cmd_stats(args):
    """显示统计信息"""
    memory = VectorMemory()
    stats = memory.get_stats()
    
    print("📊 向量记忆库统计")
    print(f"   总记忆数：{stats['total_memories']}")
    print(f"   存储路径：{stats['chroma_dir']}")

def cmd_export(args):
    """导出记忆"""
    memory = VectorMemory()
    output_path = memory.export_memories(args.output)
    print(f"✅ 记忆已导出到：{output_path}")

def cmd_delete(args):
    """删除记忆"""
    memory = VectorMemory()
    memory.delete_memory(args.id)
    print(f"✅ 记忆已删除：{args.id}")

def main():
    parser = argparse.ArgumentParser(description="🧠 向量记忆管理工具")
    subparsers = parser.add_subparsers(dest='command', help='命令')
    
    # add 命令
    add_parser = subparsers.add_parser('add', help='添加记忆')
    add_parser.add_argument('text', help='记忆内容')
    add_parser.add_argument('-c', '--category', default='general', help='分类 (默认：general)')
    add_parser.add_argument('-t', '--tags', help='标签 (逗号分隔)')
    add_parser.set_defaults(func=cmd_add)
    
    # search 命令
    search_parser = subparsers.add_parser('search', help='搜索记忆')
    search_parser.add_argument('query', help='搜索查询')
    search_parser.add_argument('-n', '--limit', type=int, default=5, help='结果数量 (默认：5)')
    search_parser.add_argument('-c', '--category', help='分类过滤')
    search_parser.set_defaults(func=cmd_search)
    
    # list 命令
    list_parser = subparsers.add_parser('list', help='列出所有记忆')
    list_parser.add_argument('-c', '--category', help='分类过滤')
    list_parser.set_defaults(func=cmd_list)
    
    # stats 命令
    stats_parser = subparsers.add_parser('stats', help='显示统计')
    stats_parser.set_defaults(func=cmd_stats)
    
    # export 命令
    export_parser = subparsers.add_parser('export', help='导出记忆')
    export_parser.add_argument('output', help='输出文件路径')
    export_parser.set_defaults(func=cmd_export)
    
    # delete 命令
    delete_parser = subparsers.add_parser('delete', help='删除记忆')
    delete_parser.add_argument('id', help='记忆 ID')
    delete_parser.set_defaults(func=cmd_delete)
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        sys.exit(1)
    
    args.func(args)

if __name__ == "__main__":
    main()
