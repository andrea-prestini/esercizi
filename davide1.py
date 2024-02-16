"""
Semplice calcolatrice usando classi ed istanza
"""


class Calcolatrice:
    print("Benvenuto nella nostra calcolatrice!")
    print("1- Somma")
    print("2- Sottrazione")
    print("3- Moltiplicazione")
    print("4- Divisione")

    def inserimento(self):
        try:
            x = int(input("Inserisci il primo numero: "))
            y = int(input("Inserisci il secondo numero: "))
            return x, y
        except ValueError:
            print("Inserisci un numero!")
            return self.inserimento()

    def somma(self):
        a, b = self.inserimento()
        print("La somma e' ", a + b)

    def sottrazione(self):
        a, b = self.inserimento()
        print("La sottrazione e' ", a - b)

    def moltiplicazione(self):
        a, b = self.inserimento()
        print("La moltiplicazione e' ", a * b)

    def divisione(self):
        a, b = self.inserimento()
        print("La divisione e' ", a / b)


c = Calcolatrice()

while True:
    what = input("Quale operazione vuoi effettuare? ")

    if what == "1":
        c.somma()
    elif what == "2":
        c.sottrazione()
    elif what == "3":
        c.moltiplicazione()
    elif what == "4":
        c.divisione()
    else:
        print("Fine procedura")
        break
