import tkinter as tk
from tkinter import ttk
import datetime
import requests

class ExpenseTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")
        self.root.geometry("1015x600")

        # Define currencies, categories, and payment methods
        self.currencies = ["USD", "EUR", "GBP", "JPY"]
        self.categories = ["Life Expenses", "Electricity", "Gas", "Rental", "Grocery", "Savings", "Education", "Charity"]
        self.payment_methods = ["Cash", "Credit Card", "Paypal"]

        # Initialize total
        self.total = 0

        # Initialize UI
        self.setup_ui()

    def setup_ui(self):
        # Create labels and entries
        tk.Label(self.root, text="Amount:").grid(row=0, column=0, sticky='w')
        self.amount_entry = tk.Entry(self.root, width=30)
        self.amount_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.root, text="Currency:").grid(row=1, column=0, sticky='w')
        self.currency_combobox = ttk.Combobox(self.root, values=self.currencies, state="readonly")
        self.currency_combobox.grid(row=1, column=1, padx=10, pady=10)
        self.currency_combobox.current(0)

        tk.Label(self.root, text="Category:").grid(row=2, column=0, sticky='w')
        self.category_combobox = ttk.Combobox(self.root, values=self.categories, state="readonly")
        self.category_combobox.grid(row=2, column=1, padx=10, pady=10)
        self.category_combobox.current(0)

        tk.Label(self.root, text="Payment Method:").grid(row=3, column=0, sticky='w')
        self.payment_combobox = ttk.Combobox(self.root, values=self.payment_methods, state="readonly")
        self.payment_combobox.grid(row=3, column=1, padx=10, pady=10)
        self.payment_combobox.current(0)

        # Add Expense button
        self.add_expense_btn = tk.Button(self.root, text="Add Expense", command=self.add_expense)
        self.add_expense_btn.grid(row=4, column=1, padx=10, pady=10)

        # Expense Table
        self.expense_table = ttk.Treeview(self.root, columns=("Amount", "Currency", "Category", "Payment Method"))
        self.expense_table.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
        self.expense_table.heading("#0", text="ID")
        self.expense_table.heading("Amount", text="Amount")
        self.expense_table.heading("Currency", text="Currency")
        self.expense_table.heading("Category", text="Category")
        self.expense_table.heading("Payment Method", text="Payment Method")

    def add_expense(self):
        amount = self.amount_entry.get()
        currency = self.currency_combobox.get()
        category = self.category_combobox.get()
        payment_method = self.payment_combobox.get()

        # Convert currency to USD
        converted_amount = self.convert_to_usd(amount, currency)

        # Update total
        self.total += converted_amount

        # Insert into table
        self.expense_table.insert("", "end", text="", values=(amount, currency, category, payment_method))

        # Update total row
        self.expense_table.insert("", "end", text="Total", values=(self.total, "USD"))

    def convert_to_usd(self, amount, currency):
        url = f"https://api.exchangerate-api.com/v4/latest/{currency}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            exchange_rate = data['rates']['USD']
            return float(amount) / exchange_rate
        else:
            print("Failed to fetch data")
            return 0

if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTrackerApp(root)
    root.mainloop()
