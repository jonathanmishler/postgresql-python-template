from db_utils.connect import connection
import psycopg3
from db_utils.tables import *
from pydantic import BaseModel, Field


class User(BaseModel):
    id: int
    name: str = Field(..., max_length=50)
    title: str = "Sales Clerk"
    active: bool
    decimal: float
    number: int

    class Config:
        schema_extra = {"primary_key": ["id", "name"], "unique": ["name"], "serial": ["id"]}


print(sql_from_schema(User.schema()))
""" with connection() as conn:

    with conn.cursor() as cur:

        cur.execute()

        cur.execute(
            "INSERT INTO test (num, data) VALUES (%s, %s)", (100, "Hello World")
        )

        cur.execute("SELECT * FROM test")
        cur.fetchone()

        for record in cur:
            print(record)

        conn.commit()
 """
