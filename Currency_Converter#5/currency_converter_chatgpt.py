import requests

def is_valid_currency(currency_code):
    """Check if the given currency code is valid."""
    url = f"https://open.er-api.com/v6/latest/{currency_code}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if currency_code in data["rates"]:
            return True
    return False

def get_currency_input(prompt):
    """Prompt user to input a valid currency code."""
    while True:
        user_input = input(prompt).upper()
        if is_valid_currency(user_input):
            return user_input
        else:
            print("Please provide a valid currency code.")

def convert_currency():
    """Convert currency based on user input."""
    # Get the initial and target currency codes
    init_currency = get_currency_input("Enter the currency you want to convert from: ")
    target_currency = get_currency_input("Enter the currency you want to convert to: ")

    # Get the amount to convert
    while True:
        try:
            amount = float(input("Enter the amount you want to convert: "))
            if amount <= 0:
                print("Please enter a valid amount.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    # Construct the API URL for currency conversion
    url = f"https://api.apilayer.com/fixer/convert?to={target_currency}&from={init_currency}&amount={amount}"
    headers = {
        "apikey": "T0YoyRW81G6iJhl7E3VefzvUdkihEpVt"
    }

    # Make a request to the currency conversion API
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("Failed to retrieve data. Please try again later.")
        print("Exiting program...")
        quit()
    else:
        print("Conversion successful!")
        result = response.json()
        print(f"{amount} {init_currency} is equal to {result['result']} {target_currency}")

# Perform currency conversion
convert_currency()
