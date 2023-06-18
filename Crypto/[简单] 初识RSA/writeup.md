# [简单] 初识RSA

## 解题思路

> 下载附件,得到一个python文件,开始分析代码,代码逻辑很简单

```
n = p * q
pq = p * q - p
pq = n - p
p = n - pq

qp = p * q - q
qp = n - q
q = n - qp
```

> 求出p后根据n求出q,最后就可以解出m

## flag

> flag{719014b3-c4e1-4f81-a7be-b4f0d65c9e10}