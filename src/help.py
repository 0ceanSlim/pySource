def help():
    print("\nAvailable Commands:\n")
    print("listDatabases - Lists all Databases in the SQL Server as defined in your sql_config.json")
    print("listTables - Lists all tables in the Database that's configured in your sql_config.json")
    print("productData - Saves a CSV with data for all products to the Output folder with the following information: \n              tProduct_ID,Sku,Product_Type,Product_Code,ShortDescription,IsActive")
    print("skuCost - Saves a CSV file for each Product Category to the Output folder that contains the items sku and associated cost")
    print("help - Display available commands")
    print("exit - Quit the program\n")
