# cr4-poor-rsa

## 解题思路

> 下载附件,得到一个文件夹,里面有2个文件,key.pub和flag.b64

> 原理很简单,先通过分析公钥得到n和e,大整数在www.factordb.com分解大整数,得到了p和q.有了p,q,求得解密私钥.

> 得到私钥m后,对flag.b64文件解密得到flag

## flag

> ALEXCTF{SMALL_PRIMES_ARE_BAD}
