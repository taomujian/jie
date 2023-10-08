
from pwn import *
import rstr
import exrex
from time import sleep
import re
 
# conect to server
r = remote('61.147.171.105', 58667)
 
# Print the question string
print(r.recvline())
 
# Counter
i = 1
 
while True:
	# Recieve the regex pattern
    reg = r.recvline()[:-1]
    print("%d -------\n"%i)
    print(reg)
    print("-------\n")
    ans = rstr.xeger(reg).replace('\n','') # Remove newlines!
    # ans=exrex.getone(reg).replace('\n','')  # Another possible option
    r.sendline(ans)
    i += 1
    sleep(0.2)