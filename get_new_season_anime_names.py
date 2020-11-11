import requests
from bs4 import BeautifulSoup

URL = 'https://myanimelist.net/anime/season'

page = requests.get(URL).text
soup = BeautifulSoup(page, 'lxml')

with open("new_anime.txt", "a", encoding='utf-8') as f:
    for i in soup.find_all('div', {"class": "title"}):
        tag = i.find('a', class_="link-title")
        name = tag.text.strip()
        f.write(name + '\n')