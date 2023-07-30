from os import urandom

def process(m, k):
    tmp = m ^ k
    res = 0
    for i in bin(tmp)[2:]:
        res = res << 1
        if int(i):
            res = res ^ tmp
        if res >> 256:
            res = res ^ P
    return res

def keygen(seed):
    key = str2num(urandom(32))
    while True:
        yield key
        key = process(key, seed)

def str2num(s):
    return int(s.hex(), 16)

P = 0x10000000000000000000000000000000000000000000000000000000000000425

src1 = 0xaf3fcc28377e7e983355096fd4f635856df82bbab61d2c50892d9ee5d913a07f
src2 = 0x630eb4dce274d29a16f86940f2f35253477665949170ed9e8c9e828794b5543c
src3 = 0xe913db07cbe4f433c7cdeaac549757d23651ebdccf69d7fbdfd5dc2829334d1b

fake_secret1 = "I_am_not_a_secret_so_you_know_me"
fake_secret2 = "feeddeadbeefcafefeeddeadbeefcafe"

k2 = src2 ^ str2num(fake_secret1.encode())
k3 = src3 ^ str2num(fake_secret2.encode())

kt = k3
for i in range(255):
    kt = process(kt, 0)

seed = kt ^ k2
print("SEED:", seed)
assert process(k2, seed) == k3

kt = k2
for i in range(255):
    kt = process(kt, 0)

k1 = kt ^ seed
print("K1:", k1)
assert process(k1, seed) == k2

m = k1 ^ src1
print(bytes.fromhex(hex(m)[2:]).decode("utf-8"))
