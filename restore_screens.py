
dims = [
    (607, 296), (600, 319), (574, 343), (574, 366), (574, 399),
    (680, 296), (774, 370), (798, 428), (885, 408), (942, 387),
    (1096, 418), (1168, 425), (1143, 383), (1095, 331), (1033, 233),
    (1028, 204), (1045, 166), (1218, 180), (1235, 218), (1198, 224),
    (1184, 193), (1164, 168), (1106, 165), (1130, 321), (1214, 428),
    (1235, 482), (1190, 626), (1108, 624), (945, 628), (868, 629),
    (788, 627), (713, 625), (574, 621), (574, 605), (574, 568),
    (574, 587), (574, 539), (616, 492), (574, 446)
]

# Sort to avoid duplicates and keep order
dims = sorted(list(set(dims)))

print("<!-- RESTORED PLACEHOLDER VIEWS -->")
for w, h in dims:
    print(f'<div class="placeholder-view" id="view-{w}-{h}">\n  {w}x{h} Screen\n  <span>Layout goes here</span>\n</div>')

print("\n\n/* RESTORED MEDIA QUERIES */")
for w, h in dims:
    # Adding a tolerance of +-4px like the user's existing code
    min_w, max_w = w-4, w+4
    min_h, max_h = h-4, h+4
    print(f'@media screen and (min-width: {min_w}px) and (max-width: {max_w}px) and (min-height: {min_h}px) and (max-height: {max_h}px) {{')
    print('  #desktop-view { display: none; }')
    print(f'  #view-{w}-{h} {{ display: flex; }}')
    print('}')
