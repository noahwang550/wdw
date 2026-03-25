#!/usr/bin/env python3
"""
Memory Screen Server
Serves the memory screen interface with real-time memory data
"""

import http.server
import socketserver
import json
import os
from pathlib import Path
from datetime import datetime

PORT = 8000
MEMORY_DIR = Path('/root/.openclaw/workspace-feishu-assistant/memory')
MAIN_MEMORY = Path('/root/.openclaw/workspace-feishu-assistant/MEMORY.md')

class MemoryHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/api/memories':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            memories = load_memories()
            self.wfile.write(json.dumps(memories, ensure_ascii=False).encode())
        else:
            super().do_GET()
    
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

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
            'content': content[:5000]  # First 5000 chars
        })
    
    # Load daily memories
    for file in sorted(MEMORY_DIR.glob('*.md'), reverse=True):
        if file.name.startswith('2026-'):
            content = file.read_text(encoding='utf-8')
            date = file.stem
            memories.append({
                'file': file.name,
                'title': f'📝 {date}',
                'date': date,
                'tags': ['日常记录', '记忆'],
                'preview': extract_preview(content, 200),
                'content': content[:5000]
            })
    
    # Load special files
    for file in MEMORY_DIR.glob('*.md'):
        if file.name not in ['飞书官方插件使用指南.md'] and not file.name.startswith('2026-'):
            content = file.read_text(encoding='utf-8')
            memories.append({
                'file': file.name,
                'title': f'📄 {file.stem}',
                'date': datetime.fromtimestamp(file.stat().st_mtime).strftime('%Y-%m-%d'),
                'tags': ['文档', '指南'],
                'preview': extract_preview(content, 200),
                'content': content[:5000]
            })
    
    return memories

def extract_preview(content, length=200):
    lines = content.split('\n')
    preview_lines = []
    for line in lines:
        if line.strip() and not line.startswith('#'):
            preview_lines.append(line.strip())
            if len(' '.join(preview_lines)) >= length:
                break
    return ' '.join(preview_lines)[:length] + '...'

if __name__ == '__main__':
    os.chdir(Path('/root/.openclaw/workspace-feishu-assistant/memory-screen'))
    
    with socketserver.TCPServer(("", PORT), MemoryHandler) as httpd:
        print(f"🌸 Memory Screen Server running at http://localhost:{PORT}")
        print(f"📊 API available at http://localhost:{PORT}/api/memories")
        print(f"💾 Serving {len(load_memories())} memories")
        httpd.serve_forever()
