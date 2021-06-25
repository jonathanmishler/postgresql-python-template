from typing import List
import psycopg3
from psycopg3 import sql
import pydantic

from db_utils.datatypes import map_dtype


def sql_cols(schema: pydantic.main.ModelMetaclass) -> str:
    sql_cols = list()
    props = schema.get("properties")
    primary_key = schema.get("primary_key")
    if primary_key is None:
        sql_cols = ["id SERIAL PRIMARY KEY"]

    for col in props.items():
        name, attrs = col
        is_primary_key = name == primary_key
        is_required = name in schema["required"]
        is_unique = name in schema["unique"]
        is_serial = name in schema["serial"]

        sql_cols.append(
            f"{name} {map_dtype(attrs, is_primary_key, is_required, is_unique, is_serial)}"
        )

    if not isinstance(primary_key, str) and primary_key is not None:
        sql_cols.append(f"PRIMARY KEY ({', '.join(primary_key)})")

    return ", ".join(sql_cols)


def sql_from_schema(schema: pydantic.main.ModelMetaclass) -> str:
    sql_head = f"CREATE TABLE IF NOT EXISTS {schema['title'].lower()}"

    return f"{sql_head} ({sql_cols(schema)})"


def create_tables(cur: psycopg3.Cursor, models: List[pydantic.main.ModelMetaclass]):

    for model in models:

        cur.execute(
            """
                CREATE TABLE IF NOT EXISTS
            """
        )
