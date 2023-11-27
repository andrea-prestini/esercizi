"""  
   a decorator doesn't need to replace one funciton with another function. It can 
   also replace a funciton with a callable clas instance. Doing so allow you to
   add propertiews and even methods to the decorated function!
"""

# create an @Elephant decorator wich remembers all the return values of the decorated function

import random


class Elephant:
    def __init__(self, fnc) -> None:

        self.__fnc = fnc
        self.__memory = []


    def __call__(self):

        retval = self.__fnc()
        self.__memory.append(retval)

        return retval

    def memory(self):
        return self.__memory




@Elephant # usiamo il maiuscolo per indicare che non è solo decoratore ma anche classe!
def random_odd_digit():

    return random.choice([1, 3, 5, 7, 9])


print(random_odd_digit())
print(random_odd_digit.memory())
print(random_odd_digit())
print(random_odd_digit.memory())
print(random_odd_digit())
print(random_odd_digit.memory())