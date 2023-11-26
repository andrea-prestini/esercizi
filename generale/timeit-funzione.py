from timeit import timeit


def miaFunzione(intervallo: int):
    risultato = 0
    for i in range(intervallo):
        risultato += i
    return risultato


numero = 100
miaFunzione_time = timeit(
    'miaFunzione(numero)', globals=globals(), number=10000000
)

print('tempo di esecuzione', round(miaFunzione_time, 2))
print('il risultato è:', miaFunzione(numero))
