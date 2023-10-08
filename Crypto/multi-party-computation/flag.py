import random
import requests
from Crypto.Util import number

def L(x, n):
    return (x-1) // n

def paillier_keygen():
    # Returns (pk, sk)
    p = number.getStrongPrime(512)
    q = number.getStrongPrime(512)
    n = p * q
    lam = (p - 1) * (q - 1) // 2  # Use integer division in Python 3
    while True:
        g = random.randrange(n ** 2)
        if number.GCD(g, n) != 1:
            continue
        mu_inv = L(pow(g, lam, n ** 2), n)
        if number.GCD(mu_inv, n) != 1:
            continue
        mu = number.inverse(mu_inv, n)
        break
    return (n, g), (lam, mu)

def paillier_encrypt(pk, m):  # Changed parameter format
    while True:
        r = random.randrange(pk[0])  # Use the first element of pk (n)
        if number.GCD(r, pk[0]) == 1:
            break
    return (pow(pk[1], m, pk[0] ** 2) * pow(r, pk[0], pk[0] ** 2)) % (pk[0] ** 2)

def paillier_decrypt(pk, sk, c):  # Changed parameter format
    return (L(pow(c, sk[0], pk[0] ** 2), pk[0]) * sk[1]) % pk[0]  # Use the first element of pk (n) and the second element of sk (mu)

if __name__ == "__main__": 
    (n, g), (lam, mu) = paillier_keygen() 
    poly = [paillier_encrypt((n, g), 0)] 
    res = sorted([paillier_decrypt((n, g), (lam, mu), x) for x in requests.post('http://54.191.171.202:1025/', json={'n': n, 'g': g, 'poly': poly}).json()])
    print(res) 
    res = ''.join(map(lambda x: chr(x % 256), res)) 
    print(res) 
    print(set('FLAG{Monic polynomials FTW}') == set(res))
