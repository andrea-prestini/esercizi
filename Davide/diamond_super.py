# Definizione della classe base Padre
class Padre:
    def __init__(self) -> None:
        print("Sono il padre")

# Definizione della classe Figlio1 che eredita da Padre


class Figlio1(Padre):
    def __init__(self) -> None:
        print("sono il figlio 1")
        # Chiamata al costruttore della classe base per
        # stampare il messaggio del padre
        super().__init__()

# Definizione della classe Figlio2 che eredita da Padre


class Figlio2(Padre):
    def __init__(self) -> None:
        print("Sono il figlio 2")
        # Chiamata al costruttore della classe
        # base per stampare il messaggio del padre
        super().__init__()

# Definizione della classe Parenti che eredita da Figlio1 e Figlio2


class Parenti(Figlio1, Figlio2):
    def __init__(self) -> None:
        print("Sono i parenti")
        super().__init__()  # Chiamata al costruttore della classe
        # base per stampare il messaggio del padre
        # attraverso la gerarchia di ereditarietà


# Creazione di un'istanza della classe Parenti
p1 = Parenti()

# Separatore per distinguere le due versioni nel output
print("-" * 100)

# Definizione della classe base Padre10


class Padre10:
    def __init__(self) -> None:
        print("Sono il padre 10")

# Definizione della classe Figlio10 che eredita da Padre10


class Figlio10(Padre10):
    def __init__(self) -> None:
        print("sono il figlio 10")
        # Chiamata esplicita al costruttore della classe base
        Padre10.__init__(self)

# Definizione della classe Figlio20 che eredita da Padre10


class Figlio20(Padre10):
    def __init__(self) -> None:
        print("Sono il figlio 20")
        # Chiamata esplicita al costruttore della classe base
        Padre10.__init__(self)

# Definizione della classe Parenti10 che eredita da Figlio10 e Figlio20


class Parenti10(Figlio10, Figlio20):
    def __init__(self) -> None:
        print("Sono i parenti 10")
        # Chiamata esplicita al costruttore di Figlio10
        Figlio10.__init__(self)
        # Chiamata esplicita al costruttore di Figlio20
        Figlio20.__init__(self)


# Creazione di un'istanza della classe Parenti10
p10 = Parenti10()
