import requests
from csv import DictWriter
from random import randint, choice
from time import time, sleep
from bs4 import BeautifulSoup


base_url = 'http://quotes.toscrape.com/'


# def scrape_quote():
all_quotes = []
url = '/page/1'

while url:
    response = requests.get(f"{base_url}{url}")
    print(f"Beginning to scrape {base_url}{url}...")
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.find_all(class_='quote')

    for quote in quotes:
        all_quotes.append({
            'text': quote.find(class_='text').text,
            'author': quote.find(class_='author').text,
            'bio_link': quote.find('a')['href']
        })

    next_button = soup.find(class_='next')
    url = next_button.find('a')['href'] if next_button else None
    # sleep(randint(8, 15))
print("Done scraping!")

quote = choice(all_quotes)
remaining_guesses = 4
print("Here's a quote: ")
print(quote['text'])
print(quote['author'])
guess = ''
while guess.lower() != quote['author'].lower() and remaining_guesses > 0:
    guess = input(f"Who said this quote? Guesses remaining: {remaining_guesses}")
    remaining_guesses -= 1
    if remaining_guesses == 3:
        response = requests.get(f"{base_url}{quote['bio_link']}")
        soup = BeautifulSoup(response.text, 'html.parser')
        print(soup.body)

print("AFTER WHILE LOOP")

# Write to a csv file
# def write_quotes(quotes):
#     with open('quotes.csv', 'w') as file:
#         headers = ['text', 'author', 'bio-link']
#         csv_writer = DictWriter(file, fieldnames=headers)
#         csv_writer.writeheader()
#         for quote in quotes:
#             csv_writer.writerow(quote)
