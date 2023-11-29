import time


class Persona:
    def __init__(self, name: str) -> None:
        self.zona = "valle camonica"
        self.name = name

    def __str__(self):
        return f"""
        Sono {self.name}
        e sono in {self.zona}"""

    def set_zona(self, new_zona: str) -> None:
        self.zona = new_zona


obj = Persona("andrea prestini")
obj1 = Persona("mario rossi")

print(obj)

print("fine procedura...")
