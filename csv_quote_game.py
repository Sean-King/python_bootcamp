import time
import requests
import pandas as pd
from random import choice
from csv import DictReader
from bs4 import BeautifulSoup

# base url that will be used for calling author bio
BASE_URL = "http://quotes.toscrape.com"

# read the csv file of what data that was scraped using "scraping_project.py"
def read_quotes(filename):
    with open('quotes.csv', 'r', encoding='utf8') as csv_file:
        csv_reader = DictReader(csv_file)
        return list(csv_reader)

# function to start the game
def start_game(quotes):
    quote = choice(quotes)
    remaining_guesses = 4
    print("Here's a quote: ")
    print(quote['text'])
    # print(quote['author'])

    guess = ''
    while guess.lower() != quote["author"].lower() and remaining_guesses > 0:
        guess = input(f"Who said this quote? Guesses remaining: {remaining_guesses}\n")

        if guess.lower() == quote["author"].lower():
            print("YOU GOT IT RIGHT!")
            break

        remaining_guesses -= 1
        # if there are 3 remaining guesses, provide a hint as to when and where the person was born
        if remaining_guesses == 3:
            res = requests.get(f"{BASE_URL}{quote['bio']}")
            soup = BeautifulSoup(res.text, "html.parser")
            birth_date = soup.find(class_="author-born-date").get_text()
            birth_place = soup.find(class_="author-born-location").get_text()
            print(f"Here's a hint: The author was born on {birth_date} {birth_place}")

        # if there are 2 guesses remaining, provide a hint as to the first letter of their first name.
        elif remaining_guesses == 2:
            print(f"Here's a hint: The author's first name starts with: {quote['author'][0]}")

        # if there is 1 guess remianing, provide a hint as to the first letter of their last name
        elif remaining_guesses == 1:
            last_initial = quote["author"].split(" ")[1][0]
            print(f"Here's a hint: The author's last name starts with: {last_initial}")

        # if there are 0 guesses remaining, provide the name of the author of the quote
        else:
            print(f"Sorry, you ran out of guesses. The answer was {quote['author']}")

    # play the game again based on input from the player
    again = ''
    while again.lower() not in ('y', 'yes', 'n', 'no'):
        again = input("Would you like to play again (y/n)?")

    if again.lower() in ('yes', 'y'):
        return start_game(quotes)

    else:
        print("Ok, goodgye.")


quotes = read_quotes('quotes.csv')
start_game(quotes)
