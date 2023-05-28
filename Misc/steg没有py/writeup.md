# steg没有py

## 解题思路

> 根据题目提示,是stegpy隐写,安装stegpy, pip3 install stegpy

> stegpy Do_you_like_misc.png -p, 密码就是文件名,打开生成的txt,能看到一串字符以及affine仿射加密特征,求出a和b,去解密得到flag,根据提示flag有些字符是大写的,把flag中开头字母大写获得flag

## flag

> flag{4f71ne_C1ph3r_15_FFFFunny!!}

## 参考

> http://www.hiencode.com/affine.html
