from contextlib import contextmanager


@contextmanager
def managed_file(name):
    try:
        print(f'Opening {name} in reading mode...')
        f = open(name, "r")
        yield f
    finally:
        print(f'Closed {name} file...')
        f.close()


with managed_file("./elenco.txt") as f:
    print(f.read())
