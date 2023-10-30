from PIL import Image

def reverse(end, data):
    p, q, m = data
    nx, ny = end
    for _ in range(m):
        x = ((p * q + 1) * nx - p * ny) % 600
        y = (ny - q * nx) % 600
        nx, ny = x, y
    return (nx, ny)

def dec_ACM(img):
    p, q, m = 66, 66, 3
    assert img.size[0] == img.size[1]
    dim = width, height = img.size
    with Image.new(img.mode, dim) as canvas:
        for x in range(width):
            for y in range(height):
                nx, ny = reverse((x, y), (p, q, m))
                canvas.putpixel((nx, ny), img.getpixel((x, y)))
    return canvas

dec_ACM(Image.open("flag_enc.jpg")).save("flag.jpg")