from dataclasses import dataclass


class Prodotto:
    def __init__(self, nome: str, prezzo: float, quantita: float) -> None:
        self.nome = nome
        self.prezzo = prezzo
        self.quantita = quantita

    def total_cost(self):
        return self.prezzo * self.quantita

    def __repr__(self) -> str:
        return (
            f"Prodotto {self.nome}"
            f"prezzo={self.prezzo}"
            f"quantità={self.quantita}"
        )

    def __eq__(self, other):
        if not isinstance(other, Prodotto):
            return NotImplemented
        return (
            self.nome == other.nome
            and self.prezzo == other.prezzo
            and self.quantita == other.quantita
        )


@dataclass
class Prodotto1:
    nome: str
    prezzo: float
    quantita: float

    def total_cost(self):
        return self.prezzo * self.quantita


a1 = Prodotto1("sale", 3, 10)
a2 = Prodotto1("pepe", 1, 3)
print(a1 == a2)
print("spesa totale sale", a1.total_cost())
print("spesa totale pepe", a2.total_cost())
