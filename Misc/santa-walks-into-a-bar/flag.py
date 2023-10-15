from PIL import Image
import pyzbar.pyzbar as pyzbar

filepath = 'a5d744fb06e04bacfde2e7b713054145\\list'
count = 1
data = '7ab7df3f4425f4c446ea4e5398da8847'
try:
    while True:
        path = "{}\\{}".format(filepath, data + '.png')
        img = Image.open(path)
        result = str(pyzbar.decode(img)[0].data.decode())
        data = result.split(' ')[5].replace("'", '')
        print(count, result, data)
        count += 1
except Exception:
    print("找到了")
    exit()
# goo.gl这个服务器已经关掉了，所以这里直接给flag，看的韩国老外博客知道的flag
# 3DS{I_h0p3_th4t_Y0u_d1d_n0t_h4v3_ch4ck3d_OnE_by_0n3}