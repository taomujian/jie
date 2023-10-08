import os
import base64

def base():
    data = '118956c97c7c4a3e9b1508c1f5ea44be/problem'
    files = os.listdir(data)
    result = base64.b64decode(''.join(files)).decode(errors ='ignore')
    print(result)
            
if __name__=='__main__':
    base()