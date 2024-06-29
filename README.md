# Repair Service Detail

<img alt="Home Image" src="docs/readme_images/home_image.png">


 Repair Service Detail is a Python command line interface  application used to enter Service Detail of a Repair Service Business. The user can enter service description and related price and view the total service and price list available.

The program automatically syncs all inputs to Google Sheets to ensure storage of and access to the service detail.

The live link can be found here [Repair Service Detail](https://servicedetail-e151ee9cb139.herokuapp.com/)

A view-only version of the Google Sheet can be viewed here.[Google Sheet](https://docs.google.com/spreadsheets/d/1HaDsMmEWqLoRjx94ya5nbn5xtAUYw9c7q6rqk3dACPQ/edit?gid=0#gid=0)


# Table of Contents

## Project Goal

* A Simple Program that makes easy input opportunity.
* All the inputs are properly validated.
* The user can view the service details in tabular format.
* An easy way to keep track of all the services.


# Logic Flow

In order to visualise the flow of steps required in the app, a Flow Diagram has been created using Lucid Charts. It gives a clear overview about the logic
of the application. 

<img alt="Flow " src="docs/readme_images/flowdiagram.png">

# Features

## Title and Introduction

* At the home page the title of the application is shown.
* In the bottom of the title there are three options given for the user.
   * 1. Add Service
   * 2. Show Service
   * 3. Exit
* User can choose any option according to their wish.

## Add Service

If the user selects Add Service by pressing '1' in keyboard and hitting enter he/she will be asked to enter a service detail.
The service should be a description between 0 to 50 Character and not a digit. Service Can not be left empty.

<img alt="Service Description Validation " src="docs/readme_images/servicedescription_validation.png">

When the user enters a proper service description command line will take the input and request the user to enter a price.

<img alt="Correct Service Description" src="docs/readme_images/correct_servicedescription.png">


The price should be a positive integer between 0 to 500.

<img alt="Service Price Validation" src="docs/readme_images/serviceprice_validation.png">

When the user enters a proper service price then the Service Details worksheet will be updated and success message would be 
shown in the terminal. And the user will be redirected to main menue again where he/she will get three options to choose.

<img alt="Service Details Updated" src="docs/readme_images/ServiceDetails_updated.png">


## Show Service

If the user selects Show Service from main menu by pressing '2' in keyboard and hitting enter the all the service description and price
from google sheet would be shown as tabular format in the command window.

<img alt="Show Service" src="docs/readme_images/Showservice.png">

Which is followed by the main menu.

## Exit

If the user wants to exit from application he/she can select '3' and press enter.

# Technologies Used

* [Python3](https://en.wikipedia.org/wiki/Python_(programming_language))
* Code Institute's [Python Esssebtials Template](https://github.com/Code-Institute-Org/python-essentials-template)
* [https://github.com/] used for version control.
* [HEROKU](https://dashboard.heroku.com/apps) used to deploy the live project.
* [Lucidchart](https://lucid.app/users/login#/login) - used to create the game flowchar
* [PEP8 Python Validator](https://pep8ci.herokuapp.com/) - used to validate all the Python code

## Python Libraries:

* [os](https://docs.python.org/3/library/os.html) was used to clear the screen when switching between menus or views.
* [pyfiglet](https://pypi.org/project/pyfiglet/0.7/) - for taking ASCII text and rendering it into ASCII art fonts.
* [colorama](https://pypi.org/project/colorama/) - for adding colour to terminal text.
* [gspread](https://pypi.org/project/gspread/) to allow communication with Google Sheets.
* [google.oauth2.service_account](https://google-auth.readthedocs.io/en/stable/index.html) used to validate credentials and grant access to google service accounts.
* [Sys](https://docs.python.org/3/library/sys.html) was used to create the typing effect on certain text outputs.#
* [Tabulate](https://pypi.org/project/tabulate/) was used to display the expense data in tables.
* [Defaultdict](https://docs.python.org/3/library/collections.html#collections.defaultdict) was used to return a new dictionary like object.





