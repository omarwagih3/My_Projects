import requests
from bs4 import BeautifulSoup

# Send a GET request to the site
url = "https://books.toscrape.com/"
response = requests.get(url)

# Checking the request status
if response.status_code == 200:
    print("Response successful")

    # Parse the page
    page = BeautifulSoup(response.content, "html.parser")

    # Search for articles and extract book details
    for article in page.find_all("article"):
        title = article.h3.get_text()
        rating = article.select_one("p.star-rating")["class"][1]
        price = article.select_one("p.price_color").get_text()

        # Print the book details
        print(f"Title: [{title}] :: Rating: [{rating}] Stars :: Price: [{price}]")
else:
    print("Failed to get response from the website")
