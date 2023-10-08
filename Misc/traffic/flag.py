a = [144,150,139,145,165,91,109,151,122,113,106,119,93,167]
for i in range(-50,50):
    flag = ''
    for j in a:
        flag += chr(i+j)  
        if 'flag' in flag:
            print(flag)