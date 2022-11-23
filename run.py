"""
This project is a simple expense tracker for personal use. It tracks the users
expenses and income. The user can input their incoem and expenses in the
terminal. Check how much they have spent or saved.
"""

import os
import time
from termcolor import colored, cprint
from datetime import datetime, timedelta, date
import gspread
from google.oauth2.service_account import Credentials

# initialise APIs from google sheets to access data and
# modify its contents

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
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

    def mini_validator():
        """
        Helper function that checks and validates the values
        that the users inputs as to not cause a value error.
        """
        dict = {"yes": "y", "no": "n"}

        while True:
            answer = input().lower()
            if answer in dict.values():
                return answer
            else:
                text = "Sorry, not an available option."
                print(colored(text, "red", attrs=["reverse"]))

    while True:
        cprint("Please Enter Your Username!", "cyan", attrs=["bold"])
        user = input()
        if user in unique_users:
            active_user.append(user)
            cprint(f"Welcome {user}!", "cyan", attrs=["bold"])
            time.sleep(2)
            os.system("clear")
            break
        else:
            c_user = colored(user, "yellow", attrs=["bold"])
            print(f"Would you like to use {c_user} as your username?")
            cprint("Press 'Y' or 'N' to continue...", "yellow")
            answer = mini_validator()
            if answer == "y":
                active_user.append(user)
                cprint("Username added!", "green")
                cprint(f"Welcome {user}!", "cyan", attrs=["bold"])
                time.sleep(2)
                os.system("clear")
                break
            elif answer == "n":
                print("Would you like to use a different username?")
                cprint("press 'Y' or 'N' to continue...", "yellow")
                answer = mini_validator()
                if answer == "y":
                    continue
                else:
                    return answer


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
    result_inc = colored(result_one, "green")

    result_two = 0
    for i, j, k, l in expenses:
        if i == active_user[0]:
            result_two += int(l)
    result_exp = colored(result_two, "red")

    print(f"Total Income: €{result_inc}, Total Expenses: €{result_exp}")
    savings = result_one - result_two
    if savings > 0:
        savings = colored(savings, "green")
    else:
        savings = colored(savings, "red")

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
    inc = colored("1.Income", "green")
    exp = colored("2.Expense", "red")
    print(f"{inc} or {exp}?")
    valid = 2
    answer = validate_value(valid)

    selection1 = "Please select What type of income you wish to add?"
    selection2 = "Please select What type of expense you wish to add?"

    if answer == 1:
        options = income_options
        worksheet = "income"
        print(colored(selection1, "cyan", attrs=["bold"]))
        print("1.Salary\n2.Other")
    if answer == 2:
        options = expense_options
        worksheet = "expenses"
        print(colored(selection2, "cyan", attrs=["bold"]))
        print("1.Entertainment\n2.Bills\n3.Food\n4.Transportation")

    data = [active_user[0], DAY]
    valid = len(options)
    choice = validate_value(valid)
    data.append(options[choice - 1])

    cprint("Please input the amount", "cyan", attrs=["bold"])
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
    inc = colored("1.Income", "green")
    exp = colored("2.Expense", "red")
    print(f"{inc} or {exp}?")
    valid = 2
    answer = validate_value(valid)
    if answer == 1:
        sheet = income
    if answer == 2:
        sheet = expenses

    print("Chose how many days back you want to see ie.")
    sel = "'7' for 7 days or '30' for 30 days"
    cprint(sel, "yellow")
    valid = None
    days = validate_value(valid)
    data = sheet

    past = date.today() - timedelta(days)
    newlist = []
    for i, j, k, l in reversed(data):
        if i == active_user[0]:
            date_str = j
            date_object = datetime.strptime(date_str, "%m/%d/%Y").date()
            if past < date_object:
                newlist.append(int(l))
    money = 0
    for amount in newlist:
        money += amount
    if sheet == income:
        money = colored(money, "green")
        days = colored(days, "yellow")
        print(f"You have earned €{money} in the last {days} days")
    else:
        money = colored(money, "red")
        days = colored(days, "yellow")
        print(f"You have spent €{money} in the last {days} days")
    input("Press Enter to go back to the main menu...\n")


def update_worksheet(data, worksheet):
    """
    Receives a list containing (date,type of expense and amount)
    that are to be inserted in the relevant worksheet.
    """

    cprint("Updating Worksheet...", "yellow")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    cprint("Update successful!", "green")
    input("Press Enter to go back to the main menu...\n")


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
    intro = "Welcome to your personal expense tracker!"
    print(colored(intro, "cyan", attrs=["bold"]))
    print("Please wait while we load everything up...")

    income_data, expense_data, unique_users = get_data()
    time.sleep(1)
    answer = get_username(unique_users)

    while True:
        if answer == "n":
            print("Goodbye!")
            break

        opt = colored("Option", "green")
        wel = "The following options are available for you "
        cprint(f"{wel}{active_user[0]}!", "cyan", attrs=["bold"])
        print(f"{opt} {colored('1', 'green')} - Show expenses and income")
        print(f"{opt} {colored('2', 'green')} - Input Your Income / Expenses")
        print(f"{opt} {colored('3', 'green')} - Check specific days ago")
        print(f"{opt} {colored('4', 'green')} - Exit")
        sel = "Please input a value '1', '2', '3' or '4' to select an option:"
        cprint(sel, "yellow")
        valid = 4
        option = validate_value(valid)

        if option == 1:
            os.system("clear")
            get_money(income_data, expense_data)
            os.system("clear")
            continue
        elif option == 2:
            os.system("clear")
            data, worksheet = input_income_expense()
            update_worksheet(data, worksheet)
            income_data, expense_data, unique_users = get_data()
            os.system("clear")
            continue
        elif option == 3:
            os.system("clear")
            specific_time_checker(income_data, expense_data)
            os.system("clear")
            continue
        elif option == 4:
            break


main()
