import time


class Capannone:
    def __init__(self, capacity) -> None:
        self.capacity = capacity

    def get_from_store(self, number):
        if number <= self.capacity:
            self.capacity -= number
            print(f"prelevato {number} pezzi su {number} richiesti...")
        else:
            print(f"prelevato {self.capacity} pezzi su {number} richiesti...")
            self.capacity = 0


obj = Capannone(100)

scarico = [10, 30, 70, 70]

for val in scarico:
    obj.get_from_store(val)
    time.sleep(1)
