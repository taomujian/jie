import string
from hashlib import md5
dic = string.printable

half_md5 = "1a4fb3fb5ee12307"

str1 = ""
for i1 in dic:
     for i2 in dic:
          for i3 in dic: 
                for i4 in dic:
                  str1 = i1 + i2 + i3 + i4 + "LiHua"
                  str1_md5 = md5(str1.encode()).hexdigest()
                  if half_md5 in str1_md5:
                      print(str1)
                      exit(0)
                    

