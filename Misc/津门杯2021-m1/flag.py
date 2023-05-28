line_list = []
for line in open('flag.txt', 'r').readlines():
    line = line.strip()
    line_list.append(line)

flag = ''
total = []
for i in range(1, 15):
    temp = []
    for line in line_list:
        if (',' + str(i) + ',1') in line:
            temp.append(line)
    total.append(temp)

for data in total:
    flag = flag + chr(int(data[-1].split('=')[-1].split(')')[0].replace('\'', '')))

print(flag)