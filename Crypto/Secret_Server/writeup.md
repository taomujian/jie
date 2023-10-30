# Secret_Server

## 解题思路

>  在线场景已经打不开了
> 解法分为以下五步：

```
1.得到加密后的flag
2.根据hitcan{的长度与get-sha 相同获得第一的块
3.找出padding的长度
4.使用第三步,由于.strip() 去除了前后的\n ,可以得到第二块的前一半
5.从第二步重复,得到第二块的后一半
```

> aes-cbc模式,unpad函数会直接去除与最后一个字符相同的所有字符

> 每次消息都会在加密后再发出,但是：

```
我们会得到一些确定消息的加密形式,比如：`send_msg('Welcome!!')`和`send_msg('command not found')`
我们可以得到未知flag的加密形式
能够得到不同哈希函数的加密形式
```

```
if __name__ == '__main__':
    proof_of_work()
    with open('flag.txt') as f:
        flag = f.read().strip()
        assert flag.startswith('hitcon{') and flag.endswith('}')
    send_msg('Welcome!!')
    while True:
        try:
            msg = recv_msg().strip()
            if msg.startswith('exit-here'):
                exit(0)
            elif msg.startswith('get-flag'):
                send_msg(flag)
            elif msg.startswith('get-md5'):
                send_msg(MD5.new(msg[7:]).digest())
            elif msg.startswith('get-time'):
                send_msg(str(time.time()))
            elif msg.startswith('get-sha1'):
                send_msg(SHA.new(msg[8:]).digest())
            elif msg.startswith('get-sha256'):
                send_msg(SHA256.new(msg[10:]).digest())
            elif msg.startswith('get-hmac'):
                send_msg(HMAC.new(msg[8:]).digest())
            else:
                send_msg('command not found')
        except:
            exit(0)
```

> 第一步： 由IV控制得到加密的flag


> 注意aes-cbc的解密操作：!aes-cbc-
decryption(`https://camo.githubusercontent.com/505c573fe43b774715d54b3c632d801724cea242/68747470733a2f2f75706c6f61642e77696b696d656469612e6f72672f77696b6970656469612f636f6d6d6f6e732f322f32612f4342435f64656372797074696f6e2e737667`)

> 注意`P_i = D(C_i) ^ C_{i-1}`中的`C_0`是`IV`块.更改`C_i`的第`j`位会影响`P_{i+1}`的第`j`位,同时如过破坏`P_i`会导致`C_i`无效.然而,如果我们对`IV`这样做,就不会有什么问题,反正```IV`会被丢弃.

> 为了得到加密的的`flag`,我们需要把`IV + E('Welcome!!' + '\x07' * 7)`变成`IV2 + E('get-flag' + '\x08' * 8)`,这很简单.

```
P_1 = D(C_1) ^ IV 
P1bar = 'get-flag' + '\x08' * 8 
IV2 = IV ^ P1 ^ P1bar D(C1) ^ IV2 = D(C1) ^ IV ^ P1 ^ P1bar = P1 ^ P1 ^ P1bar = P1bar
```

> 于是我们就可以得到加密后的flag了.

```Python 
target = 'get-flag' + '\x08'*8 
source = 'Welcome!!' + '\x07'*7 
iv2 = '' 
for i in range(16): 
    iv2 += chr(ord(target[i]) ^ ord(source[i]) ^ord(iv[i]))
```

> 第二步. 通过IV控制得到第一块

> 我们现在得到了`IV + E(hitcon{......})`,根据flag以`hitcon{` 开始的事实,我们只要重复第一步中的技巧就可以得到第一个块.

> 鉴于`hitcon` 和 `get-sha` 的长度一致,只需要把`IV2 + E(get- sha......})`的最后一个字符改变256次,等到server返回值不是`send_msg('command not found')`时我们就得到了flag的前八个字符.

```python
(for char 8 of P1) D(C1) ^ IV2 = '1' and D(C1) ^ IV = P1 ==> P1 = IV ^IV2 ^ '1'
```

> 那么如何取得第九个字符呢？ 办法是把`get-sha`向右移一位.同时需要用`\n`补全左边空出的字符.重复这个过程,我们就得到了flag的第一块：`hitcon{Paddin9_1`

> 第三步,接下来要做的就是找出padding值,这对之后的几步都很重要.使用与第一步相似的步骤,对`get_md5`操作.在MD5中而不在sha1中的字符就是我们要找的flag长度.

```python 
(for char 16 of P3) D(C3) ^ C2bar = '41' and D(C3) ^ C2 = pad_value ==> pad_value = C2 ^ C2bar ^ '41'
```

> 第四步. 得到第二块的前一部分.这一步是对之前操作的综合. \- 我们现在已经知道了`P1`是十六位的,对比`IV2 + E('\n' * 9 + 'get-md5' + C2 + C3)`.我们可以改变`C2`的最后一个值,去影响`P3`的最后一个值,当unpad执行结束,除了`P2`的第一位,其他所有部分都被丢弃了,我们就可以得到`E(MD5(1st byte of P2))`.为了不破坏解密过程呢个,我们需要这样操作：`IV2 + E('\n' * 9 + 'get-md5' + C2 + C2 + C3)`. \- 对`IV2 + E('get-md5' + char + '\x08' *
8)`尝试所有256种情况,与之前密文对比,只要匹配,我们便得到了`P2`的第一个字符. \- 有了第一字,我们就可以继续下去.在丢弃一个字符,`IV2 + E('get-md5' + 1st char of P2 + char + '\x08' * 8)`会得到第二个字符.我们可以得到：`P2 ='5_ve3y_h4r'`.

> 第五步,接下来就是对第二步开始的重复.舍弃第一段,用`5_ve3y_`替换`hitcon{`.我们就可以得到最终的九个字符：`hitcon{Paddin9_15_ve3y_h4rd__!!}`

## flag

> hitcon{Paddin9_15_ve3y_h4rd__!!}

