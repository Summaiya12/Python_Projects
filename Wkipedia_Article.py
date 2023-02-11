import webbrowser
import requests
from bs4 import BeautifulSoup
url = "https://en.wikipedia.org/wiki/Woldemar_Hottenroth"
article_page = requests.get(url)
soup= BeautifulSoup(article_page.text,"html.parser")
article_title = soup.find(id='firstHeading')
print("The article of the random article is:" ,article_title.string)
read = input("Do you want to view the article: (yes/no)")
if read == "yes":
    webbrowser.open(article_page.url)
print("The URL is:",article_title.url)
