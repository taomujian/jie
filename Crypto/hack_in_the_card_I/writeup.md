# Hack_in_the_card_I

## 解题思路

> 下载附件,解压后得到多个文件.

> 本题考的是Simple Power Analysis,通过快速幂算法可知bit为1时波峰比bit为0时的波峰更长,于是用js脚本分析数据即可得到d的值,每隔10个数采一次样,判断连续大于阈值的数据个数的大小即可,得到d则可解出ﬂag. 

> 获得了一个PEM格式的RSA公钥,一个电路图和一个网站,显示了使用该智能卡进行解密过程中电阻的电压变化.

> 当电压高或低时,图表很清楚. 也许这是一个侧信道攻击,解密过程图可能会泄露秘密指数.

> 通过使用代码成功地提取私有指数.


## flag

> HITB{My name is Alice, and this is my story, the end of my story}

## 参考

> https://github.com/sgzeng/hack-in-the-card-one

> https://www.ssleye.com/ssltool/priv_get.html