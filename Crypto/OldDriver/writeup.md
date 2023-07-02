# OldDriver 

## 解题思路

> 下载附件,得到一个txt文件,里面有很多c,e,n,是RSA题型.

> 模数n、密文c不同,加密指数e相同,且e很小.符合低加密指数广播攻击.最方便的是调用sympy库里的中国剩余定理,也就是crt(c,n)方法直接可以求出m的e次,然后开方得到m就行了

## flag

> flag{wo0_th3_tr4in_i5_leav1ng_g3t_on_it}

## 参考

> https://www.plexming.com/ctf%E5%AF%86%E7%A0%81%E5%AD%A6rsa%E7%9B%B8%E5%85%B3%E9%A2%98%E7%9B%AE%E8%A7%A3%E9%A2%98%E6%96%B9%E6%B3%95%E4%B8%8Epython%E8%84%9A%E6%9C%AC%E6%80%BB%E7%BB%93%EF%BC%88%E9%99%84%E4%BE%8B%E9%A2%98/