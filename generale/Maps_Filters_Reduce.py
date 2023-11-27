import math

def area(r):
    return math.pi * (r**2)


radii = [2,5,7.1, 0.3, 10]

#metodo DIRETTO:
areas = []
for r in radii:
    a = area(r)
    areas.append(a)
print(areas)

#metodo MAP:
#print(map(area, radii)) ATTENZIONE produce errore perchè MAP non è una lista!

print(list(map(area, radii)))
print(list(filter(lambda x: x > 5, radii)))

stati = ["asia", "", "america", "europa"]
print(list(filter(None, stati)))#il campo vuoto viene filtrato e cancellato