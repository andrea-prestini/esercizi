parole_bannabili = [
    "pandoro",
    "balocco",
    "findanzato",
    "pubblicità",
    "adv",
    "onlyfans",
    "piedi",
    "divorzio",
    "separazione",
]


messaggio = "ciao pandoro gaviano"
valori = messaggio.split()

# Usiamo intersezione di set per valutare il risultato vuoto / pieno
if set(parole_bannabili) & set(valori):
    print("Presente")
else:
    print("Assente")
