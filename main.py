from db_utils.connect import connection
import psycopg3


with connection() as conn:

    with conn.cursor() as cur:

        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS test (
                id serial PRIMARY KEY,
                num integer,
                data text)
        """
        )

        cur.execute(
            "INSERT INTO test (num, data) VALUES (%s, %s)", (100, "Hello World")
        )

        cur.execute("SELECT * FROM test")
        cur.fetchone()

        for record in cur:
            print(record)

        conn.commit()
