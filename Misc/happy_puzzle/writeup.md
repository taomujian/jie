# Happy_puzzle

## 解题思路

> 下载附件得到一个txt文本和26个data文件.

> 根据txt文本可知出题人考察的是让我们构建一个RGB、400x400的PNG图片,图片里面26个IDAT结构.

> IDAT结构：

```
IDAT_DATA的长度 + IDAT + IDAT_DATA + CRC32,CRC32 = IDAT + IDAT_DATA
```

> 文件头 + IHDR结构：

```
89 50 4E 47 0D 0A 1A 0A + 00 00 00 0D + IHDR + IM_WIDTH + IM_HEIGHT + Bits + color_type + compr_method + filter_method + interlace_method + CRC32 

CRC32 = IHDR + IM_WIDTH + IM_HEIGHT + Bits + color_type + compr_method + filter_method + interlace_method

IEND结构：00 00 00 00 49 45 4E 44 AE 42 60 82
```

> 关于IDAT层的顺序问题,如果你拼对了一层,就会得到正确的图片,直接爆破不太可能,次数太多了

> 文件大小最小的那个肯定是末尾的IDAT了,因为IDAT必须要满了才会开始一下个IDAT,这个明显就是末尾的IDAT了.

> 攻防世界设置错了,设置成了：unctf{312bbd92c1b891e1827ba519326b6688}

## flag

> unctf{312bbd92c1b291e1827ba519326b6688}
