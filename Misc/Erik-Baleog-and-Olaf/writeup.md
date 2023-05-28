# Erik-Baleog-and-Olaf

## 解题思路

> 用010 Editor打开图片,发现开头是PNG格式,修改文件为PNG格式,得到一张图片.在文件最后面发现一个提示,去下载一个图片,比较2个图片得到一个新图片,是一个二维码,扫描得到flag

## payload

```
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
```

## flag

> flag{#justdiffit}

## 参考

> https://jie.2weima.com