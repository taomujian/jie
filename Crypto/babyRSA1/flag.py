#!/usr/bin/env sage

import binascii
from pubkey import P, n, e
from sage.rings.integer import Integer
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing

R.<a> = GF(2^2049)

def encrypt(m):
    global n
    assert len(m) <= 256
    m_int = Integer(binascii.hexlify(m), 16)
    m_poly = P(R.fetch_int(m_int))
    c_poly = pow(m_poly, e, n)
    c_int = R(c_poly).integer_representation()
    c = binascii.unhexlify(format(c_int, '0256x').encode())
    return c

def decrypt(m, d):
    m_int = Integer(binascii.hexlify(m), 16)
    m_poly = P(R.fetch_int(m_int))
    c_poly = pow(m_poly, d, n)
    c_int = R(c_poly).integer_representation()
    c = binascii.unhexlify(format(c_int, '0256x').encode())
    return c

if __name__ == '__main__':
    p, q = n.factor()
    p, q = p[0], q[0]
    s = (2^p.degree()-1)*(2^q.degree()-1)
    d = inverse_mod(e, s)
    with open('flag.enc', 'rb') as f:
        ctext = f.read()
        print(decrypt(ctext, d))
