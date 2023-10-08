# Wireshark

## 解题思路

> 下载附件得到一个流量包文件,过滤所有http协议的数据包,导出http对象,发现有2个比较大的文件,010 Editor打开,发现是png图片,把多余的数据(png头为89504E470D0A1A0A,png尾为49454E44--IEND)删掉,保存为图片,得到2张png图片(从wireshark里面直接按照16进制数据再导入010 Editor保存png的方式不行,得到的图片不完整).

> 有一张图片是密钥的图案,还朝下,下面可能还有东西,爆破高度得到key:57pmYyWt

> 然后看到了第一个get请求了一个网站：tools.jb51.net/aideddesign/img_add_info,打开发现是一个在线图片加密解密工具,那么这道题可能是一道图片解密题,

> 把key和风景画图片拿到刚才得到的解密网站上去解密,然后就得到了一串16进制字符串格式的flag：

> 拿去base16解密就得到最后的flag了

## flag

> DDCTF{QEWokcpHeUo2WOfBIN7pogIWsF04iRjt}

## 参考

> http://tools.jb51.net//aideddesign/img_add_info
