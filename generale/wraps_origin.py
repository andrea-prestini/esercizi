from functools import wraps


def pulsante(fnc):
    return funzione1

def funzione1():
    return "funzione 1"


def funzione2():
    return "funzione 2"

@pulsante
def funzione3():
    return "funzione 3"


# print("funzione 1", funzione1())
# print("funzione 2", funzione2())
# print("accartoccio funzione 3", funzione3())

def mapper(fnc):
    @wraps(fnc)
    def inner(lista):
        return [fnc(val) for val in lista]
    return inner


@mapper
def camelcase(s) -> str:
    """Genera una lista di parole con prima lettera maiuscola da una stringa passata"""
    return " ".join([word.capitalize() for word in s.split("-")])


names = [
    "primo-elemento-funzione",
    "secondo-elemento-funzione",
    "terzo-elemento-funzione",
]


print(camelcase(names))
print(camelcase.__doc__)
