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

# Fetch table names from the database
try:
    cursor = connection.cursor()
    cursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE';")
    tables = [row.TABLE_NAME for row in cursor.fetchall()]
except pyodbc.Error as e:
    print(f"Error fetching table names: {e}")
    exit()

# Display available tables to the user
print("Available Tables:")
for idx, table in enumerate(tables, start=1):
    print(f"{idx}. {table}")

# Ask the user to select a table
try:
    table_index = int(input("Enter the number of the table to display its columns: ")) - 1
    if table_index < 0 or table_index >= len(tables):
        print("Invalid table number selected.")
        exit()
    table_name = tables[table_index]
except ValueError:
    print("Invalid input. Please enter a number.")
    exit()

# Get the data types of columns in the specified table
columns = []

try:
    cursor.execute(f"SELECT COLUMN_NAME, DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = ?;", (table_name,))
    rows = cursor.fetchall()
    columns = [(row.COLUMN_NAME, row.DATA_TYPE) for row in rows]
except pyodbc.Error as e:
    print(f"Error fetching column data types: {e}")
    exit()

# Print the data types of columns
print(f"Data types for table '{table_name}':")
for column_name, data_type in columns:
    print(f"{column_name}: {data_type}")

# Close the cursor and connection
cursor.close()
connection.close()
