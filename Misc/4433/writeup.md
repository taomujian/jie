# 4433

## 解题思路

> 下载附件得到一个jpg图片,用binwalk和foremost未能分离出有效信息,放到StegSolve里面,在Red plane 1里面发现一个二维码,得到一串莫斯编码的字符.

> 得到 …–.----…–…,但不知道怎么分割.根据题目名称尝试以4433进行手动分割,解码得到VYGUD,然而flag并不是这个,在摩斯电码中存在一些常用的缩写,VY代表VERY,GUD代表GOOD,所以正确的flag是VERYGOOD.

## flag

> flag{VERYGOOD}
