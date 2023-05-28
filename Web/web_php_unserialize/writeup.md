# Web_Php_Unserialize

> 考察反序列化,传递var参数,var是base64编码,要绕过/[oc]:\d+:/i

## 涉及函数

### __construct

> 在类实例化的时候,会自动调用该魔术方法,进行类的初始化

### __destruct

> 明确销毁对象或脚本结束时被调用

### preg_match

> preg_match(pattern,subject,matches,flags,offset)

> 函数用于执行一个全局正则表达式匹配,可以搜索字符串中可以和正则表达式匹配的结果,只匹配一次

### __wakeup

> 当使用unserialize时被调用,可用于做些对象的初始化操作

## 思路分析

> 反序列化,首先绕过正则表达式,正则表达式会匹配到O:数字就会退出,在php中+4和4是一样的,所序列化出来的字符串在O:和数字之间加个加号(+)就行,wakeup函数会判断当前变量file是不是等于index.php,如果不等于则会重写,所以需要绕过wakeup函数,修改序列化出来的字符串中代表变量数量的字符即可,最后base64编码得到结果

## payload

> ?var=TzorNDoiRGVtbyI6Mjp7czoxMDoiAERlbW8AZmlsZSI7czo4OiJmbDRnLnBocCI7fQ==

## flag

> ctf{b17bd4c7-34c9-4526-8fa8-a0794a197013}