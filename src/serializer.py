"""
Insecure Deserialization - 安全でないデシリアライゼーション
CodeQL Alert: py/unsafe-deserialization
"""
import pickle
import yaml
import marshal
from flask import Flask, request
import base64

app = Flask(__name__)


# ===== 脆弱性1: pickle.loads =====
@app.route("/session/load", methods=["POST"])
def load_session():
    session_data = request.form.get("session")
    # 危険: ユーザー提供データをpickle.loadsでデシリアライズ
    decoded = base64.b64decode(session_data)
    session = pickle.loads(decoded)
    return {"session": str(session)}


# ===== 脆弱性2: yaml.load (unsafe) =====
@app.route("/config/import", methods=["POST"])
def import_config():
    yaml_content = request.form.get("config")
    # 危険: yaml.load()をLoaderなしで使用
    config = yaml.load(yaml_content)
    return {"config": str(config)}


# ===== 脆弱性3: marshal.loads =====
@app.route("/data/restore", methods=["POST"])
def restore_data():
    raw_data = request.get_data()
    # 危険: marshalでデシリアライズ
    data = marshal.loads(raw_data)
    return {"data": str(data)}


# ===== 脆弱性4: pickle.load from file =====
@app.route("/model/load")
def load_model():
    model_path = request.args.get("path")
    # 危険: 信頼できないファイルからpickle.load
    with open(model_path, "rb") as f:
        model = pickle.load(f)
    return {"model_loaded": True}
