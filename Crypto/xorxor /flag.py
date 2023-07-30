from os import urandom

# Get 前五个长度的key
str_hex = 'd8db4398596f9123f9b70d6847ad6e14e1ef5ff6220cfe4f96c5520731c81c78a645cdd1aa9b95e54468'
ans_line1 = bytes.fromhex(str_hex[:32])
ans_line2 = bytes.fromhex(str_hex[32:64])
flag_predict = b'XMan{'
key_predict = b''
for i in range(len(flag_predict)):
    key_predict += (ans_line1[i%16]^flag_predict[i]).to_bytes(1,'big')
    
print(key_predict)

# Get 第二组Flag的前五个长度
flag_predict_line2 = b''
for i in range(len(key_predict)):
    flag_predict_line2 += (ans_line2[i%16]^key_predict[i]).to_bytes(1,'big')
    
print(flag_predict_line2)

# Get 拼接Key
key = key_predict + ans_line2[5:]
print(key)

# Finally
flag_1 = b''
flag_2 = b''
for i in range(len(key)):
    flag_1 += (ans_line1[i%16]^key[i]).to_bytes(1,'big')
    flag_2 += (ans_line2[i%16]^key[i]).to_bytes(1,'big')
    
print(flag_1 + flag_2)