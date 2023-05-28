# Cat

> php cURL CURLOPT_SAFE_UPLOAD和django DEBUG mode

## 思路分析

> Django使用的是gbk编码,超过%F7的编码不在gbk中有意义.当CURLOPT_SAFE_UPLOAD为true时,如果在请求前面加上@的话php curl组件是会把后面的当作绝对路径请求,来读取文件.当且仅当文件中存在中文字符的时候,Django才会报错导致获取文件内容.

> 打开首页后是一个输入框,输入baidu.com没反应,输入127.0.0.1有反应,看出是ping通IP的测试页,猜测是命令注入或者ssrf,发现有过滤字符,只要有特殊字符就不行,但是@可以.发现参数url其使用了URL编码,URL编码中ascii字符的边界是%7F,fuzz发现当url=%FF时报错.

> 将html在浏览器中打开,发现后端运行Django,由于字符编码问题而报错.在请求信息POST一项中可以找到参数url,于是大致可以猜想到是PHP向本机的Django发出了POST请求,参数就是输入的url.PHP通常使用cURL库与作为客户端与服务器通信,在cURL库的CURLOPT_POSTFILEDS选项中可以找到突破口,借此可以爆出数据库内容.根据前面发现的数据库路径,构造url=@/opt/api/database.sqlite3, 成功爆出报错信息,并由此在POST数据中找到了flag.

## payload

> ?url=@/opt/api/database.sqlite3

## flag

> WHCTF{yoooo_Such_A_G00D_@}