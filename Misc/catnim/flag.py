from pwn import *
import copy

io = remote('61.147.171.105',61274)
print(io.recvuntil(b'Do you want just have a try,if you do that you can not get flag and without time limit(Y/N)?'))
io.sendline(b'N')
io.recvline()

while True:
        pile = io.recvline().strip()
        start = pile.find(b': ')
        piles = list(map(int,pile[start+2:].split(b' ')))
        # 浅拷贝
        piles_ = copy.copy(piles)
        print(piles_)
        piles.sort()
        print(piles_)
        j = 0
        while True:
            # 这里从最小一个数遍历，用最大数会超时
            min_num = piles[j]
            print('min',min_num)
            index = piles_.index(min_num)
            print('index',index)
            xo = 0
            ff = True
            for i in piles:
                if i == min_num:
                    if ff == True:
                        ff = False
                        continue
                xo = xo ^ i
            if min_num > xo:
                print('xo',xo)
                t = min_num - xo
                print('t',t)
                print(io.recvuntil(b'where:'))
                io.sendline(str(index).encode())
                print(io.recvuntil(b'count:'))
                io.sendline(str(t).encode())
                print(io.recvline())
                print(io.recvline())
                print(io.recvline())
                break
            j = j + 1
            print(j)