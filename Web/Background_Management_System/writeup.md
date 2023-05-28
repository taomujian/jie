# Background_Management_System

## 思路分析

> 依次对http://61.147.171.105:55457/xinan/和http://61.147.171.105:55457/xinan/public进行目录扫描,发现存在http://61.147.171.105:55457/xinan/public/www.zip存,下载网站源码进行代码审计,发现一个shell.php,但是只能本地访问,猜测要利用ssrf漏洞.登陆和注册处对可控参数进行了控制,无法注入,更新密码处,未对用户名进行过滤,存在任意用户修改漏洞.注册一个admin'#的用户,修改密码后,用admin用户登陆后在个人中心发现一个php文件,访问该文件,发现存在ssrf漏洞,就和前面形成了呼应.最终执行命令,获取flag

## payload

> http://61.147.171.105:55457/xinan/public/55ceedfbc97b0a81277a55506c34af36.php?url=gopher://127.0.0.1:80/_GET%20/xinan/public/shell.php%253Fcmd=cat%2B/flag

## flag

> flag{4e8f794089b6b4ef55cd0399dca1433c}