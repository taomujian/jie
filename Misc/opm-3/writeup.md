# Opm-3

## 解题思路

> 下载附件,是一张图片.使用binwalk,没发现什么.查看十六进制,也没有发现什么附加内容.用zsteg发现存在LSB数据隐写,隐写的数据是一个zip文件,提取出来.

```
zsteg -e b1,rgb,lsb,xy a > a.zip
```

> 解压压缩包,发现里面是一个文本,打开是一些指令,结合文件名发现是ARM指令.

> 第一列在增加,因此它可能只是一个地址,右边的字节更有趣.创建了一个包含第二列的未连接(未尾)的新文件后,我们得到了一个ARM二进制文件(没有任何标头,只有汇编代码).在分析了代码之后,我们看到它接受了密码并检查它是否正确.该文件的很大一部分用于键检查功能.这也是非常重复的：大多数代码如下：

```
c7c:    e51b3050     ldr    r3, [fp, #-80]    ; 0xffffffb0
c80:    e3e0101a     mvn    r1, #26
c84:    e0030391     mul    r3, r1, r3
c88:    e0822003     add    r2, r2, r3
```

> 这意味着

```
c7c - load byte from password at position 80
c80 - r1=26
c84 - r3=r1*r3
c88 - r2+=r3
```

> r2+=password[80]*26,对每个密码字节重复此过程.然后将R2与常数进行比较.整个检查代码以不同的常数重复了几次,以确保密码是唯一的.我们很快看到密码是一个满足以下条件的字符串：

```
pass[0]*a00 + pass[1]*a01 + pass[2]*a02 ... = b0
pass[0]*a10 + pass[1]*a11 + pass[2]*a12 ... = b1
...
```

> 解析反汇编以获取a和b并不容易,例如,某些乘法被实现为逻辑移位.相反,我们使用可重定位的反编译器对代码进行了反编译.该代码看起来更好解析.我们选择了代码中有趣的部分来解压缩文件,并编写了将对其进行解析的Python代码.该代码在运行时为我们提供了答案：Tr4c1Ng_F0R_FuN!.

## flag

> flag{Tr4c1Ng_F0R_FuN!}