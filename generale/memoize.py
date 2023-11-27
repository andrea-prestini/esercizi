def memoize(func):
    cache = {}
    def inner(*args, **kwargs):
        if args in cache:
            print("ritorno risultati in cache")
            return cache[args]
        res = func(*args, **kwargs)
        cache[args] = res
    return inner

@memoize
def crea_lista(n):
    lista = [x for x in range(n)]
    print("lista completata")
    return lista