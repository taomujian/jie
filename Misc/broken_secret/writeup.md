# broken_secret

## 解题思路

> 下载附件得到一个pdf文件

> 首先打开pdf报错会发现里面的obj全部都变成了@bj

```
1 0 @bj
<<
    /Type /Catalog
    /AcroForm 5 0 R
    /Pages 2 0 R
    /NeedsRendering false
    /Extensions
    <<
        /ADBE
        <<
            /ExtensionLevel 3
            /BaseVersion /1.7
        >>
    >>
>>
end@bj
```

> 将这一步修复好之后,使用pdfstreamdumper就能够查看内部的内容了

![1](jpg/1.jpg)

> 不过发现这里存在两个object,其中一个里面写了很多文字,另一个则是一个图片,看上去被js加密了,所以我们这里需要想办法将图片解密开来.一种办法是直接将这段代码dump出来,或者我们可以选择修复pdf.如果我们现在尝试打开pdf的话,会发现此时打印的是一段假的flag,提示我们要去寻找入口.此时会发现xfa没有发生渲染,注意到在obj1中的render为false,我们需要改成true：

```
1 0 0bj
<<
    /Type /Catalog
    /AcroForm 5 0 R
    /Pages 2 0 R
    /NeedsRendering true
    /Extensions
    <<
        /ADBE
        <<
            /ExtensionLevel 3
            /BaseVersion /1.7
        >>
    >>
>>
end0bj
```

> 之后尝试打开pdf,就能见到一段和protein介绍有关的内容,这段内容提示了之后图片的含义,这里先记下来

![2](jpg/2.jpg)

> 之前我们注意到,还有一个对象,但是引用表中,有效的只有6项,第七个obj展示不出来：

```
0000000000 65535 f 
0000000019 00000 n 
0000000137 00000 n 
0000000336 00000 n 
0000000487 00000 n 
0000000706 00000 n 
0000000732 00000 n 
```

> 这里有一个小技巧,这里把第7个obj的编号改成6,即可展示6的图片

![3](jpg/3.jpg)

> 根据前面对文章dna=>rna=>protein的描述,每3个密码子可以编码为一个氨基酸,每种氨基酸都有一个英文字母的缩写,刚好有二十来种,起源于一张老图如下

![4](jpg/4.jpg)

> 例如其中的最开始的CAU,对应的就是CAT（同CAU-组氨酸),为H,故有HAPPYNEWYEAR

![5](jpg/5.jpg)

> 拿出基因序列为
AUCUAGAGGGAAGCUCUGCUGUACUAGAUGAUUUCGUCGUAGACUCACGAAUAGGAACUGGAUGAAAGGUAGGAUGCUUAC
可以在线解密https://skaminsky115.github.io/nac/DNA-mRNA-Protein_Converter.html也可以用脚本写翻译脚本

## flag

> flag{I_REALLY_MISS_THE_ELDER_DAY}
