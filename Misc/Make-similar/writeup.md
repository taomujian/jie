# Make-similar

## 解题思路

> 下载附件得到一个ogg文件.

> "120 LPM"提示气象传真(http://en.wikipedia.org/wiki/Radiofax),一个用于用于发送单色图像的模拟模式.

> OS X应用有个叫Multimode(http://www.blackcatsystems.com/software/multimode/fax.html#HOWREC)的可以把录像还原成原始的传真图片.这个软件只支持WAV文件输出，所以首先把similar.ogg转为similar.wav.结果看起来是这样的:

> 文字是这些:

```
section 1 of 1 of file rfax_man begin 644 rfax_man h5sg60BSxwp62+57aMLVTPK3i9b-t+5pGLKyPA-FxxuysvFs+BT8+o0dVsM24 hcZHRaWYEHRBGFGtqk-cMV7oqqQRzbobGRB9Kwc-pTHzCDSSMJorR8d-pxdqd hLWpvQWRv-N33mFwEicqz+UFkDYsbDvrfOC7tko5g1JrrSX0swhn64neLsohr h26K1mSxnS+TF1Cta8GHHQ-t1Cfp7nh-oZeFuVi5MEynqyzX8kMtXcAynSLQx hg4o56Pu4YUZHMqDGtczKeCwXU8PZEc4lY0FbDfFfgZpJFC-a-sHGLtGJgCMZ hksr6XNTedEUdVJqxOO5VaReoH68eEPJ2m6d9mKhlhVE7zw4Yru4DUWRCJH28 hyeth+l2I0gPnEfrTLwAc+-TPS0YKYY3K0np58gVPgdAN8RY7+rQfRDin9JSa hPG32WG7-rTl3uthvrnDO-wD09GDIRCniuoefs8UsfiWZOLq+0awOrQxAPM+C hxLwOJ9VUKwdn7dJduLn1KhBucvL1pr5lGiBFfUbL79cFFex+G27kT+fsQ7X5 h87mgPivWhDSQHKPXqpKGniDkYsIYpg66ZWbHp4PfcgtPukElDWENlQPSuNAQ hnboE4Bd8kyyokt67GgfGvBVS45sMFPtlgKRlG-QPFSgbMHujA3qYemxnuqGx hp97aXpdKpvAE8zx-oUzazoVFz32X3OxAuiWJhKEjaYKpM7f95yv1S62v+k++ + end sum —r/size 7468/769 section (from "begin" to "end") sum —r/size 36513/540 entire input file
```

> 看起来是一段xxencoded(http://en.wikipedia.org/wiki/Xxencoding)的文字.我们用在线xxencoded解码一下(http://www.webutils.pl/XXencode).得到了一个叫rfax_man的文件.

```
$ file rfax_man rfax_man: gzip compressed data, was "rfax_man.py", from FAT filesystem (MS-DOS, OS/2, NT), last modified: Thu Feb 6 17:52:39 2014, max speed
```

> 发现这是一个gzip文件:

```
gunzip < rfax_man > rfax_man_unzipped
```

> 得到的 rfax_man_unzipped 是个python脚本,得到flag

## flag

> CTF{4BDF4498E4922B88642D4915C528DA8F}
  