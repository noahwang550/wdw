#!/usr/bin/env python3
"""
生成 memories.json - 从真实记忆文件读取内容
"""

import json
from pathlib import Path
from datetime import datetime

MEMORY_DIR = Path('/root/.openclaw/workspace-feishu-assistant/memory')
MAIN_MEMORY = Path('/root/.openclaw/workspace-feishu-assistant/MEMORY.md')
OUTPUT_FILE = Path('/root/.openclaw/workspace-feishu-assistant/memory-screen/memories.json')

def extract_preview(content, length=200):
    """提取预览文本"""
    lines = content.split('\n')
    preview_lines = []
    for line in lines:
        if line.strip() and not line.startswith('#'):
            preview_lines.append(line.strip())
            if len(' '.join(preview_lines)) >= length:
                break
    return ' '.join(preview_lines)[:length] + '...'

def get_tags(content, filename):
    """根据内容提取标签"""
    tags = ['日常记录']
    if '任务' in content or 'Task' in content:
        tags.append('任务管理')
    if '飞书' in content or '多维表格' in content:
        tags.append('飞书')
    if 'AI' in content or '技能' in content:
        tags.append('AI 工具')
    if '教训' in content or '错误' in content:
        tags.append('经验教训')
    if '配置' in content or '部署' in content:
        tags.append('系统配置')
    return tags

def load_memories():
    memories = []
    
    # Load main MEMORY.md
    if MAIN_MEMORY.exists():
        content = MAIN_MEMORY.read_text(encoding='utf-8')
        memories.append({
            'file': 'MEMORY.md',
            'title': '🌸 长期知识库',
            'date': '持续更新',
            'tags': ['核心方法论', '资源索引', '技术栈', '内部工具'],
            'preview': extract_preview(content, 200),
            'content': content[:15000]  # First 15000 chars
        })
    
    # Load daily memories
    daily_files = sorted([f for f in MEMORY_DIR.glob('*.md') if f.name.startswith('2026-')], reverse=True)
    for file in daily_files:
        content = file.read_text(encoding='utf-8')
        date = file.stem
        memories.append({
            'file': file.name,
            'title': f'📝 {date} 记忆日志',
            'date': date,
            'tags': get_tags(content, file.name),
            'preview': extract_preview(content, 200),
            'content': content[:15000]
        })
    
    return memories

if __name__ == '__main__':
    memories = load_memories()
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(memories, f, ensure_ascii=False, indent=2)
    
    print(f'✅ 生成 memories.json')
    print(f'📚 共 {len(memories)} 条记忆')
    print(f'   - 长期记忆：1 条')
    print(f'   - 日常记忆：{len(memories) - 1} 条')
    print(f'📁 文件位置：{OUTPUT_FILE}')
