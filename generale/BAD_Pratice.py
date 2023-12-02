import time
from collections import defaultdict
from pathlib import Path


# NOT USE a Default mutable OBJECT

# BAD
def add_itemBAD(item: str, itemsBAD: list = []):
    # list is mutable objects
    itemsBAD.append(item)
    print(f"ID {id(item)}:", itemsBAD)
    return itemsBAD


list_a = add_itemBAD("a")
list_b = add_itemBAD("b")
# Side effects
# ID 123: ["a"]
# ID 123: ["a", "b] le 2 liste hanno lo stesso id e vengono incrementate!


# GOOD
# check if object exists
def add_itemGOOD(item: str, items: list = None):
    # list is mutable objects
    if not items:
        items: list = []
    items.append(item)
    print(f"ID {id(item)}:", items)
    return items


list_a = add_itemGOOD("a")
list_b = add_itemGOOD("b")

# Stessa cosa per tutti gli oggetti mutable come dict, set, list, string
# Il codice funziona correttamente ma genera un Side Effects!
# Prima verificare se esistono, poi eventualmente crearne di nuovi!

# def string_append(s, string="Ciao"):
#     # string is immutable object
#     string += s
#     print(s)
#     print(string)
#     return string
#
#
# string_append("B")
# string_append("I")
# string_append("C")

# NOT USE a Default Dict
print("codice non pythonico")
counts1 = {}
numbers = [1, 2, 3, 4, 5, 4, 1, 5]

for key in numbers:
    if key not in counts1:
        counts1[key] = 0
    counts1[key] += 1
print(counts1)
print()

print("codice pythonico...")
counts2 = defaultdict(lambda: 0)
for key in numbers:
    counts2[key] += 1

print(counts2)
print()

# SETDefault
print("SetDefault for Dict")
my_dict = {}
my_dict.setdefault("andrea", []).append("bicher")
print(my_dict)
print("Equivalente a...")
print()
d = {}
if "list" not in d:
    d["list"] = []
d["list"].append(3)
print(d)


#
#
# NOT USE context manager when opening files
file = "testo.txt"
# if os.path.isfile("testo.txt"):
#     with open(file, "r") as f:
#         print("leggo il contenuto del file %s" % (file))
#         time.sleep(2)
#         print(f.read())
# else:
#     print("Non trovo il file...")
#     time.sleep(2)
#     print("File %s do not Exists!" % (file))

my_file = Path("./testo.txt")
if my_file.exists():
    # exists search file or directory
    with open(file, "r") as f:
        print("leggo il contenuto del file %s" % (file))
        time.sleep(2)
        print(f.read())
else:
    print("Non trovo il file...")
    time.sleep(2)
    print("File %s do not Exists!" % (file))

print()


# NOT USE Enumerate
pass

# Overriding Built-In Names
# id = 2
# zip = 234343
# list = []
# possiamo utilizzare:
id_ = 2
zip_ = 123456
list_ = []
