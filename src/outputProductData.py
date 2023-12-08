import pyodbc
import csv
from util.sqlHandler import read_sql_config

# Read SQL credentials from the JSON file
sql_server, sql_database, sql_user, sql_password, connection_string = read_sql_config()

# Connect to the database
try:
    connection = pyodbc.connect(connection_string)
except pyodbc.Error as e:
    print(f"Error connecting to the database: {e}")
    exit()

# Define the table name and columns of interest
table_name = 'tProduct'
columns_of_interest = ['tProduct_ID', 'Sku', 'Product_Type', 'Product_Code', 'ShortDescription', 'IsActive']

# Retrieve data from the specified columns where IsActive=1
data = []

try:
    cursor = connection.cursor()
    column_names = ', '.join(columns_of_interest)
    query = f"SELECT {column_names} FROM {table_name} WHERE IsActive = 1;"
    cursor.execute(query)
    rows = cursor.fetchall()
    data = [list(row) for row in rows]
except pyodbc.Error as e:
    print(f"Error fetching data: {e}")

# Define the CSV file path
csv_file_path = 'output/tProduct_data.csv'

# Save the retrieved data to a CSV file
try:
    with open(csv_file_path, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        
        # Write the header row
        csv_writer.writerow(columns_of_interest)
        
        # Write the data rows
        csv_writer.writerows(data)
    print(f"Data saved to {csv_file_path}")
except IOError as e:
    print(f"Error saving data to CSV: {e}")

# Close the cursor and connection
cursor.close()
connection.close()
