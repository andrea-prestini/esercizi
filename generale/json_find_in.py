import json
import time


try:
    json_file = ("tabliss.json")
    with open(json_file) as in_file:
        data = json.load(in_file)
        for link in data["DATA"]["links"]:
            print(link["name"])
            print(link["url"])
            print()
            time.sleep(1)

        else:
            print("NON presente")
except Exception as e:
    print(e)
