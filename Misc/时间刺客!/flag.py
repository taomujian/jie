import os
import re

# 获取当前目录下的文件列表
file_list = os.listdir('image')
time_strings = []

# 遍历文件列表，获取每个文件的修改时间并转换为字符串
for filename in file_list:
    time_string = os.path.getmtime('image/' + filename) * (10 ** 9)  # 将文件的修改时间转换为纳秒
    time_string = int(time_string) % (2 ** 64 - 1)  # 使用模运算（取余）操作符将时间戳限制在64位范围内，避免溢出
    time_string = int(time_string) / (10 ** 9)  # 将纳秒转换为秒，通过除以10的9次方（10^9）实现
    time_strings.append(str(time_string))

# 将修改时间字符串连接成一个字符串
time_string = ''.join(time_strings)
# 使用正则表达式提取1-129和40-99之间的数字
numbers = re.findall(r'1[0-2][0-9]|[4-9][0-9]', time_string)
int_numbers = [int(i) for i in numbers]
byte_array = bytes(int_numbers)
result = byte_array.decode()
print(result)

