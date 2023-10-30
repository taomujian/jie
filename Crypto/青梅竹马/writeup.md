# 青梅竹马

## 解题思路

> 下载附件,exe文件,看雪CTF系列.

> 这是一个Win32逆向,有一个自定义的Base64编码,字符集是ABCyVPGHTJKLMNOFQRSIUEWDYZgbc8sfah1jklmnopqret5v0xX9wi234u67dz+/

> 有一个先解码再编码的操作，本质上是做了一个长度校验,另外有判断Flag前两位不是A，第6位和第12位是V,再次解码的时候V没有用到,进入下一个check，发现又是熟悉的高精度计算。。。

```
// sub_4024e1
  v7 = 0;
  memset(prime_table, 0, sizeof(prime_table));
  __0x53 = sub_40243F(_100, &v7);
  hp_new((int)&powmod_res);
  hp_new((int)&v9);
  hp_init((int)&powmod_res, 0);
  hp_init((int)&flag_num, 0);
  v4 = 1;
  hp_init((int)&mul_3_to_73, 1);
  hp_init((int)&v9, v7);
  hp_str_init(&flag_num, decoded_flag, len);
  res = hp_ldword_abs((int)&powmod_res);
  if ( __0x53 > 1 )
  {
    v5 = prime_table;
    while ( *v5 != _O )
    {
      if ( *v5 )
        hp_mul((int)&mul_3_to_73, (int)&mul_3_to_73, *v5);
      ++v4;
      ++v5;
      if ( v4 >= __0x53 )
        goto LABEL_9;
    }
    __0x53 = prime_table[v4];
  }
LABEL_9:
  if ( hp_cmp((int)&flag_num, (int)&v9) >= 0 && hp_cmp((int)&flag_num, (int)&mul_3_to_73) <= 0 )
  {
    hp_powmod((int)&powmod_res, (int)&flag_num, __0x53, (int)&mul_3_to_73);
    if ( hp_cmp((int)&powmod_res, (int)&v9) >= 0 && hp_cmp((int)&powmod_res, (int)&mul_3_to_73) <= 0 )
      res = hp_ldword_abs((int)&powmod_res);
  }
  hp_del((int)&powmod_res);
  hp_del((int)&v9);
  return res;
}
```

> 创建了几个大整数对象，其中有一个初始化为了解码后的Flag,先求出了100以内的素数，然后算了一个

```
3*5*7*11*13*17...*73
```
> 的值,然后判断Flag是否在2到这个数之间,然后做了一个powmod, flag * 83 % (3\...*73),这个结果要等于正负2,使用Wolfram解得

```
x = 20364840299624512075310661735 * n + 6602940601029543050476765433
```

> 可以解得Flag

```
>>> x = 'ABCyVPGHTJKLMNOFQRSIUEWDYZgbc8sfah1jklmnopqret5v0xX9wi234u67dz+/'
>>> y = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
>>> t = string.maketrans(y, x)
>>> hex(6602940601029543050476765433)
'0x1555d30f38b0dbcaec83c0f9L'
>>> '1555d30f38b0dbcaec83c0f9'.decode('hex').encode('base64').translate(t)
'PEDIy9102dreadyu\n'
```

> 补上两个V得最终结果: PEDIyV9102dVreadyu

## flag

> flag{PEDIyV9102dVreadyu}

## 参考

> https://bbs.kanxue.com/thread-249942.htm