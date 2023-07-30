import base64
base64chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
base64=''
 
def deBase64(base64_):
    data=''
    Bytes=""
    num=0
    for i in range(len(base64_)):
        if base64_[i] == '=':
            data = "00"
            num -= 2
            #一个“=”可以隐藏2bit数据
        else:
            data = bin(base64chars.find(base64_[i]))[2:]
            #base64chars共64个数，二进制表示0111111，所以舍弃八位二进制的最高位
            Bytes += data.zfill(6)
            #不够六位二进制的前面补0，不断往后加成字符串
    return Bytes[num:]
    #返回隐藏的数据内容
 
with open('stego.txt','rb') as f:
    #rb：以二进制格式打开一个文件用于只读，文件指针将会放在文件的开头。这是默认模式
    flag = ''
    bin_str = ''
    for line in f .readlines():
        #readlines()方法用于读取所有行（直到结束符 EOF）并返回列表
        base64 = str(line,"utf-8").strip("\n")
        #去掉每行头尾空白
        if(not base64.count('=')):
            continue
        #该行无“=”则下一行
        bin_str += deBase64(base64)
        #将隐藏的内容拼接成字符串
    for j in range(0,len(bin_str),8):
        flag += chr(int(bin_str[j:j+8],2))
        #以字节为单位，将二进制转化为对应ASCII码字符
    print("flag{{{}}}".format(flag.strip(b'\x00'.decode())))
    #去除不可见字符显示