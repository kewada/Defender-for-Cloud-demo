# ===== IaC Scanning: 脆弱なTerraform設定 =====
# Defender for Cloud の IaC スキャンで検知されます

provider "azurerm" {
  features {}
}

# 脆弱性1: ストレージアカウントのHTTPSが無効
resource "azurerm_storage_account" "demo" {
  name                     = "demostorageaccount"
  resource_group_name      = "demo-rg"
  location                 = "japaneast"
  account_tier             = "Standard"
  account_replication_type = "LRS"
  enable_https_traffic_only = false  # 危険: HTTPを許可
  min_tls_version          = "TLS1_0"  # 危険: 古いTLSバージョン
}

# 脆弱性2: NSGで全ポート開放
resource "azurerm_network_security_rule" "allow_all" {
  name                        = "AllowAll"
  priority                    = 100
  direction                   = "Inbound"
  access                      = "Allow"
  protocol                    = "*"
  source_port_range           = "*"
  destination_port_range      = "*"          # 危険: 全ポート開放
  source_address_prefix       = "*"          # 危険: 全IPから許可
  destination_address_prefix  = "*"
  resource_group_name         = "demo-rg"
  network_security_group_name = "demo-nsg"
}

# 脆弱性3: SQLサーバーのファイアウォールが全開
resource "azurerm_sql_firewall_rule" "allow_all" {
  name                = "AllowAllAzureIps"
  resource_group_name = "demo-rg"
  server_name         = "demo-sql-server"
  start_ip_address    = "0.0.0.0"   # 危険
  end_ip_address      = "255.255.255.255"  # 危険
}

# 脆弱性4: Key Vault のソフトデリートが無効
resource "azurerm_key_vault" "demo" {
  name                = "demo-keyvault"
  location            = "japaneast"
  resource_group_name = "demo-rg"
  tenant_id           = "00000000-0000-0000-0000-000000000000"
  sku_name            = "standard"
  soft_delete_retention_days = 7
  purge_protection_enabled   = false  # 危険
}

# 脆弱性5: 暗号化なしのディスク
resource "azurerm_managed_disk" "demo" {
  name                 = "demo-disk"
  location             = "japaneast"
  resource_group_name  = "demo-rg"
  storage_account_type = "Standard_LRS"
  create_option        = "Empty"
  disk_size_gb         = 100
  # 危険: encryption_settings が未設定
}

# 脆弱性6: 監査ログが無効なSQLサーバー
resource "azurerm_mssql_server" "demo" {
  name                         = "demo-sqlserver"
  resource_group_name          = "demo-rg"
  location                     = "japaneast"
  version                      = "12.0"
  administrator_login          = "sqladmin"
  administrator_login_password = "P@ssw0rd123!"  # 危険: ハードコード
  minimum_tls_version          = "1.0"  # 危険
  public_network_access_enabled = true  # 危険
}

# 脆弱性7: 公開アクセス可能なBlob
resource "azurerm_storage_container" "demo" {
  name                  = "public-data"
  storage_account_name  = azurerm_storage_account.demo.name
  container_access_type = "blob"  # 危険: パブリックアクセス
}
