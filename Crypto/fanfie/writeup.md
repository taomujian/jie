# Fanfie

## 解题思路

> 下载附件,得到一串加密字符,原题提示有如下：任务描述告诉我们标志被转换为base32并以某种方式加密(攻防世界里没这个提示)

> 假设明文是这样的：BITSCTF{***},那我们尝试将对BITSCTF进行加密

```
from base64 import b32encode

print(b32encode(b'BITSCTF'))
```

> 得到IJEVIU2DKRDA====

> 对比原始字符,我们选取前一段的:

```
MZYVMIWLGBL7CIJO
IJEVIU2DKRDA====
```

> 我们构造一个简单的字母序表:

```
A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z  2  3  4  5  6  7
0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31
```

> 可以发现原始字符和base32加密后的对应索引关系：

```
映射	        编号
M -> I	  12 -> 8
Z -> J	  25 -> 9
Y -> E	  24 -> 4
V -> V	  21 -> 21
I -> U	  8 -> 20
W -> 2	  22 -> 26
```

> 根据题目名字可以推测,学过仿射密码的都知道,并得到a = 13,b = 4, m = 32,仿射函数为y = (13x + 4 ) mod 32

> 使用仿射函数, y = （13 x + 4) mod 32,因此,我们的加密字母表将如下所示：

```
A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z  2  3  4  5  6  7
4 17 30 11 24  5 18 31 12 25  6 19  0 13 26  7 20  1 14 27  8 21  2 15 28  9 22  3 16 29 10 23
E  R  6  L  Y  F  S  7  M  Z  G  T  A  N  2  H  U  B  O  3  I  V  C  P  4  J  W  D  Q  5  K  X
```

> 举例第一列,A在原始字母表中的顺序为0,带入函数(13 * 0 + 4) mod 32 = 4,在原始字母表中,对应字母E,因此原始字符则有如下对应：

```
MZYVMIWLGBL7CIJOGJQVOA3IN5BLYC3NHI -> IJEVIU2DKRDHWUZSKZ4VSMTUN5RDEWTNPU
```

> 再进行base32解密,得到最终答案BITSCTF{S2VyY2tob2Zm}

## flag

> BITSCTF{S2VyY2tob2Zm}

## 参考

> https://blog.csdn.net/l8947943/article/details/123397127

