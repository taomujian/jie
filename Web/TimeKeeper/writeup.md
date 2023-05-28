# TimeKeeper

> 3种解法

## 思路分析

> 常规的,扫目录,发现存在console路径,访问发现需要PIN码,百度下,知道了CTF中Werkzeug Debugger常见解法.看官方WP,发现还存在其他解法.

### Werkzeug Debugger PIN

> 首先注册一个账号,登陆,把所有操作进行一遍.接下来就是要构造畸形参数出来报错页面,在购买请求中,在price和id后面分别加一个',发现得到了报错页面.接下来是要找一个任意文件读取的漏洞,在网站本身请求中找不到,只能去找静态资源了,发现/asserts/..%2f..%2f..%2f..%2f可跨目录读取文件.接下来要找下面的信息:

```
md5_list = [ 
    'root', #当前用户，可通过读取/etc/passwd获取 
    'flask.app', #一般情况为固定值 
    'Flask', #一般情况为固定值 
    '/usr/local/lib/python2.7/dist-packages/flask/app.pyc', #可通过debug错误页面获取    
    '2485377892354', #mac地址的十进制，通过读取/sys/class/net/eth0/address获取mac地址 如果不是映射端口 可以通过arp ip命令获取 
    '0c5b39a3-bba2-472c-a43d-8e013b2874e8' #机器名，通过读取/proc/sys/kernel/random/boot_id 或/etc/machine-id获取 
    ]
```

> 运行flag.py得到pin码,执行命令cat /flag得到flag

### 目录跨越

> 访问http://61.147.171.105:51323/asserts/..%2f..%2f..%2f..%2fflag.txt得到flag

### 格式化字符串+SESSION伪造+软连接读文件

> 注册一个名为{user.\__class__.\__mro__[3].\__init__.\__globals__[current_app].config}的用户名,登陆后访问个人中心，拿到secret_key,利用获取的secret_key签名session，获取admin权限.获取admin权限后可以添加商品,商品图片可以是打包的tar包,从而利用软连接读文件.上传后读取flag

```
ln -s /flag 1.png tar cvfp ./flag.tar 1.png
```


## payload

> http://61.147.171.105:51323/asserts/..%2f..%2f..%2f..%2fflag.txt

## flag

> cyberpeace{a7b844d21701c675776f80f0f22c2ba5}

## 参考

> https://blog.csdn.net/weixin_44604541/article/details/109147735