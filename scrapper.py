import requests
from bs4 import BeautifulSoup

URL = 'https://books.toscrape.com/'

response = requests.get(URL)
data = BeautifulSoup(response.text, features="html.parser")
books = data.find_all(class_='product_pod')
for book in books:
    print(book.find(class_='image_container'))
