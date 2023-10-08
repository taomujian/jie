# BabyRSA1

## 解题思路

> 下载附件,得到一些文件.

> 看来n这是GF(2)上的PolynomialRing的多项式.加密基本上将消息更改为GF(2^2049)的元素,然后将其表示为环P的元素,然后将该消息的多项式表示形式提高为emod多项式的幂n.

> 所以,可以归结为经典的RSA,与小搓那m和n现在是多项式,一切都在PolynomialRing在GF(2)calcualted.

> 发现了一篇很好的论文,描述了这个想法：http : //www.diva-portal.se/smash/get/diva2 : 823505/FULLTEXT01.pdf(Izabela Beatrice Gafitoiu的理学学士学位论文).

> 如果遵循此论点,会发现在这种情况下,d解密指数可以计算为emod的模乘逆s.特殊值s是等效的phi,从经典RSA,并且基本上是(2^p_d-1)(2^q_d-1)其中p_d和q_d正度多项式的p和q,使得p*q == n.

> 这个想法很简单：

```
1、因子多项式n成p和q
2、计算 s
3、计算 d
4、解密标志
```

## flag

> flag{P1ea5e_k33p_N_as_A_inTegeR~~~~~~}