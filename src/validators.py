"""
ReDoS (Regular Expression Denial of Service)
CodeQL Alert: py/redos, py/regex-injection
"""
import re
from flask import Flask, request

app = Flask(__name__)


# ===== 脆弱性1: ReDoS - 指数的バックトラッキング =====
def validate_email_unsafe(email: str) -> bool:
    # 危険: 壊滅的バックトラッキングが発生するパターン
    pattern = r"^([a-zA-Z0-9]+\.)*[a-zA-Z0-9]+@([a-zA-Z0-9]+\.)*[a-zA-Z0-9]+$"
    return bool(re.match(pattern, email))


# ===== 脆弱性2: ReDoS - ネストされた量指定子 =====
def validate_url_unsafe(url: str) -> bool:
    # 危険: (a+)+ パターン
    pattern = r"^https?://([\w-]+\.)+[\w-]+(/[\w-./?%&=]*)*$"
    return bool(re.match(pattern, url))


# ===== 脆弱性3: Regex Injection =====
@app.route("/search/regex")
def regex_search():
    pattern = request.args.get("pattern")
    text = request.args.get("text")
    # 危険: ユーザー入力を正規表現として直接使用
    matches = re.findall(pattern, text)
    return {"matches": matches}


# ===== 脆弱性4: ReDoS - 重複する選択肢 =====
def validate_input_unsafe(input_str: str) -> bool:
    # 危険: 重複する選択肢による指数的バックトラッキング
    pattern = r"^(a|a)*$"
    return bool(re.match(pattern, input_str))
