from Crypto.Cipher import AES
import base64

from cloudware_client.util.account import AccountUtil


class EncryptUtil(object):

    @classmethod
    def add_to_32(cls, value):
        while len(value) % 32 != 0:
            value += '\0'
        # 返回bytes
        return str.encode(value)

    @classmethod
    def encrypt(cls, plain_text, secret_key):
        # 初始化加密器
        aes = AES.new(cls.add_to_32(secret_key), AES.MODE_ECB)
        # 先进行aes加密
        encrypt_aes = aes.encrypt(cls.add_to_32(plain_text))
        # 用base64转成字符串形式
        encrypted_text = str(base64.encodebytes(encrypt_aes), encoding='utf-8')  # 执行加密并转码返回bytes
        return encrypted_text

    # 解密方法
    @classmethod
    def decrypt(cls, secret_text, secret_key):
        # 密文
        # 初始化加密器
        aes = AES.new(cls.add_to_32(secret_key), AES.MODE_ECB)
        # 优先逆向解密base64成bytes
        base64_decrypted = base64.decodebytes(secret_text.encode(encoding='utf-8'))
        # 执行解密密并转码返回str
        decrypted_text = str(aes.decrypt(base64_decrypted), encoding='utf-8').replace('\0', '')
        return decrypted_text


if __name__ == '__main__':
    secret_key = AccountUtil.get_secret_key()
    print(secret_key)
    secret_text = EncryptUtil.encrypt("lock it", secret_key)
    print(EncryptUtil.decrypt(secret_text, secret_key))
