import os
import zlib
import struct
import itertools

with open('flag.png', 'rb') as reader:
    bin_data = reader.read()

crc32key = zlib.crc32(bin_data[12:29]) # 计算crc
original_crc32 = int(bin_data[29:33].hex(), 16) # 原始crc
if crc32key == original_crc32: # 计算crc对比原始crc
    print('宽高没有问题!')
else:
    print("宽高被改了, 正在爆破宽高")
    for i, j in itertools.product(range(4095), range(4095)): # 理论上0x FF FF FF FF，但考虑到屏幕实际/cpu，0x 0F FF就差不多了，也就是4095宽度和高度
        data = bin_data[12:16] + struct.pack('>i', i) + struct.pack('>i', j) + bin_data[24:29]
        crc32 = zlib.crc32(data)
        if(crc32 == original_crc32): # 计算当图片大小为i:j时的CRC校验值，与图片中的CRC比较，当相同，则图片大小已经确定
            print(f"\nCRC32: {hex(original_crc32)}")
            print(f"宽度: {i}, hex: {hex(i)}")
            print(f"高度: {j}, hex: {hex(j)}")
            modified_chunk_data = bin_data
            modified_chunk_data = modified_chunk_data[:16] + struct.pack('!II', i, j) + modified_chunk_data[24:]
            os.remove('flag.png')
            with open('flag.png', 'wb') as writer:
                writer.write(modified_chunk_data)
            print(f"成功修改图片尺寸宽度为: {i} 高度为: {j}")
            break


