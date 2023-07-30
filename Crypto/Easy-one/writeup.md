# Easy-one

## 解题思路

> 下载附件,得到一个c文件和一些文件.

> 从c文件中可以看出,加密核心逻辑是这一行

```
c = (p + (k[i % strlen(k)] ^ t) + i*i) & 0xff;
```

> 直接运行c代码,发现加密结果不一样,说明代码中的key有改动,爆破出来这个key,一切就简单了.key可以通过明文(msg001)和密文(msg001.enc)得到

## flag

> CTF{6d5eba48508efb13dc87220879306619}

## 参考

> https://www.cnblogs.com/coming1890/p/13502960.html