# B64

## 解题思路

> 下载附件,得到1个py文件

> 在这个server.py文件中,可以看出这是一个给定端口的TCP监听程序,可以在本地对它的执行过程进行分析.首先可以看出这是一个简单的菜单类型的应用,在程序开始时,它会生成一个随机的密钥,并且允许对自己定义的信息加密最终需要指出服务器段生成的随机数.接下来分析一下这个程序的执行细节.

> 它定义了一个setup函数,每一个新的连接产生时都会调用它.初始化的代码如下：

```python
N = 8 
MAX_TRIES = 1024

def gen_secret(): 
    return os.urandom(N)

def setup(self): 
    self.tries = 0 
    self.secret = gen_secret() 
```

> 由此可见,每一次连接都会自动生成一个八个的随机字,还会初始化一个计数器用于限制每一次连接中与server端的会话次数,使无法在secret有效时间内暴力破解它.

> 接下来看一下每一次会话的消息处理,也就是server是怎么对自己输入的message进行加密的：

```python 
self.request.send("What would you like me to decode?\n> ") 
answer = self.request.recv(len(self.secret)) 
decoded = decode(answer, self.secret) 
self.request.send("Alright, here is your answer: {}\n".format(decoded))
```

> 这是整个代码里最重要的部分,的消息与secret异或,加上一个偏移值再与256取模,最后把结果转换成一个字符串.来看一下剩余的编码过程：

```python 
b64chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/"  
for c in s: 
    if c in b64chars: 
        enc+=c 

if len(enc) % 4 == 1: 
    enc = enc[:-1] 
    
while len(enc) % 4 != 0: 
    enc+="=" 

return b64decode(enc)
```

> 在这里会发生一些奇怪的事情.所有经过异或后不属于base64字符的所有字符全部会被过滤掉,剩下的那些属于base64的字符会留下来.适当的补全和合法的长度用于避免出错.

> 知道在secret和自己输入哦字符串异或后返回的是合法的base64字符.需要在1024次回话内得到server生成的secret.理想状态下,会从服务器端得到6个字.这六个字是有八个字经由base64编码得来的,8个字是的输入信息和secret的长度.所以需要做的就是方向操作这个编码的过程,就可以得到secret了.用一下这一行代码就可以实现”解码“操作：

```python 
secret = ''.join(map(lambda c: chr(((ord(c[1])-64)%256)^ord(c[0])),zip(payload.decode('hex'), b64encode(server_response.decode('hex'))))).encode('hex')
```

> 这个算法不算麻烦,可以说是比较显而易见了...

> 现在碰到的哦问题是不总是这么幸运,server总是只回复两个或是没有字.必须首先保证发送的消息至少让server回复一定数量的字,然后更改的信息让它回复更过的字,也就是说让的信息与secret异或后得到更多的合法base64字.

> 在尝试不同字符串的时候,需要注意到一个问题.server端会截断长度为1或5的字符串到0或4.所以一旦得到了三个有效字时,就不可以仅仅增加一个message中的字.

```
'A' base64.b64decode('QUI=') 'AB' base64.b64decode('QUJD') 'ABC'
base64.b64decode('QUJDRA==') 'ABCD'
```

> 可以看出,输出字符`A`对应的解码前字符串是`QQ`（注意：`QQ`后的`==`是有server补全的,在实际的base64解码中,`=`只是用作补全作用,实际上,使用任何一个非base64字符都一样.）.`QQ`就是的输入与secret的结果.通过更改的输入可以得到`QUI`这个输出,这是`AB`的base64编码.还可以发现`QUJD`对应`ABC`.这个时候不可以和之前一样仅改变的输入的最后一个字,至少需要对最后两个字符进行更改.否则,如果异或结果是`QUJDX`,会被server截断为`QUJD`,永远无法得到其他的输出.

> 我发现可以循环地尝试所有的可能行性,但是这样会十分低效甚至无法在1024次回话内完成.幸运的是,可以直接重连server,直到在一开始就获得了四位的返回值.这样的活就只需要对最后的两个字符循环地尝试就可以得到一个六个字的返回值.总之一定要得到一个六位的返回值,这在使用base64编码是会变成八位字,也就是secret的长度.

> 接下来就是编写不断更改最终字符、测试反馈,知道得到48位,即12个十六进制位,即6个字.代码如下： 

```python 
def play_round(client, hex_payload): 
    recv(client) 
    client.send('1') 
    recv(client)
    client.send(hex_payload.decode('hex')) 
    a = recv(client).strip('\n') 
    while 'answer' not in a: 
        a = recv(client).strip('\n') 
        decoded = a[a.index(':')+2:].encode('hex') 
        print '==> %s' % hex_payload print '<== %s' %decoded 
    
    return decoded

while 1: 
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('flatearth.fluxfingers.net', 1718) ) 
    banner = recv(client)
    payload = '00' * 8 
    server_response = play_round(client, payload) 
    total = 1 
    if len(server_response) < 8: 
        time.sleep(0.5) 
        continue

    for i in range(0, 16, 2): 
        for hb in hex_bytes(): 
            if hb != '00':
                candidate = payload[0:i] + hb + payload[i+2:] 
                result = play_round(client, andidate)

    if len(server_response) == 12: 
        secret = ''.join(map(lambda c:chr(((ord(c[1])-64)%256)^ord(c[0])),zip(bytes.fromhex(payload),b64encode(bytes.fromhex(server_response))))).hex() 
        print(send_secret(client, secret))
        exit()

while 1: 
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect( ('flatearth.fluxfingers.net', 1718) ) 
    banner = recv(client)
    payload = '00'*8 
    server_response = play_round(client, payload) 
    total = 1 
    if len(server_response) < 8: 
        time.sleep(0.5) 
        continue
```

> 这段代码是用于不停的连接server向他发送00000000直到返回四个字为止.

```python
for i in range(0, 16, 2): 
    for hb in hex_bytes(): 
        if hb != '00':
            candidate = payload[0:i] + hb + payload[i+2:] 
            result = play_round(client, andidate)
```

> 循环每一个十六进制值,每一次更改一位.然后检查返回结果. 最后： 

```python 
if len(server_response) == 12: 
    secret = ''.join(map(lambda c:chr(((ord(c[1])-64)%256)^ord(c[0])),zip(bytes.fromhex(payload),b64encode(bytes.fromhex(server_response))))).hex() 
    print(send_secret(client, secret)) 
    exit()
```

> 得到了完整的六位字返回后,就可以根据之前的解码函数把得到的secret值发送给server从而得到flag.