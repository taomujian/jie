# Rsa-2

## 解题思路

> 下载附件,得到一个公钥文件和一个加密后的文件,根据提示发现是用openssl生成的.得到私钥就能解密.

> 读取公钥得到n和e,n用大素数分解在线网站得到p和q,但是最后求d的时候发现报错,2个参数不互素.

> 于是转换思路

```
p = 26440615366395242196516853423447
q = 27038194053540661979045656526063
r = 32581479300404876772405716877547
x^3 mod p = ct mod p = 20827907988103030784078915883129
x^3 mod q = ct mod q = 19342563376936634263836075415482
x^3 mod r = ct mod r = 10525283947807760227880406671000

我们可以求解出三个函数分别对应的x值
```

```
#sagemath
n=26440615366395242196516853423447
c=2485360255306619684345131431867350432205477625621366642887752720125176463993839766742234027524
m=c%n
PR.<x> = PolynomialRing(Zmod(n))
f = x^3-m
x0 = f.roots()
print(x0)
[(13374868592866626517389128266735, 1), (7379361747422713811654086477766, 1), (5686385026105901867473638678946, 1)]
 
 
n=27038194053540661979045656526063
c=2485360255306619684345131431867350432205477625621366642887752720125176463993839766742234027524
m=c%n
PR.<x> = PolynomialRing(Zmod(n))
f = x^3-m
x0 = f.roots()
print(x0)
[(19616973567618515464515107624812, 1)]
 
n=32581479300404876772405716877547
c=2485360255306619684345131431867350432205477625621366642887752720125176463993839766742234027524
m=c%n
PR.<x> = PolynomialRing(Zmod(n))
f = x^3-m
x0 = f.roots()
print(x0)
[(13404203109409336045283549715377, 1), (13028011585706956936052628027629, 1), (6149264605288583791069539134541, 1)]
```

> 求解出:

```
a=[13374868592866626517389128266735,7379361747422713811654086477766,5686385026105901867473638678946]
b=[19616973567618515464515107624812]
c=[13404203109409336045283549715377,13028011585706956936052628027629,6149264605288583791069539134541]
```

> 可以看到有3*1*3=9，也就是说有9种情况需要我们来讨论（使用中国剩余定理）

```
for x in a:
    for y in b:
        for z in c:
            m = crt(p1,p2,p3,x, y, z)
            m=long_to_bytes(m)
            if b'ctf{' in m:
                print(m)
                break
```

> 最后sage运行flag.py得到flag

## flag

> 0ctf{HahA!Thi5_1s_n0T_rSa~}

## 参考

> https://www.ssleye.com/ssltool/pub_asysi.html
