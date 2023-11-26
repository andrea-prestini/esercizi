import time


class Persona:
    def __init__(self, nome, cognome, zona) -> None:
        self.nome = nome
        self.cognome = cognome
        self.zona = zona

    @property
    def get_zona(self):
        return self.zona

    @get_zona.setter
    def get_zona(self, new):
        print("Assegno proprietà zona con il nuovo valore")
        time.sleep(2)
        self.zona = new
        return f"La zona richiesta è {self.zona}"

    @get_zona.deleter
    def get_zona(self):
        print("Cancello proprietà zona")
        time.sleep(2)
        del self.zona


obj1 = Persona("andrea", "prestini", "gambara")
obj1.get_zona = "Valle Camonica"

print(obj1.get_zona)
