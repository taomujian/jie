# Flying_High

## 解题思路

> 下载附件得到一个文件,binwalk发现是一个tar文件,解压后有4个bin文件,file发现是UBIfs镜像,用ubi_reader工具进行挂载.

```
1、安装依赖:
wget http://www.oberhumer.com/opensource/lzo/download/lzo-2.10.tar.gztar -xvzflzo-2.10.tar.gz

cd lzo-2.10
mkdir build
cd build
cmake ..
make -j4
make install

2、安装python依赖

pip3 install python-lzo
pip3 install ubi reader

3、挂载

for i in ls *bin; do ubireader_extract_files $i -o extracted_$i; done.

```

> 发现生成四个文件夹,一个个点进去看,在extracted_image3.bin中(extracted_image3.bin/video/usb/)发现了一个视频文件,点开后发现flag

## flag

> HITB{96ac9a0458279711e5d61f10849e6c58}
