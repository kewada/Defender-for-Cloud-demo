"""
AWS Configuration - Secret Scanning デモ用
⚠️ これらはダミー値ですが、Secret Scanningが検知するフォーマットです
"""

# ===== Secret Scanning: AWS Access Key =====
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

# ===== Secret Scanning: AWS Session Token =====
AWS_SESSION_TOKEN = "FwoGZXIvYXdzEBYaDHqa0AP3ey0BGCExampleTokenValue1234567890abcdefghijklmnop"

AWS_CONFIG = {
    "region": "ap-northeast-1",
    "access_key": AWS_ACCESS_KEY_ID,
    "secret_key": AWS_SECRET_ACCESS_KEY,
    "s3_bucket": "production-data-backup",
}
