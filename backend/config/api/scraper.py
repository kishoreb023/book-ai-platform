import requests
from bs4 import BeautifulSoup


def scrape_books():
    url = "http://books.toscrape.com/"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    books = []

    for item in soup.select('.product_pod'):
        title = item.h3.a['title']
        price = item.select_one('.price_color').text
        rating_class = item.p['class'][1]

        rating_map = {
            "One": 1,
            "Two": 2,
            "Three": 3,
            "Four": 4,
            "Five": 5
        }

        rating = rating_map.get(rating_class, 0)

        books.append({
            "title": title,
            "description": price,
            "rating": rating,
            "url": url
        })

    return books