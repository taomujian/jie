# Lazy_cryptanalyst

## 解题思路

> 下载附件,得到一个png图片.

> 从图片中可以看到这个就是密码替换,关键是要找到替换的规律.

> 明文数据为

```
bsxz xz om rxuvi. bsiri qri oqym gbsirz vxji xb, whb bsxz gyi xz oxyi. om rxuvi xz om wizb urxiye. xb xz om vxui. x ohzb oqzbir xb qz x ohzb oqzbir om vxui. fxbsghb oi, om rxuvi xz hzivizz. fxbsghb om rxuvi, x qo hzivizz. x ohzb uxri om rxuvi brhi. x ohzb zsggb zbrqxlsbir bsqy om iyiom, fsg xz brmxyl bg jxvv oi. x ohzb zsggb sxo wiugri si zsggbz oi. x fxvv. wiugri lge x zfiqr bsxz kriie: om rxuvi qye omzivu qri eiuiyeirz gu om kghybrm, fi qri bsi oqzbirz gu ghr iyiom, fi qri bsi zqpxgrz gu om vxui. zg wi xb, hybxv bsiri xz yg iyiom, whb ciqki. uvql xz q eqm fxbsghb wvgge xz vxji q eqm fxbsghb zhyzsxyi. qoiy.
```

> 根据图片上的To Crack a Substitution Cipher谷歌搜索到这是一个密码替换工具,把密文复制进去,然后猜测密文字符对应的明文字符,就可以在右侧看到模糊的明文.测测有意义的字符,猜测其中有串字符是flag is,得到变换关系,就可以得到flag.

## flag

> a day without blood is like a day without sunshine

## 参考

> https://www.simonsingh.net/The_Black_Chamber/substitutioncrackingtool.html