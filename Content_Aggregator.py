import requests
from bs4 import BeautifulSoup
url = 'https://www.daraz.pk/'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
title = soup.find('title').get_text()
print(title)