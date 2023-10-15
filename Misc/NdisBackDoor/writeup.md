# NdisBackDoor

## 解题思路

> 下载附件得到2个文件.

> 实现一个NDIS过滤驱动监听本地数据包,模仿后门监听程序,如果是符合条件的后门激活指令(满足矩阵乘法结果),则显示相应信息.

```
1、NDIS过滤驱动的安装方式,为了安装方便,驱动和inf文件需要同时发布(见解题步骤1).
2、通过MmGetSystemRoutineAddress函数动态获取KdDisableDebugger函数地址进行反调试,较为隐蔽.
3、内核态动态获取kdbazis.dll或kdcom.dll基址,遍历导出函数KdSendPacket函数地址进行反调试,较为隐蔽.
4、对后门激活ICMP数据包中的矩阵进行rot13及模余变幻,直接获取原状态矩阵较为麻烦.

解法：反调试,逆向解密算法,通过icmp发送flag,即可
```

## flag

> F1aG{Tl-1e-Quieter-y0u-become T1-le-mOre-yOu-Are-abIe-To-1-1ear}

## 参考

> https://www.jianshu.com/p/04ef45f4b243
