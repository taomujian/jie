
def crc(x,y): 
    while(x>y): 
        l = len(bin(x)) - len(bin(y)) 
        t = int(bin(y)[2:]+'0'*l,2)
        x ^= t 
    return x 

m = 0 
for i in range(0x200): 
    if i < 100: 
        continue 
    if crc(0x24d8893ca584100,i) == 0x81 and crc(0x24d8845abf34100,i)== 0x19: 
        m = i 
        print(i) 
        break 

print(hex(crc(0x00024ddeadbeef4100,m)))
print(hex(crc(0x00024dbaada5554100,m)))