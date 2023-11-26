import time
# import numpy as np

lista1 = [1, 1, 1, 1, 1]
lista2 = [2, 2, 2, 2, 2]
lista3 = [3, 3, 3, 3, 3]


class Persona:
    '''classe persona'''

    def __init__(self) -> None:
        time.sleep(2)


def miaFunzione():
    '''ritorna lista'''
    return lista1


# print(np.random.randint(1, 100, 2))
print(__import__('numpy').random.randint(1, 100, 3))
__import__('pprint').pprint(globals())
