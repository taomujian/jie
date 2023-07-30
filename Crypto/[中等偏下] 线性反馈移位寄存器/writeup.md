# [中等偏下] 线性反馈移位寄存器

## 解题思路

> 下载附件,得到一个py和加密文件,py文件里是一个线性反馈移位寄存器


> 分析一下题目逻辑.初识化数组initState,即为LFSR(线性反馈移位寄存器)的初始状态,mask 是flag转二进制之后的数组.

> 最主要的操作就是进行256轮LFSR计算,这地方和简单LFSR有点不同

> lfsr函数,输入两个长度为128数组state,mask,输出output值为$out=\sum{state_i \times mask_i} \mod 2$

> 注意到每轮state数组取值会向右移动一个位置,同时initState长度会增长1,即数组尾部追加了output值

> 关键的关系式$out=\sum{state_i \times mask_i} \mod 2$
可改写为矩阵乘法形式$out=State \times Mask \mod 2$

> State是 $1\times128$ 向量,Mask是 $128 \times 1$ 向量

> 256轮循环最终输出 initState 数组后256个元素,命名为 outputState,其中$outputState_{0…127} \times Mask = outputState_{128} \mod 2 \
outputState_{1…128} \times Mask = outputState_{129} \mod 2 \
outputState_{1.128} \times Mask = outputState_{129} \mod 2 \
\cdots \  \cdots \
outputState_{127…254} \times Mask = outputState_{255} \mod 2$
outputState_{127.254} \times Mask = outputState_{255} \mod 2$

> 尝试模2条件下线性方程组求解.

> 求解有点问题,最后是把initState组在outputState前面一起解方程组,得到正解


## flag

> EasyMathWithSage

## 参考

> https://sagecell.sagemath.org/

> https://blog.csdn.net/figfig55/article/details/128632051

> https://coding.tools/cn/binary-to-text