vault secrets enable database

vault write database/config/postgresql \
    plugin_name=postgresql-database-plugin \
    allowed_roles=* \
    connection_url='postgresql://root:root@localhost:5432/postgres?sslmode=disable'

vault write database/roles/readonly db_name=postgresql \
        creation_statements=@readonly.sql \
        default_ttl=1h max_ttl=24h

vault policy write db_creds db_creds.hcl
