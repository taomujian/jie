# 删库跑路

## 解题思路

> 从下载附件,根据题目提示,猜测是binwalk,解压得到一个8091000文件,直接010 Editor打开看到flag

```
binwalk -e vm-106-disk-1.qcow2
```

## flag

> flag{c28c424b-fd8c-45b9-b406-0a933b1ca7b1}
