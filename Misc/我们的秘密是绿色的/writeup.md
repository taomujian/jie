# 我们的秘密是绿色的

## 解题思路

> 下载附件得到一个文件,使用Oursecret这个工具用密码0405111218192526(图片中标绿部分)得到一个try.zip的压缩包

> 根据提示生日,爆破压缩包,最后密码为19950822,解压得到一个flag.zip文件,解压需要密码

> 把try.zip里的readme.txt压缩,使用ARCHPR明文攻击得到密码Y29mZmVl

> 解压后得到flag.zip,打开需要密码,用010editor查看发现为伪加密,修改标记位后打开flag.txt

> 栅栏解密,15栏时,解密结果为：qdqnclnpqn{z*@qdpwppe%rw__zdg}

> 凯撒密码解密得到最终flag

## flag

> flag{ssctf_@seclover%coffee_*}
