from PIL import Image
import os
import bitstring

image_name = 'flag.jpg'
current_path = os.path.dirname(__file__)
with open(os.path.join(current_path,image_name),'rb') as f:
    bin_content = bitstring.Bits(f)
    im = Image.new("RGB",(1024,780),(255,0,0))
    pim = im.load()
    for i,val in enumerate(bin_content.bin):
        if val == '0':
            pim[i%1024,i/1024] = (0,255,0)
    im.save(os.path.join(current_path,'red_green.png'))


image_name = 'red_green.png'
current_path = os.path.dirname(__file__)
im = Image.open(os.path.join(current_path,image_name))
image_width = im.size[0]
image_height = im.size[1]
# load pixel
pim = im.load()
bin_result = ''
for row in range(image_height):
    for col in range(image_width):
        if pim[col,row][0] == 255:
            bin_result += '1'
        else:
            bin_result += '0'
with open(os.path.join(current_path,'result.jpg'),'wb') as f:
    f.write(bitstring.BitArray(bin=bin_result).bytes)