import string
def enc_pw(e):
  res = ''
  f = 0
  for i, c in enumerate(e):
    c = ord(c)
    if f == 1:
      c += i & 3
    c += 6
    f = c & 1
    res += chr(c)
  return res
  
encrypted = 'XYzaSAAX_PBssisodjsal_sSUVWZYYYb' # get_pw()的输出结果
flag = ''
# 逆向test_pw和index的login
for i, c in enumerate(encrypted):
  c = ord(c)
  c -= 5
  if i & 1:
    c += 3
  for d in string.printable:
    if enc_pw(flag + d)[i] == chr(c):
      flag += d
      break
  print(flag)