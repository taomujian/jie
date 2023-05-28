# Baby_Web

> 目录扫描,SSRF

## 思路分析

> 打开网址,提示不是内部用户,然后一直尝试伪造请求头,一直无果.这次忘记扫描目录了,扫描目录能发现一个ssrf.php的页面,能输入一个地址,直接输入file://flag获取flag.话说CTF题目真是越来越看不懂了.

## payload

> http://61.147.171.105:54204/ssrf.php?url=file%3A%2F%2Fflag

## flag

> cyberpeace{eef1b1ac44d33fb61f4f16dc8747540c}