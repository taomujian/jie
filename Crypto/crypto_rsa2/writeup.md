# Crypto_rsa2

## 解题思路

> 下载附件后,得到一个txt文件,RSA题目,很奇怪,没给任何python文件.直接用网站分解不出N,观察N,发现长度也不是很长,猜测是质数,用python print(isPrime(N)),拿来判断一下,发现确实是质数,这就很好解决了,p,q必然有一个是1,一个是其本身,得到flag.

## flag

> flag{bbe6ef5272d9be08a9a6e452b485aaf6}