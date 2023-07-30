#sage
from Crypto.Util.number import long_to_bytes

def string2bits(s):
    return [int(b) for b in s]

def bits2string(bs):
    s = [str(b) for b in bs]
    return ''.join(s)

if __name__ == '__main__':
    
    m = '01000101011000010111001101111001010011010110000101110100011010000101011101101001011101000110100001010011011000010110011101100101'
    
    print(bits2string(m))