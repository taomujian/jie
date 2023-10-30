from Crypto.Util.number import *

for line in open('data.txt', 'r').readlines():
    line = line.strip()
    line = int(line)
    print(long_to_bytes(line).decode(errors = 'ignore'))