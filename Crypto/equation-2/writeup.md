# Equation-2

## 解题思路

> 下载附件,得到一个png和加密文件,png里面是部分RSA私钥,通过分析RSA私钥格式可以得知dp和dq,典型的dp和dq泄漏.

> 先把已给出部分进行base64解密,得到3acf6684e41176a5b673056b9cd23bd832dc017a57509d471b024100d5a225c0d41b16699c4471570eecd3dd7759736d5781aa7710b31b4a46e441d386da1345bc97d1aa913f853f850f6d4684a80e6067fb71cf213b276c2cbaed5902401338c593d3b5428ce978bed7a553527155b3d138aeac084020c0c67f54b953015e55f60a5d31386505e02e6122dad7db0a05ecb552e448b347adc2c9170fa2f3024100d5c8d6dc583ecdf3c321663ba32ae4ab1c9a2ded6702691993184209e93914f0d5adf415634788d5919d84a8d77429959d40fba47b29cf70b943124217c9a431

```
dp = d % (p - 1)
dq = d % (q - 1)
```

```
标签头  3082025c（4 bytes）   类型为SEQUENCE   后接 604 bytes
020100   INTEGER           长度为0                             内容为：VERSION
028181   INTEGER           长度为129 bytes              内容为：  n（modulus）
0203     INTEGER                长度为3 bytes                  内容为：  e（publicExponent）
028180   INTEGER              长度为128 bytes             内容为： d（privateExponent）
0241     INTEGER                  长度为65 bytes                 内容为：    p（prime1）
0241      INTEGER                 长度为65 bytes                  内容为：   q（prime2）
0241    INTEGER                    长度为64 bytes                 内容为：   d mod（p-1） exponent1 
0240      INTEGER                 长度为 64 bytes                 内容为：      d mod (q-1)  exponent2
0241      INTEGER                  长度为65 bytes                 内容为：      q -1 mod p    coefficient
```

> 那么根据关键的标签头进行划分之后，可以得到

```
3acf6684e41176a5b673056b9cd23bd832dc017a57509d471b
0241//d mod（p-1） exponent1 
00d5a225c0d41b16699c4471570eecd3dd7759736d5781aa7710b31b4a46e441d386da1345bc97d1aa913f853f850f6d4684a80e6067fb71cf213b276c2cbaed59
0240//d mod (q-1)  exponent2
1338c593d3b5428ce978bed7a553527155b3d138aeac084020c0c67f54b953015e55f60a5d31386505e02e6122dad7db0a05ecb552e448b347adc2c9170fa2f3
0241//q -1 mod p    coefficient
00d5c8d6dc583ecdf3c321663ba32ae4ab1c9a2ded6702691993184209e93914f0d5adf415634788d5919d84a8d77429959d40fba47b29cf70b943124217c9a431
```

```
d⋅e ≡ 1 mod (p−1)(q−1) # RSA的私钥计算公式
则有：
	d⋅e ≡ 1 mod (p−1) 与 d⋅e ≡ 1 mod (q−1) 
即：
	x1⋅e ≡ 1 mod (p−1) ，x2⋅e ≡ 1 mod (q−1)
换成表达式：
	(p-1)|(x1e-1)
	(q-1)|(x2e-1)

记：
	x1⋅e − 1 = r1⋅(p − 1)；
	
由于 x1 = d mod (p−1)，则x1<(p−1)；     # 这里的推论真的看不懂
几乎可以看做 x1⋅e = r1⋅(p−1)
必有 r1 < e
同理 r2 < e
故e取65537    # 此处一脸懵逼
```

> 可以求出p和q,从而解出flag.

## flag

> 0ctf{Keep_ca1m_and_s01ve_the_RSA_Eeeequati0n!!!}

## 参考

> https://zhuanlan.zhihu.com/p/461349946?utm_id=0

> https://blog.csdn.net/zippo1234/article/details/109881959

> https://blog.csdn.net/l8947943/article/details/122985632