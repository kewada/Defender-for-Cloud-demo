"""
CORS Misconfiguration - CORS設定不備
CodeQL Alert: py/cors-misconfiguration
"""
from flask import Flask, request, jsonify

app = Flask(__name__)


# ===== 脆弱性1: ワイルドカードオリジン =====
@app.after_request
def add_cors_headers(response):
    # 危険: すべてのオリジンを許可
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "*"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    return response


# ===== 脆弱性2: リクエストオリジンをそのまま反射 =====
@app.route("/api/sensitive-data")
def get_sensitive_data():
    origin = request.headers.get("Origin", "*")
    response = jsonify({"data": "sensitive_information"})
    # 危険: リクエストのOriginをそのまま反射
    response.headers["Access-Control-Allow-Origin"] = origin
    response.headers["Access-Control-Allow-Credentials"] = "true"
    return response
