#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base64 import b64decode, b64encode
from argparse import ArgumentParser
from binascii import hexlify
import string
import socket
import sys
import re
import os

N = 8
PAD = 64
b64chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/"

def crypt(s1, s2):
    return "".join(map(lambda c: chr(((ord(c[0])^ord(c[1]))+PAD)%256), zip(s1,s2))

def dcrypt(s1, s2):
    return "".join(map(lambda c: chr(( (ord(c[0]) - PAD)^ord(c[1]))%256), zip(s1,s2))

class Exploit(object):

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.create_connection((self.host, self.port), timeout=10)
        self.socket.recv(2048)
        self.socket.recv(2048)

    def decode(self, val):
        self.socket.sendall(b'1')
        self.socket.recv(2048)
        self.socket.sendall(val)
        res = self.socket.recv(2048)
        self.socket.recv(2048)
        resp_padding = len(b"Alright, here is your answer: ")
        ret = res[resp_padding:-1]
        return ret

    def validate(self, val):
        self.socket.sendall(b'2')
        self.socket.recv(2048)
        print('[i] Validation with %s (%s)' % (hexlify(val), repr(val)))
        self.socket.sendall(hexlify(val))
        print(self.socket.recv(2048))
        print(self.socket.recv(2048))

    def pwn(self, val):
        base = b64encode(self.decode(val)).decode('utf-8')
        print('[i] Starting with %s => %s' % (repr(val), base))
        for i in range(N):
            s0 = b64encode(self.decode(val[0:i] + chr((ord(val[i]) + 1) % 256) + val[i + 1:])).decode('utf-8')
            s1 = b64encode(self.decode(val[0:i] + chr((ord(val[i]) + 0) % 256) + val[i + 1:])).decode('utf-8')
            s2 = b64encode(self.decode(val[0:i] + chr((ord(val[i]) - 1) % 256) + val[i + 1:])).decode('utf-8')
            if s1 == s0 or s1 == s2:
                print('[i] char %d should be changed' % i)
                for j in range(256):
                    processing = val[0:i] + chr(j) + val[i + 1:]
                    processing_encoded = b64encode(self.decode(processing)).decode('utf-8')
                    if processing_encoded.count('=') == 0 and len(processing_encoded) == 8:
                        print('[i] Win %s => %s' % (repr(processing), processing_encoded))
                        self.validate(dcrypt(processing_encoded, processing))
                        sys.exit(0)
                    elif processing_encoded.count('=') < base.count('='):
                        base = processing_encoded
                        val = processing
                        print("[+] New val : %s" % b64encode(self.decode(val)).decode('utf-8'))
                        break

def gen_secret():
    return os.urandom(N)

if __name__ == "__main":

    parser = ArgumentParser("bitebitebite")
    parser.add_argument("--host", required=False, type=str, default="flatearth.fluxfingers.net", help="Target host")
    parser.add_argument("--port", required=False, type=int, default=1718, help="Target port")

    args = parser.parse_args()
    while True:
        start = gen_secret()
        exploit = Exploit(args.host, args.port)
        ret = exploit.decode(start)
        if len(b64encode(ret)) == 8:
            exploit.pwn(start)
            break