class Foo:
    scatola = 0

    def __init__(self, val) -> None:
        self.val = val
        Foo.scatola += 1

    def __str__(self) -> str:
        return "Foo [%s]" % self.val

    # def __mul__(self, other):
    #     return Foo(self.val * other.val)


class Bar:
    def __init__(self, val) -> None:
        self.val = val

    def __str__(self) -> str:
        return "Bar [%s]" % self.val

    def __rmul__(self, other):
        return Bar(self.val * other.val)


# Drive code
f = Foo(3)
b = Bar(6)

# risultato = f * b # usando mul in Foo
risultato1 = f * b  # usando rmul in Bar
print(risultato1)
