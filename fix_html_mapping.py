import re

html_file = 'index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

mapping = {
    'view-617-623': '10.png',
    'view-574-423': '11.png',
    'view-725-313': '1d.png',
    'view-830-435': '2w.png',
    'view-1061-276': '2y.png',
    'view-1026-391': '3.png',
    'view-1221-238': '5y.png',
    'view-1178-361': '6.png',
    'view-1235-552': '8.png',
    'view-1027-623': '9.png'
}

# Clear all placeholder-views first (except mobile-view)
views_to_clear = [
    'view-725-313', 'view-574-423', 'view-830-435', 'view-617-623',
    'view-1026-391', 'view-1027-623', 'view-1061-276', 'view-1221-238',
    'view-1178-361', 'view-1030-384', 'view-1235-552', 'view-1150-450'
]

for view_id in views_to_clear:
    # Pattern to match <div class="placeholder-view" id="view_id"> ... </div>
    pattern = r'(<div class="placeholder-view" id="' + view_id + r'">)(.*?)(</div>)'
    
    if view_id in mapping:
        img_name = mapping[view_id]
        replacement = f'\\1\n    <img src="{img_name}" class="story-image" alt="{img_name}">\n  \\3'
        content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    else:
        # Restore dummy text for those without a matching image
        width, height = view_id.replace('view-', '').split('-')
        replacement = f'\\1\n    {width} x {height} 환경\n    <span>준비된 레이아웃이 여기에</span>\n  \\3'
        content = re.sub(pattern, replacement, content, flags=re.DOTALL)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated index.html")
