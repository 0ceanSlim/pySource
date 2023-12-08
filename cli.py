import os
import json
import subprocess
import sys
from src.help import help


def clear_console():
    # Clear console based on the operating system
    if os.name == "nt":  # For Windows
        os.system("cls")
    else:  # For Unix/Linux/Mac
        os.system("clear")


def check_python_installation():
    try:
        python_version = subprocess.check_output(
            ["python", "--version"], stderr=subprocess.STDOUT, universal_newlines=True
        )
        print(f"Python is already installed ({python_version})")
        return True
    except FileNotFoundError:
        return False


def install_python():
    print("Python is not installed. Please download and install it from:")
    print("https://www.python.org/downloads/")
    input("Press Enter to continue after installing Python...")
    sys.exit(1)


def check_sql_config():
    if os.path.exists("sql_config.json"):
        return True
    return False


def get_sql_config():
    # Define the connection string
    sql_server = input("Enter the sql server (network\location): ")
    sql_database = input("Enter the sql database: ")
    sql_user = input("Enter the sql user: ")
    sql_password = input("Enter the sql password: ")

    sql_config = {
        "sql_server": sql_server,
        "sql_database": sql_database,
        "sql_user": sql_user,
        "sql_password": sql_password,
    }

    with open("sql_config.json", "w") as config_file:
        json.dump(sql_config, config_file)


def run_script(script_name):
    script_path = os.path.join("src", f"{script_name}.py")

    if os.path.exists(script_path):
        # print(f"Running {script_name}...")
        os.system(f"python {script_path}")
    else:
        print(f"Error: {script_name} not found!")


def main():
    setup_completed = False

    while not check_python_installation():
        install_python()

    subprocess.run(["pip", "install", "-r", "requirements.txt"])

    while not check_sql_config():
        clear_console()
        print("sql config file not found.")
        user_input = input(
            "Do you have credentials for your SQL Server (yes/no)? "
        ).lower()

        if user_input in ["no", "n"]:
            print(
                "Please retrieve your server location and credentials as well as the name of the database you'd like to work with"
            )
            input("Press Enter to continue after you have this information...")
        elif user_input in ["yes", "y"]:
            get_sql_config()
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

    setup_completed = True

    print("You are ready to proceed.")
    clear_console()

    print("\nPySource Command Line Interface")
    help()

    while True:
        user_input = input("Enter a command: ")

        if user_input.lower() == "exit":
            break
        if user_input.lower() == "help":
            help()
        if setup_completed:
            run_script(user_input)
        else:
            print("Error: Setup not completed. Use 'help' to see available commands.")


if __name__ == "__main__":
    main()
