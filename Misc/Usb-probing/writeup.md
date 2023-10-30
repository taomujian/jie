# Usb-probing

## 解题思路

> 从下载附件,是一个pcap包.

> 用binwalk发现存在png,但是直接提取发现提取不出来,只能手动了.

> wireshark打开,搜索png,在第101个数据包中找到了png图片.复制16进制数据,010 Editor打开导入后保存为png,打开png得到flag.

> 有个坑点是用windows自带的图片查看器看不到flag,很模糊.发到微信上就能看到,不知道为什么.

## flag

> ALEXCTF{SN1FF_TH3_FL4G_OV3R_U58}
