# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import gspread
from google.oauth2.service_account import Credentials

from rich import print
from rich.style import Style
from rich.console import Console
from rich.table import Table
import pyfiglet

# Rich console initialize
console = Console()

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Portfolio3')

serviceDetails = SHEET.worksheet('ServiceDetail')

data = serviceDetails.get_all_values()

print(data)
       


def main_menu():
    """
    Displays title, the main menu, handles user input for various
    customer-related actions, and directs the user to the
    appropriate method based on their choice.
    """
    console.clear()
    print(pyfiglet.figlet_format(
    "Service Detail", justify="center", width=80))

    while True:  # Loop until a valid choice is made
        print("List of actions")
        table = Table(title="Menu", width=console.width)

        table.add_column("Option", justify="center", style="blue")
        table.add_column("Description", justify="center", style="blue")

        table.add_row("1", "Show all services")
        table.add_row("2", "Search service")
        table.add_row("3", "Edit service")
        table.add_row("4", "Add new service")
        table.add_row("5", "Delete service")
        table.add_row("6", "Exit")

        print(table)
        choice = input("> ").strip()

        if choice == '1':
            show_all_services()
        elif choice == '2':
            search_service()
        elif choice == '3':
            edit_service()
        elif choice == '4':
            add_new_service()
        elif choice == '5':
            delete_service()
        elif choice == '6':
            print("Program Exists!")
            return
        else:
            console.print("Invalid choice, please select a valid option.")


def main():
    """
    Creates an instance of the Service Detail application and starts it by calling
    the 'run' method.
    """
    main_menu()


main()