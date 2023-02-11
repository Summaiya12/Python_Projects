import requests
import bs4
url=input("Enter your url")
response=requests.get(url)
print(type(response))
print(response.text)