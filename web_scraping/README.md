#  Web Scraping Project

## Description
The Book Scraping project allows users to scrape book information from a website. It retrieves book titles, ratings, and prices from the "Books to Scrape" website and displays them to the user.

## Features
- Scrapes book titles, ratings, and prices from a website.
- Uses the BeautifulSoup library for web scraping.
- Displays scraped book information in the console.

## Requirements
- Python 3.x
- `requests` library
- `beautifulsoup4` library

## How to Use
1. Run the script `book_scraper.py`.
2. The script sends a GET request to the "Books to Scrape" website.
3. If the request is successful, the script parses the HTML content using BeautifulSoup.
4. It searches for book articles on the webpage and extracts information such as title, rating, and price.
5. The script then prints the scraped book information to the console.
6. Exit the program when done.

## Implementation Details
- The script sends a GET request to the specified website using the `requests` library.
- It checks the response status code to ensure the request was successful.
- BeautifulSoup is used to parse the HTML content of the webpage.
- Book information is extracted by searching for specific HTML elements and their classes.
- Scraped data is printed to the console for the user to view.

## What I've Learned
- Web scraping techniques using the BeautifulSoup library.
- Making HTTP requests and handling responses with the `requests` library.
- Parsing HTML content to extract desired information.
- Navigating through HTML elements and classes to locate specific data.
- Displaying scraped data in a readable format.

## Author
[Omar Wagih]
