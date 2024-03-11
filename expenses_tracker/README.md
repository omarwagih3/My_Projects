# Expenses Tracker

## Description
The Expenses Tracker project allows users to track their expenses by adding details such as amount, currency, category, and payment method. It calculates the total expenses in USD based on the entered currency using a currency converter API.

## Features
- Allows users to enter expenses with details like amount, currency, category, and payment method.
- Converts entered currencies into USD using a currency converter API.
- Displays the total expenses in USD in a table format.
- Supports different currencies, categories, and payment methods.

## Requirements
- Python 3.x
- `tkinter` library
- `requests` library
- `beautifulsoup4` library (for parsing HTML content if necessary)
- Internet connection for currency conversion API

## How to Use
1. Run the script `expenses_tracker.py`.
2. Enter the amount, select the currency, category, and payment method.
3. Click on the "Add Expenses" button to add the expense to the table.
4. The script converts the entered currency amount into USD and calculates the total expenses.
5. The total expenses are displayed in the table along with other expense details.
6. Exit the program when done.

## Implementation Details
- The script uses the `tkinter` library for creating a graphical user interface (GUI).
- Users can input the amount, select the currency, category, and payment method using entry fields and comboboxes.
- Currency conversion is done using the Fixer API to convert the entered currency into USD.
- The total expenses are calculated and displayed in the table along with individual expense details.
- The script handles exceptions for invalid input and failed API requests.

## What I've Learned
- Creating GUI applications using the `tkinter` library in Python.
- Handling user input and validating data entered in entry fields and comboboxes.
- Making HTTP requests to external APIs using the `requests` library.
- Parsing JSON responses from APIs and extracting relevant data.
- Displaying data in a table format using the `tkinter` `Treeview` widget.

## Author
[Omaar Wagih]
