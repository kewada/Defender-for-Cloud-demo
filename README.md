# Defender for Cloud - Advanced Security デモリポジトリ

[![GitHub last commit](https://img.shields.io/github/last-commit/kewada/Defender-for-Cloud-demo?cacheSeconds=3600)](https://github.com/kewada/Defender-for-Cloud-demo/commits)
[![GitHub repo size](https://img.shields.io/github/repo-size/kewada/Defender-for-Cloud-demo?cacheSeconds=3600)](https://github.com/kewada/Defender-for-Cloud-demo)
[![GitHub stars](https://img.shields.io/github/stars/kewada/Defender-for-Cloud-demo?cacheSeconds=3600)](https://github.com/kewada/Defender-for-Cloud-demo/stargazers)
[![GitHub issues](https://img.shields.io/github/issues/kewada/Defender-for-Cloud-demo?cacheSeconds=3600)](https://github.com/kewada/Defender-for-Cloud-demo/issues)
[![GitHub pull requests](https://img.shields.io/github/issues-pr/kewada/Defender-for-Cloud-demo?cacheSeconds=3600)](https://github.com/kewada/Defender-for-Cloud-demo/pulls)

[![CodeQL](https://github.com/kewada/Defender-for-Cloud-demo/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/kewada/Defender-for-Cloud-demo/actions/workflows/codeql-analysis.yml)
[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Java](https://img.shields.io/badge/Java-11+-orange.svg)](https://openjdk.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/kewada/Defender-for-Cloud-demo/blob/main/LICENSE)
[![Demo Only](https://img.shields.io/badge/⚠️_Demo_Only-Do_Not_Use_in_Production-red.svg)](#)

> ⚠️ **警告**: このリポジトリは **デモ・教育目的専用** です。意図的に脆弱性を含んでいます。本番環境では絶対に使用しないでください。

## 概要

Microsoft Defender for Cloud の GitHub Advanced Security 機能をデモンストレーションするためのリポジトリです。以下の3つのアラートカテゴリすべてを網羅しています。

## 検知対象アラートカテゴリ

### 1. Code Scanning (CodeQL)
| カテゴリ | ファイル | 脆弱性 |
|---------|---------|--------|
| SQL Injection | `src/app.py` | パラメータ化されていないSQL |
| XSS (Cross-Site Scripting) | `src/web/views.py` | エスケープなしの出力 |
| Path Traversal | `src/file_handler.py` | ディレクトリトラバーサル |
| Command Injection | `src/utils.py` | OSコマンドインジェクション |
| Insecure Deserialization | `src/serializer.py` | Pickle の安全でない使用 |
| SSRF | `src/api_client.py` | サーバーサイドリクエストフォージェリ |
| XXE | `src/xml_parser.java` | XML外部実体参照 |
| Hardcoded Credentials | `src/db_config.py` | ハードコードされた認証情報 |
| Weak Cryptography | `src/crypto_utils.py` | 弱い暗号アルゴリズム |
| Open Redirect | `src/web/redirect.py` | オープンリダイレクト |
| LDAP Injection | `src/auth/ldap_auth.py` | LDAPインジェクション |
| Log Injection | `src/logging_util.py` | ログインジェクション |
| ReDoS | `src/validators.py` | 正規表現DoS |
| Insecure Randomness | `src/token_gen.py` | 安全でない乱数生成 |
| Missing Auth | `src/web/admin.py` | 認証チェックの欠如 |
| CORS Misconfiguration | `src/web/cors_config.py` | CORS設定不備 |

### 2. Secret Scanning
| 種別 | ファイル |
|------|---------|
| AWS Access Key | `config/aws_config.py` |
| Azure Storage Key | `config/azure_config.py` |
| GitHub Token | `config/github_config.py` |
| Slack Webhook | `config/slack_config.py` |
| Database Connection String | `config/db_connection.py` |
| Private Key (RSA) | `config/keys/private.pem` |
| JWT Secret | `config/jwt_config.py` |
| SendGrid API Key | `config/email_config.py` |
| Google API Key | `config/gcp_config.py` |
| Stripe API Key | `config/payment_config.py` |

### 3. Dependency Scanning (Dependabot)
| 言語 | ファイル | 脆弱なパッケージ例 |
|------|---------|-------------------|
| Python | `requirements.txt` | Django, Flask, requests 等の旧バージョン |
| Node.js | `package.json` | lodash, express 等の旧バージョン |
| Java | `pom.xml` | Log4j, Spring 等の旧バージョン |
| .NET | `packages.config` | Newtonsoft.Json 等の旧バージョン |
| Go | `go.mod` | 旧バージョンの依存関係 |

## セットアップ

1. このリポジトリを GitHub にプッシュ
2. GitHub Advanced Security を有効化
3. CodeQL Analysis ワークフローを設定
4. Dependabot を有効化
5. Secret Scanning を有効化

## ワークフロー設定

`.github/workflows/codeql-analysis.yml` を使用してください。
