"""
SSRF (Server-Side Request Forgery) - サーバーサイドリクエストフォージェリ
CodeQL Alert: py/ssrf
"""
import requests
import urllib.request
from flask import Flask, request as flask_request

app = Flask(__name__)


# ===== 脆弱性1: SSRF via requests.get =====
@app.route("/proxy/fetch")
def fetch_url():
    url = flask_request.args.get("url")
    # 危険: ユーザー提供URLに直接リクエスト
    response = requests.get(url)
    return {"content": response.text, "status": response.status_code}


# ===== 脆弱性2: SSRF via urllib =====
@app.route("/proxy/image")
def fetch_image():
    image_url = flask_request.args.get("image_url")
    # 危険: 内部ネットワークへのアクセスが可能
    response = urllib.request.urlopen(image_url)
    data = response.read()
    return data


# ===== 脆弱性3: SSRF with POST =====
@app.route("/webhook/test", methods=["POST"])
def test_webhook():
    webhook_url = flask_request.form.get("webhook_url")
    payload = flask_request.form.get("payload", "{}")
    # 危険: ユーザー指定のURLにPOSTリクエスト
    response = requests.post(webhook_url, data=payload)
    return {"status": response.status_code}


# ===== 脆弱性4: SSRF in URL construction =====
@app.route("/api/service")
def call_service():
    service_host = flask_request.args.get("host", "api.internal")
    endpoint = flask_request.args.get("endpoint", "/health")
    # 危険: ユーザー入力でURL構築
    url = f"http://{service_host}:8080{endpoint}"
    response = requests.get(url, timeout=5)
    return {"result": response.json()}
