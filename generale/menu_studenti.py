import os

studenti = []
voti = []

while True:
    print(f'''
    1. inserisci studente
    2. inserisci media
    3. stampa tutto
    4. calcola media classe
    5. Esci''')

    op = int(input("Inserisci operazione\n"))
    os.system("clear")

    # opzione inserimento studente
    if op == 1:
        os.system("clear")
        nc = input('inserisci nome e cognome studente\n')
        studenti.append(nc)
        voti.append(-1)

    # opzione inserimento media studente da nome
    if op == 2:
        os.system("clear")
        nc = input("inserisci nome e cognome\n")
        if nc in studenti:
            i = studenti.index(nc)
            media = float(input("inserisci media: "))
            if media > 30 or media < 18:
                print("Valore errato, attenzione")
            else:
                voti[i] = media
        else:
            print(f'studente: {nc} non presente!')

    # opzione stampa elenco studenti e medie personali
    if op == 3:
        os.system("clear")
        for idx, val in enumerate(studenti):
            print(f'nome: {studenti[idx]}, media: {voti[idx]}')

    # calcolo e stampa valore media della classe 2 decimali
    if op == 4:
        studenti_voto = 0
        voti_validi = 0
        os.system("clear")
        for st in voti:
            if st != -1:
                voti_validi += st
                studenti_voto += 1
        print(f'''
        la media della classe è:
        {voti_validi/studenti_voto:.2f}''')

    # opzione uscita dal ciclo while
    if op == 5:
        break
