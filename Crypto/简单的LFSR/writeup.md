# 简单的LFSR

## 解题思路

> 下载附件,得到一个python文件,开始分析代码,代码逻辑很简单

> 分析一下题目逻辑.初识化数组initState,即为LFSR(线性反馈移位寄存器)的初始状态,mask是flag转二进制之后的数组.

> 最主要的操作就是进行256轮LFSR计算

> lfsr函数逻辑不算复杂,输入两个长度为128数组state, mask,输出 output 值为$out=\sum{state_i \times mask_i}$

> 注意到每轮 state 数组取值会向右移动一个位置,同时 initState 长度会增长1,即数组尾部追加了 output 值

> 关键的关系式$out=\sum{state_i \times mask_i}$

> 可改写为矩阵乘法形式$out=State \times Mask$

> State是 $1\times128$ 向量,Mask是 $128 \times 1$ 向量

> 256轮循环最终输出initState数组后256个元素,命名为outputState,其中$outputState_{0…127} \times Mask = outputState_{128} \
outputState_{1…128} \times Mask = outputState_{129} \
\cdots \
outputState_{127…254} \times Mask = outputState_{255}$

接下来就是简单的线性方程组求解了.

## flag

> flag{48eea154e05fefe7a657680a080ada3b}