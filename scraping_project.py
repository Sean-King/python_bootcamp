import random
import time
import requests
import pandas as pd
from bs4 import BeautifulSoup

# Quote website to be scrapped
base_url = 'http://quotes.toscrape.com/'

# Store information in a list
quotes = []
authors = []
bios = []


def scrape():

    # page url
    page_url = '/page/1'

    while page_url:
        # Retrieving the URL
        response = requests.get(f"{base_url}{page_url}")
        print(f"Beginning to scrape {base_url}{page_url}...")
        # Create soup variable to store the webpage HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        # store the HTML for the quote containers on the webpage
        quote_containers = soup.find_all('div', class_='quote')

        for container in quote_containers:

            # Scrape the first quote on the homepage
            quote_text = container.find('span', class_='text').text
            quotes.append(quote_text)

            # Scrape the name of the person that the quote is from
            quote_author = container.find('small', class_='author').text
            authors.append(quote_author)

            # Scrape the bio url of the quote author
            author_bio = container.find('a')["href"]
            bios.append(author_bio)

        next_page = soup.find(class_='next')
        page_url = next_page.find('a')['href'] if next_page else None

    print("Scraping finished.")


def write_csv(content):
    # Merge the data into a pandas DataFrame
    print("Merging data using pandas.")
    all_quotes = pd.DataFrame({'text': quotes,
                               'author': authors,
                               'bio': bios})

    all_quotes.to_csv('quotes.csv', index=False)
    print("Finsined writing.")


scrape_quotes = scrape()
write_csv(scrape_quotes)
