# Picture2

## 解题思路

> 下载附件,是一张图片,用foremost分离图片失败,binwalk -e得到一个文件,得到一串base64编码,解码后发现前2个字符是kp,修改为pk,后缀修改为.zip,解压需要密码,winrar打开,右边有提示,解压密码为integer division or modulo by zero,解压后得到一串字符,这是UUencode,解码得到flag.

> 果然是存在LSB隐写的,在red0、green0、blue0可以看到第一行都是存在数据的

> Data Extract功能提取一下,但是发现内容并不是明文字符串,也不是什么常见文件的十六进制

> 这是LSB隐写,用工具可以解密,解密后得到PVSF{vVckHejqBOVX9C1c13GFfkHJrjIQeMwf}

> 可以看出这个应该就是flag的变形,采用了置换加密.因为密文VSF的间隔与CTF对不上,所以应该是采用的有密码的置换加密.因为题目和提示是keyword,所以想到是Nihilist 密码（又称关键字密码）,直接找个在线解密网站解密一下.得到flag

## flag

> CISCN{2388AF2893EB85EB1B439ABFF617319F}

## 参考

> https://www.qqxiuzi.cn/bianma/uuencode.php
