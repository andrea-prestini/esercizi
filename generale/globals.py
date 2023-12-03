from varname import nameof


uno = [10]
print(type(uno), nameof(uno))


lista = ["uno", "due", "tre"]


for val in lista:
    if val not in globals():
        globals()[val] = [3]

print(f"""
    uno: {uno}
    due: {due}
    tre: {tre}
""")
