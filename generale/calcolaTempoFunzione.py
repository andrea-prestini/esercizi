import time

def calc_time(func):
    def inner(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(
f'''
La funzione ha impiegato 
    {end - start:.5f} secondi
per essere eseguita''')
        return res
    return inner

@calc_time
def produce_lista(n):
    import sys
    lista = [x for x in range(n)]
    return f'''
    {sys.getsizeof(lista):,} <- lista in byte'''


print(produce_lista(10000000))