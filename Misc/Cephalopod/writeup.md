# Cephalopod

## 解题思路

> 附件是一个pcap文件,wireshark打开,查找flag字符串,找到一个flag.png,看来是要还原这个png图片了.

> 跟踪TCP流,查找png文件的文件头：89504E47 文件尾：49454E44AE426082
,复制头到尾,粘贴到010 editor,然后另存为flag.png.得到flag

> 还可以用tcpxtract -f 直接提取图片

## flag

> HITB{95700d8aefdc1648b90a92f3a8460a2c}
