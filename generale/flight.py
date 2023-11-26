class Flight:
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)


obj1 = Flight(3)

persons = ["uno", "due", "tre", "quattro"]

for person in persons:
    success = obj1.add_passenger(person)
    if success:
        print(f"Added {person} to flight successfully.")
    else:
        print(f"No available seats for {person}.")
