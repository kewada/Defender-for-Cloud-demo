"""
Cross-Site Scripting (XSS) - 脆弱なビュー
CodeQL Alert: py/reflective-xss, py/stored-xss
"""
from flask import Flask, request, make_response, redirect
from markupsafe import Markup

app = Flask(__name__)


# ===== 脆弱性1: Reflected XSS =====
@app.route("/search")
def search():
    query = request.args.get("q", "")
    # 危険: ユーザー入力をエスケープせずHTMLに出力
    html = f"<h1>検索結果: {query}</h1><p>結果が見つかりませんでした。</p>"
    return html


# ===== 脆弱性2: Stored XSS =====
comments = []

@app.route("/comments", methods=["POST"])
def add_comment():
    comment = request.form.get("comment")
    author = request.form.get("author")
    # 危険: サニタイズなしで保存
    comments.append({"author": author, "comment": comment})
    return redirect("/comments")

@app.route("/comments")
def show_comments():
    html = "<h1>コメント一覧</h1>"
    for c in comments:
        # 危険: エスケープなしで出力
        html += f"<div><b>{c['author']}</b>: {c['comment']}</div>"
    return html


# ===== 脆弱性3: DOM-based XSS via Markup =====
@app.route("/welcome")
def welcome():
    name = request.args.get("name", "Guest")
    # 危険: Markup()で安全とマーク
    greeting = Markup(f"<h2>ようこそ、{name}さん!</h2>")
    return str(greeting)


# ===== 脆弱性4: XSS in HTTP Header =====
@app.route("/download")
def download():
    filename = request.args.get("file", "document.pdf")
    response = make_response("File content here")
    # 危険: Content-Dispositionヘッダにユーザー入力
    response.headers["Content-Disposition"] = f"attachment; filename={filename}"
    return response
