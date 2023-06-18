# Sherlock

## 解题思路

> 下载附件,得到一个txt文本,完全没思路.

> 仔细观察文本,发现文本中有很多故意加粗的大写字母,把大写的字符过滤出来

```
cat f590c0f99c014b01a5ab8b611b46c57c.txt | grep -o '[A-Z]' | tr -d '\n'
```
> 得到的字符为ZERO和ONE,分别用0和1代替,得到一串儿进制字符,再转换为字符得到flag.

## flag

> BITSCTF{h1d3_1n_pl41n_5173}
