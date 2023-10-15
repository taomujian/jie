# Blocks

## 解题思路

> 下载附件得到一个文件.

> binwalk + foremost得到一个图片,这是一张二维码图片,但是没有二维码的方框.

> 文件名是"stego_100_f78a3acde659adf7ceef546380e49e5f",使用Stegsolve在“Alpha plane 0"通道下发现中间出现一个类似的19x19的类似二维码的图片,这样就有两个19x19的图片,取异或后转为二进制,再转字符串得到flag信息

## flag

> ASIS_08213db585ffe1c93c8f04622c319594
  