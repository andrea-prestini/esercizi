import pandas as pd


df = pd.DataFrame(
    {
        'A': range(1, 6),
        'B': range(10, 0, -2),
        'C': range(10, 5, -1),
    }
)

query_uno = df.query('A > B')
classico_uno = df[df.A > df.B]

print('metodo query della libreria pandas')
print(query_uno)
print('metodo classico')
print(classico_uno)
