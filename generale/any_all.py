stringa = "questa stringa contiene diverse parole tra cui valle esine bicher"

words = ["stringa", "casa", "bicher"]

check_valori = [(parola in stringa) for parola in words]

print(check_valori)
print("Tutte le parole sono presenti?", all(check_valori))