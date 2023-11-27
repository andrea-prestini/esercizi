import csv



file_csv = open("persone.csv")
lettore = csv.reader(file_csv, delimiter=",")
# header = next(lettore)
# print(header)
print("-" * 50)
# print([(x[0], x[2]) for x in lettore if x[2] == "gambara"])
# attenzione l'oggetto lettore viene distrutto, se avessi bisogno di applicare
# altri filtri meglio creare una tupla o lista da utilizzare come fonte dei
# dati da filtrare

persone_lst = []
for x in lettore:
    persone_lst.append(x)
file_csv.close()


print([(x[0], x[1]) for x in persone_lst if x[2] == "gambara"])
print([(x[0], x[1]) for x in persone_lst if x[2] == "esine"])
print()
print("otteniamo un layout migliore")
for x in persone_lst:
    print(f'''si chiama {x[0]}
abita a {x[2]}
cognome {x[1]}''')