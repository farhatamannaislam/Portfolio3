# Libraries
import datetime
import os
import sys
import time


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



def welcome_screen():
    """
    Displays title, the main menu, handles user input for various
    customer-related actions, and directs the user to the
    appropriate method based on their choice.
    """
    
    print(pyfiglet.figlet_format(
    "Service Detail", justify="center", width=80))





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

            # Add Expenses
            if user_input == "1":
                print()

                add_expenses()
                break

            # View Expenses
            elif user_input == "2":
                print()

                view_expenses()
                break

            # Exit program
            elif user_input == "3":
                print()

                break

            # Invalid input raises error
            else:
                raise ValueError("")

        except ValueError as e:
            print()
            print(
                "Invalid input: Please select one "
                "of the options (1-3).\n", Fore.RED)
            user_input = input("> ")




# Run the main function
welcome_screen()
main_menu()