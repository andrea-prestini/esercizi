# Polimorfismo in python


class Persiano:
    def miagola(self):
        print('Il mio persiano miagola')

    def graffia(self):
        print('Il mio persiano non graffia')


class Siamese:
    def miagola(self):
        print('Il mio siamese non miagola')

    def graffia(self):
        print('Il mio siamese graffia')


# interfaccia comune
def evento1(gatto):
    gatto.miagola()


def evento2(gatto):
    gatto.graffia()


# istanza degli oggetti
andrea = Persiano()
simone = Siamese()


# passaggio degli oggetti all'interfaccia comune
evento1(andrea)
evento1(simone)
print()
evento2(andrea)
evento2(simone)
