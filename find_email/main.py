import re
import time


def estrai_emails(testo):
    path_to_find = r"[\w.]+@[\w.]+\.[\w.]+"
    return re.findall(path_to_find, testo)


with open("elenco.txt") as f:
    emails = estrai_emails(f.read())
    time.sleep(1)


for email in emails:
    print(email)
    time.sleep(1)

print("fine procedura...")
