# FILE_INCLUDE

> 首先可看到这是通过GET传递参数filename进行包含文件并显示的,是文件包含绕过,使用伪协议+编码绕过即可

## 涉及函数

### include

> 从外部引入php文件并执行,如果执行不成功,就返回文件的源码

## PHP文件包含漏洞常用伪协议

```
file:// 访问本地文件系统
http:// 访问http(s）网址
ftp:// 访问ftp
php:// 访问各个输入/输出流
zlib:// 压缩流
data:// 数据
rar:// RAR压缩包
ogg:// 音频流
```

## filters类型

> String Filters: string.rot13、string.toupper、string.tolower、string.strip_tags

> Conversion Filters: convert.base64-encode & convert.base64-decode、convert.quoted-printable-encode & convert.quoted-printable-decode、convert.iconv.*

> Compression Filters: zlib.deflate、zlib.inflate、bzip2.compress和bzip2.decompress

> Encryption Filters: mcrypt.*和 mdecrypt.*

> [官方文档]https://www.php.net/manual/zh/filters.php

> [使用参考](https://blog.csdn.net/qq_44657899/article/details/109300335)

## filters支持编码

```
UCS-4*
UCS-4BE
UCS-4LE*
UCS-2
UCS-2BE
UCS-2LE
UTF-32*
UTF-32BE*
UTF-32LE*
UTF-16*
UTF-16BE*
UTF-16LE*
UTF-7
UTF7-IMAP
UTF-8*
ASCII*
EUC-JP*
SJIS*
eucJP-win*
SJIS-win*
...
```

> [官方文档](https://www.php.net/manual/zh/mbstring.supported-encodings.php)

## 思路分析

> 通过代码可以分析得到,这是考察文件名绕过的.使用伪协议绕过,经测试,php://伪协议能使用,后面的过滤器经fuzz发现convert.iconv.*能用,后面的编码再次fuzz,得到payload

## payload

> ?filename=php://filter/convert.iconv.utf8.utf16/resource=flag.php
> 
## flag

> cyberpeace{0d2dd97f453a7ff841dd85f433931244}