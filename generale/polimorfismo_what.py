class Auto:
    def assegna_valore(self, valore):
        self.valore = valore
        return valore * 1000


class Moto:
    def assegna_valore(self, valore):
        self.valore = valore
        return valore * 1000


class Slitta:
    def assegna_valore(self, valore):
        self.valore = valore
        return valore * 1000


def quanto_spendi(mezzo, valore):
    print(mezzo.assegna_valore(valore))


uno = Auto()
due = Moto()
tre = Slitta()
quanto_spendi(uno, 111)
quanto_spendi(due, 222)
quanto_spendi(tre, 333)
