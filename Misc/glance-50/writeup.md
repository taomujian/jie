# Glance-50

## 解题思路

> 下载附件解压后发现是一个长的gif图片,很窄,先把gif分解开,kali的convert 命令可以分解图片

```
convert 9266eadf353d4ada94ededaeb96d0c50.gif flag.png
```

> 总共分离出来200个图片.使用montage合并图片

```
montage flag*.png -tile x1 -geometry +0+0 flag.png
```
> -tile 是拼接时每行和每列的图片数,这里用x1,就是只一行

> -geometry 是首选每个图和边框尺寸,我们边框为0,图照原始尺寸即可


## flag

> TWCTF{Bliss by Charles O'Rear}

## 参考

> https://tu.sioe.cn/gj/fenjie/
