import base64
from textwrap import wrap

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from Crypto.Random import get_random_bytes
import binascii
import requests

PUBLIC_KEY = 'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCFY5N+9UX+0BF+xz1svFguI4CIDvmQTfINkOZ1HOO3ltBNHGQTUirUPQTyEph/+q/l8b16YYw3I2fyTH6y15s3tHf5jMei+R/20jFRGo5udwVJUwq/RozKQIRzCtPYkXG4YWBnHKhXalZ5K2fhd5i/QtB016nVugH/7eiBDWbKVwIDAQAB'

def test():
    session = requests.session()
    salt = session.get("https://bkjwtest.guet.edu.cn/student/ldap/login-salt").text
    print(f'盐值: {salt}')
    password = "test"
    salt_password = salt + '-' + password
    pem_key = to_pem(PUBLIC_KEY)
    encrypt_password = rsa_encrypt_pkcs1_v15(pem_key, salt_password)
    form = {
        'username': '1234567',
        'password': encrypt_password
    }
    response = session.post("https://bkjwtest.guet.edu.cn/student/ldap/login", json=form)
    print(response.text)


def rsa_encrypt_pkcs1_v15(public_key_pem: str, message: str) -> str:
    public_key = RSA.import_key(public_key_pem)

    # 用 PKCS#1 v1.5 填充方式加密
    cipher = PKCS1_v1_5.new(public_key)

    # 加密
    encrypted_bytes = cipher.encrypt(message.encode('utf-8'))

    # base64编码输出
    encrypted_base64 = base64.b64encode(encrypted_bytes).decode('utf-8')

    print("加密结果:", encrypted_base64)
    return encrypted_base64

def to_pem(pubkey_b64):
    lines = [pubkey_b64[i:i+64] for i in range(0, len(pubkey_b64), 64)]
    return "-----BEGIN PUBLIC KEY-----\n" + "\n".join(lines) + "\n-----END PUBLIC KEY-----"

test()

