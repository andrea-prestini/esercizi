#!/usr/bin/python3


class FiguraGeo:
    lati = []

    def perimetro(self):
        res = 0
        for lato in self.lati:
            res += lato
        return res

    def area(self):
        return -1


class Triangolo(FiguraGeo):

    def __init__(self, lato1, lato2, lato3):
        self.lati = [lato1, lato2, lato3]


class TriangoloEquil(Triangolo):
    def __init__(self, lato):
        self.lati = [lato, lato, lato]


class Quadrato(FiguraGeo):
    def __init__(self, lato):
        self.lati = [lato] * 4

    def area(self):
        return pow(self.lati[0], 2)


t = Triangolo(3, 5, 1)
te = TriangoloEquil(5)
quad = Quadrato(10)

print("il perimetro del triangolo : ", t.perimetro())
print("il perimetro del triangolo equilatero : ", te.perimetro())
print("il perimentro del quadrato  ", quad.perimetro())
print("l'area del quadrato ", quad.area())
