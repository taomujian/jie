# 1-misc

## 解题思路

> 下载附件得到一个压缩包,直接解压提示错误,用winrar解压发现提示有密码,根据提示,用8位数字对zip文件爆破,得到密码20001228

> 解压缩得到2.zip和fakeflag.jpg,打开2.zip发现其中也有fakeflag.jpg,并且CRC32相同,可以通过明文攻击解密.将fakeflag.jpg压缩用来明文攻击,保存解密的文件2_decrypted.zip，解压缩得到3.zip

> 根据提示"没有密码"想到伪加密,用十六进制编辑器打开压缩包,修改加密标志
将两个位置的09改为00,保存文件得到flag,也可以进行文件分离得到flag

## flag

> flag{39281de6-fe64-11ea-adc1-0242ac120002}
