from binascii import *

with open('206c0533300340b19c3a18d82d806a98.mp3', 'rb') as f:
	init_mpeg_hdr = 0x1c1b8
	mpeg_data_block = 0x0
	flag = ''
	while True:
		next_mpeg_hdr = init_mpeg_hdr + mpeg_data_block
		f.seek(next_mpeg_hdr)
		bin_data = bin(int(hexlify(f.read(4)), 16))[2:]
		flag += bin_data[23]
		mpeg_data_block += 0x414
		if int(str(next_mpeg_hdr), 16) > len(f.read()):
			break
	#print(flag) #二进制
	for i in range(0, len(flag), 8):
		try:
			res_flag = chr(int(flag[i:i+8], 2))
			print(res_flag,end="")
		except:
			pass