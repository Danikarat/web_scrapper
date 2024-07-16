import requests # type: ignore
from bs4 import BeautifulSoup
import scrapy

url = 'https://stackoverflow.com/questions'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
images = soup.find_all('img')

# for image in images:
#     print(image['src'])