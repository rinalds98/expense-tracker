Expense Tracker
=

Introduction
=
Expense Tracker is a simple tracker that tracks your spending and income. You can add a username so multiple users can use the expense tracker. The user can check their total earned / saved. Be more specific with checking spending in the last few days to a month. inputing their income / expenses.


Users of app will be able to track their spending habits and how much they have saved. 


![Photo of the website on multiple different screens](#amiresponsiveimage)

The website can be viewed here: [Expense Tracker](#liveLink "Expense Tracker").

# Table of contents
- [User Experience](#userexperience)
- [Features](#features)
- [Testing](#testing)
- [Deployment](#deployment)
- [Technologies Used](#technologies)
- [Credits](#credits)

<div id='userexperience'/>

User Experience
=
## **User Stories**
- ## **As a app owner I want that:**

    1. The app provides clear and concise information on how to use the expense tracker.
    2. The app allows the user to input their username to track their own personal spending and earnings.
    3. The app allows the user to input an expense / income and allow the app to update everything correctly.
------

- ## **As a app user I want:**
    1. To easily understand how to navigate the app.
    2. To calculate my spending or income within a specific time range.
    3. To not cause a crash when inputing a invalid value.
 ------

- ## **As a returning app user I want:**
    1. To be able to retrieve my personal spending / income with my username.
    2. To be able to add more income / expenses.


# 1. Strategy

- The main purpose of this app is to make it a useful tool for users to be able to track spending / income.
- Each user can make their own username to track their own personal spending.

# 2. Scope
- After a few design choices. a elegant 4 option main screen was chosen where users can choose what they want to do.
- Adding color to add a visual distinction for different options.

# 3. Structure
- A start screen would ask for the users username to begin.
- once the user has logged on, the user would be presented with 4 options to choose what they would like to do.
- Each option would be accessed by pressing a value that corresponds to an option.
- When the user is done using the expense tracker. There would be a exit option.

# 4. Skeleton
## **Wireframes**
- The initial designs were made with pen and paper.

![Initial Designs](#photo)

# 5. Surface
 - ## **Color**
    - The basic color theme would be green for income and red for expenses.
    - Where instructing the user of how to select a specific option it would be colored yellow.
    - Any errors or invalid values chosen - the color would be red.
    - confirmation text would be green.
    - General welcome text would be cyan.

<div id='features'/>

Features
=
The app 'Expense Tracker' is a simple app that tracks income / expenses that the user inputs. Even though it looks very simple on the outside there are a lot of things working in the background so the user can have a pleasant experience while using the app.

- ## **Start Screen**
    - When first starting the app. The user will be first greeted with a start screen that asks the user for their username so they can access their data.
    
    ![Start Screen](#startscreen)

- ## **Main Game Area**
    - After the username has been verified and the user has logged on. They will be greeted with 4 options:
     Show expenses and income
     Input Your Income / Expenses
     Check specific days ago
     Exit

    ![Main Screen](#mainscreen)

<div id='testing'/>

Testing
=

## **Solved Bugs**
- when the user inputed a username but it wasn't in the spreadsheet. It would ask if they wanted to use the specific username they selected. If the user selected "no" the main screen would still show with all of the options.

## **Unfixed Bugs**
- No bugs remaining.

## **Validator Testing**

- **Testing**
    - PEP8online.com was down during testing so I installed pycodestyle in VSCode. Then I searched for Linter and selected 'pycodestyle'. This showed if I had any errors which as of deployment is error free.
    
    ![Linter Check](#imagetesting)

## **Manual Testing**
The Following was tested manually and passed:

- **Username Input**
    - By adding a new username it gets stored in local storage until the user adds an income / expense entry where the username is displayed and saved.
- **Options**
    - The main menu options work as intended selecting the correct function when selected.
    - When an option is selected by inputing a value. The value is checked against a validator so no incorrect option or invalid value has been pressed.
    - the exit option ends the program.
- **Income / Expense Checking**
    - With multiple users in the spreadsheet. Only the specific users entries are shown correctly.
    - When inputing the amount. It only allows positive values and anything higher than zero to be inputted.

<div id='deployment'/>