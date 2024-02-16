"""
Semplice calcolatrice usando funzioni
"""


print("Benvenuto nella nostra calcolatrice!")
print("1- Somma")
print("2- Sottrazione")
print("3- Moltiplicazione")
print("4- Divisione")


def inserimento():
    try:
        x = int(input("Inserisci il primo numero: "))
        y = int(input("Inserisci il secondo numero: "))
        return x, y
    except ValueError:
        print("Inserisci un numero!")
        return inserimento()


def somma():
    a, b = inserimento()
    print("La somma e' ", a + b)


def sottrazione():
    a, b = inserimento()
    print("La sottrazione e' ", a - b)


def moltiplicazione():
    a, b = inserimento()
    print("La moltiplicazione e' ", a * b)


def divisione():
    a, b = inserimento()
    print("La divisione e' ", a / b)


while True:
    what = input("Quale operazione vuoi effettuare? ")

    if what == "1":
        somma()
    elif what == "2":
        sottrazione()
    elif what == "3":
        moltiplicazione()
    elif what == "4":
        divisione()
    else:
        print("Fine procedura")
        break
