# Special-rsa

## 解题思路

> 下载附件,得到一个py文件

> 根据加密的算法,明文比分成两部分进行加密。

```
c1 = (k ^ r1 mod N) * m1 mod N
c2 = (k ^ r2 mod N) * m2 mod N
```

> 其中c1,c2,m1,m2,r1,r2,N全都为已知量

> 从以上分析可知,只要获取到加密算法中用到的密钥K,就可以对flag的密文进行还原。

```
k^r1 mod N = c1/m1 mod N
k^r2 mod N = c2/m2 mod N
```

> 由于r1,r2互素(用gcd看),根据扩展欧几里得egcd定理,有

```
g, a, b = egcd(r1, r2),其中g=1(r1和r2是互素的)
且 a, b 满足
a * r1 + b * r2 = 1
```

> 可以算出来 a, b,但是算出来b是负的,就没法用pow()函数算了,所以要自己重新写一个函数

> 检验一下

```
(k^r1)^a * (k^r2)^b = k^(a*r1 + b*r2) = k^1 = k
k = ((c1 * m1^-1 mod N) ^ a mod N) * ((c2 * m2^-1 mod N) ^ b mod N)
```

> 得到k以后,带入原解密函数解开flag即可

## flag

> BCTF{q0000000000b3333333333-ju57-w0n-pwn20wn!!!!!!!!!!!!}