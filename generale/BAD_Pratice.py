import time
from collections import defaultdict
from pathlib import Path


# NOT USE a Default mutable OBJECT


def append_number(num, numbers=[]):
    # list is mutable objects
    numbers.append(num)
    print(num)
    print(numbers)
    return numbers


x = append_number(1)
x = append_number(2)
x = append_number(3)


def string_append(s, string="Ciao"):
    # string is immutable object
    string += s
    print(s)
    print(string)
    return string


string_append("B")
string_append("I")
string_append("C")

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
print()

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
