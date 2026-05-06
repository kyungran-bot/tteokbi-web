import re

with open('index.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

pattern = re.compile(r'<svg id="us-svg".*?</svg>', re.DOTALL)
new_html_content = pattern.sub('<img id="us-svg" src="us.png" alt="us">', html_content, count=1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html_content)

print("SVG replaced with us.png successfully.")
