import re

with open('us copy.svg', 'r', encoding='utf-8') as f:
    svg_content = f.read()

svg_content = svg_content.replace('<?xml version="1.0" encoding="UTF-8"?>\n', '')
svg_content = svg_content.replace('id="bubblewand"', 'id="us-svg"')

with open('index.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

pattern = re.compile(r'<svg id="us-svg".*?</svg>', re.DOTALL)
new_html_content = pattern.sub(svg_content.strip(), html_content, count=1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html_content)

print("SVG replaced successfully.")
