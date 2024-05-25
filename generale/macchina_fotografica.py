import time


class Obiettivo:
    """
    Classe che rappresenta un obiettivo di una macchina fotografica.

    Attributi:
        apertura (float): L'apertura del diaframma dell'obiettivo.
        tempo (float): Il tempo di scatto.
    """

    def __init__(self, apertura=2.8, tempo=1.0):
        """
        Inizializza un obiettivo con valori predefiniti per apertura e tempo di scatto.

        Args:
            apertura (float): Il valore iniziale dell'apertura del diaframma. Default è 2.8.
            tempo (float): Il valore iniziale del tempo di scatto in secondi. Default è 1.0.
        """
        self.apertura = apertura
        self.tempo = tempo

    def open(self):
        """
        Aumenta l'apertura del diaframma dell'obiettivo di 1.2 unità.
        """
        print("Valore attuale diaframma:", self.apertura)
        time.sleep(1)
        print("apro il diaframma del mio obiettivo")
        self.apertura += 1.2
        time.sleep(1)
        print(f"adesso l'obiettivo ha apertura {self.apertura}")

    def close(self):
        """
        Riduce l'apertura del diaframma dell'obiettivo di 1.2 unità.
        """
        print("Valore attuale diaframma:", self.apertura)
        time.sleep(1)
        print("chiudo il diaframma del mio obiettivo")
        self.apertura -= 1.2
        time.sleep(1)
        print(f"adesso l'obiettivo ha apertura {self.apertura}")

    def increase_tempo(self):
        """
        Aumenta il tempo di scatto di 0.2 secondi.
        """
        print("Valore attuale tempo di scatto:", self.tempo, "sec")
        time.sleep(1)
        print("aumento il tempo di scatto")
        self.tempo += 0.2
        time.sleep(1)
        print(f"adesso il tempo di scatto è {self.tempo} sec")

    def decrease_tempo(self):
        """
        Riduce il tempo di scatto di 0.2 secondi.
        """
        print("Valore attuale tempo di scatto:", self.tempo, "sec")
        time.sleep(1)
        print("diminuisco il tempo di scatto")
        self.tempo -= 0.2
        time.sleep(1)
        print(f"adesso il tempo di scatto è {self.tempo} sec")

    def stato_obiettivo(self):
        """
        Mostra lo stato attuale dell'obiettivo (apertura e tempo di scatto).
        """
        print(f"hai un obiettivo con diaframma {self.apertura}")
        time.sleep(1)
        print(f"il tempo di scatto è {self.tempo} sec")


class Corpo:
    """
    Classe che rappresenta il corpo di una macchina fotografica.

    Attributi:
        nome (str): Il nome del corpo macchina.
        obiettivo (Obiettivo): Un'istanza della classe Obiettivo.
    """

    def __init__(self, nome: str) -> None:
        """
        Inizializza un corpo macchina con un nome specifico e un obiettivo.

        Args:
            nome (str): Il nome del corpo macchina.
        """
        self.nome = nome
        self.obiettivo = Obiettivo()  # Inizializziamo un obiettivo

    def scheda(self):
        """
        Mostra la scheda tecnica del corpo macchina e lo stato dell'obiettivo.
        """
        print("Stai usando il corpo:", self.nome)
        print("_" * 70)
        self.obiettivo.stato_obiettivo()

    def shutter(self):
        """
        Simula lo scatto di una foto con la macchina fotografica.
        """
        time.sleep(1)
        print("scatto la foto con la macchina...")
        time.sleep(2)
        print("Foto SCATTATA!")


# Esempio d'uso:
camera = Corpo("Canon5D")
camera.scheda()
print()
camera.obiettivo.open()
print()
camera.obiettivo.stato_obiettivo()
print()
camera.obiettivo.close()
print()
camera.obiettivo.stato_obiettivo()
print()
camera.obiettivo.increase_tempo()
print()
camera.obiettivo.stato_obiettivo()
print()
camera.obiettivo.decrease_tempo()
print()
camera.shutter()
print()
camera.obiettivo.stato_obiettivo()
print("-" * 70)
print("fine procedura di scatto...")
