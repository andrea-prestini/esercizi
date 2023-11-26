from functools import wraps
from time import time


def durata_esecuzione(funzioneparametro):
    @wraps(funzioneparametro)
    def wrapper(*args, **kwargs):
        start = round(time() * 1000, 3)
        try:
            return funzioneparametro(*args, **kwargs)
        finally:
            end_ = round(time() * 1000, 3) - start
            print(f'Tempo esecuzione:, {end_ if end_ > 0 else 0} ms')

    return wrapper
