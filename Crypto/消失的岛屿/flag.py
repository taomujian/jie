import base64

TABLE1 = "tuvwxTUlmnopqrs7YZabcdefghij8yz0123456VWXkABCDEFGHIJKLMNOPQRS9+/"

TABLE2 = ""
for i in range(0, len(TABLE1)): 
    if (ord(TABLE1[i]) >= 65 and ord(TABLE1[i]) <= 90):
        TABLE2 += chr(155 - ord(TABLE1[i]))
    elif (ord(TABLE1[i]) >= 97 and ord(TABLE1[i]) <= 122):
        TABLE2 += chr(ord(TABLE1[i]) - 64)
    elif (ord(TABLE1[i]) >= 48 and ord(TABLE1[i]) <= 57):
        TABLE2 += chr(ord(TABLE1[i]) + 50)
    elif (ord(TABLE1[i]) == 43):
        TABLE2 += chr(119)
    elif (ord(TABLE1[i]) == 47):
        TABLE2 += chr(121)
TABLE2 += '='
#注意最后添加“=”号
#print(TABLE2)

TABLE0 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/='

cip = "!NGV%,$h1f4S3%2P(hkQ94=="

cip_orgin=""
for i in cip:
    cip_orgin+=TABLE0[TABLE2.find(i)]
#print(cip_orgin)

flag = ""
flag = base64.b64decode(cip_orgin)
print(flag)