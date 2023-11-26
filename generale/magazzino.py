import time


"""Gestione magazzino con verifica dello stock
presente

"""


class Magazzino:
    """classe Magazzino con verifica stock e prelievi

    Attributes:
        stock: int
            quantità di merce presente in magazzino

    Methods:
        add_stuff(self, numero: int):
            aggiunge merce al magazzino
        remove_stuff(self, numero: int):
            rimuove merce dal magazzino
        verify_status(self):
            controlla lo stato del magazzino
    """

    def __init__(self, stock: int) -> None:
        self.stock = stock

    def add_stuff(self, numero: int) -> None:
        self.stock += numero

    def remove_stuff(self, numero: int) -> None:
        if numero <= self.stock:
            self.stock -= numero
            print(f"Ho rimosso {numero} oggetti")
        else:
            print(f"Ho rimosso {self.stock} oggetti su {numero} richiesti")
            self.stock = 0

    def verify_status(self) -> int:
        """funzione per verificare lo stato
        dello stock magazzino (non negativo)

        Returns:
            bool: True o False
            True: se lo stock magazzino è positivo
            False: se lo stock magazzino è negativo
        """

        if self.stock <= 0:
            return False
        else:
            return True


while True:
    response = input("Inserisci il valore di stock magazzino: ")
    try:
        stock = int(response)
        break

    except ValueError:
        print("Non hai inserito un numero!")


obj1 = Magazzino(stock)

lista_prelievi = [10, 40, 60, 30]

for i in lista_prelievi:
    if obj1.verify_status():
        obj1.remove_stuff(i)
        time.sleep(1)
    else:
        print("Magazzino VUOTO!")
        break
