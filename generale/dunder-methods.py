import time


class Fruit:
    def __init__(self, name: str) -> None:
        self.name = name

    def __mul__(self, other: int) -> str:
        return self.name * other

    def __call__(self, x: int) -> None:
        i = 0
        while i <= x:
            stringa = "{} - {}".format(self.name, i)
            i += 1
            print(stringa)
            time.sleep(1)


banana: Fruit = Fruit("Banana")
arancia: Fruit = Fruit("Arancia")

banana(3)
