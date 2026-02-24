"""
LDAP Injection - LDAPインジェクション
CodeQL Alert: py/ldap-injection
"""
import ldap
from flask import Flask, request

app = Flask(__name__)

LDAP_SERVER = "ldap://ldap.example.com"
BASE_DN = "dc=example,dc=com"


# ===== 脆弱性1: LDAP Injection (認証) =====
@app.route("/auth/ldap", methods=["POST"])
def ldap_authenticate():
    username = request.form.get("username")
    password = request.form.get("password")

    conn = ldap.initialize(LDAP_SERVER)
    # 危険: ユーザー入力をLDAPフィルタに直接埋め込み
    search_filter = f"(&(uid={username})(userPassword={password}))"
    result = conn.search_s(BASE_DN, ldap.SCOPE_SUBTREE, search_filter)

    if result:
        return {"authenticated": True}
    return {"authenticated": False}


# ===== 脆弱性2: LDAP Injection (検索) =====
@app.route("/directory/search")
def search_directory():
    department = request.args.get("dept")
    # 危険: フィルタインジェクション
    search_filter = "(department=" + department + ")"
    conn = ldap.initialize(LDAP_SERVER)
    conn.simple_bind_s("cn=readonly,dc=example,dc=com", "readonlypass")
    results = conn.search_s(BASE_DN, ldap.SCOPE_SUBTREE, search_filter)
    return {"results": str(results)}
