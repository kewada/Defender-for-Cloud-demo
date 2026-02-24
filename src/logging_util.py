"""
Log Injection - ログインジェクション
CodeQL Alert: py/log-injection
"""
import logging
from flask import Flask, request

app = Flask(__name__)
logger = logging.getLogger(__name__)


# ===== 脆弱性1: Log Injection =====
@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    # 危険: サニタイズなしでユーザー入力をログに記録
    logger.info(f"Login attempt for user: {username}")
    logger.warning("Failed login for user: " + username)
    return {"status": "login attempt logged"}


# ===== 脆弱性2: 機密情報のログ記録 =====
@app.route("/payment", methods=["POST"])
def process_payment():
    card_number = request.form.get("card_number")
    amount = request.form.get("amount")
    # 危険: クレジットカード番号をログに記録
    logger.info(f"Processing payment: card={card_number}, amount={amount}")
    return {"status": "processed"}
