"""
Database Connection - Secret Scanning デモ用
"""

# ===== Secret Scanning: PostgreSQL Connection String =====
POSTGRES_URI = "postgresql://dbadmin:MyS3cretP@ss!@prod-postgres.example.com:5432/production"

# ===== Secret Scanning: MySQL Connection String =====
MYSQL_URI = "mysql://root:R00tP@ssw0rd@db.internal.example.com:3306/customers"

# ===== Secret Scanning: MongoDB Connection String =====
MONGO_URI = "mongodb://admin:Adm1nP@ssw0rd123@prod-mongo.example.com:27017/analytics?authSource=admin"

# ===== Secret Scanning: Redis Connection =====
REDIS_URL = "redis://:RedisP@ssw0rd!2024@cache.internal.example.com:6379/0"
