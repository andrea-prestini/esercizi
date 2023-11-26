from functools import partial


def multiply(a: float, b: float, name: str | None = None) -> float:
    if name:
        print(f'\n{name} (a:{a} b:{b})')
    return a * b


double = partial(multiply, 2, name='double')
triple = partial(multiply, 3, name='triple')


print(double(10))
print(triple(10))
