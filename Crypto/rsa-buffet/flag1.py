from secretsharing import PlaintextToHexSecretSharer as SS

files = ["ciphertext5.txt", "ciphertext1.txt", "ciphertext4.txt"]
secrets = []
for fn in files:
    a = []
    with open(fn, "r") as f:
        a = f.readlines()

    a = a[1:] # strip the "Congratulation" line
    for i in range(0,len(a)):
        a[i] = a[i].strip("\n")

    secrets.append(a)

for i in range(0, 2):
    a = SS.recover_secret([secrets[0][i], secrets[1][i], secrets[2][i]])
    print(a)