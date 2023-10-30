from pwn import *

""" 参考材料:
https://inst.eecs.berkeley.edu/~cs191/fa07/lectures/lecture22_fa07.pdf

这次是给V了个go的源码，模拟了超过100个炸弹，可能是哑弹，也可能是真弹。类似this
experiment(`https://en.wikipedia.org/wiki/Elitzur%E2%80%93Vaidman_bomb_tester`).
我们必须不能引爆任何一颗炸弹。我们可以使用2个光量子和一组量子门。

维基百科的文件描述了如何达到33%的概率，但我们需要连续100次猜测准确。

明显这是个量子魔术，如果你有这么一个链，Hadamard - 相移 - Hadamard - 可能的第bomb[n]块，你可以判断出哪些是真弹，
哪些是哑弹。

针对这4个块，我们一共做2000次这个链，每个“相移”是pi/2000的弧度。

因此，对于每个炸弹： 1. 发送(2000*4)做为num_gates 2. 发送Hadamard gate 3. 发送一个相称 pi/2000
4. 发送Hadamard gate 5. 发送bomb n的索引 6. 接收值（0：安全，1：真弹）

以此步骤，对112个炸弹重复，然后把真弹/哑弹的列表发送回去。

"""

context.endian = "big"
context.log_level = "INFO"

# How many Hadamard-phase-Hadamard-bomb blocks

bignum = 2000

# Gate types numbers are 0x70 + the gate index

hadamard = p8(0x70 + 4)

# Phase rotation is a 64-bit float

phase_rot = p8(0x70 + 6) + struct.pack("<d", math.pi/bignum)

# r = remote("54.202.194.91", 65535)

r = remote("127.0.0.1", 8001)

bombs = []

# for bomb in range(1): # testing

for bomb in range(14 * 8):
    log.warning("bomb %d"%bomb) # num gates
    r.send(p16(bignum * 4))

    for p_b in range(bignum):
        # log.info("block %d"%p_b)
        r.send(hadamard)
        r.send(phase_rot)
        r.send(hadamard)
        r.send(p8(bomb))
    measure_final = r.recv(1)
    # Add the bomb/not-bomb indicator to the list
    bombs += [0 if u8(measure_final) else 1]
    log.warning(hex(u8(measure_final)))

# 0 gates to stop getting gates

r.send(p16(0))

print(bombs)

def getbytes(bits):
    """Yield bytes from a list of bits

    This will sometimes? give more bytes than needed.

    I found this somewhere on stack overflow
    """
    bits = iter(bits)
    done = False
    while not done:
        byte = 0
        for _ in range(0, 8):
            try:
                bit = next(bits)
            except StopIteration:
                bit = 0
                done = True
            byte = (byte << 1) | bit
        yield byte

log.info("".join("o" if x else "X" for x in bombs))

# Up the log_level because I don't want to miss the flag

context.log_level = "DEBUG"

# Pack the bytes for the bombs and send

# Limit to 14 because the getbytes was doing something screwy

for b in list(getbytes(bombs))[:14]:
    log.info("sending %d"%b)
    r.send(p8(b))

log.info("Getting flag")
while True:
    print(r.recv(1))
