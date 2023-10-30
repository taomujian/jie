# Picture1

## 解题思路

> 下载附件,是一张图片.使用binwalk,没发现什么.查看十六进制,也没有发现什么附加内容.最后使用stegsolve看看是不是存在LSB隐写

> 果然是存在LSB隐写的,在red0、green0、blue0可以看到第一行都是存在数据的

> Data Extract功能提取一下,但是发现内容并不是明文字符串,也不是什么常见文件的十六进制

> 这是LSB隐写,用工具可以解密,解密后得到一个python文件

> 有明文,有密文,DES解密得到flag.

## flag

> QCTF{eCy0AALMDH9rLoBnWnTigXpYPkgU0sU4}

## 参考

> https://github.com/livz/cloacked-pixel

> https://github.com/liupengs/DES_Python
