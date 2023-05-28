# Web2

> 把一串加密的字符进行解密,加密算法比较简单,核心内容是把字符串的每个字符的ASII值+1再进行组装编码

## 相关函数

### chr()

> 从不同ASCII值返回字符

### ord()

> 返回字符的ASCII值

### substr(string,start,length)

> 从string的start截取length的字符

### str_rot13()

> str_rot13()函数对字符串执ROT13编码,编码解码是同一个函数

### strrev()

> 反转字符串

## 思路分析

> 把一串加密的字符进行解密,加密算法比较简单,先把字符串反转,取字符串的每个字符的ASII值+1后再转化为字符,再进行组装成字符串,然后base64编码,再反转字符串,最后进行ROT-13编码.

## flag

> flag:{NSCTF_b73d5adfb819c64603d7237fa0d52977}