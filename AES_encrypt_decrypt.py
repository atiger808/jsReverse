from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes


# AES加密函数
def aes_encrypt(plain_text, key):
    # 生成随机的16字节IV (Initialization Vector)
    iv = get_random_bytes(16)

    # 创建AES加密器，使用CBC模式
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # 对明文进行PKCS7填充并加密
    ciphertext = cipher.encrypt(pad(plain_text.encode('utf-8'), AES.block_size))

    # 返回IV和密文（通常需要将IV和密文一起存储或传输）
    return iv + ciphertext


# AES解密函数
def aes_decrypt(ciphertext, key):
    # 从密文中提取IV（前16字节）
    iv = ciphertext[:16]

    # 提取实际的密文部分
    actual_ciphertext = ciphertext[16:]

    # 创建AES解密器，使用CBC模式
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # 解密并去除PKCS7填充
    plaintext = unpad(cipher.decrypt(actual_ciphertext), AES.block_size)

    # 返回解密后的明文
    return plaintext.decode('utf-8')


# 测试代码
if __name__ == "__main__":
    # 密钥必须是16字节（AES-128）、24字节（AES-192）或32字节（AES-256）
    key = get_random_bytes(32)  # 32字节密钥，对应AES-256

    # 明文
    plain_text = "Hello, this is a secret message!"

    # 加密
    encrypted_data = aes_encrypt(plain_text, key)
    print(f"Encrypted data: {encrypted_data.hex()}")

    # 解密
    decrypted_text = aes_decrypt(encrypted_data, key)
    print(f"Decrypted text: {decrypted_text}")