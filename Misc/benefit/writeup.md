# benefit

## 解题思路

> 下载附件得到1张图片,file发现是一个jpeg文件,修改后缀,然后binwalk -e和foremost没啥收获.010 Editor打开,发现有一串特殊的字符.

> 得到的字符串进行base16解码,每7位一组,转成ascii,根据图片提示caesar,通过94位数(string.printable[:-6])凯撒位移写爆破脚本运行得到flag.


## flag

> 
