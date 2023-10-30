# In-plain-sight

## 解题思路

> 攻防世界有点奇怪,什么附件也没有.给出了AES的key,iv,但是没给出密文.

> 题目名为"就在眼前",除了给出的关于AES算法的信息外,我们破解的唯一难点就是密文的信息.既然题目说了就在眼前,那猜测密文为描述中要我们解密的HiddenCiphertext.疑惑的是,可以生成这种包含信息的密文吗,答案是肯定的,在一些文章中可以找到相似的理论.https://blog.skullsecurity.org/2016/going-the-other-way-with-padding-oracles- encrypting-arbitrary-data

> 直接解密得到flag.

## flag

>  1d010f248d