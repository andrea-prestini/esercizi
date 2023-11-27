anni = int(input("quanti anni hai?\n"))
patente = input("hai la patente?\n")

print(f"hai {anni}, e la patente è {patente}")
print(type(anni), type(patente))

if anni >= 18 and patente == "si":
    print("puoi noleggiare una Ferrari")
elif anni >= 18 and patente != "si":
    print("mi dispiace non hai la patente")
elif anni < 18 and patente == "si":
    print("bugia, non puoi avere la patente se non hai 18 anni!")
else:
    print("sei piccolo e non hai la patente!")
