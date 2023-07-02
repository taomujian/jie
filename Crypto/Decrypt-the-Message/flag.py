#!/usr/bin/env python
import string

encrypted = ["sebt", "yuwi", "ytrr", "ortl", "rbon", "aluo", "konf", "ihye", "cyog",
 "rowh", "prhj", "feom", "ihos", "perp", "twnb", "tpak", "heoc", "yaui", "usoa", "irtd",
  "tnlu", "ntke", "onds", "goym", "hmpq"]

passphrase = "yoursshallpausepeaceyears"
alph = string.ascii_lowercase
count = 1
passkey = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for a in alph:
	for i in range(len(passphrase)):
		if passphrase[i:i+1] == a:
			passkey[i] = count
			count +=1

print("Key is " + str(passkey))

result =""
for i in range(4):
	for j in range(len(passkey)):
		test = j + 1
		for k in range(len(passkey)):
			if test == passkey[k]:
				result = result + encrypted[k][i:i+1]

print("Decrypted message is " + result)