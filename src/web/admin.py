"""
Missing Authentication - 認証チェックの欠如
CodeQL Alert: py/missing-rate-limiting, py/insecure-default-value
"""
from flask import Flask, request, jsonify

app = Flask(__name__)

# ===== 脆弱性: 管理者エンドポイントに認証なし =====
@app.route("/admin/users", methods=["GET"])
def list_all_users():
    # 危険: 認証チェックなし
    return jsonify({"users": ["admin", "user1", "user2"]})


@app.route("/admin/users/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    # 危険: 認可チェックなし
    return jsonify({"deleted": user_id})


@app.route("/admin/config", methods=["PUT"])
def update_config():
    # 危険: レート制限なし、認証なし
    new_config = request.get_json()
    return jsonify({"updated": True, "config": new_config})


@app.route("/admin/export")
def export_data():
    # 危険: 機密データの漏洩
    export_format = request.args.get("format", "csv")
    return jsonify({"format": export_format, "data": "all_user_records..."})
