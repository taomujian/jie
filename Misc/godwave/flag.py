with open('data.txt', 'r') as f:
    data = f.readline()
    print(len(data))
    count = 0
    res = 0
    ans = bytearray()  # 使用 bytearray 来保存字节数据

    while data != '':
        pac = data[:2]
        if pac != '':
            if pac[0] == '0' and pac[1] == '1':
                res = (res << 1) | 0
                count += 1
            if pac[0] == '1' and pac[1] == '0':
                res = (res << 1) | 1
                count += 1
            if count == 8:
                ans.append(res)  # 将结果添加到 bytearray 中
                count = 0
                res = 0
        else:
            break
        data = data[2:]

with open('out.png', 'wb') as f2:
    f2.write(ans)
