# Onetimepad

## 解题思路

> 下载附件,得到一些加密字符串和一个加密的py脚本

> 分析函数process(m,k):

```
def process(m, k):
    tmp = m ^ k
    res = 0
    for i in bin(tmp)[2:]:
        res = res << 1;
        if (int(i)):
            res = res ^ tmp
        if (res >> 256):
            res = res ^ P
    return res
```

> res = res << 1代表乘以x,多项式的系数全体左移一位

> if (int(i)):res^=tmp等价于res^=int(i)*tmp,代表+𝑡<sub>𝑖</sub>⋅𝑓<sub>𝑡</sub>

> if (res>>256):res^=P代表模本原多项式g

> 综上,process(m,k)实际上实现了𝐺𝐹(2<sup>256</sup>)上的元素𝑚与𝑘之和的平方(𝑚+𝑘)<sup>2</sup>

> 解密过程:


𝑘<sub>2</sub>=(𝑘<sub>1</sub>+𝑠𝑒𝑐𝑟𝑒𝑡)<sup>2</sup>,𝑘<sub>3</sub>=(𝑘<sub>2</sub>+𝑠𝑒𝑐𝑟𝑒𝑡)<sup>2</sup>
(在GF(2<sup>256</sup>)上的运算)

𝑐<sub>1</sub>=𝑚<sub>1</sub>⊕𝑘<sub>1</sub>,𝑐<sub>2</sub>=𝑚<sub>2</sub>⊕𝑘<sub>2</sub>,𝑐<sub>3</sub>=𝑚<sub>3</sub>⊕𝑘<sub>3</sub>
,其中𝑐<sub>i</sub>(𝑖=1,2,3),𝑚<sub>i</sub>(𝑖=1,2)
已知

则𝑘<sub>2</sub>=𝑚<sub>2</sub>⊕𝑐<sub>2</sub>,𝑘<sub>3</sub>=𝑚<sub>3</sub>⊕𝑐<sub>3</sub>
,可解出secret：𝑠𝑒𝑐𝑟𝑒𝑡=𝑘<sub>3</sub><sup>1/2</sup>+𝑘<sub>2</sub>
(在GF(2<sup>256</sup>)上的运算)

接下来解出𝑘<sub>1</sub>
：𝑘<sub>1</sub>=𝑘<sub>2</sub><sup>1/2</sup>+𝑠𝑒𝑐𝑟𝑒𝑡
(在GF(2<sup>256</sup>)上的运算)

然后解出flag(即𝑚1
)：𝑚<sub>1</sub>=𝑐<sub>1</sub>⊕𝑘<sub>1</sub>


## flag

> flag{t0_B3_r4ndoM_en0Ugh_1s_nec3s5arY}

## 参考

> https://www.cnblogs.com/coming1890/p/13607557.html

> https://blog.csdn.net/weixin_44604541/article/details/111514621
