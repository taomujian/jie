from PIL import Image

exp = Image.open("22kUrzm.png") # 从winhex中最后一行下载的图片
cipher = Image.open("stego100.png") # 题目给的图片
new = Image.new("RGBA", size=exp.size)
for i in range(640):
    for j in range(480):
        y_p = exp.getpixel((i, j))
        c_p = cipher.getpixel((i, j))
        if y_p == c_p:
            pass
        else:
            new.putpixel((i,j), (255,255,255))
new.save("result.png")