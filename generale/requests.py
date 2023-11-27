import requests

response = requests.get("https://github.com")
info = []
info.append(response.headers["Date"])
info.append(response.headers["Server"])

lista = list(response.headers.items())[:11]

for i,v in enumerate(lista):
    print(i,v)