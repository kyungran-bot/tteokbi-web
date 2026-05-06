images = {
    '10.png': (2576, 2576),
    '11.png': (2392, 1764),
    '1d.png': (3022, 1305),
    '2w.png': (3459, 1804),
    '2y.png': (4422, 1150),
    '3.png': (4276, 1630),
    '5y.png': (5089, 993),
    '6.png': (4894, 1505),
    '8.png': (5146, 2294),
    '9.png': (4280, 2597)
}

views = [
    (725, 313), (574, 423), (830, 435), (617, 623),
    (1026, 391), (1027, 623), (1061, 276), (1221, 238),
    (1178, 361), (1030, 384), (1235, 552), (1150, 450)
]

for img, (iw, ih) in images.items():
    img_ratio = iw / ih
    best_view = None
    best_diff = float('inf')
    for (vw, vh) in views:
        view_ratio = vw / vh
        diff = abs(img_ratio - view_ratio)
        if diff < best_diff:
            best_diff = diff
            best_view = (vw, vh)
    print(f"{img} -> view-{best_view[0]}-{best_view[1]} (img ratio: {img_ratio:.3f}, view ratio: {(best_view[0]/best_view[1]):.3f})")

