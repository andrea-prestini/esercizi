import time
import random

# lista randomica di numeri generata con random.randint,
# estremi e cicli modificabili
nums = [(random.randint(1, 100)) for x in range(100)]

# numero target: il numero che deve essere ottenuto dalla somma
target = 30


def twoSum(lista):
    """Funzione che da una lista numeri trova tutte le coppie la cui somma
    corrisponde al target

    Args:
        lista (int): lista di interi popolata con la funzione random.randint

    Returns:
       risultato: dict{} posizione nella lista nums del complemento al target
    """

# hashmap per ridurre la BigO time della funzione
    hashmpap = {}

    for i in range(len(lista)):
        diff = target - lista[i]
        if diff in hashmpap:
            hashmpap[diff] = i
        else:
            hashmpap[lista[i]] = "vuoto"

    return hashmpap


# utilizzo della funzione e print di alcune informazioni utili
print("Risultato")
# start time for execution
start = time.time()
risultato = twoSum(nums)
print(risultato)
print()
# print numero elementi che soddisfano la sommatoria trovati
print("lunghezza risultato", len(risultato), "elementi")
# print del nummero target che vogliamo ottenere
print("Target:", target)
# scartiamo tutte le voci del dizionario che non hanno
# ottenuto una soluzione, stato "vuoto"
no_empty = {k: v for k, v in risultato.items() if risultato[k] != "vuoto"}

print()
# stampiamo i complementi trovati per poter verificare
# visivamente la bontà del risultato
print("complementi trovati nella lista numeri...")
print("Target number:", target)
for v in no_empty.values():
    print("complemento", nums[v])

# end time for execution
end = time.time()

print()
# print finali di informazione
print("Risultati non vuoti ottenuti", no_empty, sep="\n")
print()
print("Tempo esecuzione", ((end - start) * 1000), "secondi")
