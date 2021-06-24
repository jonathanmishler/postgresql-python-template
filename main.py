from settings import Settings
import psycopg3

config = Settings()

conn_string = (
    f"host={config.db_host} "
    f"port={config.db_port} "
    f"dbname={config.db_name} "
    f"user={config.db_username} "
    f"password={config.db_password} "
)

with psycopg3.connect(conn_string) as conn:

    with conn.cursor() as cur:

        cur.execute("""
            CREATE TABLE test (
                id serial PRIMARY KEY,
                num integer,
                data text)
        """)

        cur.execute(
            "INSERT INTO test (num, data) VALUES (%s, %s)",
            (100, "Hello World")
        )

        cur.execute("SELECT * FROM test")
        cur.fetchone()

        for record in cur:
            print(record)
        
        conn.commit()