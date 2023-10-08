from Crypto.Cipher import AES
import base64

aes_instance = AES.new(b'weigongcun'.ljust(16, b'\0'), AES.MODE_ECB)

cipher = base64.b64decode('7SsQWmZ524i/yVWoMeAIJA==')

plaintext = aes_instance.decrypt(cipher)

print(plaintext)