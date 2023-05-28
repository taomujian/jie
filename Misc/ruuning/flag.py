bytearray=b"njCp1HJBPLVTxcMhUHDPwE7mPW"

flag="flag{"

for i in range(len(bytearray)):
    if i % 2==0:
        c=bytearray[i]
        c-=1
        flag+=chr(c)

    else:
        c=bytearray[i]
        c+=1
        flag+=chr(c)

flag+="}"
print (flag)