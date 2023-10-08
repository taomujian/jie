import random

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        temp = a % b
        a = b
        b = temp
    return a

def getpq(n, e, d):
    p = 1
    q = 1
    while p == 1 and q == 1:
        k = d * e - 1
        g = random.randint(0, n)
        while p == 1 and q == 1 and k % 2 == 0:
            k /= 2
            y = pow(g, k, n)
            if y != 1 and gcd(y - 1, n) > 1:
                p = gcd(y - 1, n)
                q = n / p
        return p, q

n = 0x73cec712124b33c0294e01eb52e8c3cd2fe9ddbcbf457b3b950360063dfae42cbbe9855bd986bcfea0948fadfb252f5e2ff3c982ff47afb6596a496636f1fc5ecfe9f5db7620b23fe9e30d230aa9299ab9a78bfb5e0630fd1149259b2b2104ea65d2e27b89785e4bf01d0594d9f94575cbcc3383f63c5aabe4d5b48eb761cce3ab21689b3f3155b5f15efee240d5ac149318ff80bd72a75fccdc57402aa197b472d98758019df8e9edb31bda82967dc66bcad845df824775eeb66ee304664d7929e8405122f9b0a5406887729dbe9760eb62dd7018087723c07c07082d1d51035fb211a9fc6d8fb5b3ee5bb91af5e3d0b89addce289041a5683a1fe7dc06a3bae283062ba3febdd987b5ac9b9a8ae4b8b02b804accc0a413bb144680fd8d0d8d8bebe176e5a9121f7653c31ede984d234ccce50e688f7048a0bfdfc84004c006ae912c4d4e514c200883e8dabaeb4bf57a5f628eb4bd2e6688d9b7688bc3eed4ce03831be5044dedbd5fddc43a3274b26c990a0e444fcf4a607de59c4906dfd1ea111920c38b4a365c5838e9cf1a22b146aa7afbc6e2e29ebe35aee4bf4d2fbe186c0f359c71f80b8f6298ad38619168d5986a857f558017c546d6df896c690896601aabd48398e957b77ef0e15d6cda339050b74cda3328c34c889306d089efc95ff467a4a775d3e104642cd9819f002b5db8c5f39b4e8d1a83007276b8a0b7
e = 0x10001
d = 0x37f2646fd190ad1e9f95c50d97cf4590a21e1c766bfd382cafafa2bb41442ce9839aac47944e288de6abfec1b17be4675f492a47f3e600f85a3823df9299d32f46c8a372f39d961f9471914e257f55cf1ef3d7878783fc34b61e1d61da332879c8d9597b0f0dac988916ac349e1d73b615cfbfef778ceeccee4f63dc32b1b7d7213c9199b6acb1d8a5141c94d777a29b89f8e0aea457788eaa9ca43626a24c74ebab355c89e3747626d4899745d148500c91416c782f2b30c9332f5cd32a4d3144d2a407ce9acc00f99dc619d425586285350cff734cdba9d4fad636d7fcbabfa382965005d8343e36ffe72604e557bae5044435ad990b6dca6d922e64387cee4abc0574d2eeeb42dda977be1e1064f6a6b00e78db75a7bf8e6e0c2ac3c6a52b2e6670cad3c907d990e53a7a311ef7b097c7644ff6f2bf96573e47d33031eeabf22620bdbc254a8fff8b0fa6f90d320c45e8d9094c26401f78560e16f77d6e09bc219c9849f1b68dc84ed36eb0cec7df16c4672c16a6b704ef2185ce04539f08688b72d48f9491e55be0095ee74f9622e8ae6835381e2efcd520cd02d1eeeb09bc11ab75bc903053102bc92718f2bf8691561a40026e53e950674f712aaef8cc69360df54c1af8b1f4aef997371b8a108e9b193a51002fe8d61f3991153e7ebd9593d68cd03b2f252c3d9d7a5bf802dcd150bd86028bd3b07cb415b767d716c1
p, q = getpq(n, e, d)
print("p: " + hex(p))
print("q: " + hex(q))
