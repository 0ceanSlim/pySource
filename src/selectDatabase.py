import json
import pyodbc

# Function to read SQL config from json
def read_sql_config():
    with open('sql_config.json', 'r') as config_file:
        return json.load(config_file)

# Function to write SQL config to json
def write_sql_config(config_data):
    with open('sql_config.json', 'w') as config_file:
        json.dump(config_data, config_file, indent=4)

# Read SQL config from json
sql_config = read_sql_config()

# Define the connection string
connection_string = (
    f"DRIVER={{ODBC Driver 17 for SQL Server}};"
    f"SERVER={sql_config['sql_server']};"
    f"DATABASE=master;"
    f"UID={sql_config['sql_user']};"
    f"PWD={sql_config['sql_password']}"
)

try:
    # Connect to the database
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()

    # Fetch database names
    cursor.execute("SELECT name FROM sys.databases WHERE database_id > 4")  # Exclude system databases
    databases = [row[0] for row in cursor.fetchall()]

    # Display available databases to the user
    print("Available Databases:")
    for idx, db in enumerate(databases, start=1):
        print(f"{idx}. {db}")

    # Ask the user to select a database
    try:
        db_index = int(input("Enter the number of the database to use: ")) - 1
        if db_index < 0 or db_index >= len(databases):
            print("Invalid database number selected.")
            exit()
        selected_db = databases[db_index]
    except ValueError:
        print("Invalid input. Please enter a number.")
        exit()

    # Update the JSON config with the selected database
    sql_config['sql_database'] = selected_db
    write_sql_config(sql_config)

    print(f"Selected database updated to '{selected_db}' in sql_config.json.")

except pyodbc.Error as e:
    print(f"Error connecting to the database: {e}")

finally:
    # Close the connection
    cursor.close()
    connection.close()
