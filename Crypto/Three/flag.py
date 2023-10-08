import zipfile
from Crypto.Util.number import inverse, long_to_bytes

def extract(file, password):
    file.extractall(path='.', pwd=''.join(password).encode('utf-8'))

password_lst = []
prestr='2022-08-27 20:16:17.'
for i in range(0,999999):
    s=str(i)
    tmpnum='0'*(6-len(s))+s
    password_lst.append(prestr+tmpnum)

zfile = zipfile.ZipFile("544baa20-91e2-42c2-96dc-a19d02c7052d/C.zip", 'r')
for pwd in password_lst:
    try:
        extract(zfile,pwd)
        print(pwd)
        break
    except:
        continue

def Mul_loc_compute(x1,y1,x2,y2):
    mulx=x1*y1+x1*y2+x2*y1
    return mulx

A0 = 28829613228241459
A00_true=200254991086689
A01_true=200241552690281
X00_true=200058430391504
X01_true=200401773940794
C00_true=Mul_loc_compute(A00_true,X00_true,A01_true,X01_true)
C00_mask=C00_true+507412160912
B00_true=199957680670222
Y00_true=C00_mask+B00_true
Y00_mask=Y00_true+(-1008362525723)
Y02_mask=924422050091362838179268571917871
Y02_true=Y02_mask-507036073644
Y01_mask = 12163251699969281466186532960410
Y0=Y00_mask+Y01_mask+Y02_mask
C02_mask=924422050091355025836012334663090
B02_true = Y02_true-C02_mask
B00_true=199957680670222
B01_true=200362172648094
B0=B00_true+B01_true+B02_true
X0=(Y0-B0)//A0
flag = long_to_bytes(A0) + long_to_bytes(X0) + long_to_bytes(B0)
print(flag)