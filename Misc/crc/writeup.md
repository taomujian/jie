# Crc

## 解题思路

> 下载附件得到一个zip文件,不是伪加密,爆破也没线索,题目名字为CRC,可知是CRC32碰撞,用crc32碰撞1.txt、2.txt、3.txt得到3个有意义字符,得到压缩包密码forum_91ctf_com_66

> 解压后在convert.txt中看到很多二进制字符,把字符转换为ASCII,得到base64格式的图片,转为图片得到二维码图片,扫描得到flag

## flag

> flag{owid0-o91hf-9iahg}

## 参考

> https://github.com/theonlypwner/crc32
