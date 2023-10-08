# Peoples-square-6

## 解题思路

> 下载附件

> 我们从解包和分析我们在挑战中得到的二进制文件开始.事实上,这个二进制文件并不适用于我们的电脑(不是每个人都有最新的笔记本电脑型号),但尽管如此,我们还是成功地对它进行了反编译.反编译结果只是分析的第一步,因为(自动反编译通常是这样)代码不太可读.很难分析：

```
const __m128i *__fastcall sub_4013C5(const __m128i *a1, __int64 a2)
{
  __m128i v2; // xmm0@1
  __m128i v3; // xmm0@2
  __m128i v6; // xmm0@4
  const __m128i *result; // rax@4
  signed __int64 i; // [sp+18h] [bp-98h]@1
  __int128 v11; // [sp+30h] [bp-80h]@1
  __int128 v12; // [sp+40h] [bp-70h]@1
  __int128 v13; // [sp+50h] [bp-60h]@1
  __int128 v14; // [sp+60h] [bp-50h]@2
  __int128 v15; // [sp+70h] [bp-40h]@2
  __int128 v16; // [sp+80h] [bp-30h]@4
  __int128 v17; // [sp+90h] [bp-20h]@4
  __int128 v18; // [sp+A0h] [bp-10h]@4

  v2 = _mm_load_si128((const __m128i *)a2);
  _mm_store_si128((__m128i *)&v12, _mm_loadu_si128(a1));
  _mm_store_si128((__m128i *)&v13, v2);
  _mm_store_si128(
    (__m128i *)&v11,
    _mm_xor_si128(_mm_load_si128((const __m128i *)&v13), _mm_load_si128((const __m128i *)&v12)));
  for ( i = 1LL; (unsigned __int64)i <= 3; ++i )
  {
    v3 = _mm_load_si128((const __m128i *)(16 * i + a2));
    _mm_store_si128((__m128i *)&v14, _mm_load_si128((const __m128i *)&v11));
    _mm_store_si128((__m128i *)&v15, v3);
    _XMM0 = _mm_load_si128((const __m128i *)&v14);
    __asm { aesenc  xmm0, [rbp+var_40] }
    _mm_store_si128((__m128i *)&v11, _XMM0);
  }
  v6 = _mm_load_si128((const __m128i *)(a2 + 64));
  _mm_store_si128((__m128i *)&v16, _mm_load_si128((const __m128i *)&v11));
  _mm_store_si128((__m128i *)&v17, v6);
  _XMM0 = _mm_load_si128((const __m128i *)&v16);
  __asm { aesenclast xmm0, [rbp+var_20] }
  _mm_store_si128((__m128i *)&v11, _XMM0);
  _mm_store_si128((__m128i *)&v18, _mm_load_si128((const __m128i *)&v11));
  result = a1;
  _mm_storeu_si128((__m128i *)a1, _mm_load_si128((const __m128i *)&v18));
  return result;
}
```

> 我们首先手动重构提供的代码,使之更易于管理.我们得出这样的结论：

```
__int64 realMain()
{
  char keyProbably;
  char ciphertextFor0[16];
  char ciphertextFor1[16];
  __int64 v14 = 0LL;
  __int64 v16 = 0LL;
  sub_400ABE(&v14); // put encrypted flag into buffer
  __int64 v10 = 0LL;
  sub_400A74(&v10);
  generateKey((const __m128i *)&v10, (__int64)&keyProbably);
  __int64 v6 = 0LL;
  __int64 initTime = time(0LL);
  for (__int64 i = 0LL; i <= 0x3FF; i++)
  {
    memsetAndEncrypt((__int64)&keyProbably, &ciphertextFor0, &ciphertextFor1, i, initTime);
    unsigned int v5 = rand() & 1;
    char *v1;
    if (v5) {
      v1 = &ciphertextFor0;
    } else {
      v1 = &ciphertextFor1;
    } 
    hexdump((__int64)v1, 0x10);
    puts("0 or 1?");
    user_bit = getchar() - 48;
    puts("ciphertext for 0 is: ");
    hexdump(&ciphertextFor0, 0x10);
    puts("ciphertext for 1 is: ");
    hexdump(&ciphertextFor1, 0x10);
    if ( user_bit == v5 )
    {
      puts("Correct!");
      ++v6;
    }
    else
    {
      puts("Incorrect!");
    }
  }
  if ( v6 == 1024 )
  {
    puts("Now I will give you the flag:");
    realEncrypt((const __m128i *)&v14, (__int64)&keyProbably); // decrypt flag
    realEncrypt((const __m128i *)&v16, (__int64)&keyProbably);
    hexdump((__int64)&v14, 0x20uLL);
  }
  return 0;
}

void memsetAndEncrypt(__int64 keyProbably, char ciphertext0[16], char ciphertext1[16], __int64 iter, __int64 initTime)
{
  memset(ciphertext0, 0, 0x10uLL);
  memset(ciphertext1, 1, 0x10uLL);
  memcpy((char *)ciphertext0 + 8,  &iter,     4uLL);
  memcpy((char *)ciphertext1 + 8,  &iter,     4uLL);
  memcpy((char *)ciphertext0 + 12, &initTime, 4uLL);
  memcpy((char *)ciphertext1 + 12, &initTime, 4uLL);
  realEncrypt((const __m128i *)ciphertext0, keyProbably);
  realEncrypt((const __m128i *)ciphertext1, keyProbably);
}

void realEncrypt(__m128i *a1, __m128i *key)
{
  __int128 state;

  *state = a1 ^ key[0];
  for (int i = 1LL; i <= 3; ++i) {
    *state = aesenc(state, key[i];
  }
  *a1 = aesenclast(state, key[4]);
}
```

> 如果与我们之前的相比(例如,我之前粘贴的函数现在称为“realEncrypt” 没错,重构后的代码只有4行).可以看到,所有这些代码只是AES加密一些数据.realcrypt确实是传统的AES,但它只使用了4轮,而不是10轮,因为AES128应该是正确的(只有因为它,我们才能够破解它).重申一下,在伪代码中,我们的程序可以总结如下：

```
uint32_t initTime = time()

for (uint32_t i = 0; i < 1024; i++) {
    // 16 byte array: [ 8 ones ] [ i (4 bytes) ] [ initTime (4 bytes) ]
    uint8_t ones[16];
    memset(ones, 0, 16);
    memcpy(ones + 8, &i, 4);
    memcpy(ones + 12, &initTime, 4);

    // 16 byte array: [ 8 zeroes ] [ i (4 bytes) ] [ initTime (4 bytes) ]
    uint8_t zeroes[16];
    memset(zeroes, 0, 16);
    memcpy(zeroes + 8, &i, 4);
    memcpy(zeroes + 12, &initTime, 4);

    bool bit = rand() % 2;
    if (bit == 0) {
        print(encrypt(zeroes));
    } else {
        print(encrypt(zeroes));
    }
    
    print("guess?");
    bool guess = read();
    if (guess == bit) {
        goodGuesses++;
    }

    print(encrypt(zeroes));
    print(encrypt(ones));
}

if (goodGuesses == 1024) {
    print("you won");
    print encrypt(encryptedFlag); // will actually decrypt flag for us
}
```

> 其中encrypt是我们修改的4轮AES.我们怎么开始破解这样的东西？我们可以使用众所周知的密码攻击技术,称为平方攻击或积分密码分析.要了解此攻击的工作原理,我们需要首先获得AES的高级(简化)概述.因此AES正在处理128位块.这128位被视为4x4字节数组,我们正在该数组上执行一些“操作”.子字节-使用固定的关联表(所谓的替换框,也称为sbox)将矩阵中的每个字节替换为另一个字节.所以给定矩阵：

```
in_matrix: 1 2 3 4 6 7 8 5 11 12 9 10 16 13 14 15
电话：+86-21 - 88888888传真：+86-21 - 88888888
```

> 我们的结论是：

```
out_matrix:
S[1]  S[2]  S[3]  S[4]
S[6]  S[7]  S[8]  S[5]
S[11] S[12]  S[9] S[10]
S[16] S[13] S[14] S[15]
```

> 移位-矩阵行按行数位置向左移位.例如给定矩阵：

```
in_matrix:
1  2  3  4
5  6  7  8
9 10 11 12
13 14 15 16
```

> 得到：

```
out_matrix:
1  2  3  4
6  7  8  5
11 12  9 10
16 13 14 15
```

> 混合列-矩阵列中的值彼此混合(很明显,我知道)(准确地说,列被视为多项式并乘以固定多项式,但这现在并不重要)重要的是列中的最终值仅依赖于该列中的其他值：

```
in_matrix:
A  E  I  M
B  F  J  N
C  G  K  O
D  H  L  P

nA, nB, nC, nD = mix(A, B, C, D)
nE, nF, nG, nH = mix(E, F, G, H)
nI, nJ, nK, nL = mix(I, J, K, L)
nM, nN, nO, nP = mix(M, N, O, P)

out_matrix:
nA nE nI nM
nB nF nJ nN
nC nG nK nO
nD nH nL nP
```

> AddRoundKey-我们正在向矩阵中的每个字节添加round key(不要那样看我,不是我的错,每个操作都已经有了描述性的名称).关键是,我们使用的是“xor”运算,而不是传统的加法运算(用技术术语来说,这是因为我们在galios油田进行运算,这里的“xor”是加法类比).

```
in_matrix:
A  E  I  M
B  F  J  N
C  G  K  O
D  H  L  P

round_key:
R0 R1 R2 R3
R4 R5 R6 R7
R8 R9 RA RB
RC RD RE RF

out_matrix:
A^R0  E^R1  I^R2  M^R3
B^R4  F^R5  J^R6  N^R7
C^R8  G^R9  K^RA  O^RB
D^RC  H^RD  L^RE  P^RF
```

> 为什么要为那些理论操心呢？因为现在我们要描述实际的攻击.假设我们可以得到256个(由我们)选择的明文的密文——这样,所有明文中的每个字节都是常数,除了一个字节可以得到每个可能的字节值.这类集合的示例可以是：

```
00 00 00 00 00 ... 00

01 00 00 00 00 ... 00

02 00 00 00 00 ... 00

03 00 00 00 00 ... 00

04 00 00 00 00 ... 00

..

FE 00 00 00 00 ... 00

FF 00 00 00 00 ... 00
```

> 然后我们可以用下面的矩阵表示AES状态：

```
X   C   C   C
C   C   C   C
C   C   C   C
C   C   C   C
```

> C意味着对于我们集合中的每一个被考虑的明文,在矩阵中相应位置上的字节是相同的.X意味着那个位置的字节得到了一些被考虑的明文的所有可能的字节值.所以,让我们检查AES将如何处理我们选择的明文集：初始值.

```
X   C   C   C
C   C   C   C
C   C   C   C
C   C   C   C
```

> 如前所述,第一个字节取所有可能的值,其余字节为常量.子字节之后：

```
X   C   C   C
C   C   C   C
C   C   C   C
C   C   C   C
```

> 当然,每个“C”都被更改为相同的值(因此它们仍然是常数).接下来是什么？

```
X   C   C   C
C   C   C   C
C   C   C   C
C   C   C   C
```

> 什么都没变.混合柱后：

```
X   C   C   C
X   C   C   C
X   C   C   C
X   C   C   C
```

> 现在我们有进展了.现在“C”值在查看单个状态时并不完全相同,但对于choosen集合中的每个明文,它们都得到相同的值,这才是重要的.类似地,每个标记为“X”的字节将为我们的一个明文取所有可能的值.我希望这是清楚的,让我们继续.在AddKey之后：

```
X   C   C   C
X   C   C   C
X   C   C   C
X   C   C   C
```

> 现在进行第二轮：子字节之后：

```
X   C   C   C
X   C   C   C
X   C   C   C
X   C   C   C
```

> ShiftRows后：ShiftRows后:

```
X   C   C   C
C   C   C   X
C   C   X   C
C   X   C   C
```

> 混合柱后：

```
X   X   X   X
X   X   X   X
X   X   X   X
X   X   X   X
```

> 在AddKey之后：

```
X   X   X   X
X   X   X   X
X   X   X   X
X   X   X   X
```

> 现在发生了什么？现在每个字节都取所有可能的值.好可怕！还是这样？这意味着,如果我们固定了任何状态位置(例如,第二行和第二列)并对它们执行异或运算：(state_xx表示集合中第xx个明文的状态)

```
state_01[2][2] ^ state_02[2][2] ^ state03_[2][2] ^ ... ^ stateFF[2][2] = 0
```

> 那我们就永远得0分！那是因为我们知道那个字节是取所有可能的字节,值,所以我们是异或(以随机顺序)数字

```
0 ^ 1 ^ 2 ^ 3 ... ^ 0xFE ^ 0xFF
```

> 那又怎么样？毕竟,我们的AES有4轮,而不是3轮.但在第四轮之后,我们可以猜测一个字节的密钥来解密一个字节的加密数据.根据previos关系,我们可以得出这样的结论：如果我们正确地猜测字节,用它解密密文中的某个字节,并将其全部异或,我们必须得到0.然后我们可以重复这个过程16次-每个字节的密钥一次.平均来说,我们会找到两个好的值(一个正确,256*1/256的假阳性几率).我们可以尝试每一种可能性-这将给我们2的16攻击复杂性-比天真的2 ^ 128好多了.我们还可以很容易地从任何一个圆密钥中恢复主密钥.我们能在这次挑战中使用这种攻击吗？当然,如果我们取前256个明文,我们可以看到它们中的每一个只在“i”的ony字节-最低字节上有所不同.所以我们可以在python中实现该攻击(这里跳过AES实现,但它将以writeup的形式提供完整的代码):

```
def integrate(index):
    potential = []

    for candidateByte in range(256):
        sum = 0
        for ciph in ciphertexts:
            oneRoundDecr = backup(ciph, candidateByte, index)  # decrypt one round of one byte
            sum ^= oneRoundDecr     # xor result with sum
        if sum == 0:   # if sum is equal to 0 - candidateByte stays a candidate
            potential.append(candidateByte)
    return potential


from itertools import product
def integral():
    candidates = []
    for i in range(16):
        candidates.append(integrate(i))    # compute all possible candidate bytes for all positions
    print 'candidates', candidates
    for roundKey in product(*candidates):  # check all possibilities
        masterKey = round2master(roundKey)
        plain = ''.join(chr(c) for c in decrypt4rounds(ciphertexts[1], masterKey))
        if '\0\0\0\0' in plain:  # we know that plaintext contains 4 '0' bytes, and it's unlike to be accident
            print 'solved', masterKey
```

> 对提供的密文运行后,我们得到以下结果：

```
candidates [[95, 246], [246], [1, 99], [78, 187], [123], [106], [98, 223], [96], [211], [44, 63, 102], [192, 234], [167], [9, 135, 234], [36], [146, 166], [107]]
solved [23, 74, 34, 20, 64, 53, 100, 117, 220, 227, 160, 55, 163, 23, 237, 75]
```

> 令人惊叹的！现在我们可以解密加密标志(毕竟我们有密钥).

```
0CTF{~R0MAN_l0VES_B10CK_C1PHER~}
```

> 攻击中使用的完整代码包含在integral.py文件中.代码模板和使用的攻击主要是从http://opensecuritytraining.info/cryptlanalysis.html(通过sa 3.0许可证抄送)课程中借用的.因此,我们的代码是通过SA许可证在CC 3.0上发布的,但是writeup文本和我们的代码(writeup中的片段)使用我们通常的许可证.

## flag

> flag{br0k3n_h4rdw4r3_l34d5_70_b17_fl1pp1n6}