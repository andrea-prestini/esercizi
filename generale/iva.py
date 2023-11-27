#!/usr/bin/python3


def debug(txt):
    print(txt)


def aggiunta_iva(valore, iva):
    """
    aggiunta iva al valore ==> lordo
    prende l'importo "valore" e restituisce
    l'importo al lordo di iva"""
    return valore * (1 + iva / 100)


def togli_iva(valore, iva):
    return valore * (1 - iva / 100)


def leggi_valori():
    valore = int(input("quale valore vuoi utilizzare?\n"))
    iva = int(input("inserisci il valore dell'iva\n"))
    return (valore, iva)


func = None


def scelta_opzione():
    risposta = input("quale operazione vuoi effettuare? 1- aggiunta 2- scorporo\n")
    if risposta == "1":
        debug("aggiunta")
        func = aggiunta_iva
    elif risposta == "2":
        debug("scorporo")
        func = togli_iva
    else:
        print("Paramentro non valido!")
        exit()
    if func:
        valore, iva = leggi_valori()
        return func(valore, iva)


print(scelta_opzione())
