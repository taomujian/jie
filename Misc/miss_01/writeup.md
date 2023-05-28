# Miss_01

## 解题思路

> 下载下来直接就是一个带密码的压缩包,010查看发现可能是伪加密,因为第6位和7位的数据为0,用winrar打开压缩包,然后使用工具里面的修复压缩文件得到一个新的压缩包,打开得到一个doc文档和压缩包.打开doc文档,发现有隐藏字符,这是希尔加密加密的,解密得到一段字符: love and peaceee

> doc文件里的字符U2Fsd开头,这是Rabbit加密的,用love and peaceee解密得到base32编码的字符,解码后得到一串unicode字符,转换为中文得到新佛曰开头的字符,新佛曰解码得到Live beautifully, dream passionately, love completely.

> 用Live beautifully, dream passionately, love completely.当作密码解压fun.zip,得到一个wav文件,用Audacity打开文件,在fun选择频谱图,得到flag

## flag

> flag{m1sc_1s_funny2333}

## 参考

> http://www.atoolbox.net/Tool.php?Id=914
> http://www.jsons.cn/rabbitencrypt/
> https://www.bejson.com/encrypt/base32/
> https://www.bejson.com/convert/unicode_chinese/
> http://hi.pcmoe.net/buddha.html
