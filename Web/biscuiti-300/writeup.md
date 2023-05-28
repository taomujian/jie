# Biscuiti-300

## 思路分析

> 下载附件得到php代码,分析下来,如果SESSION["isadmin"]为真,则得到flag.扫目录得到了/users.db路径,下载users.db,得到了admin加密后的密码为wCqHs1eDcCePiImvDZzwXw==

> 从源码上来看数仅查询了usernam、enc_password字段,并⽆isadmin字段,所以即便登录成功,默认肯定不是admin⽤户.

> 继续分析,可以发现其cookie验证逻辑使⽤的是基于aes-128-cbc的加解密.其将⽤户session进⾏序列化后,以加密的形式存储到cookie中.

> 因为session是保存在cookie中的,所以可以尝试对其进⾏修改.通过传统解密⽅式的话,发现题⽬中所给的ENC_KEY,并不是部署环境中的key,所以没法直接进⾏解密修改.但因为其采⽤了不安全的加密⽅式,即CBC模式,其因为分组加密的特性.导致可以去对其进⾏爆破,得到iv值,进⽽继续爆破,得到明⽂.也就是padding oracle攻击(iv为16个"\0").然后在通过cbc翻转攻击来对cookie内容进⾏修改即可.

> 那接下来的主要要点就是两点⼀、登陆成功获取cookie. ⼆、伪造cookies中的session,并保证后缀的mac值与session加密后一致

> 登陆这⾥,可以发现是存在⼀个SQL注⼊的.在这⾥,可以采⽤联合查询来去让其获取到想要的数据.可以利用如下payload绕过password验证,该payload组成的sql查询结果集为(username, enc_password)=("username", "")

```
username=' union select 'username', '
```

> AES加密的时候块的大小为16,将得到的序列化字符串分为16字节一组,第三组的内容为可控部分.根据CBC加密原理,已知所有的明文和一块密文（cookie的末16位）,可以恢复所有的密文,要想获得flag,需要修改密文块,使最后反序列化的值为$SESSION['isadmin']=1

## flag

> cyberpeace{d2c1259b867ad94097474b8a46f8aa51}

## 参考

> http://blog.zhaojie.me/2010/10/padding-oracle-attack-in-detail.html

> https://github.com/ssst0n3/ctf-wp/tree/master/2016/seccon/WEB/biscuiti