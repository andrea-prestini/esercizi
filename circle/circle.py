from math import pi


def circle_area(r):
    if r < 0:
        raise ValueError('radius must be positive')

    if type(r) not in [int, float]:
        raise TypeError('radius must be a non negative real number')
    return pi * (r**2)
