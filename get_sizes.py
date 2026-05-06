import struct, imghdr, glob

def get_image_size(fname):
    try:
        with open(fname, 'rb') as f:
            head = f.read(24)
            if len(head) != 24: return None
            if imghdr.what(fname) == 'png':
                check = struct.unpack('>i', head[4:8])[0]
                if check != 0x0d0a1a0a: return None
                width, height = struct.unpack('>ii', head[16:24])
                return (width, height)
    except: return None

for img in sorted(glob.glob('*.png')):
    if img not in ['cr.png', 'us.png', '2014.11.01.png']:
        size = get_image_size(img)
        print(f'{img}: {size}')
