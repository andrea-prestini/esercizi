import time


class Oggetto:
    def __init__(self, nome, stato="Spento"):
        self.nome = nome
        self.stato = stato

    def accendi(self):
        self.stato = "Acceso"
        print(f"Oggetto {self.nome} acceso")

    def spegni(self):
        self.stato = "Spento"
        print(f"Oggetto {self.nome} spento")

    def get_stato(self):
        print(f"Stato {self.nome.upper()}: {self.stato}")


class Casa:
    @classmethod
    def crea_oggetti_da_lista(cls, lista_oggetti):
        oggetti_creati = []
        for oggetto in lista_oggetti:
            nuovo_oggetto = Oggetto(oggetto.lower())
            oggetti_creati.append(nuovo_oggetto)
        return oggetti_creati


# Esempio di utilizzo:
lista_oggetti_casa = ["Lampada", "Televisore",
                      "Frigorifero", "Asciugatrice", "Finestra"]

for oggetto in Casa.crea_oggetti_da_lista(lista_oggetti_casa):
    oggetto.get_stato()
    time.sleep(1)
    oggetto.accendi()
    time.sleep(1)
    oggetto.get_stato()
    time.sleep(1)
    oggetto.spegni()
    time.sleep(1)
    oggetto.get_stato()
    print("\n")
