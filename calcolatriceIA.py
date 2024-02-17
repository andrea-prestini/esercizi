class Calcolatrice:
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b

    @staticmethod
    def somma(a, b):
        return a + b

    @staticmethod
    def sottrazione(a, b):
        return a - b

    @staticmethod
    def moltiplicazione(a, b):
        return a * b

    @staticmethod
    def divisione(a, b):
        try:
            return a / b
        except ZeroDivisionError:
            print("Non posso dividere per ZERO!")

    @classmethod
    def calcola(cls):
        status = ["1", "2", "3", "4"]

        while True:
            print("Scegli l'operazione da eseguire:")
            print("1- Somma")
            print("2- Sottrazione")
            print("3- Moltiplicazione")
            print("4- Divisione")

            response = input("Quale operazione vuoi eseguire? ")

            if response not in status:
                print("Arrivederci e grazie!")
                break

            try:
                a = int(input("Inserisci il primo numero: "))
                b = int(input("Inserisci il secondo numero: "))

                if response == "1":
                    print("Somma:", cls.somma(a, b))
                elif response == "2":
                    print(("Sottrazione:", cls.sottrazione(a, b)))
                elif response == "3":
                    print("Moltiplicazione:", cls.moltiplicazione(a, b))
                elif response == "4":
                    print("Divisione:", cls.divisione(a, b))
                else:
                    print("Operazione non valida!")
            except ValueError:
                print("I valori inseriti devono essere numeri!")


# Lanciamo la nostra classe calcolatrice
Calcolatrice.calcola()
