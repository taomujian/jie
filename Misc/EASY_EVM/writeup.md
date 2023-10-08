# EASY_EVM

## 解题思路

> 下载附件得到一个.DS_Store文件和info.txt,.DS_Store尝试利用失败,搜了下info.txt里面的内容,是以太坊EVM字节码,这就更不懂了.

> 考点是EVM逆向,比较简单,中间夹杂了中国剩余定理的知识,源码如下
改了一下bytecode使得不能反编译,可以自己手动改过来反编译,也可以直接分析opcode,逻辑也不复杂

```
pragma solidity ^0.5.0;

contract EASY_EVM_CRYPTO{
    
    // flag = "flag{An_E4sy_EVM_y0u_sO1ve_it!}"
    string private FLAG;
    uint private x;
    uint private y;
    uint private z;
    
    // flag = 0x666c61677b416e5f453473795f45564d5f7930755f734f3176655f6974217d
    constructor() public payable {
        x = 231412341286754812414291;
        y = 126381254785148123414597;
        z = 438712649816519864511367;
    }
    
    function GetFlag() public view returns (string memory flag) {
        assembly {
            flag := sload(0)
        }
    }
    
    function Convert(string memory source) public pure returns (uint result) {
        bytes32 tmp;
        assembly {
            tmp := mload(add(source, 32))
        }
        result = uint(tmp) / 0x100;
    }
    
    function Require() public view {
        uint tmp = Convert(FLAG);
        require(tmp%x == 193913535844325315514675);
        require(tmp%y == 59349569214207838388981);
        require(tmp%z == 153559101645126489682469);
    }
}
```

> 需要注意的是,x、y、z的值可从initialization code获得,然后便是中国剩余定理的知识,简单的密码学

```
from functools import reduce
from Crypto.Util.number import long_to_bytes,bytes_to_long

def egcd(a, b):
    if 0 == b:
        return 1, 0, a
    x, y, q = egcd(b, a % b)
    x, y = y, (x - a // b * y)
    return x, y, q

def chinese_remainder(pairs):
    mod_list, remainder_list = [p[0] for p in pairs], [p[1] for p in pairs]
    mod_product = reduce(lambda x, y: x * y, mod_list)
    mi_list = [mod_product//x for x in mod_list]
    mi_inverse = [egcd(mi_list[i], mod_list[i])[0] for i in range(len(mi_list))]
    x = 0
    for i in range(len(remainder_list)):
        x += mi_list[i] * mi_inverse[i] * remainder_list[i]
        x %= mod_product
    return x

if __name__=='__main__':
    result = chinese_remainder([(231412341286754812414291, 193913535844325315514675), (126381254785148123414597, 59349569214207838388981), (438712649816519864511367, 153559101645126489682469)])
    Least_common_multiple = 231412341286754812414291 * 126381254785148123414597 * 438712649816519864511367
    for i in range(1, 100000):
        print i
        flag = Least_common_multiple * i + result
        flag = long_to_bytes(flag)
        if 'flag{' in flag:
            print(flag)
            break
```

## flag

> flag{An_E4sy_EVM_y0u_sO1ve_it!}

## 参考

> https://ethervm.io/decompile