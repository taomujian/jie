# [中等] QR1

## 解题思路

> 下载附件得到一个空白的png图片,不过有一些点点

> 仔细观察发现这些点点在图片边边角角排列组成的样子,有类似二维码定位符,猜测这张图片为二维码,由于图片太大了,5330x5330改为533x533,然后用Stegsolve打开缩小后的图片,然后调为Random colour map 2,发现二维码,保存,然后用二维码识别工具识别,得到flag！

## flag

> flag{AHA_U_Kn0w_QR_c0d3_312468ed-ea59-4fe9-9cd2-b5e9d8b39498}

## 参考

> https://www.zhizuotu.com/msize
