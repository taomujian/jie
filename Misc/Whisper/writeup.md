# Whisper

## 解题思路

> 从下载附件,得到1个rar文件,1个png,1个exe文件.rar解压需要密码

> 这种情况,一般是hin 1.png里面藏着解压密码,因为文件名是提示.foremost文件失败,用binwalk -e提取出来很多list文件

> list文件(第一个list文件)打开是base64字符,解码保存,保存的这个文件binwalk发现有很多bzip2文件,再次binwalk -e.

> 使用Linux下的strings命令来搜索文件夹内中文本内容里面所含的关键字,找到了解压密码,用这个密码去解压压缩包看看

```
cat * |grep -a password
```

> 解压出一个flag.txt文件,里面放着flag

## flag

> ZCTF{Nightingale}
