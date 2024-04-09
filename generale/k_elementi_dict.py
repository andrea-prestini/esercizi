def estrai_primi_k_elementi(dictionary, k):
    # Ordina il dizionario in base alle chiavi
    dizionario_ordinato = dict(sorted(dictionary.items()))

    # Estrai i primi k elementi
    primi_k_elementi = {k: dizionario_ordinato[k]
                        for k in list(dizionario_ordinato)[:k]}

    return primi_k_elementi


# Esempio di utilizzo
dizionario_casuale = {'b': 2, 'c': 3, 'a': 1, 'e': 5, 'd': 4}
k = 3

primi_k_elementi = estrai_primi_k_elementi(dizionario_casuale, k)
print("Primi", k, "elementi:", primi_k_elementi)
