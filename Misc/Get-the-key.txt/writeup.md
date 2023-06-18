# Get-the-key.txt

## 解题思路

> 下载附件后,使用binwalk -e提取文件

> 使用file命令,发现是一个文件系统数据,forensic100: Linux rev 1.0 ext2 filesystem data

> 根据题目名称可知,我们要找key.txt文件.使用-file _forensic100.extracted/ext-root/* r key.txt命令查找此文件

> 最后使用gunzip < 1命令读取文件,得到flag

## flag

> SECCON{@]NL7n+-s75FrET]vU=7Z}
