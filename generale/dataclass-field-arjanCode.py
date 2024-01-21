import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    return "".join(random.choices(string.ascii_uppercase, k=12))


@dataclass(frozen=False)  # Default value if True error in post init
class Person:
    name: str
    address: str
    active: bool = True
    email_adresses: list[str] = field(default_factory=list)
    id: str = field(default_factory=generate_id)
    _search_string: str = field(init=False, repr=False)

    def __post_init__(self) -> None:
        self._search_string = f"{self.name} {self.address}"


if __name__ == "__main__":
    person1 = Person(name="andrea", address="via Pioppi, Esine")
    person2 = Person(
        name="federica", address="via Lago, Sirmione", active=False)
    print(person1)
    print()
    print(person2)
