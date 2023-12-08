import pyodbc
from util.sqlHandler import read_sql_config

# Read SQL credentials from the JSON file
sql_server, sql_database, sql_user, sql_password, connection_string = read_sql_config()

# Connect to the database
try:
    connection = pyodbc.connect(connection_string)
except pyodbc.Error as e:
    print(f"Error connecting to the database: {e}")
    exit()

# Define the SQL query
sql_query = "SELECT name FROM sys.databases;"

# Execute the query and fetch the results
try:
    cursor = connection.cursor()
    cursor.execute(sql_query)
    rows = cursor.fetchall()

    for row in rows:
        print(row.name)
except pyodbc.Error as e:
    print(f"Error executing the query: {e}")
finally:
    # Close the cursor and connection
    cursor.close()
    connection.close()
