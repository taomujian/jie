with open("flag.exe", "rb") as file:
    binary_data = file.read()

result_data = bytes(x ^ 0x37 for x in binary_data)

# 保存结果到一个新文件
with open("result", "wb") as output_file:
    output_file.write(result_data)

