# RSA

## 解题思路

> 下载附件,得到一个文件夹,里面有2个文件,1个公钥文件,1个py文件

> 根据公钥文件,很快就能得出n,e,在线分解网站得到p和q,还以为能直接解密,发现并不能

> 继续分析给出的py文件,发现最后加密用到的并不是公钥中的,因为RSA加密需要公钥n的长度至少是大于消息的长度的,否则加密出来的密文会无法解密,从py文件中可以看到,如果不满足加密条件,就会重新构造p、q、e.

> 按照py文件重新p、q、e的方法循环构造私钥进行解密即可.


## flag

> flag{f@cToR__N_bY_!teratlnG!}