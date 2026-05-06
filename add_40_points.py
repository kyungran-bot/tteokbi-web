import re

points = """
607x296
600x319
574x343
574x366
574x399
680x296
774x370
798x428
885x408
942x387
1096x418
1168x425
1143x383
1095x331
1033x233
1028x204
1045x166
1218x180
1235x218
1198x224
1184x193
1164x168
1106x165
1130x321
1214x428
1235x482
1190x626
1108x624
945x628
868x629
788x627
713x625
574x621
574x605
574x568
574x587
574x539
616x492
1162x425
574x446
""".strip().split()

html_appends = []
css_appends = ["\n/* =========================================\n   추가 40개 별도 화면 좌표 구간\n========================================= */\n"]

for p in points:
    w, h = map(int, p.split('x'))
    
    html_appends.append(f"""  <div class="placeholder-view" id="view-{w}-{h}">
    {w} x {h} 환경
    <img src="" alt="PNG 이미지 공간" style="max-width: 200px; margin-top: 20px;">
    <span>준비된 레이아웃이 여기에</span>
  </div>""")

    css_appends.append(f"""
/* {w}x{h} */
@media screen and (min-width: {w-8}px) and (max-width: {w+8}px) and (min-height: {h-8}px) and (max-height: {h+8}px) {{
  #desktop-view {{
    display: none;
  }}

  #view-{w}-{h} {{
    display: flex;
  }}
}}""")

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Insert before </body>
insert_pos = content.rfind('</body>')
if insert_pos != -1:
    new_content = content[:insert_pos] + "  <!-- 별도로 추가된 40개의 빈 화면 -->\n" + "\n".join(html_appends) + "\n" + content[insert_pos:]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
else:
    print("</body> not found in index.html")

with open('style.css', 'a', encoding='utf-8') as f:
    f.write("\n".join(css_appends) + "\n")

print("Done appending 40 points.")
