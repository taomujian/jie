# 7-2

## 解题思路

> 下载附件得到很多文件,解压后发现大堆文件名,尝试base64

```
ls|tr -d ' '|base64 -d
```

> 发现<p@<uk'2Pz1KFAN߬r9HSLainidexingzhuang>$Il{arGks!gb|5
爱你的新装字样,定位到文件YWluaWRleGluZ3podWFuZw

> 打开文件内容,进行键盘密码和凯撒解密得到flag.

## flag

> wdflag{ylyoselfve}
