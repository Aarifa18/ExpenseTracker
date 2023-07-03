# Expense Tracker

This is a simple expense tracker program that allows you to add, list, and remove expenses. It provides a command-line interface for interacting with the expense tracker.

## Features
- Add a new expense: You can enter the amount and category of the expense.
- Remove an expense: You can choose an expense from the list and remove it.
- List all expenses: It displays a list of all recorded expenses.

## Data Storage
The expenses are stored in a list called `expenses`. Each expense is a dictionary with the keys `'amount'` and `'category'`, representing the amount and category of the expense, respectively.

## Note
- This expense tracker does not persist data between program runs. Once the program is terminated, all recorded expenses will be lost.
- The input validation for amount and category is not comprehensive in the provided code. You may want to enhance the code to handle various input scenarios and error conditions.

Feel free to customize and extend the code to suit your specific needs and requirements.
