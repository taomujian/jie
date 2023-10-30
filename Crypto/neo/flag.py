import requests
import base64
import binascii
import threading
import time
import string
import urllib.request
import copy

threads = 20
alphabet = ''.join([chr(i) for i in range(16)]) + string.printable
alphabet_blocks = [alphabet[i : i + threads] for i in range(0, len(alphabet), threads)]
data = 'vwqB+7cWkxMC6fY55NZW6y/LcdkUJqakXtMZIpS1YqbkfRYYOh0DKTr9Mp2QwNLZkBjyuLbNLghhSVNkHcng+Vpmp5WT5OAnhUlEr+LyBAU='
ciphertext = binascii.hexlify(base64.b64decode(data))[:]
offset = len(ciphertext) // 2 - 16

def flip_cipher(ciphertext, known, i):
    modified_ciphertext = copy.copy(ciphertext)
    for j in range(1, i):
        modified_ciphertext[offset - j] = ciphertext[offset - j] ^ ord(known[-j]) ^ i
    return modified_ciphertext

ciphertext = [int(ciphertext[i:i+2], 16) for i in range(0, len(ciphertext), 2)]
count, known = 1, ''

while True:
    print('Found so far:', [known])
    for block in alphabet_blocks:
        responses, payloads = {}, {}
        modified_ciphertext = flip_cipher(ciphertext, known, count)

        for char in block:
            modified_ciphertext[offset - count] = ciphertext[offset - count] ^ ord(char) ^ count
            payloads[''.join([hex(symbol)[2:].zfill(2) for symbol in modified_ciphertext])] = char

        for payload in payloads.keys():
            threading.Thread(target=oracle, args=(payload,)).start()

        while len(responses.keys()) != len(payloads):
            time.sleep(0.1)

        if True in responses.values():
            known = payloads[list(responses.keys())[list(responses.values()).index(True)]] + known
            alphabet_blocks.remove(block)
            alphabet_blocks.insert(0, block)
            count = count + 1
            break