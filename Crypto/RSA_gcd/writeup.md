# RSA_gcd

## 解题思路

> 下载附件,得到2个txt文件,已知多个n,e,和之前的低指数加密广播攻击相比,e很大.

> 属于公因数攻击,题目会给你很多组n和c.n=p*q,而p、q是两个大素数.当有很多组n的时候,很有可能出现两个n之间存在公因数.而这个公因数就是p和q其中的一个,当然知道其中一个另一个也就知道了.就可以求出d进而根据对应密文求出m.

## flag

> flag{336BB5172ADE227FE68BAA44FDA73F3B}