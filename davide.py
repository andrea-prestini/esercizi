"""
Semplice calcolatrice usando classi senza istanza
"""


class Calcolatrice:
    print("Benvenuto nella nostra calcolatrice!")
    print("1- Somma")
    print("2- Sottrazione")
    print("3- Moltiplicazione")
    print("4- Divisione")

    @staticmethod
    def inserimento():
        try:
            x = int(input("Inserisci il primo numero: "))
            y = int(input("Inserisci il secondo numero: "))
            return x, y
        except ValueError:
            print("Inserisci un numero!")
            return Calcolatrice.inserimento()

    @staticmethod
    def somma():
        a, b = Calcolatrice.inserimento()
        print("La somma e' ", a + b)

    @staticmethod
    def sottrazione():
        a, b = Calcolatrice.inserimento()
        print("La sottrazione e' ", a - b)

    @staticmethod
    def moltiplicazione():
        a, b = Calcolatrice.inserimento()
        print("La moltiplicazione e' ", a * b)

    @staticmethod
    def divisione():
        a, b = Calcolatrice.inserimento()
        try:
            print("La divisione e' ", a / b)
        except ZeroDivisionError:
            print("Non posso dividere per ZERO!")


Calcolatrice()

while True:
    what = input("Quale operazione vuoi effettuare? ")

    if what == "1":
        Calcolatrice.somma()
    elif what == "2":
        Calcolatrice.sottrazione()
    elif what == "3":
        Calcolatrice.moltiplicazione()
    elif what == "4":
        Calcolatrice.divisione()
    else:
        print("Fine procedura")
        break
