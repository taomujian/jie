# Miscmisc

## 解题思路

> 下载附件得到一个png文件,foremost得到一个chadiand.zip压缩包和一张chayidian.jpg图片,压缩包不是伪加密.

> jpg文件foremost得到一个zip文件,解压后得到一个txt文本,巧合的是上一步获得的chadiand.zip文件里也有一个flag.txt,查看两个文件的CRC32可知两个文件一样,典型的明文攻击,使用ARCHPR明文攻击得到密码z$^58a4w

> 解压后继续解压flag.zip,world1.png用zsteg得到一个密码z^ea

> 还有一个word文件,word基本上就是隐藏信息了,可在文件选项中单击"文件"-》选项-》显示,选择"隐藏文字"复选框,即可查看,把每一行隐藏的字符和z^ea组成密码z^ea4zaa3azf8解压whoami.zip,得到flag.


## flag

> flag{12sad7eaf46a84fe9q4fasf48e6q4f6as4f864q9e48f9q4fa6sf6f48}
