# 3-11

## 解题思路

> 下载附件得到一个文件,binwalk,宽高没问题,StegSolve打开,RGB低通道保存数据为zip文件,然后直接用zip打开会报错,用winrar打开,这时直接解压也是错误的,使用winrar的修复工具修复,解压得到一个txt文本,里面是一串base64编码,转换为图片得到flag


## flag

> FLAG{LSB_i5_SO_EASY}
