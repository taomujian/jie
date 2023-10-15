# 3-2

## 解题思路

> 下载附件解压后发现是一个轮播的gif图片,先把每一帧图片提取出来.

```
convert f151fa08fb984d7d861e72620b788639.gif flag.png
```

> 总共分离出来4个图片,发现每一张图片都不是全的,4张图片分别有1个角(大的方形块),把这4个图片合并成1个即可.

> 在线网站分析二维码图片,得到一串16进制字符,导入到010 Editor发现这是一个pyc文件,然后用uncompyle6 data.pyc得到py文件

> 调用py文件里面的2个函数,得到flag,python2运行能得到flag,python3会得到乱码,是因为python3的默认编码是utf-8导致.


## flag

> flag{U_r_Greatt!}

## 参考

> https://online-barcode-reader.inliteresearch.com
