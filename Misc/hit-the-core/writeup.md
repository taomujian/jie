# Hit-the-core

## 解题思路

> 下载附件得到一个.core文件,core文件时linux系统程序崩溃生成的文件,里面有内存映射和存储调试信息的文件,在kali下用strings 8deb5f0c2cd84143807b6175f58d6f3f.core得到如下的字符串

```
cvqAeqacLtqazEigwiXobxrCrtuiTzahfFreqc{bnjrKwgk83kgd43j85ePgb_e_rwqr7fvbmHjklo3tews_hmkogooyf0vbnk0ii87Drfgh_n kiwutfb0ghk9ro987k5tfb_hjiouo087ptfcv}
```

> 然后发现大写的XCTF每个字母之间只隔了四个字母,使用python提取一下,得到flag

## payload

```
num='cvqAeqacLtqazEigwiXobxrCrtuiTzahfFreqc{bnjrKwgk83kgd43j85ePgb_e_rwqr7fvbmHjklo3tews_hmkogooyf0vbnk0ii87Drfgh_n kiwutfb0ghk9ro987k5tfb_hjiouo087ptfcv}'
flag = ''
for i in  range(3,len(num),5):
   flag += num[i]
print(flag)
```

## flag

> ALEXCTF{K33P_7H3_g00D_w0rk_up}
