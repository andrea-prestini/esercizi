import re
import csv
import time


# new_number = re.sub(r"^\+39(?:\+39|\s)", "+39", row)

numeri_corretti = []

with open("./elenco.csv", ) as filecsv:
    lettore = csv.reader(filecsv, delimiter="\n")
    for row in lettore:
        new_number = re.sub(r"^\+39(?:\+39|\s)", "+39", row[0]).replace(",", "")
        numeri_corretti.append(new_number)

with open("numeri.csv", "w") as file:
    for line in numeri_corretti:
        file.write(line)
        file.write("\n")


print("creo il file con i numeri modificati...")
time.sleep(5)
print("procedura terminata...")
