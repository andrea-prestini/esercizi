from varname import nameof


uno = [1, 10, 100, 1000]
due = [2, 20, 200, 2000]
print(type(uno), nameof(uno))


lista = ["uno", "due", "tre", "quattro", "cinque"]


for val in lista:
    if val not in globals():
        exec(f"{val} = [3]")


print(f"""
uno: {uno}
due: {due}
tre: {tre}
quatro: {quattro}
cinque: {cinque}
""")
