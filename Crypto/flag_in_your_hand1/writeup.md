# Flag_in_your_hand1

## 解题思路

> 下载附件,得到一个html文件和JS文件.分析代码发现无论在token输入框中输入什么字符串,getFlag()都会算出一个hash值,实际上是showFlag()函数中ic的值决定了hash值即flag是否正确.在script-min.js中找到ic取值的函数ck(),找到一个token使得ck()中ic =true即可.token是[118, 104, 102, 120, 117, 108, 119, 124, 48,123,101,120]每个数字减3得到的ascii码所对应的字符,即security-xbu,输入得到flag.

## flag

> RenIbyd8Fgg5hawvQm7TDQ

