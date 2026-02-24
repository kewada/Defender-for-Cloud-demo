# ===== IaC Scanning: 脆弱なDockerfile =====

# 脆弱性1: 古いベースイメージ
FROM python:3.14-slim

# 脆弱性2: rootユーザーで実行
USER root

# 脆弱性3: シークレットをイメージに埋め込み
ENV DATABASE_PASSWORD="ProductionP@ssw0rd!"
ENV API_KEY="sk-demo-embedded-in-dockerfile-123456"

# 脆弱性4: すべてのファイルをコピー(.envも含む)
COPY . /app

# 脆弱性5: 不要なパッケージをインストール
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    netcat-openbsd \
    ssh \
    telnet \
    && rm -rf /var/lib/apt/lists/*

# 脆弱性6: pip install --trusted-host (MITM攻撃の可能性)
RUN pip install --trusted-host pypi.org -r /app/requirements.txt

# 脆弱性7: すべてのポートを公開
EXPOSE 0-65535

# 脆弱性8: 特権モードに関連する設定
RUN chmod 777 /app

WORKDIR /app
CMD ["python", "src/app.py"]
