/**
 * 脆弱な Node.js Express サーバー
 * CodeQL で検出される脆弱性を意図的に含む
 * ⚠️ デモ目的専用 - 本番環境では使用しないこと
 */
const express = require('express');
const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');
const serialize = require('serialize-javascript');

const app = express();
app.use(express.urlencoded({ extended: true }));
app.use(express.json());

// ===== 脆弱性1: XSS (Cross-Site Scripting) =====
// CodeQL Alert: js/reflected-xss
app.get('/search', (req, res) => {
    const query = req.query.q;
    // 危険: ユーザー入力をエスケープせずに出力
    res.send(`<h1>Search results for: ${query}</h1>`);
});

// ===== 脆弱性2: SQL Injection =====
// CodeQL Alert: js/sql-injection
app.get('/user', (req, res) => {
    const userId = req.query.id;
    const sequelize = require('sequelize');
    const db = new sequelize('sqlite::memory:');
    // 危険: パラメータ化されていないSQL
    db.query(`SELECT * FROM users WHERE id = '${userId}'`);
});

// ===== 脆弱性3: Command Injection =====
// CodeQL Alert: js/command-line-injection
app.get('/ping', (req, res) => {
    const host = req.query.host;
    // 危険: ユーザー入力をコマンドに直接渡す
    const result = execSync(`ping -c 1 ${host}`);
    res.send(result.toString());
});

// ===== 脆弱性4: Path Traversal =====
// CodeQL Alert: js/path-injection
app.get('/file', (req, res) => {
    const filename = req.query.name;
    // 危険: パストラバーサル攻撃が可能
    const content = fs.readFileSync('/data/' + filename, 'utf8');
    res.send(content);
});

// ===== 脆弱性5: Open Redirect =====
// CodeQL Alert: js/server-side-unvalidated-url-redirection
app.get('/redirect', (req, res) => {
    const url = req.query.url;
    // 危険: 未検証のURLへリダイレクト
    res.redirect(url);
});

// ===== 脆弱性6: Hardcoded Secret =====
// CodeQL Alert: js/hardcoded-credentials
const API_SECRET = 'sk_live_demo_hardcoded_secret_key_12345';
const DB_PASSWORD = 'SuperSecretPassword123!';

// ===== 脆弱性7: Prototype Pollution =====
// CodeQL Alert: js/prototype-pollution
app.post('/config', (req, res) => {
    const config = {};
    const userInput = req.body;
    // 危険: プロトタイプ汚染
    for (const key in userInput) {
        config[key] = userInput[key];
    }
    res.json(config);
});

// ===== 脆弱性8: SSRF =====
// CodeQL Alert: js/request-forgery
app.get('/fetch', async (req, res) => {
    const url = req.query.url;
    const fetch = require('node-fetch');
    // 危険: ユーザー指定URLへのリクエスト
    const response = await fetch(url);
    const data = await response.text();
    res.send(data);
});

app.listen(3000);
