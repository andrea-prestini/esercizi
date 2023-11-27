import json
import time
import os


lista_assenti = []
lista_presenti = []

with open("classe.json") as json_file:
    stanza = json.load(json_file)


for elemento in stanza["persone"]:
    if elemento["presente"] is True:
        elemento["nome"] = elemento["nome"].title()
        elemento["cognome"] = elemento["cognome"].capitalize()
        lista_presenti.append(elemento)
        elemento["presente"] = "PRESENTE"
    else:
        elemento["nome"] = elemento["nome"].title()
        elemento["cognome"] = elemento["cognome"].capitalize()
        lista_assenti.append(elemento)
        elemento["presente"] = "ASSENTE"
    print(f'''
    nome: {elemento["nome"]}
    cognome: {elemento["cognome"]}
    presente: {elemento["presente"]}''')
    time.sleep(1)

with open("presenti.json", "w") as presenti:
    json.dump(lista_presenti, presenti, indent=2)

with open("assenti.json", "w") as assenti:
    json.dump(lista_assenti, assenti, indent=2)

print()
print("creo i files con i dati filtrati")
time.sleep(5)
for i in range(1, 120):
    os.system("clear")
    print("-"*i)
    time.sleep(0.05)
print()
print("files persone presenti ed assenti alla riunione CREATI!")
