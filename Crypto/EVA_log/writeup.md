# EVA_log

## 解题思路

> 下载附件,得到2个txt文件.

> 在EVA_log.txt里面发现了RSA题目的参数,n、c、e,直接解密发现提示p和q不互质.

> 看WP发现考察点为Coppersmith定理相关攻击,https://github.com/mimoo/RSA-and-LLL-attacks给出的demo2逻辑可以解密flag的第一部分.https://github.com/mimoo/RSA-and-LLL-attacks 给出的demo1逻辑可以解密flag的第二部分.



## flag

> flag{c16cd5d9-3537-4a84-aacb-7d2490cf6b5f}
