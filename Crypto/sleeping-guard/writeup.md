# Sleeping-guard

## 解题思路

> 连接给出的ip端口,得到一大串字符.题目说是要看到图片,base64解码得到乱码,没看到png头.

> 猜测是加png整张图片加密了,对比png头部,就有了密文和明文,应该是是异或加密.用png头部信息和密文得到异或所用到的key,解密整张图片,得到flag.

## flag

> flag{l4zy_H4CK3rs_d0nt_g3T_MAg1C_FlaG5}

## 参考

> https://blog.csdn.net/zgzhzywzd/article/details/123390548