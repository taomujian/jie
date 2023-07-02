# OldDriver 

## 解题思路

> 下载附件,得到一个txt文件,里面是一个字母表和密钥,还有密文.根据题目得知这是转轮机加密,字母表按照密钥进行转动.

> 最开始的1-13表示的是密码表,然后有密钥,就是用密钥的顺序调整密码表,然后用密文进行旋转.

> 比如第一个密钥是2,找到第2行 KPBELNACZDTRXMJQOYHGVSFUWI,第一个密文字符是N,把N和N之后的字符放到最前面,成为NACZDTRXMJQOYHGVSFUWIKPBEL,依此类推,转换之后,出来并不知道该怎么找明文,根据提示,在竖行,只能试了,得到flag

## flag

> fireinthehole
