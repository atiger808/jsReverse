# -*- coding:utf-8 -*-
# @FileName  :DES_DES3_AES_RSA_MD5_SHA_HMAC.py
# @Time      :2022-10-27 10:58
# @Author    :admin

"""
目前总结有下面几点：

对称加密（加密解密密钥相同）：DES、DES3、AES

非对称加密（分公钥私钥）：RSA

信息摘要算法/签名算法：MD5、HMAC、SHA

前端实际使用中MD5、AES、RSA使用频率是最高的

几种加密方式配合次序：采用非对称加密算法管理对称算法的密钥，然后用对称加密算法加密数据，用签名算法生成非对称加密的摘要

DES、DES3、AES、RSA、MD5、SHA、HMAC传入的消息或者密钥都是bytes数据类型，不是bytes数据类型的需要先转换；密钥一般是8的倍数

Python实现RSA中，在rsa库中带有生成签名和校对签名的方法

安全性：DES<DES3=AES<RSA,至于MD5、SHA、HMAC不好说了
"""

import base64
import rsa
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from pyDes import des, CBC, PAD_PKCS5
from Crypto.Cipher import DES3
import hashlib
import hmac

from loguru import logger


class USE_AES:
    """
    AES
    除了MODE_SIV模式key长度为：32, 48, or 64,
    其余key长度为16, 24 or 32
    CBC模式穿入iv参数
    本例使用常用的ECB模式
    """

    def __init__(self, key):
        if len(key) > 32:
            key = key[:32]
        self.key = self.to_16(key)

    def to_16(self, key):
        """
        转为16倍数的bytes数据
        """
        key = bytes(key, encoding='utf8')
        while len(key) % 16 != 0:
            key += b'\0'
        return key

    def aes(self):
        return AES.new(self.key, AES.MODE_ECB)  # 初始化加密器

    def encrypt(self, text):
        aes = self.aes()
        # 加密
        return str(base64.encodebytes(aes.encrypt(self.to_16(text))), encoding='utf8').replace('\n', '')

    def decodebytes(self, text):
        aes = self.aes()
        # 解密
        return str(aes.decrypt(base64.decodebytes(bytes(text, encoding='utf8'))).rstrip(b'\0').decode('utf8'))

from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
import base64
from cryptography.fernet import Fernet

class AesUtil(object):
    def __init__(self, key, encodeType='base64'):
        self.key = key
        self.encodeType = encodeType

    def encrypt(self, text):
        result = ''
        try:
            f = Fernet(self.key)
            if self.encodeType == 'base64':
                result = f.encrypt(text.encode()).decode()
            else:
                result = b2a_hex(f.encrypt(text.encode())).decode()
        except Exception as e:
            logger.info(f'error: {e}')
        return result

    def decrypt(self, text):
        result = ''
        try:
            f = Fernet(self.key)
            if self.encodeType == 'base64':
                result = f.decrypt(text.encode()).decode()
            else:
                result = f.decrypt(a2b_hex(text)).decode()
        except Exception as e:
            logger.info(f'error: {e}')
        return result



class USE_RSA:
    """
    生成密钥可保存.pem格式文件
    1024位证书， 加密时最大支持117个字节， 解密时为128；
    2048位证书， 加密时最大支持245个字节， 解密时为256.
    加密大文件时需要先用AES或者DES加密， 再用RSA加密密钥
    详细见文档：https://stuvel.eu/files/python-rsa-doc/usage.html/#generating-keys
    """

    def __init__(self, number=1024):
        """
        :param number: 公钥， 私钥
        """
        self.pubkey, self.privkey = rsa.newkeys(number)

    def rsaEncrypt(self, text):
        """
        :param text: str
        :return: bytes
        """
        content = text.encode('utf-8')
        crypto = rsa.encrypt(content, self.pubkey)
        return crypto

    def rsaDecrypt(self, text):
        """
        :param text: bytes
        :return str
        """
        content = rsa.decrypt(text, self.privkey)
        con = content.decode('utf-8')
        return con

    def savePem(self, path_name, text):
        """
        :param path_name: 保存路径
        :param text: str
        :return: bytes
        """
        if 'PEM' in path_name.upper():
            path_name = path_name[:-4]
        with open(f'{path_name}.pem', 'bw') as f:
            f.write(text.save_pkcs1())

    def readPem(self, path_name, key_type):
        """
        :param path_name: 密钥文件
        :param key_type: 类型
        :return:
        """
        if 'pubkey' in key_type:
            self.pubkey = rsa.PublicKey.load_pkcs1(path_name)
        else:
            self.privkey = rsa.PublicKey.load_pkcs1(path_name)
        return True

    def sign(self, message, priv_key=None, hash_method='SHA-1'):
        """
        生成明文的哈希签名以便还原后对照
        :param message: str
        :param priv_key:
        :param hash_method: 哈希的模式
        """
        if None == priv_key:
            priv_key = self.privkey
        return rsa.sign(message.encode(), priv_key, hash_method)

    def checkSign(self, mess, result, pubkey=None):
        """
        验证签名：传入解密后明文，签名， 公钥， 验证成功返回哈希方法， 失败则报错
        :param mess: str
        :param result: bytes
        :param pubkey:
        :return: str
        """
        if None == pubkey:
            pubkey = self.pubkey
        try:
            result = rsa.verify(mess, result, pubkey)
            return result
        except:
            return False


class USE_DES:
    """
    des(key, [mode], [IV], [pad], [pad mode])
    key: 必须正好8字节
    mode(模式)：ECB, CBC
    iv: CBC模式中必须提供长8字节
    pad：填充字符
    padmode:加密填充模式 PAD_NORMAL, OR PAD_PKCS5
    """

    def __init__(self, key, iv):
        if not isinstance(key, bytes):
            key = bytes(key, encoding='utf8')
        if not isinstance(iv, bytes):
            iv = bytes(iv, encoding='utf8')
        self.key = key
        self.iv = iv

    def encrypt(self, text):
        """
        DES 加密
        :param text: 原始字符串
        :return: 加密后字符串，bytes
        """
        if not isinstance(text, bytes):
            text = bytes(text, 'utf-8')
        secret_key = self.key
        iv = self.iv
        k = des(secret_key, CBC, iv, pad=None, padmode=PAD_PKCS5)
        en = k.encrypt(text, padmode=PAD_PKCS5)
        return en

    def decrypt(self, text):
        """
        DES 解密
        :param text: 加密后的字符串， bytes
        :return: 解密后的字符串
        """
        secret_key = self.key
        iv = self.iv
        k = des(secret_key, CBC, iv, pad=None, padmode=PAD_PKCS5)
        de = k.decrypt(text, padmode=PAD_PKCS5)
        return de.decode()


class USE_DES3:
    """
    new(key, mode, *args, **kwargs)
    key: 必须8bytes倍数介于16-24
    mode:
    iv: 初始化向量适用于MODE_CBC, MODE_CFB, MODE_OFB, MODE_OPENPGP,四种模式
        MODE_CBC, MODE_CFB, and MODE_OFB 长度为8bytes
        MODE_OPENPGP 加密时8bytes， 解密时10bytes
        未提供默认随机生成
    nonce: 仅在 MODE_EAX and MODE_CTR 模式中使用
            MODE_EAX 建议16bytes
            MODE_CTR 建议 [0, 7]长度
            未提供随机生成
    segment_size: 分段大小， 仅在 MODE_CFB 模式中使用， 长度为8倍数， 未指定则默认8
    mac_len: 使用 MODE_EAX模式， 身份验证标记的长度（字节）， 它不能超过8（默认值）
    initial_value: 使用 MODE_CTR， 计数器的初始值计数器块。默认为 0.
    """

    def __init__(self, key):
        self.key = key
        self.mode = DES3.MODE_ECB

    def encrypt(self, text):
        """
        传入明文
        :param text: bytes类型， 长度是KEY的倍数
        :return:
        """
        if not isinstance(text, bytes):
            text = bytes(text, 'utf-8')
        x = len(text) % 8
        text = text + b'\0' * x
        cryptor = DES3.new(self.key, self.mode)
        ciphertext = cryptor.encrypt(text)
        return ciphertext


    def decrypt(self, text):
        cryptor = DES3.new(self.key, self.mode)
        plain_text = cryptor.decrypt(text)
        st = str(plain_text.decode('utf-8')).rstrip('\0')
        return st


def USE_MD5(text):
    if not isinstance(text, bytes):
        text = bytes(text, 'utf-8')
    m = hashlib.md5()
    m.update(text)
    return m.hexdigest()


def USE_HMAC(key, text):
    if not isinstance(key, bytes):
        key = bytes(key, 'utf-8')
    if not isinstance(text, bytes):
        text = bytes(text, 'utf-8')
    h = hmac.new(key, text, digestmod='MD5')
    return h.hexdigest()


def USE_SHA(text):
    if not isinstance(text, bytes):
        text = bytes(text, 'utf-8')
    sha = hashlib.sha1(text)
    encrypts = sha.hexdigest()
    return encrypts


from string import printable
from hashids import Hashids

# 混淆ID
HASHIDS_OBJ = Hashids(salt='live_video', min_length=16, alphabet=printable[10:62])


if __name__ == "__main__":
    key = 'qwwasdzxcc'
    d = USE_AES(key)
    text = '你好啊'
    print(d.key)
    r = d.encrypt(text)
    print(r)
    r = d.decodebytes(r)
    print(r)

    text = '测试加密'
    rsa_test = USE_RSA()
    a = rsa_test.rsaEncrypt(text)
    print(a)
    b = rsa_test.rsaDecrypt(a)
    print(b)

    des_test = USE_DES(b'12345678', b'12345678')
    a = des_test.encrypt(text)
    print(a)
    b = des_test.decrypt(a)
    print(b)

    des3_test = USE_DES3(b'123456789qweasdz')
    a = des3_test.encrypt(text)
    print(a)
    b = des3_test.decrypt(a)
    print(b)

    md5_test = USE_MD5(text)
    print(md5_test)
    hmac_test = USE_HMAC('123456', text)
    print(hmac_test)
    sha_test = USE_SHA(text)
    print(sha_test)

    key = 'Ow2Qd11KeZS_ahNOMicpWUr3nu3RjOUYa0_GEuMDlOc='
    p = AesUtil(key, encodeType='base64')
    encode_str = 'gAAAAABmaQ8_MkUHKHSbbinTQ7nr5IW7tow3kJQCcjrdNFxu3Z3dxyZ71CuDKxEZZyMx1jfsfFoQyh8vcGcMCoLi5S_PIQGHWw=='
    decode_str = p.decrypt(encode_str)  # 解密
    print(f'decode_str: {decode_str}')

    video_id = 'xbyYqWergVJGjagd'
    video_id = 'qzjgvOMDxEpGBmbE'
    decode_video_id = HASHIDS_OBJ.decode(video_id)
    print(f'decode_video_id: {decode_video_id}')

