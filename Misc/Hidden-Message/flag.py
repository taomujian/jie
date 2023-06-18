import json, binascii
allData = json.load(open("flag.json", encoding='utf-8'))
d = "0b"
for data in allData:
    tmp = int(data["_source"]["layers"]["udp"]["udp.srcport"]) - 3400
    d += "1" if tmp == 0 else "0"
print(binascii.a2b_hex(hex(int(d, 2)).replace("0x", "")))