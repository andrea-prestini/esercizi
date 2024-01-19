from typing import Self


class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def __repr__(self) -> str:
        return f'{self.name} {self.age}'

    def __lt__(self, other: Self) -> bool:
        print("Using: __lt__")
        return self.age < other.age

    def __gt__(self, other: Self) -> bool:
        print("Using: __gt__")
        return self.age > other.age

    def __eq__(self, other: Self) -> bool:
        print("Using: __eq__")
        return self.age == other.age


def main() -> None:
    people: list[Person] = [Person("Bob", 19),
                            Person("James", 22),
                            Person("Maria", 27),
                            Person("X-Machina-Elon-Stop-Doing-This-LOL", 12)]

    print(people[0] < people[1])


if __name__ == "__main__":
    main()
