# 第四扩展FS

## 解题思路

> 下载附件得到一张图片

> binwalk+foremost得到一个压缩包,解压需要密码,不是伪加密,爆破无效.

> 查看图片属性,在备注发现一个单词Pactera,试了下,这个就是密码,解压得到一个txt文件,里面是一些字符.

> 根据题目提示频次有时候非常重要,仔细观察这些字符,发现其中重复出现了D、C、T、F、{、}等等,明显是要统计这些字符出现的频率,用python得到flag,得到DCTF{ka1f4NgxIntAi},题目有问题,提交的flag是DCTF{ka1f4NgxlntAi}

## flag

> DCTF{ka1f4NgxlntAi}
  