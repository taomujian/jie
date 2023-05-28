# UNSEPING

> 首先可看到这是通过GET传递参数code进行反序列化的,考察的是反序列化,把字符串转换为原始的对象结构,php反序列化过程中会调用魔术方法__wakeup,但是wakeup一被调用就会退出,所以得绕过wakeup,从而达到目的获取flag

## 涉及函数

### __wakeup

> 当使用unserialize时被调用,可用于做些对象的初始化操作


## 思路分析

> 首先可看到这是通过GET传递参数code进行反序列化的,考察的是反序列化,把字符串转换为原始的对象结构,php反序列化过程中会调用魔术方法__wakeup,但是wakeup一被调用就会退出,所以得绕过wakeup,从而达到目的获取flag.当被反序列化的字符串其中对应的对象的属性个数发生变化时,会导致反序列化失败而同时使得_wakeup()函数失效,通过修改序列化出来的字符串来获取flag,正常的字符串是O:4:"xctf":1:{s:4:"flag";s:3:"111";},修改为O:4:"xctf":2:{s:4:"flag";s:3:"111";}来获取flag.


## payload

> ?code=O:4:"xctf":2:{s:4:"flag";s:3:"111";}

## flag

> cyberpeace{b050f7123aa55a20bde5df1e76778c06}