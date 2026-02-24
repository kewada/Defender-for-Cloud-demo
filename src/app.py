"""
SQL Injection - 脆弱なデータベースクエリ
CodeQL Alert: py/sql-injection
"""
import sqlite3
from flask import Flask, request

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("app.db")
    return conn


# ===== 脆弱性1: SQL Injection (文字列連結) =====
@app.route("/users/search")
def search_users():
    username = request.args.get("username")
    conn = get_db_connection()
    # 危険: ユーザー入力を直接SQL文に埋め込み
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    results = conn.execute(query).fetchall()
    return {"users": results}


# ===== 脆弱性2: SQL Injection (f-string) =====
@app.route("/users/<user_id>")
def get_user(user_id):
    conn = get_db_connection()
    # 危険: f-stringでSQL構築
    query = f"SELECT * FROM users WHERE id = {user_id}"
    result = conn.execute(query).fetchone()
    return {"user": result}


# ===== 脆弱性3: SQL Injection (format) =====
@app.route("/orders")
def get_orders():
    status = request.args.get("status")
    sort_by = request.args.get("sort", "created_at")
    conn = get_db_connection()
    # 危険: format()でSQL構築
    query = "SELECT * FROM orders WHERE status = '{}' ORDER BY {}".format(
        status, sort_by
    )
    results = conn.execute(query).fetchall()
    return {"orders": results}


# ===== 脆弱性4: Second-Order SQL Injection =====
@app.route("/profile/update", methods=["POST"])
def update_profile():
    bio = request.form.get("bio")
    user_id = request.form.get("user_id")
    conn = get_db_connection()
    # 危険: バイオをそのまま保存し、後でクエリに使用
    conn.execute(
        "UPDATE users SET bio = '" + bio + "' WHERE id = " + user_id
    )
    conn.commit()
    return {"status": "updated"}


if __name__ == "__main__":
    app.run(debug=True)
