# Normal_png

## 解题思路

> 用stegSovle打开文件,没有找到隐写信息.看一下文件format,发现CRC不对.

```
CRC = 36b4f5fd Calculated CRC = fbe7c429
```

> 010 Editor打开图片,然后修改宽的值为40b.


## flag

> flag{B8B68DD7007B1E406F3DF624440D31E0}
