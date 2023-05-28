import requests

url = "http://61.147.171.105:64223/shop?page="

for i in range(1000):
    response = requests.get(url + str(i))
    if "lv/media/task/writeup/cn/bilibili/6.png" in response.text():
        print(i)
        break
    
