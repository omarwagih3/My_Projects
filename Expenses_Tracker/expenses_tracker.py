import tkinter as tk
from tkinter import ttk
import datetime
import requests

def currency_converter(amount ,currency):
    init_currency = currency
    target_currency = "USD"

    while True:
        try:
            amount = amount
        except:
            print("invalid amount enter numeric value")
            continue
        if amount == 0:
            print("0 is not a valid amount")
            continue
        else:
            break

    url = (f"https://api.apilayer.com/fixer/convert?to="
        f"{target_currency}"
        f"&from={init_currency}&amount={amount}"
        )

    payload = {}

    headers= {
    "apikey": "T0YoyRW81G6iJhl7E3VefzvUdkihEpVt"
    }

    response = requests.request("GET", url, headers=headers, data = payload)

    status_code = response.status_code

    if status_code != 200:
        print("there was a problem, please try later! :(")
        print("Exiting program ....")
        quit()
    else:
        print("success")
        result = response.json()
    return result


def fill_table(amount ,currency ,category ,payment_method):
    newItem = [amount ,currency ,category ,payment_method]
    global total 
    result = currency_converter(amount ,currency)
    total = total + result['result']
    rows = table.get_children()
    if len(rows) != 0:
        table.delete(rows[-1])
    table.insert('' ,tk.END ,value = newItem)
    table.insert('' ,tk.END,value = [total ,"USD"])
    print (total)
    

#setup the window
window = tk.Tk()
window.title("Expenses Tracker")
window.config(bg = "#262626")
window.geometry("800x550")

#add style
style = ttk.Style()
style.theme_use("clam")
style.map("Treeview"
          ,background = [("selected","green")])

#required attributes
currency_options = ["USD" ,"EGP" ,"EUR" ,"GBP"]
category_options = ["life expenses", "electricity", "gas", "rental", "grocery", "savings", "education", "charity"]
payment_options = ["Cash", "Credit Card" ,"Paypal"]
total = 0
date =datetime.datetime.now()
#creating labels ,entry fields ,combobox fields.....
amount_label = tk.Label(window ,text ="Amount" ,font =("Arial",15) ,bg = "#262626" ,fg ="#5b7aa8")
amount_entry_field = tk.Entry(window ,width = 26)
currency_label = tk.Label(window ,text ="Currency" ,font =("Arial",15) ,bg = "#262626" ,fg ="#5b7aa8")
currency_option_list = ttk.Combobox(window ,value = currency_options ,width = 23)
category_label = tk.Label(window ,text ="Category" ,font =("Arial",15) ,bg = "#262626" ,fg ="#5b7aa8")
category_option_list = ttk.Combobox(window ,value = category_options ,width = 23)
payment_method_label = tk.Label(window ,text ="Payment Method" ,font =("Arial",15) ,bg = "#262626" ,fg ="#5b7aa8")
payment_option_list = ttk.Combobox(window ,value = payment_options ,width = 23)
Date_label = tk.Label(window ,text ="Date" ,font =("Arial",15) ,bg = "#262626" ,fg ="#5b7aa8")
date_input_label = tk.Label(window ,text = date.strftime("%Y-%m-%d") ,font =("Arial",10) ,width = 19)
add_expenses_btn = tk.Button(window ,text ="Add Expenses" ,font =("Arial",10) ,bg = "#10234a" ,fg ="#ffffff" ,command =
                              lambda: fill_table(amount_entry_field.get() ,currency_option_list.get() ,category_option_list.get() ,payment_option_list.get()))


#creating the table of expenses
columns =("amount" ,"currency" ,"category" ,"payment method")
table = ttk.Treeview(window ,columns = columns ,show = "headings")
table.heading("amount" ,text="Amount")
table.heading("currency" ,text="Currency")
table.heading("category" ,text="Category")
table.heading("payment method" ,text="Payment Method")

#positioning
amount_label.grid(row = 0 ,column = 0)
currency_label.grid(row = 1 ,column = 0)
category_label.grid(row = 2 ,column = 0)
payment_method_label.grid(row = 3 ,column = 0)
Date_label.grid(row = 4 ,column = 0)
amount_entry_field.grid(row = 0 ,column = 1 ,padx = 200)
currency_option_list.grid(row = 1 ,column = 1 ,padx = 200)
category_option_list.grid(row = 2 ,column = 1 ,padx = 200)
payment_option_list.grid(row = 3 ,column = 1 ,padx = 200)
date_input_label.grid(row = 4 ,column = 1 ,padx = 200)
add_expenses_btn.grid(row = 5 ,column = 1 ,padx = 200 ,pady = 5)
table.grid(row = 6 ,columnspan=4)


window.mainloop()
