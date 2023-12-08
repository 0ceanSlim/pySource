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

# Get a list of all tables in the database
tables = []

try:
    cursor = connection.cursor()
    cursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE';")
    rows = cursor.fetchall()
    tables = [row.TABLE_NAME for row in rows]
except pyodbc.Error as e:
    print(f"Error fetching table names: {e}")

# Print the names of all tables
for table in tables:
    print(table)

# Close the cursor and connection
cursor.close()
connection.close()
