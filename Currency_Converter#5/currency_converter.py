import requests

init_currency = input("enter initial currency: ")
target_currency = input("enter target currency: ")

while True:
    try:
        amount = float(input("enter amount: "))
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
       f"&from={init_currency}&amount={amount}")

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
    print(f"{amount} {init_currency} = {result['result']} {target_currency}")
