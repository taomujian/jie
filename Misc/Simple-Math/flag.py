
from hashlib import sha1

# sage

a = '1 1 0 1 1 0 1 1 1 10 0 1 1 0 0 0 1 1 01 0 1 1 0 0 1 1 1 00 1 0 1 0 1 1 1 0 00 0 0 0 1 1 0 1 1 11 1 1 1 1 0 0 0 1 01 0 0 0 0 1 0 1 1 10 0 0 1 0 1 0 0 0 10 1 1 0 0 0 1 1 1 00 0 0 1 0 0 1 1 0 1'
a = a.replace(' ','')
a = list(a)
a = matrix(ZZ,10,10,a)

b='1011000101'
b=list(b)
b=[int(i) for i in b]
b=matrix(ZZ,10,1,b)

for i in range(2**10):
    x='{:010b}'.format(i)
    x=list(x)
    x=[int(i) for i in x]
    x=matrix(ZZ,10,1,x)
    m=a*x
    m=[i%2 for i in m]
    m=matrix(ZZ,10,1,m)
    
    if m==b:
        #print('x=',x)
        astr=list()
        for i in x:
            astr.append(str(i))
        astr=''.join(astr).replace('(','').replace(')','')
        #print(astr)
        break
        
flag=sha1(astr.encode()).hexdigest()
print('XSCTF{'+flag+'}')