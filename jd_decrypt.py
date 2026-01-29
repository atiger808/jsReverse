# -*- coding: utf-8 -*-
# @File   :jd_decrypt.py
# @Time   :2025/1/7 15:03
# @Author :admin

from Crypto.Cipher import AES
import base64



class AESUtil:
    def __init__(self, key):
        self.key = key.encode('utf-8')
        self.block_size = AES.block_size

    def encrypt(self, data):
        data = self.pkcs5_pad(data.encode('utf-8'))
        cipher = AES.new(self.key, AES.MODE_ECB)
        encrypted = cipher.encrypt(data)
        return base64.b64encode(encrypted).decode('utf-8')

    def decrypt(self, encrypted_data):
        encrypted_data = base64.b64decode(encrypted_data)
        print(f'encrypted_data: {encrypted_data}')
        print(f'encrypted_data: {type(encrypted_data)}')
        cipher = AES.new(self.key, AES.MODE_ECB)
        decrypted = cipher.decrypt(encrypted_data)
        return self.pkcs5_unpad(decrypted).decode('utf-8')

    def pkcs5_pad(self, text):
        pad = self.block_size - (len(text) % self.block_size)
        return text + bytes([pad] * pad)

    def pkcs5_unpad(self, text):
        pad = text[-1]
        if pad > len(text):
            raise ValueError("Invalid padding")
        if text[-pad:] != bytes([pad] * pad):
            raise ValueError("Invalid padding")
        return text[:-pad]


# 以上代码翻译成php代码

from Crypto.Cipher import AES
import base64
import json

class AESUtil2:
    def __init__(self, encrypt_key):
        self.encrypt_key = encrypt_key.encode('utf-8')  # 确保密钥是字节类型
        self.block_size = AES.block_size

    def encrypt_text(self, params):
        # 如果参数是字典或列表，转换为 JSON 字符串
        if isinstance(params, (dict, list)):
            params = json.dumps(params)
        # 确保输入是字节类型
        params = params.encode('utf-8')
        # 使用 AES-256-ECB 模式加密
        cipher = AES.new(self.encrypt_key, AES.MODE_ECB)
        # 加密并返回 Base64 编码的结果
        encrypted = cipher.encrypt(self.pkcs5_pad(params))
        return base64.b64encode(encrypted).decode('utf-8')

    def decrypt_text(self, data):
        # Base64 解码
        decode_data = base64.b64decode(data)
        # 使用 AES-256-ECB 模式解密
        cipher = AES.new(self.encrypt_key, AES.MODE_ECB)
        # 解密并去除填充
        decrypted = self.pkcs5_unpad(cipher.decrypt(decode_data))
        # 返回解密后的字符串
        return decrypted.decode('utf-8')

    def pkcs5_pad(self, text):
        # PKCS5 填充
        pad = self.block_size - (len(text) % self.block_size)
        return text + bytes([pad] * pad)

    def pkcs5_unpad(self, text):
        # 去除 PKCS5 填充
        pad = text[-1]
        if pad > len(text):
            raise ValueError("Invalid padding")
        if text[-pad:] != bytes([pad] * pad):
            raise ValueError("Invalid padding")
        return text[:-pad]

import hashlib
from Crypto.Cipher import AES
import base64


class AesUtil:
    # 加密算法
    KEY_ALGORITHM = 'AES-128-ECB'
    # 编码方式
    ENCODING_TYPE = 'utf-8'
    # 私钥
    ASSETS_DEV_PWD_FIELD = '!6vTrQnaT$fFSydTEfjm@h3V'

    @staticmethod
    def encrypt(content: str) -> str:
        try:
            # 生成密钥
            key = AesUtil.get_secret_key(AesUtil.ASSETS_DEV_PWD_FIELD)
            # 创建 AES 加密器
            cipher = AES.new(key, AES.MODE_ECB)
            # 对内容进行填充
            padded_content = AesUtil.pkcs5_pad(content.encode(AesUtil.ENCODING_TYPE))
            # 加密
            encrypted = cipher.encrypt(padded_content)
            # 返回 Base64 编码的加密结果
            return base64.b64encode(encrypted).decode(AesUtil.ENCODING_TYPE)
        except Exception as e:
            print(f"aesencrypt000 error: {e}")
            return None

    @staticmethod
    def decrypt(encrypted_content: str) -> str:
        try:
            # 生成密钥
            key = AesUtil.get_secret_key(AesUtil.ASSETS_DEV_PWD_FIELD)
            # 创建 AES 解密器
            cipher = AES.new(key, AES.MODE_ECB)
            # Base64 解码
            decoded_content = base64.b64decode(encrypted_content)
            # 解密
            decrypted = cipher.decrypt(decoded_content)
            # 去除填充
            unpadded_content = AesUtil.pkcs5_unpad(decrypted)
            # 返回解密后的字符串
            return unpadded_content.decode(AesUtil.ENCODING_TYPE)
        except Exception as e:
            print(f"aesdecrypt000 error: {e}")
            return None

    @staticmethod
    def get_secret_key(password: str) -> bytes:
        # 使用 SHA1 算法生成密钥
        hash_value = hashlib.sha1(password.encode(AesUtil.ENCODING_TYPE)).digest()
        # 取前 16 字节作为 AES-128 密钥
        return hash_value[:16]

    @staticmethod
    def pkcs5_pad(data: bytes) -> bytes:
        # PKCS5 填充
        pad_size = AES.block_size - (len(data) % AES.block_size)
        return data + bytes([pad_size] * pad_size)

    @staticmethod
    def pkcs5_unpad(data: bytes) -> bytes:
        # 去除 PKCS5 填充
        pad_size = data[-1]
        if pad_size > len(data):
            raise ValueError("Invalid padding")
        if data[-pad_size:] != bytes([pad_size] * pad_size):
            raise ValueError("Invalid padding")
        return data[:-pad_size]

    @staticmethod
    def main():
        origin = '{"data":{"code":"uUjzC5ZDZSTymmhZBWM7qftn14101683","grant_type":"authorization_code"},"method":"taobao.top.auth.token.create"}'
        print("加密前：" + origin)

        # 加密
        encrypt_result = AesUtil.encrypt(origin)
        print("加密后：" + encrypt_result)

        # 解密
        decrypt_result = AesUtil.decrypt(encrypt_result)
        print("解密后：" + decrypt_result)




if __name__ == '__main__':
    # 运行示例
    # AesUtil.main()

    # # 使用示例
    # key = "1234567890123456"  # 128 位密钥，长度为 16 字节
    # key = "uUjzC5ZDZSTymmhZBWM7qftn14101683"  # 128 位密钥，长度为 16 字节
    # key = "56D96CE24AC4CF3432AD930977DFCE59"  # 128 位密钥，长度为 16 字节
    # key = "56D96CE24AC4CF3432AD930977DFCE59"  # 128 位密钥，长度为 16 字节
    # aes_util = AESUtil(key)
    # # data = "Hello, World!"
    # # encrypted = aes_util.encrypt(data)
    # # print("Encrypted:", encrypted)
    encrypted = 'vTZhMun/tiJtPokoMp1ssmbs3wC8iOdy663Hyvm+REHstpaGmhTQT1cFvRgtSP0iefxr+J/QXd1uBalobMbRIop6idrA69NuwAKctOTvMDz7hSPxVcRvsbz6oODRdAk3Jk61irvbKo6R54ozPhNhhT1zJci4vyfVbyS2lz1I7tg='

    encrypted = 'gCpD/bD6J8Afga/doqLs7gOuqiIaGSjG7XcFZMaMvFsTzNw9wGl5/394F25JJuBwHy2IYJTF1hATJN7BSTx/E5X9pXB3fUvG/dNiiLgG+MXqjiQ9sRGa6mPHCaDM22DNlNvYbXfnx6VGuF1Udj56vawEOKAHcuWJhA/gN8UjBTA='


    encrypted = 'vTZhMun/tiJtPokoMp1ssvon8qqehNZsFtlaA8uETBZRUxklRUoDmEMFtLeZPIRXgC20HpV2xht6jaGPcWETUop6idrA69NuwAKctOTvMDz7hSPxVcRvsbz6oODRdAk3Jk61irvbKo6R54ozPhNhhT1zJci4vyfVbyS2lz1I7tg='

    encrypted = 'vTZhMun/tiJtPokoMp1ssvon8qqehNZsFtlaA8uETBZRUxklRUoDmEMFtLeZPIRXgC20HpV2xht6jaGPcWETUop6idrA69NuwAKctOTvMDz7hSPxVcRvsbz6oODRdAk3Jk61irvbKo6R54ozPhNhhT1zJci4vyfVbyS2lz1I7tggSShjidC8iherHyrUmB4t'


    encrypted = 'tiJtPokoMp1ssvon8qqehNZsFtlaA8uETBZRUxklRUoDmEMFtLeZPIRXgC20HpV2xht6jaGPcWETUop6idrA69NuwAKctOTvMDz7hSPxVcRvsbz6oODRdAk3Jk61irvbKo6R54ozPhNhhT1zJci4vyfVbyS2lz1I7tggSShjidC8iherHyrUmB4t'


    # encrypted = 'vTZhMun/tiJtPokoMp1sstZQw/AIJAhVInAkx2uuWjkBQUfc7Fklrp36lZn4SMqBefxr+J/QXd1uBalobMbRIop6idrA69NuwAKctOTvMDz7hSPxVcRvsbz6oODRdAk3Jk61irvbKo6R54ozPhNhhT1zJci4vyfVbyS2lz1I7tggSShjidC8iherHyrUmB4t'

    key = '!6vTrQnaT$fFSydTEfjm@h3V'
    aes_util = AESUtil(key)


    data = {"data":{"code":"GtIXIQZV7HUdrqnaUKfl1E6S22728179","grant_type":"authorization_code"},"method":"taobao.top.auth.token.create"}



    # data = {"data":{"code":"uUjzC5ZDZSTymmhZBWM7qftn14101683","grant_type":"authorization_code"},"method":"taobao.top.auth.token.create"}
    #
    data = json.dumps(data)
    print(data)
    #
    encrypted = aes_util.encrypt(data)
    print('Encrypted:', encrypted)
    decrypted = aes_util.decrypt(encrypted)
    print("Decrypted:", decrypted)

    # 使用示例
    # encrypt_key = "56D96CE24AC4CF3432AD930977DFCE59"  # 256 位密钥，长度为 32 字节
    # # encrypt_key = "uUjzC5ZDZSTymmhZBWM7qftn14101683"  # 256 位密钥，长度为 32 字节
    # # encrypt_key = "3EB2C31888D04C1578BD03CFD5FB0DCA"  # 256 位密钥，长度为 32 字节
    # # encrypt_key = "!6vTrQnaT$fFSydTEfjm@h3V"  # 256 位密钥，长度为 32 字节
    # aes_util = AESUtil(encrypt_key)
    #
    # # 加密
    # # params = {"name": "Alice", "age": 30}
    # # encrypted = aes_util.encrypt_text(params)
    #
    # encrypted = 'vTZhMun/tiJtPokoMp1sstZQw/AIJAhVInAkx2uuWjkBQUfc7Fklrp36lZn4SMqBefxr+J/QXd1uBalobMbRIop6idrA69NuwAKctOTvMDz7hSPxVcRvsbz6oODRdAk3Jk61irvbKo6R54ozPhNhhT1zJci4vyfVbyS2lz1I7tggSShjidC8iherHyrUmB4t'
    #
    #
    # encrypted = 'tja7/todePjs1gh/7BhmY/jVVBbv9ptMlVr8jJh7e0EhRh3M5YL5Lat0H0+g4d6cpmG2lYCV0jc67W6/gYnBbakFSsYwoHergqSjOSE25E0ppNE1sshkNtoJwYnMhKdi7fnv8CkxlC+I+rV02ZBCKUlhmt9E6i+gkwlrqzE0CN0='
    #
    #
    # print("Encrypted:", encrypted)
    #
    # # 解密
    # decrypted = aes_util.decrypt_text(encrypted)
    # print("Decrypted:", decrypted)
