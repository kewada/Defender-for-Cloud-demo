"""
Insecure Randomness - 安全でない乱数生成
CodeQL Alert: py/insecure-randomness
"""
import random
import time
import hashlib
from flask import Flask

app = Flask(__name__)


# ===== 脆弱性1: random.randint でトークン生成 =====
def generate_session_token() -> str:
    # 危険: 暗号論的に安全でない乱数
    token = "".join([str(random.randint(0, 9)) for _ in range(32)])
    return token


# ===== 脆弱性2: random.choice でパスワードリセットトークン =====
def generate_reset_token() -> str:
    chars = "abcdefghijklmnopqrstuvwxyz0123456789"
    # 危険: random.choiceは予測可能
    return "".join(random.choice(chars) for _ in range(20))


# ===== 脆弱性3: タイムスタンプベースのトークン =====
def generate_api_key() -> str:
    # 危険: タイムスタンプから予測可能
    timestamp = str(time.time())
    return hashlib.md5(timestamp.encode()).hexdigest()


# ===== 脆弱性4: シードが固定 =====
def generate_otp() -> str:
    # 危険: 固定シードで乱数を初期化
    random.seed(42)
    return str(random.randint(100000, 999999))


# ===== 脆弱性5: random.getrandbits =====
def generate_csrf_token() -> str:
    # 危険: CSRFトークンに非暗号論的乱数
    return hex(random.getrandbits(128))[2:]
