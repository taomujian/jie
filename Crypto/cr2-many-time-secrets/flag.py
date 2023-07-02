import Crypto.Util.strxor as xo
import libnum, codecs, numpy as np

def isChr(x):
    if ord('a') <= x and x <= ord('z'): return True
    if ord('A') <= x and x <= ord('Z'): return True
    return False


def infer(index, pos):
    if msg[index, pos] != 0:
        return
    msg[index, pos] = ord(' ')
    for x in range(len(c)):
        if x != index:
            if len(c[x]) > len(c[index]):
                c[index] = c[index].ljust(len(c[x]), b'\x00')
            elif len(c[index]) > len(c[x]):
                c[x] = c[x].ljust(len(c[index]), b'\x00')
            msg[x][pos] = xo.strxor(c[x], c[index])[pos] ^ ord(' ')

def know(index, pos, ch):
    msg[index, pos] = ord(ch)
    for x in range(len(c)):
        if x != index:
            if len(c[x]) > len(c[index]):
                c[index] = c[index].ljust(len(c[x]), b'\x00')
            elif len(c[index]) > len(c[x]):
                c[x] = c[x].ljust(len(c[index]), b'\x00')
                
            msg[x][pos] = xo.strxor(c[x], c[index])[pos] ^ ord(ch)


dat = []

def getSpace():
    for index, x in enumerate(c):
        res = []
        for y in c:
            if x != y:
                if len(x) > len(y):
                    y = y.ljust(len(x), b'\x00')
                elif len(y) > len(x):
                    x = x.ljust(len(y), b'\x00')
                res.append(xo.strxor(x, y))
                
        f = lambda pos: len(list(filter(isChr, [s[pos] for s in res])))
        cnt = [f(pos) for pos in range(len(x))]
        for pos in range(len(x)):
            dat.append((f(pos), index, pos))

c = [codecs.decode(x.strip().encode(), 'hex') for x in open('f331d71a103f49bc94c2cc7838c29a9c', 'r').readlines()]

msg = np.zeros([len(c), len(c[0])], dtype=int)

getSpace()

dat = sorted(dat)[::-1]
for w, index, pos in dat:
    infer(index, pos)

know(10, 21, 'y')
know(8, 14, 'n')

print('\n'.join([''.join([chr(c) for c in x]) for x in msg]))
key = xo.strxor(c[0], ''.join([chr(c) for c in msg[0]]).encode())
print(key)