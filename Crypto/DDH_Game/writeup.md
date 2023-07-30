# DDH_Game

## 解题思路

> 下载附件,得到一个txt文件和sage文件,是椭圆曲线离散对数问题,不太懂,密码学高深啊,看WP,本地先安装一个sagemath

> 这里n有两个大因子所以求阶也是很困难的,但只需要求的a、b、c即可判定,因为当成立的时候,再全部模一个数也是成立的.有个坑点在于sols = m.bits()函数是低位高位倒置的,所以求出来还要倒转比特.

> 由于题目中的BLS曲线是配对友好曲线,所以可以计算双线性对.双线性对满足e(aG,bG)=e(G,abG)这就给了我们一个解DDHP的后门.因此如果随便选一个椭圆曲线点群,ECDDH假设通常是不成立的,并且攻击方法就很简单：看等式e(aG,bG)=e(G,cG)是否成立.

## flag

> CatCTF{f0r_s0me_curves_ECDDHP_1s_e4sy_nyan}

## 参考

> https://www.cnblogs.com/ZimaBlue/articles/17024728.html

> https://www.anquanke.com/post/id/159893

> https://xia0ji233.pro/2023/01/01/Nepnep-CatCTF2022/#%E8%A7%A3%E6%B3%95%E4%B8%80