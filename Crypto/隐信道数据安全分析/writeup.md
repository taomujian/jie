# 隐信道数据安全分析

## 解题思路

> 下载附件得到1个map文件,题目提示mp3的private有问题.

> 在010Editor中打开mp3文件,可以发现在每个MPEG_FRAME mf下的4字节MPEG_HEADER mpeg_hdr中的第24个bit有一个private bit,那么将文件中所有MPEG_FRAME mf下的private bit全部提取出来即可得到一串二进制数据,然后转换成字符即可得到flag


## flag

> flag{pr1v4t3_bi7}
