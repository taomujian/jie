# MISCall

## 解题思路

> 下载附件,用binwalk查看文件,发现一个bzip文件,用foremost提取文件,得到一个zip文件,解压后里面有个flag.txt,但是flag.txt里面没有flag.解压zip文件时发现存在隐藏目录.git,查看提交历史,恢复之前的文件,得到一个s.py文件,运行得到flag.

```
tar -xjvf d02f31b893164d56b7a8e5edb47d9be5
git stash list
git stash show
git stash apply
```

> 需要注意的是执行git命令之前要把存在的flag.txt删掉再去执行

## flag

> NCN4dd992213ae6b76f27d7340f0dde1222888df4d3