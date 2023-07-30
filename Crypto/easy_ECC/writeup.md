# Easy_ECC

## 解题思路

> 下载附件,得到一个文本,里面有一些参数,用利用工具ECCTOOL解题,把已知的参数填上去得到flag.

> 还有一种解法,利用椭圆曲线计算xG的方法即可求出公钥对（具体原理见https://www.jianshu.com/p/e41bc1eb1d81）,一个较重要的点是利用逆元求分数的取模,有两种方法：费马小定理和欧几里得算法,这里采用了费马小定理计算,编写脚本

## flag

> cyberpeace{19477226185390}

## 参考

> https://bbs.kanxue.com/thread-66683.htm

> https://blog.csdn.net/weixin_39934520/article/details/121772659