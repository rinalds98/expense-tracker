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


def get_money():
    """
    Calculates The total income and expenses from the google spreadsheet
    """
    income = SHEET.worksheet("income").col_values(3)
    income.pop(0)

    result_one = 0
    for i in income:
        result_one += int(i)

    expenses = SHEET.worksheet("expenses").col_values(3)
    expenses.pop(0)

    result_two = 0
    for i in expenses:
        result_two += int(i)

    print(f"Total income: {result_one},Total Expenses: {result_two}\n")
    savings = result_one - result_two
    print(f"You have currently saved: {savings}")


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
    while True:
        if option == 1:
            get_money()
            print("Thank you for using this service.\nGoodbye!")
            break
        # elif option == 2:
        #  x = 2  # allow user to input income / expenses
        # break
        # elif option == 3:
        # break
        # else:
        #  print("you gave the wrong value")
        # break


main()
