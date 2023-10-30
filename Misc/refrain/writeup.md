# refrain

## 解题思路

> 下载文件得到一个perf.data文本,binwalk发现里面有很多so文件.

> 谷歌搜索显示,perf.data是perf工具(一个Linux分析器)的一种记录格式,安装perf,读取perf.data,并在终端中看到一些统计数据表,从分析结果中可以看到一些库和地址被调用.运行下面的命令:

```
perf report -D
```

> 读取到perf record中的库确切的版本.

```
0x6178 [0xa8]: event: 10
.
. ... raw event: size 168 bytes
.  0000:  0a 00 00 00 02 00 a8 00 e7 61 00 00 e7 61 00 00  .........a...a..
.  0010:  00 00 40 00 00 00 00 00 00 10 00 00 00 00 00 00  ..@.............
.  0020:  00 00 00 00 00 00 00 00 fd 00 00 00 00 00 00 00  ................
.  0030:  ad 5e 46 00 00 00 00 00 71 95 13 17 00 00 00 00  .^F.....q.......
.  0040:  05 00 00 00 02 18 00 00 2f 75 73 72 2f 6c 69 62  ......../usr/lib
.  0050:  2f 78 38 36 5f 36 34 2d 6c 69 6e 75 78 2d 67 6e  /x86_64-linux-gn
.  0060:  75 2f 49 6d 61 67 65 4d 61 67 69 63 6b 2d 36 2e  u/ImageMagick-6.
.  0070:  38 2e 39 2f 62 69 6e 2d 51 31 36 2f 63 6f 6e 76  8.9/bin-Q16/conv
.  0080:  65 72 74 00 00 00 00 00 e7 61 00 00 e7 61 00 00  ert......a...a..
.  0090:  43 be 7a 60 88 a8 00 00 00 00 00 00 00 00 00 00  C.z`............
.  00a0:  15 00 00 00 00 00 00 00                          ........

```

> 另一个有用的命令是perf report–header only

```
# cmdline : /usr/lib/linux-hwe-tools-4.10.0-42/perf record -e intel_pt// convert -font 
Courier text:- image.png
```

> 这告诉我们使用perf分析的确切命令： convert-font-courier-text:-image.png,一个imagemagick命令,从stdin读取文本(可能是标志)并将其呈现为png图像.

> 至于perf调用, Intel_pt//bit指的是Intel处理器跟踪,它是内核事件的一个来源,除其他外,它跟踪是否执行了每个条件分支.它的跟踪不会超过这个数量——很多数据实际上只是一个编码序列,表示TS(“taken”)和 NS(“nottaken”),可以在 perf report-d中看到,但是如果您有与命令使用的完全相同的可执行文件和库,这就足以完美地重建控制流,因为您无法跟踪他组装并随时知道下一个分支指令是什么.我在一台运行Ubuntu18.04的笔记本电脑上做了这个挑战,很快就得出结论,我没有同样的库.幸运的是,我有一个16.04的虚拟机,大部分都有,所以我可以在虚拟机中获得更好的性能报告.我还使用了perf脚本命令,该命令产生至少千兆字节的数据,但会将每个条件分支中涉及的名称和地址尽其所能地以类似这样的数百万行的格式报告,这些行可以被grep通过.

```
convert 32608 [002] 1659210.049834:         
 1     branches: 7f794df893e9 strcmp (/lib/x86_64-linux-gnu/ld-2.27.so) 
 =>              7f794df8a250 strcmp (/lib/x86_64-linux-gnu/ld-2.27.so)
```

> 现在,需要找出一个地方,在理论上,这些信息允许重建由convert绘制的文本.这并不容易.跟踪只显示条件分支,而不显示任何正在计算或传递的数据的值,而且很多时候不同的字符或不同的像素不会导致不同的控制流;它们将像其他字符或像素值一样传递.在对ImageMagick源进行了一段时间的挖掘,并在gdb中执行了一些convert的测试之后,我回到了FreeType库的调用中,特别是对 FT_glyph_to_bitmap的调用中,这是最有可能导致不同字符产生不同控制流的地方,尽管直到我真正编写代码时我才确定.那就行了.其思想是不同的字形将具有不同的笔画数量,并导致绘制的像素数量不同,这将改变控制流.

> 然而,即使有了这个想法,也很难通过每个字形的控制流来解释每个字符的重构.这可能需要对跨越数千条装配线的数百个分支之间的细微差异进行推理.相反,我们更愿意让计算机为我们做这项工作,在已知的明文中对相同的库运行相同的convert命令,并将我们记录的分支模式与那些分支模式进行比较.

> 不幸的是,虽然我可以在我的虚拟机上阅读性能报告,但我不能让IntelPT录制在其中工作,这并不奇怪,因为它必须在非常低的水平上与处理器交互才能工作.因此,我最终在我的主机笔记本电脑上找到并强制将libfreetype6降级为2.6.1-0.1ubuntu2.3,这与我的虚拟机中的版本完全相同,挑战也被记录在案.这足以让 Perf脚本找到它想要的符号,并让我们对给定记录进行引用记录,使每个字形具有相同的分支行为,至少在 libfreetype6中花费时间.

> ASLR意味着在两个地址之间进行分支的地址在运行时不会完全相同,但它仍然会保留地址 mod212,因此只需取所有相关地址的最后三个十六进制数字,就可以得到非常可靠的指纹.

> 经过大量的探索性grep,我找到了一个我喜欢的条件分支,它出现在某个0x132FT_Glyph_To_Bitmap上.我在perf脚本中为这一行和后面的一千行添加了grep(因为我假设 grep能够比随意编写的python脚本更有效地读取数百万行),然后用python脚本进行后处理以提取一些分支模式的哈希值,这可以与生成的哈希值进行比较.与给定的性能数据相同.我用一些非常简单的perf.data进行了测试,结果证实了相同的字母似乎有着相同的指纹(尽管在重复之前和之后,整个文本似乎被渲染了四次,但这并不难被忽略).

> 举个例子,这里是记录flag{aaabbbccddd}转换和后处理的结果,因为所有行都有数千个字符长,所以右侧的行被截断.除了末尾的哈希值之外,这些行看起来是相同的,因为它们直到中有数百个字符才会分开,但是结尾的哈希值让我们很容易看到相同和不同的分支行为.特别是,你可以看到feb2cf、01c5bc、20a3ce和115279每个重复三次,表明它们分别对应于glyphs a、b、c和d的渲染.然后您可以确认feb2cf仅在几行之前重新出现,对应于a的flag.整个过程重复了四次,由75A768包围和分隔,一开始还有一个别的1C418A,我不确定它的意义,但是由于这些哈希在做题记录的指纹中出现在相同的位置,我们不必担心它们

```
1c418a 132FTGTB 833FTRGI 8b2FTRGI 845FTRGI 875FTRGI f9d fd8 fcc
75a768 132FTGTB 833FTRGI 8b2FTRGI 845FTRGI 875FTRGI f9d fd8 fcc
43dffc 132FTGTB 833FTRGI 8b2FTRGI 845FTRGI 875FTRGI f9d fd8 fcc
92c2d1 132FTGTB 833FTRGI 8b2FTRGI 845FTRGI 875FTRGI f9d fd8 fcc
feb2cf 132FTGTB 833FTRGI 8b2FTRGI 845FTRGI 875FTRGI f9d fd8 fcc
6db238 132FTGTB 833FTRGI 8b2FTRGI 845FTRGI 875FTRGI f9d fd8 fcc
215a7d 132FTGTB 833FTRGI 8b2FTRGI 845FTRGI 875FTRGI f9d fd8 fcc
feb2cf 132FTGTB 833FTRGI 8b2FTRGI 845FTRGI 875FTRGI f9d fd8 fcc
feb2cf 132FTGTB 833FTRGI 8b2FTRGI 845FTRGI 875FTRGI f9d fd8 fcc
feb2cf 132FTGTB 833FTRGI 8b2FTRGI 845FTRGI 875FTRGI f9d fd8 fcc
01c5bc 132FTGTB 833FTRGI 8b2FTRGI 845FTRGI 875FTRGI f9d fd8 fcc
01c5bc 132FTGTB 833FTRGI 8b2FTRGI 845FTRGI 875FTRGI f9d fd8 fcc
01c5bc 132FTGTB 833FTRGI 8b2FTRGI 845FTRGI 875FTRGI f9d fd8 fcc
20a3ce 132FTGTB 833FTRGI 8b2FTRGI 845FTRGI 875FTRGI f9d fd8 fcc
20a3ce 132FTGTB 833FTRGI 8b2FTRGI 845FTRGI 875FTRGI f9d fd8 fcc
20a3ce 132FTGTB 833FTRGI 8b2FTRGI 845FTRGI 875FTRGI f9d fd8 fcc
115279 132FTGTB 833FTRGI 8b2FTRGI 845FTRGI 875FTRGI f9d fd8 fcc
115279 132FTGTB 833FTRGI 8b2FTRGI 845FTRGI 875FTRGI f9d fd8 fcc
115279 132FTGTB 833FTRGI 8b2FTRGI 845FTRGI 875FTRGI f9d fd8 fcc
215a7d 132FTGTB 833FTRGI 8b2FTRGI 845FTRGI 875FTRGI f9d fd8 fcc
75a768 132FTGTB 833FTRGI 8b2FTRGI 845FTRGI 875FTRGI f9d fd8 fcc
43dffc 132FTGTB 833FTRGI 8b2FTRGI 845FTRGI 875FTRGI f9d fd8 fcc
92c2d1 132FTGTB 833FTRGI 8b2FTRGI 845FTRGI 875FTRGI f9d fd8 fcc
feb2cf 132FTGTB 833FTRGI 8b2FTRGI 845FTRGI 875FTRGI f9d fd8 fcc
6db238 132FTGTB 833FTRGI 8b2FTRGI 845FTRGI 875FTRGI f9d fd8 fcc
215a7d 132FTGTB 833FTRGI 8b2FTRGI 845FTRGI 875FTRGI f9d fd8 fcc
feb2cf 132FTGTB 833FTRGI 8b2FTRGI 845FTRGI 875FTRGI f9d fd8 fcc
feb2cf 132FTGTB 833FTRGI 8b2FTRGI 845FTRGI 875FTRGI f9d fd8 fcc
feb2cf 132FTGTB 833FTRGI 8b2FTRGI 845FTRGI 875FTRGI f9d fd8 fcc
01c5bc 132FTGTB 833FTRGI 8b2FTRGI 845FTRGI 875FTRGI f9d fd8 fcc
01c5bc 132FTGTB 833FTRGI 8b2FTRGI 845FTRGI 875FTRGI f9d fd8 fcc
01c5bc 132FTGTB 833FTRGI 8b2FTRGI 845FTRGI 875FTRGI f9d fd8 fcc
20a3ce 132FTGTB 833FTRGI 8b2FTRGI 845FTRGI 875FTRGI f9d fd8 fcc
20a3ce 132FTGTB 833FTRGI 8b2FTRGI 845FTRGI 875FTRGI f9d fd8 fcc
20a3ce 132FTGTB 833FTRGI 8b2FTRGI 845FTRGI 875FTRGI f9d fd8 fcc
115279 132FTGTB 833FTRGI 8b2FTRGI 845FTRGI 875FTRGI f9d fd8 fcc
115279 132FTGTB 833FTRGI 8b2FTRGI 845FTRGI 875FTRGI f9d fd8 fcc
115279 132FTGTB 833FTRGI 8b2FTRGI 845FTRGI 875FTRGI f9d fd8 fcc
215a7d 132FTGTB 833FTRGI 8b2FTRGI 845FTRGI 875FTRGI f9d fd8 fcc
75a768 132FTGTB 833FTRGI 8b2FTRGI 845FTRGI 875FTRGI f9d fd8 fcc
43dffc 132FTGTB 833FTRGI 8b2FTRGI 845FTRGI 875FTRGI f9d fd8 fcc
92c2d1 132FTGTB 833FTRGI 8b2FTRGI 845FTRGI 875FTRGI f9d fd8 fcc
feb2cf 132FTGTB 833FTRGI 8b2FTRGI 845FTRGI 875FTRGI f9d fd8 fcc
6db238 132FTGTB 833FTRGI 8b2FTRGI 845FTRGI 875FTRGI f9d fd8 fcc
215a7d 132FTGTB 833FTRGI 8b2FTRGI 845FTRGI 875FTRGI f9d fd8 fcc
feb2cf 132FTGTB 833FTRGI 8b2FTRGI 845FTRGI 875FTRGI f9d fd8 fcc
feb2cf 132FTGTB 833FTRGI 8b2FTRGI 845FTRGI 875FTRGI f9d fd8 fcc
feb2cf 132FTGTB 833FTRGI 8b2FTRGI 845FTRGI 875FTRGI f9d fd8 fcc
01c5bc 132FTGTB 833FTRGI 8b2FTRGI 845FTRGI 875FTRGI f9d fd8 fcc
01c5bc 132FTGTB 833FTRGI 8b2FTRGI 845FTRGI 875FTRGI f9d fd8 fcc
01c5bc 132FTGTB 833FTRGI 8b2FTRGI 845FTRGI 875FTRGI f9d fd8 fcc
20a3ce 132FTGTB 833FTRGI 8b2FTRGI 845FTRGI 875FTRGI f9d fd8 fcc
20a3ce 132FTGTB 833FTRGI 8b2FTRGI 845FTRGI 875FTRGI f9d fd8 fcc
20a3ce 132FTGTB 833FTRGI 8b2FTRGI 845FTRGI 875FTRGI f9d fd8 fcc
115279 132FTGTB 833FTRGI 8b2FTRGI 845FTRGI 875FTRGI f9d fd8 fcc
115279 132FTGTB 833FTRGI 8b2FTRGI 845FTRGI 875FTRGI f9d fd8 fcc
115279 132FTGTB 833FTRGI 8b2FTRGI 845FTRGI 875FTRGI f9d fd8 fcc
215a7d 132FTGTB 833FTRGI 8b2FTRGI 845FTRGI 875FTRGI f9d fd8 fcc
75a768 132FTGTB 833FTRGI 8b2FTRGI 845FTRGI 875FTRGI f9d fd8 fcc
43dffc 132FTGTB 833FTRGI 8b2FTRGI 845FTRGI 875FTRGI f9d fd8 fcc
92c2d1 132FTGTB 833FTRGI 8b2FTRGI 845FTRGI 875FTRGI f9d fd8 fcc
feb2cf 132FTGTB 833FTRGI 8b2FTRGI 845FTRGI 875FTRGI f9d fd8 fcc
6db238 132FTGTB 833FTRGI 8b2FTRGI 845FTRGI 875FTRGI f9d fd8 fcc
215a7d 132FTGTB 833FTRGI 8b2FTRGI 845FTRGI 875FTRGI f9d fd8 fcc
feb2cf 132FTGTB 833FTRGI 8b2FTRGI 845FTRGI 875FTRGI f9d fd8 fcc
feb2cf 132FTGTB 833FTRGI 8b2FTRGI 845FTRGI 875FTRGI f9d fd8 fcc
feb2cf 132FTGTB 833FTRGI 8b2FTRGI 845FTRGI 875FTRGI f9d fd8 fcc
01c5bc 132FTGTB 833FTRGI 8b2FTRGI 845FTRGI 875FTRGI f9d fd8 fcc
01c5bc 132FTGTB 833FTRGI 8b2FTRGI 845FTRGI 875FTRGI f9d fd8 fcc
01c5bc 132FTGTB 833FTRGI 8b2FTRGI 845FTRGI 875FTRGI f9d fd8 fcc
20a3ce 132FTGTB 833FTRGI 8b2FTRGI 845FTRGI 875FTRGI f9d fd8 fcc
20a3ce 132FTGTB 833FTRGI 8b2FTRGI 845FTRGI 875FTRGI f9d fd8 fcc
20a3ce 132FTGTB 833FTRGI 8b2FTRGI 845FTRGI 875FTRGI f9d fd8 fcc
115279 132FTGTB 833FTRGI 8b2FTRGI 845FTRGI 875FTRGI f9d fd8 fcc
115279 132FTGTB 833FTRGI 8b2FTRGI 845FTRGI 875FTRGI f9d fd8 fcc
115279 132FTGTB 833FTRGI 8b2FTRGI 845FTRGI 875FTRGI f9d fd8 fcc
215a7d 132FTGTB 833FTRGI 8b2FTRGI 845FTRGI 875FTRGI f9d fd8 fcc
75a768 132FTGTB 833FTRGI 8b2FTRGI 845FTRGI 875FTRGI f9d fd8 fcc
```

> 然后我记录了一个这样的perf.data(数字是三倍的,如上所述,很容易注意到重复哈希值的三倍和稍微错误的正确位置)：

```
echo 'flag{abcdefghijklmnopqrstuvwxyz000111222333444555666777888999}'
sudo perf record -e intel_pt// convert -font Courier text:- image.png
```

> 这将在每个分支后的接下来几行中生成一个 0x132FT_Glyph_To_Bitmap.

```
perf script -i perf.data | grep "132 FT_Glyph_To_Bitmap" -A 1000 | python3 post1000.py > pout
```

> 在最后一步中用于生成所有上述文本转储的post1000.py脚本是以下非常简单的片段,对于从0x132FT_Glyph_To_Bitmap的每个分支,它提取mod-212地址以及完全在libfreetype中着陆的下一对分支的一些大写字母,希望人工检查将如果出了问题,可以恢复一些信息,然后对结果进行哈希值以便比较.没出什么问题,所以剩下的线没关系.(我们不希望超出libfreetype的分支是正在绘制的字母或glyph的确定函数-例如,如果libfreetype必须对任何内存进行malloc,则malloc中的控制流可能会混乱地依赖于先前在不同glyph或处理的不同部分上发生的各种分配.出于同样的原因,我们不希望在libfreetype控制流中每个分支0x132FT_Glyph_To_Bitmap后的1000个分支都停止在完全相同的位置,因此我们只弄乱随便一个前缀.)

```
import sys
import hashlib

def show(buf):
    s = ' '.join(buf)
    print(hashlib.sha256(s[:1000].encode('utf-8')).hexdigest()[:6] + ' ' + s)

line_buf = []

for line in sys.stdin:
    if "branches:" in line:
        _, rest = line.split("branches:")
        if "132 FT_Glyph_To_Bitmap" in rest and line_buf:
            show(line_buf)
            line_buf = []
        if rest.count("libfreetype") >= 2:
            tok1, tok2, *_ = rest.split()
            line_buf.append(tok1[-3:] + ''.join(c for c in tok2 if c.isupper()))

if line_buf:
    show(line_buf)
```

> 在这之后,我不再费心编写提取flag的脚本,只花了几分钟的时间手动比较从challenge perf.data生成的哈希与从已知的纯文本perf.data生成的哈希,并在vim中逐个标记flag的字符.

> 最后生成flag： flag{1df9e1d99ff7ea50bbe782492430b223}

## flag

> flag{1df9e1d99ff7ea50bbe782492430b223}

## 参考

> https://blog.vero.site/post/refrain