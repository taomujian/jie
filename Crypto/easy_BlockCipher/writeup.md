# easy_BlockCipher

## 解题思路

> 下载附件,得到一个py文件和一个加密后的文件.

> 分析py文件,可知加密时采用了DES算法,并且在OFB模式下对明文进行加密.因此在已知 IV = ‘12345678’ 的情况下,只需要知道Key,即可对密文进行破解.

> 根据已知信息,仅有IV以及未知的Key,所以想到DES加密种存在弱密钥.在 DES 的计算中,56bit 的密钥最终会被处理为 16 个轮密钥,每一个轮密钥用于 16 轮计算中的一轮,DES 弱密钥会使这 16 个轮密钥完全一致,所以称为弱密钥.其中四个弱密钥为：

```
0x0000000000000000
0xFFFFFFFFFFFFFFFF
0xE1E1E1E1F0F0F0F0
0x1E1E1E1E0F0F0F0F
```

> 利用四组若密钥尝试对密文进行破解,得到flag.


## flag

> flag{_poor_single_dog_has_found_an_echo_from_it}
