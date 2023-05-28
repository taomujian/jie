# Confusion2

## 思路分析

> Confusion2和Confusion1相比只是多了注册和登录的功能,在注册和登录页面有md5的验证码,说明和sql注入无关.注册一个账号后登录,发现cookies里除了正常的sessionid外还有一个token,根据经验发现这是Json web token

> 这个JWT并非标准JWT的,加密的算法是sha256,并不是标准的加密算法,除了加密算法不同外其他的都和JWT一样.解密这个token

> 可以看到在JWT的data里存放了一个类似PHP序列化的字符串,在这个字符串中又有一个user_data的值,有经验的师傅这时候就可以看出来这是⼀个Python序列化的字符串⽽且这个字符串中出现了两个很突出的部分: 登录的⽤户名和⼀串hash,⽽这串hash就是⽤户名的md5.把这个字符串⼿动在python⾥反序列化⼀下会发现这是⼀个列表,第⼀个元素是⽤户名,第⼆个元素是⽤户名的md5这是python的序列化字符串,用reduce方法可以RCE,但是需要先绕过JWT的验证

> 根据Hint,sha256中需要加上前一道题中拿到的salt,添加到末尾,这样就可以伪造JWT通过验证,格式为jwt_header + '.' + jwt_payload + salt

> 注意在php的序列化字符串中user_data的字符数量必须和前面的数字相等

## flag

> cyberpeace{03f1deaaff9a585fb0bdbe24dbf612f4}

## 参考

> https://www.freebuf.com/articles/web/239385.html