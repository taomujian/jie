import zipfile
import re

file_name = 'pic/' + 'f932f55b83fa493ab024390071020088.zip'
while True:
    try:
        zf = zipfile.ZipFile(file_name)
        re_result = re.search('[0-9]*', zf.namelist()[0])
        passwd = re_result.group()
        zf.extractall(path='pic/', pwd=re_result.group().encode('ascii'))
        file_name = 'pic/' + zf.namelist()[0]
    except:
        print("get the result")
        break
