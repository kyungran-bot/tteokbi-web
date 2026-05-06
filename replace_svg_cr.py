with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(
    '<img src="0month!.svg" class="mobile-svg-graphic" alt="Broken tailbone graphic">',
    '<img src="cr.png" class="mobile-cr-graphic" alt="Broken tailbone graphic">'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("index.html updated")
