from functools import total_ordering
from typing import Self


@total_ordering
class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def work(self) -> None:
        print(f"{self.name} is working...")

    def eat(self) -> None:
        print(f"{self.name} cannot eat right now, bacause they have to work...")

    def sleep(self) -> None:
        print(f"{self.name} is now sleeping, but dreams about working...")

    def __lt__(self, other: Self) -> bool:
        return (self.name.lower(), self.age) < (other.name.lower(), other.age)


bob: Person = Person("Bob", 35)
luigi: Person = Person("Luigi", 40)

print("bob minore di luigi")
print(bob < luigi)
print()
print("bob uguale a luigi")
print(bob == luigi)
print()
print("bob maggiore di luigi")
print(bob > luigi)
print()
print("bob maggiore uguale di luigi")
print(bob >= luigi)
