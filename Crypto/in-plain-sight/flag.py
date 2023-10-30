#!/usr/bin/env python3

import binascii
from Crypto.Cipher import AES

class Aes_Crypto():
    def __init__(self, key, iv):
        self.key = binascii.unhexlify('c086e08ad8ee0ebe7c2320099cfec9eea9a346a108570a4f6494cfe7c2a30ee1')
        self.iv = binascii.unhexlify('0a0e176722a95a623f47fa17f02cc16a') 

    def pkcs7padding(self, text):

        """
        明文使用PKCS7填充
        最终调用AES加密方法时，传入的是一个byte数组，要求是16的整数倍，因此需要对明文进行处理

        :param str text: 待加密内容(明文)
        :return:
        """

        bs = AES.block_size  # 16
        length = len(text)
        bytes_length = len(bytes(text, encoding='utf-8'))
        # tips：utf-8编码时，英文占1个byte，而中文占3个byte
        padding_size = length if(bytes_length == length) else bytes_length
        padding = bs - padding_size % bs
        # tips：chr(padding)看与其它语言的约定，有的会使用'\0'
        padding_text = chr(padding) * padding
        return text + padding_text

    def pkcs7unpadding(self, text):

        """
        处理使用PKCS7填充过的数据

        :param str text: 解密后的字符串
        :return:
        """

        length = len(text)
        unpadding = ord(text[length-1])
        return text[0:length-unpadding]

    def encrypt(self, content):

        """
        AES加密
        key,iv使用同一个
        模式cbc
        填充pkcs7

        :param str key: 密钥
        :param bytes content: 加密内容
        :return:
        """

        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        # 处理明文
        content_padding = self.pkcs7padding(content)
        # 加密
        encrypt_bytes = cipher.encrypt(bytes(content_padding, encoding='utf-8'))
        return encrypt_bytes

    def decrypt(self, content):

        """
        AES解密
        key,iv使用同一个
        模式cbc
        去填充pkcs7
        
        :param str key:
        :param str content:
        :return:
        """
        
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        # base64解码
        decrypt_bytes = cipher.decrypt(content)
        # 重新编码
        result = str(decrypt_bytes, encoding='utf-8')
        # 去除填充内容
        result = self.pkcs7unpadding(result)
        return result

if __name__ == '__main__':
    aes = Aes_Crypto('c086e08ad8ee0ebe7c2320099cfec9eea9a346a108570a4f6494cfe7c2a30ee1', '0a0e176722a95a623f47fa17f02cc16a')
    print(aes.decrypt(b'HiddenCiphertext'))