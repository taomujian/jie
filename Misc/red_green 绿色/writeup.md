# Red_green 绿色

## 解题思路

> 下载附件得到一个文件,010 Editor打开,发现是一张图片

> 使用winhex看并没有发现flag信息,binwalk和foremost分解也分解不出任何东西

> 使用Stegsolve不断变化通道查看也无任何信息

> 使用Stegsolve分析功能-data extract功能,勾选红、绿、蓝的低位看也找不到有用信息,结合题目的red-green提示,可能需要两两结合或者单独勾选通道看,最后勾选Red通道时看到JFIF的开头,怀疑是一张图片,最后save bin导出命名为.png结尾的文件。

> 打开图片发现flag

## flag

> flag{134699ac9d6ac98b}
