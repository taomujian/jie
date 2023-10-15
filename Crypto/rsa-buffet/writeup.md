# Rsa-buffet

## 解题思路

> 下载附件得到2个py文件和其他的文件.

> generate-plaintexts.py这个文件是用message1.txt-message5.txt来生成plaintext-1.txt-plaintext-5.txt.

> encrypt.py文件有对应的加解密函数,用随机生成的RSA公钥和明文作为参数传递给加密函数,加密函数随机生成一个对称密钥,用公钥加密随机生成的对称密钥得到一个消息头,随机生成一个iv,用AES的CFB模式、对称密钥和这个iv去加密明文,得到消息题,最后用消息头+iv+消息体作为加密后的结果返回.要想解密就得有随机生成的RSA私钥才行,有了RSA私钥就能解密消息头得到对称密钥,其中iv已知,又知道对称密钥,就可以得到明文消息了.

> 用GitHub上的https://github.com/RsaCtfTool/RsaCtfTool工具尝试恢复私钥,得到了key-1.pem、key-2.pem、key-3.pem所对应的私钥,经过尝试发现分别解开对应的ciphertext-5.bin、ciphertext-1.bin、ciphertext-4.bin,得到三段字符

> 接下来就是Shamir秘密共享解密得到flag.

```
pip3 install secretsharing
```

## flag

> FLAG{ndQzjRpnSP60NgWET6jX}
