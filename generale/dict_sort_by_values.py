dizionario = {
    "a": 15,
    "b": 11,
    "c": 4,
    "d": 4,
    "e": 56,
    "f": 6,
    "g": 78,
    "h": 33,
    "i": 23,
    "j": 17,
}


sorted_dictionary = dict(sorted(dizionario.items(), key=lambda x: x[-1]))

for k, v in sorted_dictionary.items():
    print(k, v)
