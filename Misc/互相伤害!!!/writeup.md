# 互相伤害!!!

## 解题思路

> 附件下载解压后使用file发现是一个pcapng文件,wireshark打开,导出所有的http对象.发现一张带有二维码的图片,扫描二维码得到一串字符

> 用http://www.jsons.cn/aesencrypt/根据提示用aes解密,密码是用CTF,得到668b13e0b0fc0944daf4c223b9831e49

> foremost分离出压缩包,输入密码668b13e0b0fc0944daf4c223b9831e49解压文件

> 扫描二维码中间的二维码得到flag{97d1-0867-2dc1-8926-144c-bc8a-4d4a-3758}

> 根据题目提示输入97d1-0867-2dc1-8926-144c-bc8a-4d4a-3758

## flag

> 97d1-0867-2dc1-8926-144c-bc8a-4d4a-3758

## 参考

> https://github.com/AngelKitty/stegosaurus
