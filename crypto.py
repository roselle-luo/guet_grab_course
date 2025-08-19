import base64

from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA

from common import PUBLIC_KEY


def rsa_encrypt_pkcs1_v15(public_key_pem: str, message: str) -> str:
    public_key = RSA.import_key(public_key_pem)

    # 用 PKCS#1 v1.5 填充方式加密
    cipher = PKCS1_v1_5.new(public_key)

    # 加密
    encrypted_bytes = cipher.encrypt(message.encode('utf-8'))

    # base64编码输出
    encrypted_base64 = base64.b64encode(encrypted_bytes).decode('utf-8')

    #print("加密结果:", encrypted_base64)
    return encrypted_base64

def to_pem(pubkey_b64):
    lines = [pubkey_b64[i:i+64] for i in range(0, len(pubkey_b64), 64)]
    return "-----BEGIN PUBLIC KEY-----\n" + "\n".join(lines) + "\n-----END PUBLIC KEY-----"

def crypto_login_password(password, salt) -> str:
    salt_password = salt + '-' + password
    pem_key = to_pem(PUBLIC_KEY)
    encrypt_password = rsa_encrypt_pkcs1_v15(pem_key, salt_password)
    return encrypt_password