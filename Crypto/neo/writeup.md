# Neo

## 解题思路

>  在线场景已经打不开了.

> 进入到一个界面发现一些base64编码的数据，显而易见这应当是一个aes加密,目前我们已知一个加密的id，以及iv,该种加密方式容易受到padding-oracle攻击

> 这是一种利用AES-CBC性质的攻击，即Pᵢ = Dec(Cᵢ, k) ⊕ Cᵢ₋₁,因为函数dec是双射的,所以对于改变的密文 C'ᵢ₋₁,存在有效的明文P'ᵢ₋₁ = Dec(Cᵢ₋₁, k),通过设置修改Cᵢ₋₁使得,C'ᵢ₋₁ = Cᵢ₋₁ ⊕ 0x0...1 ⊕ 0x0...0[guessed byte] 

> 我们可以确定P的相应位置的值,首先,我们定义一个oracle 如下: 

```python 
def oracle(payload): 
  global responses 
  r = requests.post('http://crypto.chal.csaw.io:8001', 
  data = {'matrix-id' : base64.b64encode(binascii.unhexlify(payload))}) 
  if 'Caught exception during AES decryption...' in r.text: 
    responses[payload] = False 
  else: responses[payload] = True
``` 

> 如果有填充错误，它将返回False，否则返回True,编写分析脚本

```
import requests
import base64
import binascii
import threading
import time
import string
import urllib.request
import copy

threads = 20
alphabet = ''.join([chr(i) for i in range(16)]) + string.printable
alphabet_blocks = [alphabet[i : i + threads] for i in range(0, len(alphabet), threads)]
data = 'vwqB+7cWkxMC6fY55NZW6y/LcdkUJqakXtMZIpS1YqbkfRYYOh0DKTr9Mp2QwNLZkBjyuLbNLghhSVNkHcng+Vpmp5WT5OAnhUlEr+LyBAU='
ciphertext = binascii.hexlify(base64.b64decode(data))[:]
offset = len(ciphertext) // 2 - 16

def flip_cipher(ciphertext, known, i):
    modified_ciphertext = copy.copy(ciphertext)
    for j in range(1, i):
        modified_ciphertext[offset - j] = ciphertext[offset - j] ^ ord(known[-j]) ^ i
    return modified_ciphertext

ciphertext = [int(ciphertext[i:i+2], 16) for i in range(0, len(ciphertext), 2)]
count, known = 1, ''

while True:
    print('Found so far:', [known])
    for block in alphabet_blocks:
        responses, payloads = {}, {}
        modified_ciphertext = flip_cipher(ciphertext, known, count)

        for char in block:
            modified_ciphertext[offset - count] = ciphertext[offset - count] ^ ord(char) ^ count
            payloads[''.join([hex(symbol)[2:].zfill(2) for symbol in modified_ciphertext])] = char

        for payload in payloads.keys():
            threading.Thread(target=oracle, args=(payload,)).start()

        while len(responses.keys()) != len(payloads):
            time.sleep(0.1)

        if True in responses.values():
            known = payloads[list(responses.keys())[list(responses.values()).index(True)]] + known
            alphabet_blocks.remove(block)
            alphabet_blocks.insert(0, block)
            count = count + 1
            break
```

> 运行后得到flag

## flag

> flag{what_if_i_told_you_you_solved_the_challenge}
