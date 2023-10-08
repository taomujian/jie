# Picture3

## 解题思路

> 下载附件得到一个jpg文件,binwalk发现存在一个zip文件,foremost提取,打开需要密码,并没密码的提示,猜测是伪加密,成功打开,解压后的文件有一段base64编码字符,解码发现并不是所想要的,猜测是base64隐写,得到flag.这道题用的知识点都遇到过,考察综合利用.

## flag

> flag{Ba5e_64OFive}