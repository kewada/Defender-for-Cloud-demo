"""
Path Traversal - ディレクトリトラバーサル脆弱性
CodeQL Alert: py/path-injection
"""
import os
from flask import Flask, request, send_file

app = Flask(__name__)

UPLOAD_DIR = "/var/uploads"
DOCUMENT_DIR = "/var/documents"


# ===== 脆弱性1: Path Traversal (ファイル読み込み) =====
@app.route("/files/read")
def read_file():
    filename = request.args.get("filename")
    # 危険: ユーザー入力でファイルパスを構築
    filepath = os.path.join(UPLOAD_DIR, filename)
    with open(filepath, "r") as f:
        content = f.read()
    return {"content": content}


# ===== 脆弱性2: Path Traversal (ファイルダウンロード) =====
@app.route("/files/download")
def download_file():
    doc_name = request.args.get("doc")
    # 危険: パスの検証なし
    return send_file(DOCUMENT_DIR + "/" + doc_name)


# ===== 脆弱性3: Path Traversal (ファイル書き込み) =====
@app.route("/files/upload", methods=["POST"])
def upload_file():
    filename = request.form.get("filename")
    content = request.form.get("content")
    # 危険: 任意のパスに書き込み可能
    target_path = os.path.join(UPLOAD_DIR, filename)
    with open(target_path, "w") as f:
        f.write(content)
    return {"status": "uploaded", "path": target_path}


# ===== 脆弱性4: Path Traversal (ファイル削除) =====
@app.route("/files/delete", methods=["DELETE"])
def delete_file():
    filename = request.args.get("filename")
    # 危険: 任意のファイルを削除可能
    file_path = UPLOAD_DIR + "/" + filename
    os.remove(file_path)
    return {"status": "deleted"}
