from Crypto.Cipher import AES
from Crypto import Random
import base64

def decrypt(data, password):
    unpad = lambda s: s[0:-s[-1]]
    iv = data[:16]
    cipher = AES.new(password, AES.MODE_CBC, iv)
    data = cipher.decrypt(data[16:])
    return data

if __name__ == '__main__':
    password = b'FK4Lidk7TwNmRWQd'

    encrypt_data1 = base64.b64decode('OYzmTh2MGNclc5gALl+2lJ/xu58d4dAtidJc2w4dRhB1cuh/pXAt17QSjEIFMPiSE6w+DXpXJk9zm0FD39MGvwL4ZNpr2YndIPnjnb0W3xNeP+e5r//GhTYkNTdPo4xpT4d+HMihDB1mZNcQ8Gib69l5NlqC8PFjEeABWPfJezqG0LozsEjukHJOCMhVlRrirtkI7/ExFZAgH+G1i/gaw84nJ0DbGXQEpA2wySh6/iXeJD1ZYgt7jRgKLCL6CGggxsAEP9+m3QTZkxEitNqplA==')
    
    encrypt_data2 = base64.b64decode('Mvw3nE7h3GtoC0xqGKmjboBW7h+WyH+QhJRd1EL+Qc7cgRAaVNYwWrWDMByHOIlSig+MvEg0GTihcnuNdgRpD4fgmEgjvAvScqJkQUes+Mxbi4NNkCv6YANnbGFbZSUVs3YbulPu6Xzj+/nBmJcOsti94BHja8Cjym4l2qpmIkjR6kONAs2e7uAkduLR1zH9')

    decrypt_data1 = decrypt(encrypt_data1, password)
    print('decrypt_data1:\n', decrypt_data1)
    
    decrypt_data2 = decrypt(encrypt_data2, password)
    print('decrypt_data2:\n', decrypt_data2)
