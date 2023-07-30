# base64stego

## 解题思路

> 下载附件得到一个zip文件,解压需要密码,题目没有给出密码的提示,猜测是伪加密,果然,010 Editor打开后发现是我伪加密,修改对应的标志位,解压得到一个txt文本,里面的字符串直接打开bas464解码发现有乱码,根据题目和之前做过的Crypto题目,说明考察的是base64隐写.

## flag

> flag{Base_sixty_four_point_five}
