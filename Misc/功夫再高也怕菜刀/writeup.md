# 功夫再高也怕菜刀

## 解题思路

> 下载附件后,得到1个pcapng文件,wireshark打开,查看http流量,发现果然是菜刀webshell管理工具的流量,foremost分离得到压缩包,但是缺少密码,密码肯定就在流量中.第1150个数据包有点奇怪,跟随TCP流量包,发现了上传了奇怪的字符,发现是jpg图片,jpg格式是以:FFD8FF开头,以FFD9结尾
的.复制所有内容,用010 Editor导入16进制字符,改名后缀为jpg便可得到解压缩密钥,输入密钥到解压缩便可获得flag

## flag

> flag{3OpWdJ-JP6FzK-koCMAK-VkfWBq-75Un2z}