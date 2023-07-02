# 3-1

## 解题思路

> 下载附件得到一个文件,010 Editor打开,发现是rar文件,于是修改后缀解压得到一个文件.

> 这个文件先用binwalk -e提取出来得到2个rar文件,然后其中一个下面有flag.txt,但是有密码.

> 010 Editor打开修改后缀解压得到的文件,发现有wireshark字符,怀疑是流量包文件,wireshark打开,发现有telnet流量包,追踪下TCP数据流,发现执行了很多命令.

> 有一个AES加解密的python脚本,还有一串加密字符,解密得到rar解压密码,解压得到flag.txt,得到flag.

## flag

> WDCTF{Seclab_CTF_2017}
