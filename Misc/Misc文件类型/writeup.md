# Misc文件类型

## 解题思路

> 下载附件得到一个txt文本,里面是一些16进制的字符串,转换为ASCII码,前面46ESAB即BASE64倒序,删除前面7个字符进行base64解码,看到PK字符,典型的zip文件,将base64的数据转换为16进制,通过010 Editor导入,保存为zip文件,然后解压得到flag.

## flag

> flag{0bec0ad3da2113c70e50fd5617b8e7f9}

## 参考

> https://1024doc.com/exts/HexBaseBiConverter

> https://tool.hiofd.com/hex-convert-ascii-online/