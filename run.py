"""
This project is a simple expense tracker for personal use. It tracks the users
expenses and income. The user can input their incoem and expenses in the
terminal. Check how much they have spent or saved.
"""

import gspread
from google.oauth2.service_account import Credentials

# initialise APIs from google sheets to access data and
# modify its contents

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("expense-tracker")


sales = SHEET.worksheet("income")
data = sales.get_all_values()
# print(data)


def main():
    """
    This is the main function that loads on startup. It asks the user what
    option they wish to take.
    """
    print("Hey there! what would you like to do today?")
    print("The following options are available to you!\n")
    print("Option 1 - Show expenses and income")
    print("Option 2 - Input Your Income / Expenses")
    print("Option 3 - Exit\n")
    print("Please input a value '1', '2' or '3' to select an option: ")
    option = int(input())
    while option != 4:
        if option == 1:
            x = 1  # show expenses and income
        elif option == 2:
            x = 2  # allow user to input income / expenses
        elif option == 3:
            break
        else:
            print("you gave the wrong value")
            break


main()
