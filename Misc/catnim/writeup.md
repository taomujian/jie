# catnim

## 解题思路

> 打开在线场景.

> 这是尼姆博弈,只要满足每一轮拿掉物品之后的所有堆异或值为0即可,我的思路：设一共有n堆,让n-1堆先异或得到一个值xo,从剩下的那一堆拿掉一些值t,使其等于xo就行.如何选取剩下的那个值很重要,因为有时(很多时候),取的那个值小于xo,这就无法从里面取值,解决方案也很简单,就是从min开始遍历.

## flag

> cyberpeace{e6912aa1f417ad5cb94f02c47855ab88}