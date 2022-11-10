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

TODAY = date.today()
DAY = TODAY.strftime("%m/%d/%Y")


def input_income_expense():
    """
    Asks the user if they want to input income or expenses. Once they
    have selected the program asks the user what type and the amount
    data gets validated by the "validate_value" function.
    """
    income_options = ["salary", "other"]
    expense_options = ["entertainment", "bills", "food", "transportation"]
    print("1.Income or 2.expense?")
    valid = 3
    answer = validate_value(valid)
    if answer == 1:
        options = income_options
        worksheet = "income"
        print("Please select What type of income you wish to add")
        print("1.Salary\n2.Other")
    if answer == 2:
        options = expense_options
        worksheet = "expenses"
        print("Please select What type of expense you wish to add")
        print("1.Entertainment\n2.Bills\n3.Food\n4.Transportation")

    data = [DAY]
    valid = len(options) + 1
    choice = validate_value(valid)
    data.append(options[choice - 1])

    print("Please input the amount")
    valid = 99999
    amount = validate_value(valid)
    data.append(amount)

    return data, worksheet


def get_money():
    """
    Takes the values from both income and expenses worksheets
    (from google sheets) and calculates the total income/expenses.
    Also calculates the amount saved.
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

    print(f"Total income: €{result_one}, Total Expenses: €{result_two}\n")
    savings = result_one - result_two
    print(f"You have currently saved: €{savings}")


def update_worksheet(data, worksheet):
    """
    Receives a list containing (date,type of expense and amount)
    that are to be inserted in the relevant worksheet.
    """
    print("Updating Worksheet...")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print("Update successful")


def validate_value(valid):
    """
    Inside the try, asks to input an integer value
    Raises ValueError if anything but an integers is added
    and if its within the range of options.
    """
    while True:
        try:
            value = int(input())

        except ValueError:
            print("Please input a valid value")
            continue

        if value < valid:
            return value
        else:
            print("Sorry, not an available option")
            continue


def main():
    """
    This is the main function that loads on startup. it prints
    what options are available to the user. When the user
    types in a value, it gets checked to see if its a valid option.
    It then calls the correct function that the user selected. When the
    user is done, they have an option to exit the program.
    """
    print("Hey there! what would you like to do today?")

    while True:
        print("The following options are available to you!\n")
        print("Option 1 - Show expenses and income")
        print("Option 2 - Input Your Income / Expenses")
        print("Option 3 - Exit\n")
        print("Please input a value '1', '2' or '3' to select an option: ")
        valid = 4
        option = validate_value(valid)

        if option == 1:
            get_money()
            print("Thank you for using this service.\n")
            continue
        elif option == 2:
            data, worksheet = input_income_expense()
            update_worksheet(data, worksheet)
            print("Thank you for using this service.\n")
            continue
        elif option == 3:
            break


main()
