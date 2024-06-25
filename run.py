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
from termcolor import colored
from colorama import Fore, Style, init


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

#data = serviceDetails.get_all_values()

#print(data)
       
# Add Expenses Menu Functions

def validate_price():
    """
    Validates user's price input.
    While loop will repeatedly request data until it is valid.
    """
    print("Please enter a Price:\n")

    # Loop repeats until valid input is received
    while True:
        # Try... except for exception / error handling
        try:
            # global so variable can be accessed in other functions
            global price_input
            price_input = float(input("> "))

            # Input cannot be empty
            # Input must be between 0 and 10000
            if price_input != "" and 0 <= price_input <= 500:
                break

            # Invalid input raises error
            else:
                raise ValueError("")

        except ValueError as e:
            print("Invalid input: Please enter a price "
                        "between 0 and 500.\n")



def validate_service_description():
    """
    Validates user's service description input.
    While loop will repeatedly request data until it is valid.
    """
    print("Please enter a service description.\n")

    # Loop repeats until valid input is received
    while True:
        # Try... except for exception / error handling
        try:
            # global so variable can be accessed in other functions
            global service_input
            service_input = input("> ")

            # Input cannot be empty
            # Input cannot be longer than 25 characters
            if service_input != "" and len(service_input) < 50:
                break

            # Invalid input raises error
            else:
                raise ValueError("")

        except ValueError as e:
            print()
            typingPrint("Invalid input: "
                        "Please enter a service description between "
                        "0 and 50 characters.\n")

def show_all_service():
    """
    Displays all services.
    """
    console.clear()
    data = serviceDetails.get_all_values()

    print("------ The Service Details and Corresponding Prices are here ------\n ")
    
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
        print("Please select an option:\n")
        table = Table(title="Menu", width=console.width)

        table.add_column("Option", justify="center", style="blue")
        table.add_column("Description", justify="left", style="blue")

        table.add_row("1", "Show all services")
        table.add_row("2", "Add service")
        table.add_row("3", "Exit")

        print(table)
        choice = input("> ").strip()

        # Try... except for exception / error handling
        try:
            user_input = input("> ")

            # Show all services
            if user_input == "1":
                print()
                show_all_service()
                break

            # Add Service
            elif user_input == "2":
                add_service()
                break

            # Exit program
            elif user_input == "3":
                break

            # Invalid input raises error
            else:
                raise ValueError("")

        except ValueError as e:
            print()
            print(
                "Invalid input: Please select one "
                "of the options (1-3).\n")
            user_input = input("> ")







def main():
    """
    Creates an instance of the Service Detail application and starts it by calling
    the 'run' method.
    """
    #show_all_service()
    main_menu()
    #validate_price()
    #validate_service_description()


main()