class File:
    def __init__(self, name) -> None:
        self.name = name

    def __enter__(self):
        print(f'Opening {self.name} in reading mode...')
        print()
        self.file = open(self.name, "r")
        return self.file

    def __exit__(self, type, val, trackback):
        if self.file:
            self.file.close()
            print("-" * 50)
            print(f'file {self.name} closed...')

with File("./elenco.txt") as f:
    print(f.read())