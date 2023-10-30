# Secret_in_the_center

## 解题思路

> 下载附件得到一个文件,binwalk发现是一个zip文件,打开发现报错,010 Editor打开,发现zip 头部信息错误,应该为50 4B 03 04的,修改完后解压得到1个文件.

> 里面是3个坐标,根据题目名称secret_in_the_center,知道是要计算中心的点,计算后把数字转换字节,得到flag.

## flag

> flag{cef44b46f16ae8ecf664df4266ffdbf9}
