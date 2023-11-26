from functools import wraps


def caramella(funzioneparamentro):
    @wraps(funzioneparamentro)
    def wrapper(*args, **kwargs):
        return funzioneparamentro(*args, **kwargs).upper()

    return wrapper


def stampa_nome(n: str) -> str:
    return n


stampa_decorata = caramella(stampa_nome)

print(stampa_nome('andrea'))
print(stampa_decorata('mario'))
