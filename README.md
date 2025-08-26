
# ExpenseTracker

A simple Python-based tool to record and analyze categorized expenses for a specific date. It collects multiple expense entries, calculates totals and statistics, and exports the results to a CSV file.

## Features

* Prompts the user to enter the date of the expenses (year, month, day)
* Records multiple expenses, each with a category and a non-negative amount
* Calculates:

  * Total expense
  * Average expense
  * Highest and lowest individual expenses
  * Totals by category
* Displays a summary of all recorded expenses
* Validates all numeric inputs and handles invalid entries
* Exports all expense data to a CSV file named using the provided date

## How It Works

* The user is prompted to enter the year, month, and day
* The user enters multiple expenses by:

  * Typing a category or description for each
  * Entering a corresponding non-negative amount
* The entry process continues until the user types `done`
* Once complete:

  * A summary of the expenses is printed to the console
  * The data is saved to a file in the format `expenses_YYYY-MM-DD.csv`

## Sample Interaction

Enter the year (e.g., 2025):
2025
Enter the month (1-12):
8
Enter the day (1-31):
24
Enter the type of expense (or 'done' to finish):
groceries
Enter the amount for groceries:
45.75
Enter the type of expense (or 'done' to finish):
rent
Enter the amount for rent:
1200
Enter the type of expense (or 'done' to finish):
entertainment
Enter the amount for entertainment:
80
Enter the type of expense (or 'done' to finish):
done

Expense Summary:
Total Expense: \$1325.75
Average Expense: \$441.92
Highest Expense: rent - \$1200.00
Lowest Expense: groceries - \$45.75
Expenses by Category:
groceries: \$45.75
rent: \$1200.00
entertainment: \$80.00

Expenses exported to 'expenses\_2025-08-24.csv' successfully.

## Code Overview

**ExpenseTracker class**

**init(self)**
Initializes an empty list to store expense entries.

**add\_expense(self, expense\_type, amount)**
Adds a new expense with the specified type and amount.

**get\_expenses(self)**
Returns a list of all recorded expenses.

**calculate\_total(self)**
Calculates the total value of all expenses.

**calculate\_average(self)**
Returns the average expense amount.

**find\_highest\_expense(self)**
Returns the highest individual expense and its category.

**find\_lowest\_expense(self)**
Returns the lowest individual expense and its category.

**category\_totals(self)**
Returns a dictionary of total expenses grouped by category.

**print\_summary(self)**
Displays a formatted summary of total, average, highest, and lowest expenses, as well as category breakdowns.

**export\_to\_csv(self, filename)**
Exports the list of expenses to a CSV file with the given filename.

**Supporting Functions**

**get\_user\_date()**
Prompts the user for a valid year, month, and day and returns the formatted date.

**get\_user\_expenses(tracker)**
Handles the user input loop for collecting expense entries and adds them to the tracker.

**main()**
Coordinates the program flow: prompts for date, collects expenses, prints the summary, and saves the data to a CSV file.

