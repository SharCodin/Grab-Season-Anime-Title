import requests
from bs4 import BeautifulSoup

URL = 'https://myanimelist.net/anime/season'

page = requests.get(URL).text
soup = BeautifulSoup(page, 'lxml')

with open("new_anime.txt", "wb") as f:
    for i in soup.find_all('p', {"class": "title-text"}):
        name = str(i.text).strip()
        name = name.encode("utf-8")
        # name = name.decode("utf-8", "replace")
        f.write(name)
        newline = "\n".encode("utf-8")
        f.write(newline)
    