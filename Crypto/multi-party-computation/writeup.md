# Multi-party-computation

## 解题思路

> 下载附件,得到一个python文件,完全看不懂,越来越难了

> 这是一个两方的隐私集合交集协议的实现,其中使用了Paillier公钥密码系统.发送公钥和多项式,服务端评估多项式,做一些计算.(令`f(x)`为多项式,一些计算的定义如下`f(secret_value) * random() + secret_value`)

> 发送`0`做为多项式,可以收到一个`secret_value`。

> 因此,flag可解出`FLAG{Monic polynomials FTW}`

## flag

> FLAG{Monic polynomials FTW}