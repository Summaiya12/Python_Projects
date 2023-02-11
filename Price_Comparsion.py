import requests
from bs4 import BeautifulSoup
import webbrowser
webbrowser.open("https://www.daraz.pk/")
header={
    'Url-Agent':"https://www.daraz.pk/"
}

response = requests.get("https://www.daraz.pk/")
def price_check():
    print("money Rs 500000")
    print("money Rs 450000")
price_check()