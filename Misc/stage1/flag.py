def flag():
    str = [65,108,112,104,97,76,97,98]
    flag = '' 
    for i in str:
        flag += chr(i)
    print(flag)

flag()