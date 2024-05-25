import time


class Persona:
    def __init__(self, nome: str, cognome: str) -> None:
        self.nome = nome
        self.cognome = cognome

    def scheda(self):
        print(f"il mio nome è {self.nome.capitalize()}")
        time.sleep(1)
        print(f"il mio cognome è {self.cognome.capitalize()}")

    def stampa(self):
        class Stampa:
            def __init__(self) -> None:
                print("sono la classe stampa di Persona")

            def uno(self):
                print("sono uno")

            def due(self):
                print("sono due")

            def tre(self):
                print("sono tre")

            def quattro(self):
                class Colori:
                    def __init__(self) -> None:
                        print("Sono la classe Colori del metodo quattro di Persona")

                    def rosso(self):
                        print("sono il colore rosso")

                    def blu(self):
                        print("sono il colore blu")

                    def giallo(self):
                        print("sono il colore giallo")

                    def verde(self):
                        print("sono il colore verde")

                return Colori()

        return Stampa()


p1 = Persona("andrea", "prestini")
p1.scheda()

print()
p1.stampa().quattro().rosso()
