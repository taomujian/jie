# 达芬奇密码

## 解题思路

> 下载附件,得到1个exe文件.看雪系列,需要逆向.

> 此题是窗体程序，可通过字符串直接定位到按钮响应函数sub_401EA0。流程比较简单，先检查输入是16字节且不为0，然后进入主校验函数sub_4010E0进行校验，返回1则打印成功信息。

```
v1 = this;
 v7 = this;
 String[0] = 0;
 memset(&String[1], 0, 0x1FEu);
 v5[0] = 0;
 memset(&v5[1], 0, 0xFFu);
 CWnd::GetDlgItemTextW(v1, 1000, String, 20);
 if ( wcslen(String) == 16 )
 {
   v2 = 0;
   while ( !(String[v2] & 0xFF00) )
   {
     v5[v2] = String[v2];
     if ( ++v2 >= 16 )
     {
       v6 = 64;
       flOldProtect = 0;
       VirtualProtect(sub_4010E0, 0xD17u, 0x40u, &flOldProtect);
       if ( GetLastError() )
         return CWnd::MessageBoxW(v1, L"Wrong!", 0, 0);
       qmemcpy(sub_4010E0, sub_5647B8, 0x330u);
       VirtualProtect(sub_4010E0, 0xD17u, flOldProtect, &v6);
       if ( !GetLastError() )
       {
         v8 = 0;
         v8 = sub_4010E0();
         if ( v8 == 1 )
           return CWnd::MessageBoxW(v7, L"Congratulations! You are right!", 0, 0);
       }
       v1 = v7;
       return CWnd::MessageBoxW(v1, L"Wrong!", 0, 0);
     }
   }
 }
 return CWnd::MessageBoxW(v1, L"Wrong!", 0, 0);
```

> 主校验函数sub_4010E0在执行前被函数sub_5647B8覆写，大小为816字节，而sub_5647B8则在窗体初始化时在OnInitDialog函数中进行了改写，具体操作是与0xAB异或。

```
v1 = this;
CDialog::OnInitDialog(this);
SendMessageW(*((HWND *)v1 + 8), 0x80u, 1u, *((_DWORD *)v1 + 29));
SendMessageW(*((HWND *)v1 + 8), 0x80u, 0, *((_DWORD *)v1 + 29));
v2 = 0;
do
  *((_BYTE *)sub_5647B8 + v2++) ^= 0xABu;
while ( v2 < 0x330 );
```

> 真正的主校验函数看起来代码有点多，就不贴了，实际上就表示了一个式子，具体过程为：

&nbsp;&nbsp;1.输入作为两个64bits的整数，分别异或一个64bits的常量整数，得到X，Y
&nbsp;&nbsp;2.校验X > 0x100000000000000,Y > 0x100000000000000,X < 0x1000000000000000
&nbsp;&nbsp;3.计算XX,YY
&nbsp;&nbsp;4.校验XX-7Y*Y == 8

> 计算好久没出结果，最后拿出mathematica:

```
In[7]:= Solve[x^2 - 7*y^2 == 8 && x > 72057594037927936 && x < 1152921504606846976,{x,y},Integers]
 
Out[7]= {{x -> 385044246406735194, y -> -145533045678356702},
 
>    {x -> 385044246406735194, y -> 145533045678356702}}
```

> X，Y的hex值为5aa5e1b9b3f35705de38bdb288090502，与常量异或后得到原始输入：

```
>>> a='5aa5e1b9b3f35705de38bdb288090502'.decode('hex')
>>> b='16968CE381986E648408DC81BE4D484F'.decode('hex')
>>> for i in range(16):
...   print chr(ord(a[i])^ord(b[i])),
...
L 3 m Z 2 k 9 a Z 0 a 3 6 D M M
```

## flag

> flag{L3mZ2k9aZ0a36DMM}
