from os import startfile
import requests
from bs4 import BeautifulSoup
from timeit import default_timer as Timer

startTimer = Timer()



URL = 'https://myanimelist.net/anime/season'

page = requests.get(URL).text
soup = BeautifulSoup(page, 'lxml')

with open("new_anime.txt", "w", encoding='utf-8') as f:

    for i in soup.find_all('p', {"class": "title-text"}):
        name = str(i.text).strip()
        f.write(name + '\n')


# ====================  ====================
stopTimer = Timer()
print(str(round(stopTimer - startTimer, 2)))
print('-' * 20)
