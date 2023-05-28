# 神奇的Modbus

## 解题思路

> 下载附件得到一个pcapng,用wireshark打开,筛选下modbus协议数据包,然后随意选择一个跟踪TCP流,发现有Easy_Mdbus字符,这个便是flag,不过flag中明显少了一个o字符,加上得到完整的flag

## flag

> sctf{Easy_Mdbus}
