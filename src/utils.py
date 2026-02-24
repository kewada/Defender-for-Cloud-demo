"""
Command Injection - OSコマンドインジェクション
CodeQL Alert: py/command-line-injection
"""
import os
import subprocess
from flask import Flask, request

app = Flask(__name__)


# ===== 脆弱性1: os.system によるコマンドインジェクション =====
@app.route("/system/ping")
def ping_host():
    hostname = request.args.get("host")
    # 危険: ユーザー入力をそのままOSコマンドに渡す
    os.system("ping -c 4 " + hostname)
    return {"status": "ping sent"}


# ===== 脆弱性2: subprocess.call + shell=True =====
@app.route("/system/dns")
def dns_lookup():
    domain = request.args.get("domain")
    # 危険: shell=Trueでコマンド実行
    result = subprocess.check_output(
        "nslookup " + domain, shell=True
    )
    return {"result": result.decode()}


# ===== 脆弱性3: eval() の使用 =====
@app.route("/calculate")
def calculate():
    expression = request.args.get("expr")
    # 危険: eval()でユーザー入力を実行
    result = eval(expression)
    return {"result": str(result)}


# ===== 脆弱性4: exec() の使用 =====
@app.route("/run-script", methods=["POST"])
def run_script():
    code = request.form.get("code")
    output = {}
    # 危険: exec()でユーザー提供コードを実行
    exec(code, {"output": output})
    return {"result": output}


# ===== 脆弱性5: os.popen =====
@app.route("/system/disk")
def disk_usage():
    path = request.args.get("path", "/")
    # 危険: os.popenでコマンド実行
    result = os.popen("du -sh " + path).read()
    return {"usage": result}
