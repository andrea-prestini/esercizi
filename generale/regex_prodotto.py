import re
import time


stringa = '''
il prodotto richiesto dal cliente ha ID 501
abbiamo in magazzino il codice ID 301
il prodotto richiesto si trova in magazzino con ID 304
il prodotto richiesto si trova in magazzino con ID 305
il prodotto richiesto si trova in magazzino con ID 306
in arrivo ci sono pezzi del prodotto ID 599
il prodotto richiesto dal  ha ID 100
il prodotto richiesto dal cliente ha ID 502
il prodotto richiesto dal cliente ha ID 503
il prodotto richiesto dal cliente ha ID 504
il prodotto richiesto dal cliente ha ID 505
il prodotto richiesto dal cliente ha ID 506
il prodotto richiesto dal cliente ha ID 507
il prodotto richiesto si trova in magazzino con ID 302
il prodotto richiesto si trova in magazzino con ID 303
'''
patternCliente = r"(?:cliente\s\w*\sID\s)(\d+)"
patternMagazzino = r"(?:magazzino\s\w*\sID\s)(\d+)"

resultCliente = re.findall(patternCliente, stringa)
resultMagazzino = re.findall(patternMagazzino, stringa)
print("=" * 50)
breakpoint()
print("Abbiamo trovato nei clienti:")
for i in range(len(resultCliente)):
    print("prodotto ID ->", resultCliente[i])
    time.sleep(1)

print("-" * 50)

print("Abbiamom trovato nel magazzino:")
for i in range(len(resultMagazzino)):
    print("prodotto ID ->", resultMagazzino[i])
    time.sleep(1)

time.sleep(2)
print("\n" * 5)
print("=============================================================")
print("fine del procedimento...".upper())
print("=============================================================")
