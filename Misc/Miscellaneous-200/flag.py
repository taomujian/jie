from PIL import Image
#设置画布的大小
x = 503
y = 122
 
im = Image.new('RGB', (x, y))#建一个画布
with open('flag.txt') as f:#打开1.txt文件命名为f
    for i in range(x):
        for j in range(y):#遍历坐标值
            line = f.readline()#读取文件一行数据
            s = line.split(',')#以空格分开获得RGB颜色的十进制代码
            im.putpixel((i, j), (int(s[0]), int(s[1]), int(s[2])))#在对应的坐标上画上对应颜色的像素点
im.save('flag.jpg')#保存图片