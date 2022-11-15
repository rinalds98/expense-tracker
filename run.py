"""
This project is a simple expense tracker for personal use. It tracks the users
expenses and income. The user can input their incoem and expenses in the
terminal. Check how much they have spent or saved.
"""

import os
from termcolor import colored, cprint
from datetime import datetime, timedelta, date
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
active_user = []


def get_data():
    """
    Gets all the information from the spreadsheet and
    parses it into useful information such as usernames
    income data and expense data
    """

    income_data = SHEET.worksheet("income").get_all_values()
    expense_data = SHEET.worksheet("expenses").get_all_values()
    income_data.pop(0)
    expense_data.pop(0)

    data = income_data + expense_data
    unique_users = []
    for user in data:
        if user[0] not in unique_users:
            unique_users.append(user[0])

    return income_data, expense_data, unique_users


def get_username(unique_users):
    """
    Asks user for their username and checks the google spreadsheet
    if it has been used previously. If it has it welcomes them. If not
    it creates it. the user gets added to a 'active users' variable which
    is used to get that specific users data or input new data under
    their username.
    """

    print("Please Enter Your Username!")
    user = input()
    if user in unique_users:
        active_user.append(user)
        print(f"Welcome {user}!")
    else:
        print(f"would you like to use {user} as your username from now?")
        print("press 'y' or 'n'")
        answer = input()
        if answer == "y":
            active_user.append(user)
            print("Done")
        else:
            print("thank you good bye")


def get_money(income, expenses):
    """
    Takes the values from both income and expenses worksheets
    (from google sheets) and calculates the total income/expenses.
    Also calculates the amount saved.
    """

    result_one = 0
    for i, j, k, l in income:
        if i == active_user[0]:
            result_one += int(l)

    result_two = 0
    for i, j, k, l in expenses:
        if i == active_user[0]:
            result_two += int(l)

    print(f"Total Income: €{result_one}, Total Expenses: €{result_two}\n")
    savings = result_one - result_two
    print(f"You have currently saved: €{savings}\n")
    input("Press Enter to go back to the main menu...\n")


def input_income_expense():
    """
    Asks the user if they want to input income or expenses. Once they
    have selected the program asks the user what type and the amount.
    Data gets validated by the "validate_value" function.
    """

    income_options = ["salary", "other"]
    expense_options = ["entertainment", "bills", "food", "transportation"]
    print("1.Income or 2.Expense?")
    valid = 2
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

    data = [active_user[0], DAY]
    valid = len(options)
    choice = validate_value(valid)
    data.append(options[choice - 1])

    print("Please input the amount")
    valid = None
    amount = validate_value(valid)
    data.append(amount)

    return data, worksheet


def specific_time_checker(income, expenses):
    """
    Asks the user if they wish to check their
    income / expenses. The function allows the user
    to check specific amount of days ago how much they
    have spent or earned.
    """

    print("1.Income or 2.Expense?")
    valid = 2
    answer = validate_value(valid)
    if answer == 1:
        sheet = income
    if answer == 2:
        sheet = expenses

    print("Chose how many days back you want to see ie.")
    print("'7' for 7 days or '30' for 30 days")
    days = int(input())
    data = sheet

    past = date.today() - timedelta(days)
    newlist = []
    for i, j, k, l in reversed(data):
        if i == active_user[0]:
            date_str = j
            date_object = datetime.strptime(date_str, '%m/%d/%Y').date()
            if past < date_object:
                newlist.append(int(l))
    money = 0
    for amount in newlist:
        money += amount
    if sheet == "income":
        print(f"You have earned €{money} in the last {days} days")
    else:
        print(f"You have spent €{money} in the last {days} days")
    input("Press Enter to go back to the main menu...\n")


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
            text = "Please input a valid value."
            print(colored(text, "red", attrs=["reverse"]))
            continue

        if valid is None:
            if value <= 0:
                text = "Sorry, the amount can't be '0' or negative."
                print(colored(text, "red", attrs=["reverse"]))
                continue
            else:
                return value

        if value <= valid and value > 0:
            return value
        else:
            text = "Sorry, not an available option."
            print(colored(text, "red", attrs=["reverse"]))
            continue


def main():
    """
    This is the main function that loads on startup. it prints
    what options are available to the user. When the user
    types in a value, it gets checked to see if its a valid option.
    It then calls the correct function that the user selected. When the
    user is done, they have an option to exit the program.
    """
    print("Welcome to your personal expense tracker!")
    print("Please wait while we load everything up...")
    income_data, expense_data, unique_users = get_data()
    get_username(unique_users)
    print("What would you like to do today?")

    while True:
        print("The following options are available to you!\n")
        print("Option 1 - Show expenses and income")
        print("Option 2 - Input Your Income / Expenses")
        print("Option 3 - Check specific days ago")
        print("Option 4 - Exit")
        print("Please input a value '1', '2', '3' or '4' to select an option:")
        valid = 4
        option = validate_value(valid)

        if option == 1:
            get_money(income_data, expense_data)
            os.system("clear")
            continue
        elif option == 2:
            data, worksheet = input_income_expense()
            update_worksheet(data, worksheet)
            # os.system("clear")
            continue
        elif option == 3:
            specific_time_checker(income_data, expense_data)
            os.system("clear")
            continue
        elif option == 4:
            break


main()


# usernames1 = income_data.col_values(1)
# print(income_data)

# text = colored("Hello, World!", "red", )
# print(colored("Wrong Answer!", "red", attrs=["reverse"]))
# print(text)
