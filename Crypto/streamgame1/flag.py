from Crypto.Util.number import*

f = open('e05281b9394c4032b443f9793b76be2a/key','rb').read()
r = bytes_to_long(f)
bin_out = bin(r)[2:].zfill(12*8)
R = bin_out[:19]    #获取输出序列中与掩码msk长度相同的值
print(R)
mask = '1010011000100011100'  #顺序 c_n,c_n-1,。。。,c_1
key =  '0101010100111000111'

R = ''
for i in range(19):
    output = 'x'+key[:18]
    out = int(key[-1])^int(output[-3])^int(output[-4])^int(output[-5])^int(output[-9])^int(output[-13])^int(output[-14])^int(output[-17])
    R += str(out)
    key = str(out)+key[:18]

print('flag{'+R[::-1]+'}')