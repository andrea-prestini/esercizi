import time
import os

lista = []
nomeFile = ""

path = os.path.dirname(os.path.abspath(__file__))
# path = os.path.dirname(__file__) è equivalente
os.chdir(path)
print("Ci troviamo nella directory", os.path.dirname(__file__))
time.sleep(5)


def creaLista():
    # crea la lista da portare sul file

    print("digita X per concludere la procedura!")
    while True:
        elemento = input(
            "cosa vuoi aggiungere alla lista? (X per terminare)\n")
        if elemento == "X":
            break
        else:
            lista.append(elemento)
    risposta = input("scrivo la lista nel file locale? (y/n)\n")
    if risposta == "y":
        scriviFile()
        time.sleep(2)
        print("ho scritto la lista nel file creato")
        time.sleep(1)
        risposta = input("vuoi aggiungere elementi alla lista?\n")
        if risposta == "si":
            creaLista()
        else:
            print("arrivederci")
    else:
        print("Arrivederci e grazie...")


def creaFile():
    # crea il file su cui scrivere la lista

    global nomeFile

    creaFile = input(
        "vuoi creare un nuovo file? si per iniziare, altro per terminare\n")
    if creaFile == "si":
        nomeFile = input("come vuoi chiamare il nuovo file?\n")
        time.sleep(2)
        print("ho creato il file " + nomeFile)
        creaLista()
    else:
        print("arrivederci e grazie")


def scriviFile():
    # scrive la lista nel file creato

    global nomeFile

    with open(nomeFile, "w") as f:
        for riga in lista:
            f.write(str(riga)+"\n")


creaFile()
