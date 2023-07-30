# Keyword

## 解题思路

> 下载附件,是一张图片,内容是keyword:lovekfc,应该是什么东西的密码.使用binwalk,没发现什么.查看十六进制,也没有发现什么附加内容.最后使用stegsolve看看是不是存在LSB隐写

> 果然是存在LSB隐写的,在red0、green0、blue0可以看到第一行都是存在数据的

> Data Extract功能提取一下,但是发现内容并不是明文字符串,也不是什么常见文件的十六进制

> 这是LSB隐写,用工具可以解密,解密后得到PVSF{vVckHejqBOVX9C1c13GFfkHJrjIQeMwf}

> 可以看出这个应该就是flag的变形,采用了置换加密.因为密文VSF的间隔与CTF对不上,所以应该是采用的有密码的置换加密.因为题目和提示是keyword,所以想到是Nihilist 密码（又称关键字密码）,直接找个在线解密网站解密一下.得到flag

## flag

> QCTF{cCgeLdnrIBCX9G1g13KFfeLNsnMRdOwf}

## 参考

> https://github.com/livz/cloacked-pixel

> http://www.hiencode.com/keyword.html
