#原始加密文件目录位置
src_dir='enc'
#解密后存放目录位置
dst_dir='flag'

#解压后目录下的文件
files=$(ls  $src_dir)

#nums数组存储了000-268等宽的数字用于命名 
i=0
nums=()
for j in $(seq -w 268);do
        nums[$i]=$j
        ((i++))
done

n=0
for file in $files;do
        openssl rsautl -decrypt -inkey key -in $src_dir/$file -out $dst_dir/${nums[$n]}
        ((n++))
done

#合并图片

cat flag/* > flag.jpg