import json

def read_sql_config(filename="sql_config.json"):
    with open(filename, "r") as config_file:
        config = json.load(config_file)

    sql_server = config["sql_server"]
    sql_database = config["sql_database"]
    sql_user = config["sql_user"]
    sql_password = config["sql_password"]
    connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={sql_server};DATABASE={sql_database};UID={sql_user};PWD={sql_password}'

    return sql_server, sql_database, sql_user, sql_password, connection_string
