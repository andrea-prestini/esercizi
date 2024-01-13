from bs4 import BeautifulSoup
import requests
import collections

collections.Callable = collections.abc.Callable

url = "https://www.corriere.it/tecnologia/"
req = requests.get(url)

print(req.status_code)

soup = BeautifulSoup(req.text, "html.parser")
print(soup.prettify())
print(soup.title.text)
