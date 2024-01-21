name = "sara"

# Sintassi che genera un errore, viene garantito accesso a nome errato!


def test1(var):
    if var == "andrea" or "giovanni" or "federica":
        print("Access Granted!")
    else:
        print("Access Denied!")


# Sintassi corretta
def test2(var):
    if var in ["andrea", "giovanni", "federica"]:
        print("Access Granted!")
    else:
        print("Access Denied!")


test1(name)
test2(name)
