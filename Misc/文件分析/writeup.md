# 文件分析

## 解题思路

> 下载文件得到一个docx文件,用binwalk发现存在图片,但是用binwalk和foremost都提取不出来,用python脚本提取.

> 提取出来的文件搜索字符串发现存在flag is (3ijnhygvfr)H

> 这个试了下,并不是真的flag.从(3ijnhygvfr)H可以发现所有的字符会在键盘上组成一个"W"字符的形状.

> 根据还原出来的图片可以找到一些线索.根据G代码和还原的零件图形可以看到整个刀片的行进轨迹是两次变相的三个W,再根据(3ijnhygvfr)H可以读出(3w)H的信息

> 3w hex之后得到flag为3377.

## flag

> flag<3377>
