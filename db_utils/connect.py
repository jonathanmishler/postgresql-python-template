from db_utils.settings import Settings
import psycopg3


def connection() -> psycopg3.Connection:
    config = Settings()

    conn_string = (
        f"host={config.db_host} "
        f"port={config.db_port} "
        f"dbname={config.db_name} "
        f"user={config.db_username} "
        f"password={config.db_password} "
    )

    return psycopg3.connect(conn_string)
