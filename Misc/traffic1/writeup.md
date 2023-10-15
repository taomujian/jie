# Traffic1

## 解题思路

> 下载附件得到一个pcapng文件,wireshark打开.

> 打开后发现存在FTP和TLS2中协议的流量,分析FTP流量,获悉存在2个flag.zip文件,foremost获取到2个zip文件.

> 获取到的2个zip文件,发现一个是伪加密,一个是真加密.伪加密里面的文件内容是个假flag.

> 继续分析FTP的数据得到一个key.log的内容,这个文件可以解密HTTPS流量,导入wireshark中得到http流量

> 分析http流量发现存在一个zip文件,导出发现一个mp3文件,Audacity打开后,查看频谱图,得到一个key: AaaAaaaAAaaaAAaaaaaaAAAAAaaaaaaa!,是另一个zip文件的解压密码,解压得到flag.


## flag

> flag{4sun0_y0zora_sh0ka1h@n__#>>_<<#}
