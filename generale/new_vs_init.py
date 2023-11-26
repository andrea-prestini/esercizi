import time


class Connection:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            print('Connecting...')
            cls._instance = super().__new__(cls)
            return cls._instance
        else:
            print('WARNING: already connected!')


print('Creo connessione 1')
time.sleep(1)
conn1 = Connection()
time.sleep(1)
print('Creo connessione 2')
time.sleep(1)
conn2 = Connection()
print('-' * 50)


class Vehicle:
    def __new__(cls, wheels: int):
        if wheels == 2:
            return Motorbike()
        elif wheels == 4:
            return Car()
        else:
            return super().__new__(cls)

    def __init__(self, wheels) -> None:
        self.wheels = wheels
        print(f'Initializing vehicle with {self.wheels} wheels')


class Motorbike:
    def __init__(self) -> None:
        print('Initializing motorbike')


class Car:
    def __init__(self) -> None:
        print('Initializing Car')


uno = Vehicle(2)
time.sleep(1)
due = Vehicle(4)
time.sleep(1)
tre = Vehicle(3)
