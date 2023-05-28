# Easytornado

> tornado ssti注入

## 思路分析

> tornado ssti注入,打开网站,发现有3个链接.

> 打开第1个,发现flag存在fllllllllllllag文件中.

> 打开第2个链接得到render,得知render是python中的一个渲染函数,渲染变量到模板中,即可以通过传递不同的参数形成不同的页面,说明肯定是ssti注入.直接访问/fllllllllllllag发现会报错,响应头中有/error?msg=Error,怀疑z这里存在服务端模板注入攻击,尝试/error?msg={{datetime}},发现解析了,说明这个就是注入点

> 打开第3个链接发现md5(cookie_secret+md5(filename)),对这几个链接分析发现是文件名和一个文件哈希值(md5)组成的,那么说明直接访问/fllllllllllllag是不行的,还需要一个md5值,这个md5值就是md5(cookie_secret+md5(filename)),文件名是知道的,现在就要确定cookie_secret是什么.

> 在Tornado的前端页面模板中,datetime是指向python中datetime这个模块,Tornado提供了一些对象别名来快速访问对象,可以参考Tornado官方文档
> 通过查阅文档发现cookie_secret在Application对象settings属性中,还发现self.application.settings有一个别名RequestHandler.settings
> handler指向的处理当前这个页面的RequestHandler对象,RequestHandler.settings指向self.application.settings,因此handler.settings指向RequestHandler.application.settings.

> 构造payload获取cookie_secret, /error?msg={{handler.settings}}得到cookie_secret

## payload

> /error?msg={{handler.settings}}

> /file?filename=/fllllllllllllag&filehash=53f8261527589a3f2e2bf29633956ec1

## flag

> flag{3f39aea39db345769397ae895edb9c70}