"""
Azure Configuration - Secret Scanning デモ用
⚠️ これらはダミー値ですが、Secret Scanningが検知するフォーマットです
"""

# ===== Secret Scanning: Azure Storage Account Key =====
AZURE_STORAGE_ACCOUNT = "prodstorageaccount"
AZURE_STORAGE_KEY = "dGhpcyBpcyBhIGR1bW15IGtleSBmb3IgZGVtbyBwdXJwb3Nlcw0KZG8gbm90IHVzZSBpbiBwcm9kdWN0aW9u"

# ===== Secret Scanning: Azure Connection String =====
AZURE_STORAGE_CONNECTION_STRING = (
    "DefaultEndpointsProtocol=https;"
    "AccountName=prodstorageaccount;"
    "AccountKey=dGhpcyBpcyBhIGR1bW15IGtleSBmb3IgZGVtbyBwdXJwb3Nlcw0K;"
    "EndpointSuffix=core.windows.net"
)

# ===== Secret Scanning: Azure SQL Connection String =====
AZURE_SQL_CONNECTION = (
    "Server=tcp:prod-sqlserver.database.windows.net,1433;"
    "Database=ProductionDB;"
    "User ID=sqladmin;"
    "Password=Str0ngP@ssw0rd!2024;"
    "Encrypt=True;"
)

# ===== Secret Scanning: Azure Service Principal =====
AZURE_CLIENT_ID = "12345678-1234-1234-1234-123456789012"
AZURE_CLIENT_SECRET = "abC8Q~dummysecretvalue.for-demo_purposes"
AZURE_TENANT_ID = "87654321-4321-4321-4321-210987654321"
