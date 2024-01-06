import requests
import time
from bs4 import BeautifulSoup


# URL of the web page you want to scrape
domanda = input("Quale url vuoi cercare? ")
url = "https://" + domanda

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)

if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find elements based on HTML tags, classes, IDs, etc.
    # For example, find all <a> tags (links) and print their href attribute
    lista = []
    links = soup.find_all('a')
    parole = input("Che parola vuoi cercare nella pagina web? ")
    print("Sto cercando...")
    time.sleep(3)

    for link in links:
        if parole in link.get('href'):
            lista.append(link.get('href'))
    if len(lista) == 0:
        print("Non ci sono elementi")
    else:
        print("Ci sono", len(lista), "elementi")
        time.sleep(3)
        for val in lista:
            print(val)
            time.sleep(1)
