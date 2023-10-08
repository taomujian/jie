# Picture

## 解题思路

> 下载附件后,得到1个png图片

> 图片用binwalk -e分离,分离出97E4和97E4.zlib

> 97E4打开是一串base64文本,解密保存成文件,文件头是KP,改为PK,打开压缩包
压缩包有注释,此时直接解压发现报错,得用winrar工具打开修复下,解压密码为注释中python的错误信息integer division or modulo by zero

> 解压后发现有一个code文件,里面有一些字符

```
G0TE30TY[,C,X.$%&,C@Y,T5".#5%0C%"-#,Y04)&1C8Q-S,Q.49]
```

> UUencode解码得到flag

## flag

> CISCN{2388AF2893EB85EB1B439ABFF617319F}