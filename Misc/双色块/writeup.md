# 双色块

## 解题思路

> 下载附件得到一个⼀个gif,binwalk分析发现尾部有png,拿出来是⼀个密码

> gif轮播之后发现是⼀个2424的像素点,每个像素为1010,每个点颜⾊为00ﬀ00或是ﬀ00ﬀ 先把gif分离成单帧

> 然后读取每个png中的对应点的信息,并按照8bit转换为ascii,然后进⾏DES解密即可得到flag


## flag

> flag{2ce3b416457d4380dc9a6149858f71db}

## 参考

> http://tool.chacuo.net/cryptdes
