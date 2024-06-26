# Libraries
import os
import sys


import gspread
from google.oauth2.service_account import Credentials
import colorama
from colorama import Back, Fore, Style
colorama.init(autoreset=True)
import pyfiglet


from collections import defaultdict
from tabulate import tabulate


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

# Variables to access spreadsheet
# Guidance provided by Code Institute's course material
CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Portfolio3')

serviceDetails = SHEET.worksheet('ServiceDetail')
data = serviceDetails.get_all_values()



def home_screen():
    """
    Displays title, the main menu, handles user input for various
    customer-related actions, and directs the user to the
    appropriate method based on their choice.
    """
    
    print(pyfiglet.figlet_format(
    "Service Detail", justify="center", width=80))


def validate_service_description():
    """
    Validates service description
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
            # Input should not be digit
            if service_input != "" and len(service_input) < 50 and service_input.isdigit()==False:
                break

            # Invalid input raises error
            else:
                raise ValueError("")

        except ValueError as e:
            print()
            print(Fore.RED+"Invalid input: "
                        "Please enter a description between "
                        "0 and 50 characters which is not digit.\n")

def validate_service_price():
    """
    Validates service price.
    While loop will repeatedly request data until it is valid.
    """
    print("Please enter a price:\n")

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
            print()
            print(Fore.RED+ "Invalid input: Please enter a number "
                        "between 0 and 500.\n")


def view_service():
    """
    Runs the service view menu.
    """
    service = SHEET.worksheet('ServiceDetail')
    print("                                                       "
              "---- Service Details ----\n")
    data = service.get_all_values()

    #print(data)
    print(tabulate(data, headers='firstrow', tablefmt='fancy_grid'))

 

def add_service():
    """
    Collects service details from users.
    Runs separate function to collect each aspect of details in order.
    After all data is collected and validated, a summary is shown to users.
    """
    print()
    print("---- Add Service ----\n")
    print("Please add service details below.\n")


    validate_service_description()
    print()
    validate_service_price()
    print()
    entered_service = [
        service_input,
        price_input
        ]
    update_worksheet(entered_service)
  

def update_worksheet(service):
    """
    Updates the worksheet.
    Appends a new row with the provided expense details.
    """
    print("Updating ServiceDetail worksheet...\n")
   
    # Adds new service to google sheet as a new row
    service_worksheet = SHEET.worksheet("ServiceDetail")
    service_worksheet.append_row(service)
    print("Service Detail worksheet updated successfully.\n")


# Main Menu Functions


def main_menu():
    """
    Runs the main menu of the program.
    Allows users to navigate to one of two sub-menus.
    """
    # Loop repeats until valid input is received
    while True:
        print()
        print(Fore.BLUE+ "                       "
              "---- MAIN MENU ----\n")
        print("Please select one of the following options:\n")
        print()
        print("    1. Add Service")
        print("    2. Show Service")
        print("    3. Exit")
        print()

        # Try... except for exception / error handling
        try:
            user_input = input("> ")

            # Add Service
            if user_input == "1":
                print()

                add_service()
                break

            # View Service
            elif user_input == "2":
                print()

                view_service()
                break

            # Exit program
            elif user_input == "3":
                print()

                break

            # Invalid input raises error
            else:
                raise ValueError("")

        except ValueError as e:
            print(Fore.RED+
                "Invalid input: Please select one "
                "of the options (1-3).\n")
            user_input = input("> ")


def return_to_main():
    """
    Clears the screen and returns to the main menu
    """
    print(Fore.YELLOW+ "Loading Main Menu...\n")
    
    main_menu()

# Run the main function
home_screen()
main_menu()