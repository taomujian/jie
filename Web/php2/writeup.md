# Php2

> 通过get方式传递参数id通过验证


## 思路分析

> 通过get方式传递参数id通过验证,id为admin是发现不允许,对admin进行url编码,发现浏览器会进行一次编码,发到php还是admin,所以需要再次编码,admin->%61admin->%2561dmin


## payload

> ?id=%2561dmin

## flag

> cyberpeace{3f589b9844341ccc22e974d09b7077e0}