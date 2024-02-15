class Calcolatrice:
    print("Benvenuto nella nostra calcolatrice!")
    print("1- Somma")
    print("2- Sottrazione")
    print("3- Moltiplicazione")
    print("4- Divisione")

    @staticmethod
    def inserimento():
        x = int(input("Inserisci il primo numero: "))
        y = int(input("Inserisci il secondo numero: "))
        return x, y

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
