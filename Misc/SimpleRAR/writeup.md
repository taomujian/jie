# SimpleRAR

## 解题思路

> 下载附件后,得到1个RAR文件,直接用winrar打开,提示图片文件头错误

> 010 Editor 打开压缩包,rar文件块的开头是A8 3C 74, 但是这里是A8 3C 7A,是子块的意思,因secret.png为一个文件,A8 3C 7A改为A8 3C 74,解压文件,得到png图片,010 Editor打开发现是GIF的文件头,把secret.png后缀改为secret.gif.用ps工具分离图层后分别保存再使用图片分析工具Stegsolve分别找到两个图层里上半部分和下半部分的二维码,最后组合起来扫描二维码得到flag.

## flag

> flag{yanji4n_bu_we1shi}