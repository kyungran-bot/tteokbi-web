with open('style.css', 'r', encoding='utf-8') as f:
    content = f.read()

marker = '/* =========================================\n   추가 40개 별도 화면 좌표 구간'
pos = content.find(marker)
if pos != -1:
    new_content = content[:pos]
    with open('style.css', 'w', encoding='utf-8') as f:
        f.write(new_content.rstrip() + '\n')
    print("Deleted 40 points css.")
else:
    print("Marker not found.")
