from PIL import Image

for img_name in ['1d.png', '2w.png', '3.png', '2y.png', '5y.png']:
    try:
        with Image.open(img_name) as img:
            img = img.convert('RGB')
            r, g, b = img.getpixel((0, 0))
            # Convert to hex
            print(f"{img_name}: #{r:02x}{g:02x}{b:02x}")
    except Exception as e:
        print(f"Error on {img_name}: {e}")
