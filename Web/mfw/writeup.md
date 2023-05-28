# Mfw

> Git文件泄露+命令执行

## 相关函数

### strpos

> strpos(string,find,start),返回find在string中第一次出现的位置,如果没有找到字符串则返回FALSE.注释:字符串位置从0开始,不是从1开始.

### assert

> bool assert(mixed $assertion[, Throwable $exception ]),assert这个函数在php语言中是用来判断一个表达式是否成立,返回true or false.如果assertion是字符串,它将会被assert()当做PHP代码来执行,如果你传入了boolean的条件作为assertion,这个条件将不会显示为断言函数的参数;在调用你定义的assert_options()处理函数时,条件会转换为字符串,而布尔值 FALSE 会被转换成空字符串.

## 思路分析

> Git文件泄露+命令执行,扫目录,发现.git目录,用githack工具还原代码,发现存在/?page=flag,直接访问为空,获取不了flag.看到了assert函数,assert函数中如果assertion是字符串,它将会被assert()当做PHP代码来执行,尝试构造payload,').phpinfo();//,当传递到index.php第15行时,file_exists('\$file')就变成了,file_exists('').phpinfo();//'),phpinfo();被执行,继续构造payload,得到flag

## payload

> /?page=%27).system("cat%20templates/flag.php");//

## flag

> cyberpeace{6fb2319e0c5056cc5c5eaa45d5e18870}