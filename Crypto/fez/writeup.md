# Fez

## 解题思路

> 下载附件,得到1个py文件和1个log文件.

```
1.a^a=0;
2.a^a^b=b;
3.由前两个式子可以推出若:a^b=aa;c^b=cc;则有aa^cc=a^c;(本题重要的解题点)
```

> 代码的含义如下:

```
1.K 是一个有7个元素的数组,每个元素是一个长度为27的字符串.
2.test是一个长度为54的随机字符串.
3.所以题目中加密方式一样,flag一样但每次所给的fez.log内容都不一样.
4.fez.log中的三行字符串分别是,test,test与k进行加密的结果,k与m(也就是flag)进行加密的结果.
5.每次加密都是调用fez()函数,在这个函数是循环7次,每次都是将K的元素与传入的另一个54位的字符串按round()函数那样进行运算,在round()函数中调用了xor()函数,xor()函数就是异或运算.
```

> 模拟一下这个fez.py的加密方式

```
test和K.test的左边为Lt,右边为Rt
第一次循环: Rt+Rt^Lt^K1
第二次循环: Rt^Lt^K1+Lt^K1^K2
第三次循环: Lt^K1^K2+Rt^K2^K3
第四次循环: Rt^K2^K3+Lt^Rt^K1^K3^K4
第五次循环: Lt^Rt^K1^K3^K4+Lt^K1^K2^K4^K5
第六次循环: Lt^K1^K2^K4^K5+Rt^K2^K3^K5^K6
第七次循环: Rt^K2^K3^K5^K6+Rt^Lt^K1^K3^K4^K6^K7=T_K

K和m.m的左边为Lm,右边为Rm.
第一次循环: Rm+Rm^Lm^K1
第二次循环: Rm^Lm^K1+Lm^K1^K2
第三次循环: Lm^K1^K2+Rm^K2^K3
第四次循环: Rm^K2^K3+Lm^Rm^K1^K3^K4　
第五次循环: Lm^Rm^K1^K3^K4+Lm^K1^K2^K4^K5
第六次循环: Lm^K1^K2^K4^K5+Rm^K2^K3^K5^K6
第七次循环: Rm^K2^K3^K5^K6+Rm^Lm^K1^K3^K4^K6^K7=K_M
```

> 此时我们可以根据第3个知识点,发现,将这两次密文结果进行异或运算可以消除K,也就是密钥.

```
T_K^K_M=Rt^Rm+Rt^Lt^Rm^Lm=T^M
```

> 这时只要再将结果异或T就可以得到M: Rt^Rm^(Rt)=Rm

> Rt^Lt^Rm^Lm^(Rt^Lt^Rm)=Lm

> Lm+Rm=m即包含flag的字符串.

## flag

> flag{festel_weak_666_lol9991234admin}͡

## 参考

> https://www.cnblogs.com/nldyy/p/9800260.html