def help():
    print("\nAvailable Commands:\n")
    print("selectDatabase - Lists all databases on your SQL Server and prompts for a selection of database you want to use")
    print("listDatabases - Lists all Databases in the SQL Server as defined in your sql_config.json")
    print("listTables - Lists all tables in the Database that's configured in your sql_config.json")
    print("listTableData - Lists all the tables in the Database that's configured in your sql_config.json, then prompts\n               for a table selection to show the column for that table")
    print("outputProductData - Saves a CSV with data for all products to the Output folder with the following information: \n              tProduct_ID,Sku,Product_Type,Product_Code,ShortDescription,IsActive")
    print("outputSkuCost - Saves a CSV file for each Product Category to the Output folder that contains the items sku and associated cost")
    print("help - Display available commands")
    print("exit - Quit the program\n")
