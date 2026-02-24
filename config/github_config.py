"""
GitHub Configuration - Secret Scanning デモ用
⚠️ これらはダミー値ですが、Secret Scanningが検知するフォーマットです
"""

# ===== Secret Scanning: GitHub Personal Access Token =====
GITHUB_PAT = "ghp_ABCDEFGHIJKLMNOPQRSTUVWXYZabcdef01"

# ===== Secret Scanning: GitHub OAuth App =====
GITHUB_OAUTH_CLIENT_ID = "Iv1.abc123def456ghi7"
GITHUB_OAUTH_CLIENT_SECRET = "abcdef0123456789abcdef0123456789abcdef01"

# ===== Secret Scanning: GitHub App Private Key =====
GITHUB_APP_ID = "12345"
GITHUB_APP_PRIVATE_KEY = """-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEA0Z3VS5JJcds3xfn/ygWyF8PbnGy0AHB7MhgHcTz6sE2I2yPB
aNlHHhEOGMXe0n2rW8oMzPmTSzLgEzSxVo5eLbOExampleKeyForDemoPurposes
OnlyDoNotUseInProductionThisIsFakeDataForSecurityScanningDemo1234
ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz012345678
SecondLineOfFakeKeyMaterialThatLooksRealisticButIsCompletelyDummy
ThirdLineOfDummyDataForThePrivateKeyDemonstrationPurposesOnly12
FourthLineContinuingTheFakePrivateKeyForGitHubAdvancedSecurity00
-----END RSA PRIVATE KEY-----"""

GITHUB_CONFIG = {
    "token": GITHUB_PAT,
    "org": "example-corp",
    "repo": "internal-tools",
}
