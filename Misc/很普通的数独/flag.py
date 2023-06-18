# 此脚本用于从数独图片获取密码，有值为1，无值为0
import cv2
from PIL import Image

black = (0,0,0) # 黑色RGB
white = (255,255,255) # 白色RGB

# 获取给定路径图片的结果数组
def getBin(picPath):
    image = cv2.imread(picPath)
    height = image.shape[0]  # 图片宽度
    wide = image.shape[1]  # 图片高度
    formWide = (wide-6)/9  # 每一格宽度
    res = [] # 结果数组
    tem = '' # 暂存数组
    for i in range(9):
        for j in range(wide-6):
            px = image[int(i*(formWide-1)+(formWide/2)), j+3]
            if (px == white).all() and (j+3)%formWide > (formWide*3/4) and (j+3)/formWide > len(tem):
                tem += '0'
            if (px == black).all() and (j+3) % formWide > (formWide/4) and (j+3) % formWide < (3*formWide/4) and (j+3)/formWide > len(tem):
                tem += '1'
        res.append(tem)
        tem = ''
    return res

# 获取整合25张图片，获取最终结果
def getRes():
    tem = [] # 临时存储返回值
    res = [] # 存储结果数组
    for i in range(5):
        for j in range(5):
            picPath = 'dee83d60aeda4a8cae93c5aac8f8a2ff/' + str(i*5+j+1) + '.png' # 构造文件名
            tem = getBin(picPath)
            if len(res)==0:
                res = tem
            else:
                if len(res)==(i+1)*9:
                    for x in range(len(tem)):
                        res[(i*9)+x] += tem[x]
                else:
                    for x in range(len(tem)):
                        res.append(tem[x])
    return res

resList = getRes()
resImg = Image.new('RGB',(45,45))
# 绘制图片
for x in range(45):
    for y in range(45):
        if resList[x][y] == '0':
            resImg.putpixel((x,y),white)
        else:
            resImg.putpixel((x,y),black)
resImg.save('flag.png')