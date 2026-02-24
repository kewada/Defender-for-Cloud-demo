"""
Hardcoded Credentials - ハードコードされた認証情報
CodeQL Alert: py/hardcoded-credentials
"""
import sqlite3
import pymysql


# ===== 脆弱性1: ハードコードされたDB認証情報 =====
DB_HOST = "db.production.internal"
DB_USER = "admin"
DB_PASSWORD = "P@ssw0rd123!"  # 危険: パスワードをハードコード
DB_NAME = "production_db"


def get_mysql_connection():
    # 危険: ハードコードされた認証情報で接続
    return pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
    )


# ===== 脆弱性2: ハードコードされたAPIキー =====
INTERNAL_API_KEY = "sk-proj-abc123def456ghi789jkl012"  # 危険


# ===== 脆弱性3: 接続文字列にパスワード埋め込み =====
CONNECTION_STRING = "postgresql://admin:SuperSecret123@prod-db.example.com:5432/maindb"


# ===== 脆弱性4: ハードコードされた暗号化キー =====
ENCRYPTION_KEY = b"0123456789abcdef0123456789abcdef"
SECRET_IV = b"abcdef0123456789"
