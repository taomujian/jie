# upload3

## 思路分析

> 根据题目提示,扫目录得到网站源码.然后注册账号,登陆后发现有一个上传文件的功能.翻看源码,找到了上传文件功能的相关源码Profile.php,其中upload_img函数就是处理上传文件的.

> upload_img函数调用了login_check函数,可以看到这里有个unserialize函数,第一时间先想到反序列化漏洞,继续看,简单来说这个检查函数就是先把cookie中的user取出来,接着base64解码,反序列化后的值与数据库中根据id查询出来的值进行对比,相同即返回1,不同即返回0.

> 接着检查是否上传了文件,若有文件被上传,继续往下,filename_tmp为在服务端储存的临时文件名,filename为客户端文件的原名称的md5值并加上了".png",接着调用ext_check()函数对后缀进行检查,若后缀为png则返回1,否则返回0.

> 继续往下,当ext()检查函数返回1后进入if语句,先getimagesize()函数简单判断传入的文件是否为图片类型,接着复制临时文件filename_tmp到md5值+png后缀的filename文件,然后再删除临时文件filename_tmp

> 把filename赋值给img后,调用update_img()函数,该函数先从数据库根据id取出img的值,检查img的值是否为空,为空则表明是第一次上传,然后提示"Upload img successful!",返回home目录,

如果不为空,即之前已经上传过一次图片了,则报错'Upload file failed!',返回index目录

> 剩下的就是update_cookie()函数,功能是把filename的路径(也就是我们图片上传后的路径)的值赋给profile[img],接下来就是对profile进行序列化,base64加密,再更新客户端中的cookie.

> 再来看看Profile.php最后的两个函数,这两个都是魔术方法,先来看第一个__get(),它的作用是当其他类读取其不可访问属性的值时自动触发.在这里,就是当其他类读取了profile类中不可访问属性的值时自动返回except数组的内容.第二个是__call()魔术方法,跟第一个类似,它是对象中调用一个不可访问方法时触发.也就是说,这两个魔术方法里的内容合起来,只要构造成功,就可以随意调用该类中的某一个方法.

> 接下来看到Register.php中的最后一个函数,也是一个魔术方法_destruct(),该函数的作用是当对象的所有引用都被删除或者当对象被显式销毁时执行.同时看这里它执行的内容,可以调用index方法.

> 到这里,一条反序列的攻击链已经呼之欲出了,接下来就是要思考怎么整合这些可利用的点并构造反序列化了.思路如下:

> 首先,无论打开哪个页面,都先调用login_check()函数来检查是否已登录,而login_check()函数中就把cookie中的user值提出来并反序列化,得从这里先入手.那么在构造序列化的时候要先new哪一个类呢？在register类的最后一个魔术方法是一个比较好的选择,因为可以控制它去访问profile类中的index方法.而profile类中没有index方法,自动触发__call()魔术方法,先if语句判断index的值是否存在,而index在profile中是不存在的,所以又自动触发了__get()魔术方法,我们可以控制except数组返回的值为upload_img,从而来调用upload_img()函数,成功地调用到了upload函数后,再让filename_tmp的值改为已经上传的图片的路径+文件名,再把filename改为php后缀的文件,就可以让图片里的代码成功解析了.

> 总的来说就是通过上传包含有恶意代码的图片,通过修改cookie来达到反序列化的一系列操作,把png后缀的文件改为php文件从而来实现了真正的上传绕过.

## flag

> flag{5ab961aa85fb6f1118e3ea2a77db2045}

## 参考

> https://www.cnblogs.com/v1ntlyn/p/13549811.html