# CoolCat

## 解题思路

> 测试几个小图片发现,服务器总是返回600*600的加密图片(会对小图片进行重复拼接),所以为了方便跟踪前后坐标的变化,尝试把整张图片的值全设为0,0,0,只保留一个像素点的值为255,255,255,然后跟踪这个点的移动情况.

> 构造600x600黑色图片并设置一个白像素点：

```python
from PIL import Image

def generate_image(pos, img_name):
    img = Image.new("RGB", (600, 600), (0, 0, 0))
    img.putpixel(pos, (255, 255, 255))
    img.save(img_name)

def get_point(img_name):
    img = Image.open(img_name)
    width, height = img.size
    dim = width, height = img.size
    pList = []
    for x in range(width):
        for y in range(height):
            if sum(img.getpixel((x, y))) >= 200*3:
                pList.append((x, y))
    return pList

(1, 0) --> (409, 330)
(0, 1) --> (330, 589)
(0, 2) --> (60, 578)
(57, 89) --> (483, 431)
```

> 用得到的这些信息(明文-密文对)对p,q,m进行爆破,得到25组情况(取2-4个点都是同样的25组).

```python
from tqdm import tqdm

def f(start, p, q):
    x, y = start
    nx = (x + y * p) % 600
    ny = (x * q + y * (p * q + 1)) % 600
    return (nx, ny)

def reverse(end, data):
    p, q, m = data
    nx, ny = end
    for _ in range(m):
        x = ((p * q + 1) * nx - p*ny) % 600
        y = (ny - q * nx) % 600
        nx, ny = x, y
    return (nx, ny)

def bf(start, target):
    ans = []
    for p in tqdm(range(600)):
        for q in range(600):
            tmp = start
            for m in range(10):
                tmp = [f(t, p, q) for t in tmp]
                if tmp == target and start == [reverse(e, (p, q, m+1)) for e in target]:
                    print("[+]", p, q, m)
                    ans.append((p, q, m))
    return ans

r = bf([(1, 0), (0, 1), (0, 2), (57, 89)], [(409, 330), (330, 589), (60, 578), (483, 431)])
```

```
[+] p  q  m
[+] 66 66 4
[+] 66 186 4
[+] 66 306 4
[+] 66 426 4
[+] 66 546 4
[+] 186 66 4
[+] 186 186 4
[+] 186 306 4
[+] 186 426 4
[+] 186 546 4
[+] 306 66 4
[+] 306 186 4
[+] 306 306 4
[+] 306 426 4
[+] 306 546 4
[+] 426 66 4
[+] 426 186 4
[+] 426 306 4
[+] 426 426 4
[+] 426 546 4
[+] 546 66 4
[+] 546 186 4
[+] 546 306 4
[+] 546 426 4
[+] 546 546 4
```

> 可以发现m恒为4,p,q有很多组取值情况,反推验证发现这些都是符合条件的.但是尝试了几组p,q,m去解加密的flag图片还是解不出,可能是筛选pqm的样本太少了.

```
p, q, m = 66, 66, 4

def f(pos):
    x, y = pos
    nx = (x + y * p) % 600
    ny = (x * q + y * (p * q + 1)) % 600
    return (nx, ny)

def g(pos):
    x, y = pos
    nx = ((p * q + 1) * x - p * y) % 600
    ny = (y - q * x) % 600
    return (nx, ny)
f0 = (569, 284)
f1 = f(f0)
f2 = f(f1)
f3 = f(f2)
f4 = f(f3)
f5 = f(f4)
(f1,f2,f3,f4,f5)
# ((113, 542), (485, 152), (317, 74), (401, 140), (41, 446))
```

> 测试不同图片格式的时候发现,同样位置的白点,只要格式不一样,返回的图片(jpeg格式)上的白点位置也会不一样,所以有参数发生了变化.列出m不同情况下的569,284偏移量,发现317,74和41,446,分别对应m=3,m=5,所以m发生了变化,这时只需要对m∈[1,5]枚举一下,p q选择66 66,即可解密得到原图.

```
jpg : (569, 284) --> (317, 74)
jpeg: (569, 284) --> (41, 446)
```

## flag

