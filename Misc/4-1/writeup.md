# 4-1

## 解题思路

> 下载附件得到一个图片,binwalk + foremost得到一个压缩包,然后解压得到一个提示和一个压缩包,压缩包解压得到2张图片,提示是说day2藏有flag,怀疑是盲水印,两个相同的图片,第二个东西比较多,很容易想到盲水印.


> 用BlindWatermark解码得到flag.

## flag

> wdflag{My_c4t_Ho}

## 参考

> https://github.com/chishaxie/BlindWaterMark