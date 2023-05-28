# blgdel

> 文件上传,.htaccess

## 思路分析

> 首先扫目录,发现了/config.txt,里面是php源码,还有/sql.txt,里面是sql语句.还有/uploads存在目录遍历,就可以猜出考察点有文件上传.注册用户并登陆,发现需要达到一定的积分才可以上传,这个通过刷推荐人就可以了.直接上传一句话,会发现发现<被过滤,通过查看config.txt也能发现上传的文件内容过滤了<等符号.此时可以上传.htaccess文件,用.htaccess修改配置文件.

> 上传的.htaccess文件内容如下,含义是设置访问一个php文件时,在该文件解析之前先自动包含并解析master://search/path=%2fhome%2f&name=flag,因为config.php中使用stream_wrapper_unregister('php')、stream_wrapper_unregister('phar')、stream_wrapper_unregister('zip')禁止了执行php、phar、zip协议,只能通过master协议来执行后面的操作了. 

> config.php中会根据传入的数据流的第一个参数来执行不同的操作,当是search会用来搜索文件名.

```
php_value auto_append_file master://search/path=%2fhome%2f&name=flag
```

> 得到文件名是hiahiahia_flag,继续构造如下的.htaccess文件,含义是设置访问一个php文件时,在该文件解析之前先自动包含并解析/home/hiahiahia_flag文件,然后再访问一句话就可以获取flag了.

```
php_value auto_append_file /home/hiahiahia_flag
```

## payload

```
php_value auto_append_file master://search/path=%2fhome%2f&name=flag
php_value auto_append_file /home/hiahiahia_flag
```

## flag

> cyberpeace{1218de3fc18864366069fa106e44057a}

## 参考

> https://blog.csdn.net/m0_61448651/article/details/125885822
> https://blog.csdn.net/qq_46263951/article/details/122271104
> https://www.cnblogs.com/huacheng1122/p/15311288.html

