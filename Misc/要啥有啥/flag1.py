import sys

if len(key) % 2 == 1:
    print("KeyLengthError")
    sys.exit(1)

n = len(key) // 2
encrypted = ''
for c in flag:
    c = ord(c)
    key1, key2 = key[:n], key[n:]
    for a, b in zip(key1, key2):
        c = (ord(a) - c + ord(b)) % 251
        encrypted += '%02x' % c

print(encrypted)
