import pyodbc
import csv
import os
from util.sqlHandler import read_sql_config

# Read SQL credentials from the JSON file
sql_server, sql_database, sql_user, sql_password, connection_string = read_sql_config()

# Connect to the database
try:
    connection = pyodbc.connect(connection_string)
except pyodbc.Error as e:
    print(f"Error connecting to the database: {e}")
    exit()

# Define the directory to save CSV files
output_directory = 'output/product_type_csv'
os.makedirs(output_directory, exist_ok=True)

# Define the SQL query to retrieve data
query = """
SELECT tProduct.Product_Type, tProduct.Sku, tCost.Cost
FROM tProduct
INNER JOIN tProductgroup_Product
    ON tProduct.tProduct_ID = tProductgroup_Product.tProduct_ID
INNER JOIN tCost
    ON tProductgroup_Product.tProductgroup_Product_ID = tCost.tProductgroup_Product_ID
WHERE tProduct.IsActive = 1
"""

# Execute the SQL query
try:
    cursor = connection.cursor()
    cursor.execute(query)

    # Fetch the data and group by Product_Type
    data = {}
    for row in cursor.fetchall():
        product_type, sku, cost = row
        if product_type not in data:
            data[product_type] = []
        data[product_type].append((sku, cost))
except pyodbc.Error as e:
    print(f"Error executing SQL query: {e}")
    exit()

# Close the cursor and connection
cursor.close()
connection.close()

# Save data to separate CSV files for each Product_Type
for product_type, rows in data.items():
    csv_file_path = os.path.join(output_directory, f"{product_type}_data.csv")
    with open(csv_file_path, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['Sku', 'Cost'])
        csv_writer.writerows(rows)
    print(f"Data for {product_type} saved to {csv_file_path}")
