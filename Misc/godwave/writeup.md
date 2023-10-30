# Godwave

## 解题思路

> 下载的wav附件用分Audacity打开就是一段稀奇古怪的音频信号,仔细观察,发现不同段落其幅值有明显差异,应该是调幅了,MATLAB导入wav文件看数据,发现大概是以64个点为周期,那么取幅值高的为1,幅值低的为0.

> flag在matlab中运行后生成文件data.txt(metlab的bin文件夹),data.txt中的数据是曼彻斯特编码,解码后是一张二维码图片,扫描这个图片得到flag.

## flag

> PCTF{Good_Signal_Analyzer}
