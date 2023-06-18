# Flag_universe

## 解题思路

> 下载附件得到一个pcapng文件,用wireshark打开图片,发现是去连接FTP服务区查看下载文件,共访问了3个文件.分别是flag.txt、universe.png、new_universe.png,flag.txt内容提示是一个虚假flag.那么flag就是在这2张图片里了.

> 分别保存2张图片,发现new_universe.png存在LSB隐写,得到flag

## flag

> flag{Plate_err_klaus_Mail_Life}
