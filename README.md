Expense Tracker
=

Introduction
=
Expense Tracker is a simple tracker that tracks your spending and income. You can add a username so multiple users can use the expense tracker. The user can check their total earned/saved. Be more specific with checking spending in the last few days to a month. inputting their income/expenses.


Users of the app will be able to track their spending habits and how much they have saved. 


![Photo of the website on multiple different screens](#amiresponsiveimage)

The website can be viewed here: [Expense Tracker](#liveLink "Expense Tracker").

# Table of contents
- [User Experience](#userexperience)
- [How To Use](#how-to-use)
- [Features](#features)
- [Future Ideas / Development](#future)
- [Testing](#testing)
- [Deployment](#deployment)
- [Technologies Used](#technologies)
- [Credits](#credits)

<div id='userexperience'/>

User Experience
=
## **User Stories**
- ## **As an app owner I want that:**

    1. The app provides clear and concise information on how to use the expense tracker.
    2. The app allows the user to input their username to track their spending and earnings.
    3. The app allows the user to input an expense/income and allows the app to update everything correctly.
------

- ## **As an app user I want:**
    1. To easily understand how to navigate the app.
    2. To calculate my spending or income within a specific time range.
    3. To not cause a crash when inputting an invalid value.
 ------

- ## **As a returning app user I want:**
    1. To be able to retrieve my spending/income with my username.
    2. To be able to add more income/expenses.


# 1. Strategy

- The main purpose of this app is to make it a useful tool for users to be able to track spending/income.
- Each user can make their username to track their spending.

# 2. Scope
- After a few design choices. an elegant 4 option the main screen was chosen where users can choose what they want to do.
- Adding color to add a visual distinction for different options.

# 3. Structure
- A start screen would ask for the user's username to begin.
- once the user has logged on, the user would be presented with 4 options to choose what they would like to do.
- Each option would be accessed by pressing a value that corresponds to an option.
- When the user is done using the expense tracker. There would be an exit option.

# 4. Skeleton
## **Wireframes**
- The initial design was made using Lucid Charts.

![Lucid Charts](assets/images/lucidchart.png)

# 5. Surface
 - ## **Color**
    - The basic color theme would be green for income and red for expenses.
    - Where instructing the user on how to select a specific option would be colored yellow.
    - Any errors or invalid values are chosen - the color would be red.
    - confirmation text would be green.
    - General welcome text would be cyan.

<div id='how-to-use'/>

How To Use
=
# 1. Upon Runtime
- Once the program is started it will ask the user to enter a username.
    - The username gets checked against previous entries in google sheets.
- If it is a new user it will confirm if the user wants this as their username.
# 2. Main Screen
- There are 4 options for the user to choose from. The yellow color indicates what the user should do to activate the option.
- using the number (1,2,3,4) to select an option. If the user inputs an invalid value an error will be displayed saying "incorrect value".
# 3. Options
 ## - Option 1: Show expenses and income.
  - This option will display the user's total income and expenses that they inputted. It will also display how much they have saved. A green or red color of the value will denote if it is a negative or positive value as a visual reference.
 ## - Option 2: Input Your Income / Expenses.
  - This option will allow the user to input an expense or income. Once they have selected their desired option the program will ask what type of income/expense they wish to add such as (income (salary, other)), (expense(entertainment, bills, food, transportation)).
  - The program will then ask the user to input the amount.
  - Once the user clicks enter, the google worksheet will be updated with the values supplied.
 ## - Option 3: Check Specific Days Ago.
  - Very similar to option 1. The only difference is that the program will ask the user how many days back they wish to see their income/expense. ie. inputting 7 will result in showing the user how much they have spent/earned in the last 7 days.
 ## - Option 4: Exit.
  - Allows the user to exit the program without crashing it.

<div id='features'/>

Features
=
The app Expense Tracker is a simple app that tracks the income/expenses that the user inputs. Even though it looks very simple on the outside there are a lot of things working in the background so the user can have a pleasant experience while using the app.

- ## **Start Screen**
    - When first starting the app. The user will be first greeted with a start screen that asks the user for their username so they can access their data.
    
    ![Start Screen](assets/images/startscreen.png)

- ## **Main Game Area**
    - After the username has been verified and the user has logged on. They will be greeted with 4 options:
     Show expenses and income
     Input Your Income / Expenses
     Check specific days ago
     Exit

    ![Main Screen](assets/images/mainmenu.png)

<div id='future'/>

Future Development
=

## **Further Development**
 - When the program first gets initiated it pulls all of the information from google sheets which works great with small amounts of data but would slow the program down if there were many entries. Further development would include; after the user has inputted their username it would check against a list of active usernames. Then it would parse through the income/expense sheet to pull only the specific user's information.


<div id='testing'/>

Testing
=

## **Solved Bugs**
- when the user inputs a username but it wasn't in the spreadsheet. It would ask if they wanted to use the specific username they selected. If the user selected "no" the main screen would still show all of the options.

## **Unfixed Bugs**
- No bugs remaining.

## **Validator Testing**

- **Testing**
    - PEP8online.com was down during testing so I installed pycodestyle in VSCode. Then I searched for Linter and selected 'pycodestyle'. This showed if I had any errors which as of deployment is error-free.
    - The 3 problems that are shown are not related to the project itself. They are from the Code Institute template.
    
    ![Linter Check](assets/images/errorfree.png)

## **Manual Testing**
The Following was tested manually and passed:

- **Username Input**
    - By adding a new username it gets stored in local storage until the user adds an income/expense entry where the username is displayed and saved.
- **Options**
    - The main menu options work as intended selecting the correct function when selected.
    - When an option is selected by inputting a value. The value is checked against a validator so no incorrect option or invalid value has been pressed.
    - the exit option ends the program.
- **Income / Expense Checking**
    - With multiple users in the spreadsheet. Only the specific user entries are shown correctly.
    - When inputting the amount. It only allows positive values and anything higher than zero to be inputted.

<div id='deployment'/>
Deployment
=

**The app was deployed using Code Institute's mock terminal for Heroku. The steps to deploy are as follows:**
- Create a new Heroku app.
- Set the buildbacks for Python and NodeJS in that order.
- Link the Heroku app to the repository.
- Click on Deploy. 

The live link can be found here [Expense Tracker](#livelink "Expense Tracker").

<div id='technologies'/>

Technologies Used
=

- ## Languages
    - Python

- ## Modules
    - OS Module - To clear the screen after specific actions done by the user to keep the terminal clean and tidy.
    - Date Time Module - To keep track of time to be able to have income/expense entries with a time stamp.
    - Time Module - To slow down the program after specific actions are taken, so the user can see what is happening.
    - Termcolor Module - To add color and visual design to the terminal
    - Gspread Module and google.oauth2.service_account - To be able to access a spreadsheet from google spreadsheet.

<div id='credits'/>

Credits
=

## **Content**
- To track time and to be able to convert between DateTime class and string I used this website to gain insight into how to do it
    - https://www.digitalocean.com/community/tutorials/python-string-to-datetime-strptime
    -![DateTime Credits](assets/images/datetime-credits.png)
- To get the google sheets API set up. I used Code Institutes video tutorial and took this code for use in my project.
 -![Code Institute Credits](assets/images/code-institute-code.png)

- Code Institute - the deployment terminal.