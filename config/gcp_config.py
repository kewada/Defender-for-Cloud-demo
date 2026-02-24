"""
Google Cloud Configuration - Secret Scanning デモ用
"""

# ===== Secret Scanning: Google API Key =====
GOOGLE_API_KEY = "AIzaSyDummyKeyForDemoPurposesOnly12345678"

# ===== Secret Scanning: Google OAuth Client Secret =====
GOOGLE_CLIENT_ID = "123456789012-abcdefghijklmnopqrstuvwxyz012345.apps.googleusercontent.com"
GOOGLE_CLIENT_SECRET = "GOCSPX-DummySecretForDemo1234567"

# ===== Secret Scanning: Google Service Account Key (embedded) =====
GCP_SERVICE_ACCOUNT = {
    "type": "service_account",
    "project_id": "demo-project-12345",
    "private_key_id": "key123456789",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDummyKeyDataForDemoPurposesOnlyDoNotUseInProduction\n-----END PRIVATE KEY-----\n",
    "client_email": "demo-sa@demo-project-12345.iam.gserviceaccount.com",
    "client_id": "123456789012345678901",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
}
