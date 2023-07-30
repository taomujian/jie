# 信号不好先挂了

## 解题思路

> 下载附件得到一个图片,zsteg发现图片lsb隐写了一个zip文件,使用StegSolve把隐写的数据保存为一个zip文件,直接解压提示文件受损,用winrar打开并进行修复,得到另一个图片,图片内容一样,大小不一样,猜测是盲水印.

> 用BlindWatermark解码得到flag.

## flag

> unctf{9d0649505b702643}