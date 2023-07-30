from Crypto.Util.number import bytes_to_long, getStrongPrime, getRandomRange, getRandomNBitInteger
from secret import flag


class CatCrypto():
    
    def get_p_q(self) -> tuple:
        def get_blum_prime():
            while True:
                p = getStrongPrime(self.nbits // 2)
                if p % 4 == 3:
                    return p

        p = get_blum_prime()
        q = 2
        while gcd(p-1, q-1) != 2:
            q = get_blum_prime()
            
        return p, q
    
    # KeyGen:
    def __init__(self, nbits=1024):
        self.nbits = nbits
        
        self.p, self.q =  self.get_p_q()
        p, q = self.p, self.q
        
        self.n = p * q
        n = self.n
        
        self.lam = (p-1) * (q-1) // 2
        
        self.g = self.n + 1
        
        x = getRandomRange(1, n)
        h = -x^2 
        self.hs = int(pow(h, n, n^2))

        
    # Enc(pk, -) = Epk(-):
    def enc(self, m: int) -> int:
        n = self.n
        hs = self.hs
        
        a = getRandomNBitInteger(ceil( n.bit_length() / 2 ))
        c = (1 + m*n) * pow(hs, a, n^2)
        return int(c)
        
    # Dec(sk, -) = Dsk(-):
    def dec(self, c: int) -> int:
        lam = self.lam
        n = self.n
        
        L = lambda x: (x-1)//n
        
        mu = inverse_mod(lam, n)
        m = L( int(pow(c, lam, n^2)) ) * mu % n
        return m
        
        
    @property
    def nbits(self):
        return self.__nbits
    
    @nbits.setter
    def nbits(self, nbits):
        self.__nbits = nbits

cat = CatCrypto(nbits=1024)

m = bytes_to_long(flag)
assert m.bit_length() < 1024

m1 = getRandomNBitInteger(m.bit_length() - 1)
m2 = getRandomNBitInteger(m.bit_length() - 2)
m3 = m - m1 - m2

c1 = cat.enc(m1)
c2 = cat.enc(m2)
c3 = cat.enc(m3)

print(f'dec(c1*c2) = {cat.dec(c1*c2)}')
print(f'dec(c2*c3) = {cat.dec(c2*c3)}')
print(f'dec(c3*c1) = {cat.dec(c3*c1)}')

"""
dec(c1*c2) = 127944711034541246075233071021313730868540484520031868999992890340295169126051051162110
dec(c2*c3) = 63052655568318504263890690011897854119750959265293397753485911143830537816733719293484
dec(c3*c1) = 70799336441419314836992058855562202282043225138455808154518156432965089076630602398416
"""