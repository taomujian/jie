def xor(a, b):
    assert len(a) == len(b)
    c = b""
    for i in range(len(a)):
        c += bytes([a[i] ^ b[i]])
    return c

test = bytes.fromhex('6c34525bcc8c004abbb2815031542849daeade4f774425a6a49e545188f670ce4667df9db0b7ded2a25cdaa6e2a26f0d384d9699988f')
test_K = bytes.fromhex('8cf87cc3c55369255b1c0dd4384092026aea1e37899675de8cd3a097f00a14a772ff135240fd03e77c9da02d7a2bc590fe797cfee990')
K_M = bytes.fromhex('ec42b9876a716393a8d1776b7e4be84511511ba579404f59956ce6fd12fc6cbfba909c6e5a6ab3e746aec5d31dc62e480009317af1bb')

Lt = test[0:27]
Rt = test[27:54]

Kl = xor(test_K[0:27], Rt)
Kr = xor(Lt, xor(test_K[27:54], Rt))

Mr = xor(Kl, K_M[0:27])
Ml = xor(Mr, xor(Kr, K_M[27:54]))

print((Ml+Mr).decode(errors ='ignore'))

def string2bits(s):
    return [int(b) for b in s]

if __name__ == '__main__':
    initState = [0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0]
    outputState = string2bits('1010100001001011101000000100100001101011010100101011010101011010100100001110010010110111010111110000000000011011001110100011000111110100110011011011100111000000001100001000001011010011011010110110111100110101001110001001001000001110111011110001111001111111')
    states = initState + outputState
    
    ms = MatrixSpace(GF(2), 128, 128)
    mv = []
    for i in range(128):
        mv += states[i : i + 128]
    m= ms(mv)
    
    vs = MatrixSpace(GF(2), 128, 1)
    vv = outputState[0:128]
    v = vs(vv)
    
    secret = m.inverse() * v
    M=secret.str().replace('\n','').replace('[','').replace(']','')
    print(M)