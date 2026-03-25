import sys
from html.parser import HTMLParser

class StructureAnalysis(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        
    def handle_starttag(self, tag, attrs):
        if tag in ('meta', 'link', 'br', 'hr', 'img', 'input', 'path', 'source', 'col'):
            return
        attrs_dict = dict(attrs)
        el_id = attrs_dict.get('id', '')
        cls = attrs_dict.get('class', '')
        self.stack.append({'tag': tag, 'id': el_id, 'class': cls})
        if el_id == 'dashboard-presentation':
            print("Path to dashboard-presentation:")
            for p in self.stack:
                print(f"  {p['tag']}#{p['id']} .{p['class']}")

    def handle_endtag(self, tag):
        if tag in ('meta', 'link', 'br', 'hr', 'img', 'input', 'path', 'source', 'col'):
            return
        if self.stack and self.stack[-1]['tag'] == tag:
            self.stack.pop()
        else:
            # handle unclosed tag mismatches
            for i in range(len(self.stack)-1, -1, -1):
                if self.stack[i]['tag'] == tag:
                    self.stack = self.stack[:i]
                    break

parser = StructureAnalysis()
with open('/home/vinicius2026/Desktop/VDA UL 24 03/index.html', 'r', encoding='utf-8') as f:
    parser.feed(f.read())
