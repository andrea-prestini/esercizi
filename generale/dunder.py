class Fruit:
    def __init__(self, *, name: str, grams: float) -> None:
        self.name = name
        self.grams = grams

    def __format__(self, format_spec: str) -> str:
        if format_spec == "kg":
            return f"{self.grams / 1000:.2f} kg of {self.name}"
        if format_spec == "hg":
            return f"{self.grams / 100:.2f} hg of {self.name}"
        else:
            raise ValueError("Unknow format specification...")


f1 = Fruit(name="apple", grams=2300)

print(f"{f1.name} is {f1:kg}")
print(f"{f1.name} is {f1:hg}")
# print(f"{f1.name} is {f1}")
