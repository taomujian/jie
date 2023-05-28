# Ditf

## 解题思路

> binwalk、foremost走起,得到一个压缩包,打开需要密码,用010 Editor打开图片报错,发现crc报错，猜测可能是图片隐写,修改高度,得到压缩包密码StRe1izia.打开得到一个pcapng文件,打开,搜错字符串png,看到请求了一个kiss.png,发现神秘字符串,base64解密得到flag.

## flag

> flag{Oz_4nd_Hir0_lov3_For3ver}
