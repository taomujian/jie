# Hidden Write

## 解题思路

> 下载附件得到一个png图片,打开图片有水印的提示.

> zsteg发现存在额外数据,提取出来

```
zsteg -E "extradata:0" maomao1.png > 1.png
```

> 010 Editor打开,发现缺少PNG文件头,手动补全,得到一张和maomao1.png一样的图片,用盲水印解密得到一张图片,打开发现存在903ef}这个字符串.

```
python2 bwm.py decode maomao1.png 1.png flag.png
```

> 对这个1.png继续进行zsteg,发现另一张图片,仍然是进行PNG头修复,然后对这个修复后的图片继续进行zsteg得到hxb2018{490fe1033073e985这一段字符.

> 用010 Editor打开maomao1.png时,发现尾部存在ef4526a41ea这段字符,把所有得到的字符进行拼接得到flag.

## flag

> hxb2018{490fe1033073e985ef4526a41ea903ef}
