import requests
import os
import json
from bs4 import BeautifulSoup
from datetime import datetime, timezone

current_dir = os.path.join(os.path.dirname(__file__))

def map_rating_to_number(rating):
    ratings = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }
    return ratings[rating]

def write_data(filename, data):
    now = datetime.now(timezone.utc).isoformat()

    # write the scraped data to a JSON file
    filepath = os.path.join(current_dir, "..", "..", f"{filename}-{now}.json")
    with open(filepath, 'w') as f:
        f.write(json.dumps(data, indent=4))
        print(f"Successfully created {filename}-{now}.json")

def get_soup(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html5lib')
    return soup

def scrape_hacker_news():
    url = 'https://news.ycombinator.com'
    soup = get_soup(url)
    articles = []

    # Loop through all the Hacker News post rows e.g. HTML elements that match <tr class="athing ...">
    for item in soup.find_all('tr', class_="athing"):
        title_tag = item.find('span', class_="titleline").find('a')
        title = title_tag.text
        link = title_tag.get('href', 'N/A')
        new_article = {
            "title": title,
            "link": link
        }
        articles.append(new_article)

    for idx, item in enumerate(soup.find_all("span", class_="hnuser")):
        articles[idx]['author'] = item.text

    for idx, item in enumerate(soup.find_all("span", class_="score")):
        articles[idx]['upvotes'] = item.text

    for idx, item in enumerate(soup.find_all("span", class_="age")):
        articles[idx]['age'] = item.find('a').text

    write_data("data/scraping/hackernews/news", articles)

def scrape_books():
    url = 'https://books.toscrape.com'
    soup = get_soup(url)
    books = []
    for item in soup.find_all("article", class_="product_pod"):
        title_tag = item.find("h3").find("a")
        title = title_tag.get("title")
        link = title_tag.get("href")
        price = item.find("p", class_="price_color").text
        availability = item.find("p", class_="availability").text
        rating_tag = item.find("p", class_="star-rating")
        rating = rating_tag.get("class")[1]
        cover_image = item.find("img", class_="thumbnail").get("src")
        new_book = {
            "title": title,
            "link": link,
            "rating": map_rating_to_number(rating),
            "price": price.replace('\u00c2\u00a3', ''),
            "availability": availability.replace('\n', '').strip(),
            "cover_image": cover_image
        }
        books.append(new_book)
    write_data("data/scraping/books-to-scrape/books", books)

scrape_hacker_news()
scrape_books()
