class Animale:
    pelo = "lungo"
    zampe = 4
    verso = "bau"
    tipo = "animale"

    def __init__(self):
        print("inizializzo classe " + self.tipo)

    def __repr__(self):
        res = "Animale: %s\nZampe %d\nVerso %s" % (
            self.tipo, self.zampe, self.verso)
        print(res)

    def __del__(self):
        print("fine classe " + self.tipo)

    def __str__(self):
        return "il %s fa %s" % (self.tipo, self.verso)


class Cane(Animale):
    tipo = "cane"
    verso = "bau"


class Gatto(Animale):
    tipo = "gatto"
    verso = "miao"


c = Cane()
print(str(c))
