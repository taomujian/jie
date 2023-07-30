from secret import flag
from os import urandom

assert flag.startswith(b'XMan{' ) and flag.endswith(b'}')
key=urandom(16)

def padding(m):
    l = 16 - (len(m) % 16)
    return m+(b'\x00'*l)

flag=padding(flag)+urandom(10)

enc=b''
for i in range(len(flag)):
    enc+=(key[i%16]^flag[i]).to_bytes(1,'big')
print(enc.hex())

# d8db4398596f9123f9b70d6847ad6e14e1ef5ff6220cfe4f96c5520731c81c78a645cdd1aa9b95e54468



