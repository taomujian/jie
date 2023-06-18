# Recover-Deleted-File

## 解题思路

> 下载附件,得到一个文件,题目提示要恢复文件,通过fls列出该文件有哪些文件及操作记录,发现有一个flag文件,恢复出文件,执行文件,得到flag.

## payload

```
fls disk-image

extundelete disk-image --restore-all
```

## flag

> de6838252f95d3b9e803b28df33b4baa
