
"""
    Versione con class method
"""


class SingletonLogger:

    _instance = None

    def __init__(self) -> None:
        raise RuntimeError("This is Singleton, invoke by get instance()")

    @classmethod
    def get_istance(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
        return cls._instance


"""
Versione con staticmethod
"""


class PersonSingleton:

    __instance = None

    @staticmethod
    def get_instance():
        if PersonSingleton.__instance is None:
            PersonSingleton("Default name", 0)
        return PersonSingleton.__instance

    def __init__(self, name, age) -> None:
        if PersonSingleton.__instance is not None:
            raise Exception("Singletone solo one time!")
        else:
            self.name = name
            self.age = age
            PersonSingleton.__instance = self


"""
Versione con Andrey Ivanov
"""


class SingletoneIvanov():

    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance


"""
Versione di ArjanCodes
"""


class SingletonArjan(type):

    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super().__call__(*args, **kwargs)
        return cls._instance[cls]


class Logger(metaclass=SingletonArjan):
    def log(self, msg):
        print(msg)


# logger1 = Logger()
# logger2 = Logger()
# logger1.log("ciao")
# logger2.log("Arrivederci")

" hanno la stessa posizione di memoria, sono  lo stesso oggetto"
# print(logger1)
# print(logger2)


"""POOL reusable object"""


class Reusable:
    def test(self):
        print(f'Using object {id(self)}')


class ReusablePool:

    def __init__(self, size) -> None:
        self.size = size
        self.in_use = []
        self.free = []
        for _ in range(size):
            self.free.append(Reusable())

    def acquire(self):
        if len(self.free) <= 0:
            raise Exception("No more objects are available")
        r = self.free[0]
        self.free.remove(r)
        self.in_use.append(r)
        return r

    def release(self, r):
        self.in_use.remove(r)
        self.free.append(r)


pool = ReusablePool(2)
r1 = pool.acquire()
r2 = pool.acquire()
r1.test()
r2.test()
