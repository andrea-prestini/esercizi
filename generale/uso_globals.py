squadra = []


class Persona:
    def __init__(self, nome, cognome) -> None:
        self.nome = nome
        self.cognome = cognome
        self.reparto = "Da assegnare..."

    # def __str__(self) -> str:
    #     return f"""
    #     Questo è il metodo str:
    #     nome: {self.nome}
    #     cognome: {self.cognome}
    #     reparto: {self.reparto}
    #     """
    #
    # def __repr__(self) -> str:
    #     return f"""
    #     Questo è il metodo repr:
    #     nome: {self.cognome}
    #     cognome: {self.cognome}
    #     reparto: {self.reparto}
    #     """


class Operaio(Persona):
    def __init__(self, istanza, nome, cognome) -> None:
        super().__init__(nome, cognome)
        self.istanza = istanza
        self.reparto = "Produzione"
        squadra.append(self.istanza)


class Amministrazione(Persona):
    def __init__(self, istanza,  nome, cognome) -> None:
        super().__init__(nome, cognome)
        self.istanza = istanza
        self.reparto = "Contabilità"
        squadra.append(self.istanza)


obj1 = Operaio("obj1", "roberto", "tanzini")
obj2 = Amministrazione("obj2", "eleonora", "favagrossa")
obj3 = Persona("andrea", "prestini")

# print(obj1)
# print(repr(obj1))
print(globals())
