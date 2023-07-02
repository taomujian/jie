# Warmup

## 解题思路

> 下载附件得到一个zip文件,解压后发现是open_forum.png和一个加密压缩包,可以发现加密压缩包里也有一个open_forum.png,推测是明文攻击.

> 用winrar工具讲该png转为zip,打开ARCHPR工具,攻击类型为明文,选择对应的加密文件,明文文件选择open_forum.zip,开始攻击,然后会发现要爆破1小时,但是不需要等直接结束,然后保存解密压缩包,就可以正常打开里面的fuli.png和fuli2.png.

> 两张相似的图片,可能会想到用stegsolve中的combine,但是尝试后没有发现什么信息;改用工具Blind-Water-Mark,用法：python3 bwmforpy3.py decode fuli.png fuli2.png 2.png,得到的2.png就会出现flag.

## flag

> flag{bWm_Are_W0nderfu1}
