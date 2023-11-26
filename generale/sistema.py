import os
import time


cwd = os.getcwd()
directory = os.listdir()
nome = os.path.exists(("pomodoro.txt"))

# Elenco mie liste disponibili
lista1 = ["andrea", "eleonora", "roberto", "federica"]
lista2 = ["breno", "gambara", "leno", "darfo"]
lista3 = ["lombardia", "veneto", "lazio", "umbria"]


def cerca_file(file_da_cercare: str):
    """Cerco il file passato come parametro
    Args:
        file_da_cercare str: il nome del file che deve essere cercato nel path
    """
    if os.path.exists(file_da_cercare):
        print(f"file {file_da_cercare} presente nel sistema")
    else:
        print(f"il file {file_da_cercare} NON esiste nel sistema!")
        time.sleep(2)
    scrivi_lista(file_da_cercare)


def scrivi_lista(file_da_cercare):
    """Scrivo, se richiesto, una lista passata come
    parametro al file non presente
    nel path e poi creato come richiesto

    Args:
        file_da_cercare (): il file che creato nel
        path deve essere scritto con la lista scelta
    """
    if input("Vuoi scrivre la tua lista? (y/n) ") == "y":
        lista_da_stampare = input("Quale lista vuoi inserire? ")
        open(file_da_cercare, "a").close()
        print(f"ho creato il file {file_da_cercare}")
        time.sleep(2)
        print("Inserisco la tua lista nel file...")
        time.sleep(2)

        with open(file_da_cercare, "a") as f:
            for val in globals()[lista_da_stampare]:
                f.write("%s\n" % val)
        print("ho finito la scrittura sul file!")
    else:
        print("OK hai deciso di NON creare il file mancante!")


cerca_file("pippo.txt")
