# SM1

## 解题思路

> 下载附件,得到一个py文件和一些文件.分析python代码.

> 整个过程可分为生成ps、根据bchoose和ps生成r、用choose生成key对flag做AES加密得到ef

> 所以对应思路为根据ps和r得到bchoose、通过bchoose得到choose、然后解flag

```
r=0
for i in range(512):
    if bchoose[i]=='1':
        r=r^ps[i]
```

> 即𝑟=∑<sup>512</sup><sub>𝑖=1</sub>bchoose[i]⋅ps[i]
(此处的加法是异或)；虽然生成方式类似背包加密,但是由于ps具有很好的性质,我们不使用破解背包加密的方法来解此题；我们来分析生成ps的gen512num函数：

```
def gen512num():
    order=[]
    while len(order)!=512:
        tmp=randint(1,512)
        if tmp not in order:
            order.append(tmp)
    ps=[]
    for i in range(512):
        p=getPrime(512-order[i]+10)
        pre=bin(p)[2:][0:(512-order[i])]+"1"
        ps.append(int(pre+"0"*(512-len(pre)),2))
    return ps
```

> order是1,2,...,512的一个随机的排列,对ps[i]:首先生成一个长度为512-order[i]+10的素数,去掉此素数的最后10位,同时在尾部追加一个二进制位1,最后在后面填充0使得长度为512；我们首先考虑生成r的最后1个二进制位,ps中只有1个数最后1位为1,其余数最后1位均为0,那么最后1位为1的数如果没有"加入"异或运算,那么r的最后1位一定为0,否则,一定为1,这样我们通过r的最后1位就可以推断出bchoose的第j位(记order[j]=1)。接下来,𝑟⊕(bchoose[j]⋅ps[j])=∑<sub>𝑖≠𝑗</sub>bchoose[i]⋅ps[i]
,在{ps[i]| i≠
j}中,只有1个数倒数第2位为1,同理,可推断出bchoose的第k位(记order[k]=2),直到推断出bchoose所有位。

## flag

> flag{shemir_alotof_in_wctf_fun!}

## 参考

> https://www.cnblogs.com/coming1890/p/13547193.html