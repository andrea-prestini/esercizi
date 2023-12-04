from collections import defaultdict


counts1 = {}
numbers = [1, 2, 3, 4, 5, 4, 1, 5]
# setdefault per valori non presenti, se presenti
# restituisce il valore corripondente alla chiave richiesta
persona = {'nome': 'andrea'}

# key is not in the dictionary
persona.setdefault("paese", "Esine")
persona.setdefault("zona", "Valle Camonica")
persona.setdefault("nazione", "Italia")
persona.setdefault("gruppo", "Europa")

print(persona["nome"])
print(persona["paese"])
print(persona["zona"])
print(persona["nazione"])
print(persona["gruppo"])

# default dict from collections
print("SetDefault for Dict")
my_dict: dict[str, list] = {}
my_dict.setdefault("andrea", []).append("bicher")
print(my_dict)
print("Equivalente a...")
print()
d: dict[str, list] = {}
if "list" not in d:
    d["list"] = []
d["list"].append(3)
print(d)


# GOOD
print("codice pythonico...")
counts2: dict[int, int] = defaultdict(lambda: 0)
for key in numbers:
    counts2[key] += 1

print(counts2)
