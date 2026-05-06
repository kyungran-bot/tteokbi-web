
import math

placeholders = [
    (607, 296), (600, 319), (574, 343), (574, 366), (574, 399),
    (680, 296), (774, 370), (798, 428), (885, 408), (942, 387),
    (1096, 418), (1168, 425), (1143, 383), (1095, 331), (1033, 233),
    (1028, 204), (1045, 166), (1218, 180), (1235, 218), (1198, 224),
    (1184, 193), (1164, 168), (1106, 165), (1130, 321), (1214, 428),
    (1235, 482), (1190, 626), (1108, 624), (945, 628), (868, 629),
    (788, 627), (713, 625), (574, 621), (574, 605), (574, 568),
    (574, 587), (574, 539), (616, 492), (574, 446)
]

images = [
    ("10_1.png", 2393, 1860),
    ("10_2.png", 2393, 2523),
    ("10_3.png", 2393, 2247),
    ("10_4.png", 2393, 2589),
    ("11_0.png", 2393, 1660),
    ("11_2.png", 2393, 1526),
    ("11_3.png", 2394, 1430),
    ("11_4.png", 2531, 1235),
]

def find_best_match(img_w, img_h):
    img_ratio = img_w / img_h
    best_ph = None
    min_diff = float('inf')
    for ph_w, ph_h in placeholders:
        ph_ratio = ph_w / ph_h
        diff = abs(img_ratio - ph_ratio)
        if diff < min_diff:
            min_diff = diff
            best_ph = (ph_w, ph_h)
    return best_ph

results = []
for name, w, h in images:
    match = find_best_match(w, h)
    results.append((name, match))
    print(f"{name} ({w}x{h}, ratio {w/h:.3f}) matches view-{match[0]}-{match[1]} (ratio {match[0]/match[1]:.3f})")

