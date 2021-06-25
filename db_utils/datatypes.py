def sql_varchar(attrs: dict) -> str:
    if attrs.get("max_length"):
        sql = f"VARCHAR({attrs.get('max_length')})"
    else:
        sql = "VARCHAR(255)"

    if attrs.get("default"):
        sql = f"{sql} DEFAULT \"{attrs.get('default')}\""

    return sql


def sql_boolean(attrs: dict) -> str:
    sql = "BOOLEAN"
    if attrs.get("default"):
        sql = f"{sql} DEFAULT \"{str(attrs.get('default')).upper()}\""

    return sql


def sql_float(attrs: dict) -> str:
    sql = "FLOAT4"
    if attrs.get("default"):
        sql = f"{sql} DEFAULT {float(attrs.get('default'))}"

    return sql


def sql_integer(attrs: dict) -> str:
    sql = "INT4"
    if attrs.get("default"):
        sql = f"{sql} DEFAULT {int(attrs.get('default'))}"

    return sql


def map_dtype(
    attrs: dict,
    is_primary_key: bool = False,
    is_required: bool = False,
    is_unique: bool = False,
    is_serial: bool = False,
) -> str:
    dtypes_funcs = {
        "string": sql_varchar,
        "boolean": sql_boolean,
        "number": sql_float,
        "integer": sql_integer,
    }
    dtype = attrs["type"]
    if is_serial:
        sql = "SERIAL"
    else:
        sql = dtypes_funcs[dtype](attrs)

    if is_primary_key:
        sql = f"{sql} PRIMARY KEY"
    else:
        if is_required:
            sql = f"{sql} NOT NULL"
        if is_unique:
            sql = f"{sql} UNIQUE"
    

    return sql
