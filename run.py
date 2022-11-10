"""
This project is a simple expense tracker for personal use. It tracks the users
expenses and income. The user can input their incoem and expenses in the
terminal. Check how much they have spent or saved.
"""

from datetime import date
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
SHEET = GSPREAD_CLIENT.open("expense_tracker")


expense_tracker = SHEET.worksheet("income")

data = expense_tracker.get_all_values()
today = date.today()
day = today.strftime("%m/%d/%Y")


def input_expenses():
    """
    Asks the user to input their expenses so it can be added to the
    google worksheet
    """

    print("Please select What type of expense you wish to add")
    print("1.Entertainment\n2.Bills\n3.Food\n4.Transportation")

    options = ["entertainment", "bills", "food", "transportation"]
    stuff = [day]

    choice = int(input()) - 1
    stuff.append(options[choice])

    print("Please input the amount")
    amount = int(input())
    stuff.append(amount)

    worksheet_to_update = SHEET.worksheet("expenses")
    worksheet_to_update.append_row(stuff)


def input_income():
    """
    Asks the user to input their income so it can be added to the
    google worksheet
    """

    print("Please select What type of income you wish to add")
    print("1.Salary\n2.Other")

    options = ["salary", "other"]
    stuff = [day]

    choice = int(input()) - 1
    stuff.append(options[choice])

    print("Please input the amount")
    amount = int(input())
    stuff.append(amount)

    worksheet_to_update = SHEET.worksheet("income")
    worksheet_to_update.append_row(stuff)


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
            get_money()  # prints the total income/expenses
            print("Thank you for using this service.\nGoodbye!")
            break
        elif option == 2:
            input_income()  # allow user to input income / expenses
            print("thank you")
            break
        elif option == 3:
            break
        else:
            print("you gave the wrong value")
            break


main()
