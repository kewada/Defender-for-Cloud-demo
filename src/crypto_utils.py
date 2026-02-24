"""
Weak Cryptography - 弱い暗号アルゴリズムの使用
CodeQL Alert: py/weak-cryptographic-algorithm, py/insecure-hash
"""
import hashlib
import hmac
from Crypto.Cipher import DES, ARC4, Blowfish
from Crypto.Hash import MD5, SHA


# ===== 脆弱性1: MD5によるパスワードハッシュ =====
def hash_password_md5(password: str) -> str:
    # 危険: MD5はパスワードハッシュに不適切
    return hashlib.md5(password.encode()).hexdigest()


# ===== 脆弱性2: SHA1によるパスワードハッシュ =====
def hash_password_sha1(password: str) -> str:
    # 危険: SHA1はパスワードハッシュに不適切
    return hashlib.sha1(password.encode()).hexdigest()


# ===== 脆弱性3: DES暗号化 =====
def encrypt_des(data: bytes, key: bytes) -> bytes:
    # 危険: DESは56-bitキーで安全でない
    cipher = DES.new(key[:8], DES.MODE_ECB)
    padded = data + b"\0" * (8 - len(data) % 8)
    return cipher.encrypt(padded)


# ===== 脆弱性4: RC4暗号化 =====
def encrypt_rc4(data: bytes, key: bytes) -> bytes:
    # 危険: RC4は既知の脆弱性あり
    cipher = ARC4.new(key)
    return cipher.encrypt(data)


# ===== 脆弱性5: ECBモード =====
def encrypt_ecb(data: bytes, key: bytes) -> bytes:
    # 危険: ECBモードはパターンが漏洩
    cipher = Blowfish.new(key, Blowfish.MODE_ECB)
    padded = data + b"\0" * (8 - len(data) % 8)
    return cipher.encrypt(padded)


# ===== 脆弱性6: ソルトなしハッシュ =====
def hash_without_salt(password: str) -> str:
    # 危険: ソルトなしでハッシュ
    return hashlib.sha256(password.encode()).hexdigest()


# ===== 脆弱性7: 弱いHMAC =====
def create_weak_hmac(message: bytes, key: bytes) -> str:
    # 危険: MD5ベースのHMAC
    return hmac.new(key, message, hashlib.md5).hexdigest()
