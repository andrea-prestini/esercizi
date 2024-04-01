import requests
import time


for _ in range(3):

    num1, num2, num3, num4, num5 = \
        requests.get(
            "http://www.randomnumberapi.com/api/v1.0/random?min=1&max=1000&count=5").json()

    namejs = requests.get(
        "https://randomuser.me/api/?results=1").json()["results"][0]

    gender = namejs["gender"]
    name = namejs["name"]["first"]
    city = namejs["location"]["state"]
    state = namejs["location"]["country"]
    email = namejs["email"]
    password = namejs["login"]["password"]
    print(f"""
    numeri  casuali: {num1, num2, num3, num4, num5}
    {name = }
    {city = }
    {state = }
    {gender = }
    {email = }
    {password = }""")
    time.sleep(1)

print("fine generatore utenti")
