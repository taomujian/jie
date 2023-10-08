# Interesting

## 解题思路

> 下载附件,得到一个py文件和一个txt文件.


> AES_CBC比特翻转攻击: 在CBC模式的加密中，在我们不知道密钥，但是知道了一组明密文对应的情况下，可以做到修改部分密文，使得修改后的密文解密后的明文串中特定的字符变成我们想要的字符

> 再看回代码，发现admin、group从0变成了1，这里的改动刚好是counter=2，比特翻转的关键代码如下：

```
def cbc_bit_attack_mul(c,m,position,target):
    l = len(position)
    r=c
    for i in range(l):
        change=position[i]-16
        tmp=chr(ord(m[position[i]])^ord(target[i])^ord(c[change]))
        r=r[0:change]+tmp+r[change+1:]
    return r
```

> 根据比特翻转后的密文可以获知seed，就此推出iv和password，就可以进行AES_CBC的解密，解密后还需要一连串的decode操作

## flag

> flag{ri_bu_luo_de_xia_tian_ai_de_ming_xing+pian}