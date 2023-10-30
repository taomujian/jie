# PyHAHA

## 知识点

> pyc隐写、pyc反编译、zip伪加密、DeEgger Embedder、base32隐写、OTP加密、二值图像

## 解题思路

> 下载附件,解压得到一个pyc文件,直接反编译失败.

> 010 Editor打开后发现galf字符,猜测是倒序了,用flag.py得到正序的文件,再次打开,发现少文件头03F30D0A,补上,反编译成功,且发现存在一个mp3文件.

> mp3文件用audacity没发现,用DeEgger Embedder获得了隐藏的文件,里面是许多base32编码字符,直接解码得到的东西不对,猜测隐写,尝试发现base32解码再编码后尾部不同.是有隐写了,用flag2.py得到隐写的数据.

> 分析反编译的python文件,encrypt实现的是一个256bit随机数生成器的功能,generate实现的是在有限域GF(2256)下的平方运算：new_key=(old_key+seed)<sub>2</sub>,flag1和flag2的密文在前面的zip注释信息已给出,脚本对三段明文使用了同个Seed做了加密,其中后两段明文和密文还有第一段的密文（在那大段的base32里）已知

> 考虑是OTP加密,先由后两段明文和密文算出 key2 和 key3,再在 GF(2256)下进行开方即可得到 seed,key3 = (key2+seed)<sub>2</sub>,再由第一段密文(即base32隐藏的数据)key1 和seed解得 key1,Key2= (key1+seed)<sub>2</sub>,最后对第一段密文(即base32隐藏的数据)和22次叠加的key1做异或得到原始二进制数据

> 最后解密得到一堆2进制字符,转换为图片,得到flag.

## flag

> flag{H4pPy_pY_C0dlng}

## 参考

> https://blog.csdn.net/weixin_44604541/article/details/112468128