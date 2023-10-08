# Mysterious-GIF

## 解题思路

> 下载附件得到一个gif文件

> 上binwalk和foremost得到一个zip压缩包,解压得到一个temp压缩包,继续解压直接一个enc文件,此时用binwalk看下temp.zip这个文件,发现存在好多隐藏的enc文件,binwalk -e提取出来,从partaa.enc开始一直到partke.enc,共265个且都是256个字节

> 在gif图片中发现了一串16进制字符串,解码得到一串字符,这个像是RSA加密的密钥了,接下来就是用openssl进行解密

```
identify -format "%c" 382e5c74bb7b4214ac6b855e503a56b9.gif > hex.data
```

## flag

> FelicityIsFun