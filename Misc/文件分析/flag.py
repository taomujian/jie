data = open('a247926c049a4054a84785e4ec292fbe.docx', 'rb').read()
img_data = data[4365: 4365 + 0x110D]

with open('flag', 'wb') as writer:
    writer.write(img_data)