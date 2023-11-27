lista = ["andrea", "eleonora", "roberto", "simone"]

def mia_funzione(lista):
    output = ["amico " + val for val in lista]
    return output
        
print(mia_funzione(lista) if input("Come ti chiami? ") == "andrea" else "Mi dispiace non ti conosco...")
print("-" * 30)

print(mia_funzione(lista) if input("Chi sei? ") in lista else "Arrivederci")