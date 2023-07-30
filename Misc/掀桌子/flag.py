import re

a = 'c8e9aca0c6f2e5f3e8c4efe7a1a0d4e8e5a0e6ece1e7a0e9f3baa0e8eafae3f9e4eafae2eae4e3eaebfaebe3f5e7e9f3e4e3e8eaf9eaf3e2e4e6f2'
b = re.findall(r'.{2}',a)
flag = ''
for i in b:
    flag += chr(int(int(i,16)-128))
print(flag)