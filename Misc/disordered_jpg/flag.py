f1=open('3a13f19128074c2b9a909f1c08b4b3f6.jpg','rb').read()
f2=open('flag.jpg','ab+')
for i in range(0,len(f1),4):
	f2.write(f1[i:i+4][::-1])
f2.close()