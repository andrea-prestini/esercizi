import re


stringa = "bicher \
sono in via bicher \
al numero 3 che è una via di esine \
in valle camonica in via bicher e si chiama bicher the one \
the one è il nostro motto"

pattern = r"bicher"

# usiamo la funzione match, trova solo all'inizio della stringa
print("match")
result = re.match(pattern, stringa)
print(result)
print("-" * 50)

# usiamo la funzione findall, cerca in tutta la stringa ma risulta meno veloce
print("findall")
result1 = re.findall(pattern, stringa)
print(result1)
print("-" * 50)

# usiamo la funzione finditer che itera sul risultato
print("finditer")
result2 = re.finditer(pattern, stringa)
print(result2)
print("-" * 50)

# iteriamo sull'oggetto creato da finditer usando la lista group con indice per
# per ottenere il risultato richiesto
print("MATCH GROUP")
for match in result2:
    print(match.group())
print("group con indice 0...")
print(match.group(0))
print("-" * 50)

print("split")
result3 = re.split(pattern, stringa)
print(result3)
print("-" * 50)
