import requests
from bs4 import BeautifulSoup

#send a Get request to site
url = "https://books.toscrape.com/"
response = requests.get(url)

#checking the request status
if response.status_code == 200:
    #testing
    print("response successful")

    #testing
    print("parse page")
    page = BeautifulSoup(response.content, "html.parser")
    #testing 
    print("search for articles")

    articles = page.find_all("article")
    
    for article in articles:
        title = article.find("h3").get_text()
        rating= article.find("p",class_="star-rating").get("class")[1]
        price = article.find("p",class_="price_color").get_text()

        print(f"title:[{title}]  ::  rating:[{rating}]Stars  ::  Price:[{price}]")

else:
    print("failed to get response")        