import time


var = 'Python'

match var:
    case str():
        print('stringa')
    case bool():
        print('Bool')
    case int():
        print('Intero')
    case _:
        print('Non presente!')

nome = 'andrea'

match nome:
    case 'andrea':
        print('ciao amico mio')
    case 'mario':
        print('benvenuto in valle camonica!')
    case 'federica':
        print('benvenuta nella mia dimora!')
    case _:
        print('Mi dispiace, non ti conosco!')

time.sleep(2)
print(f'Ciao tu che ti chiami {nome}')
