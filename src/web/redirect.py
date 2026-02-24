"""
Open Redirect - オープンリダイレクト
CodeQL Alert: py/url-redirection
"""
from flask import Flask, request, redirect

app = Flask(__name__)


# ===== 脆弱性: Open Redirect =====
@app.route("/login/callback")
def login_callback():
    return_url = request.args.get("return_to", "/")
    # 危険: ユーザー入力URLにリダイレクト
    return redirect(return_url)


@app.route("/logout")
def logout():
    next_page = request.args.get("next")
    # 危険: 外部サイトへリダイレクト可能
    return redirect(next_page)
