def moltiplicatore():
    try:
        a = int(input("valore a: "))
        b = int(input("valore b: "))
        risultato = a * b
        print(risultato)
    except ValueError as text:
        print(f"C'è stato un errore {text}!")
        print("Solo caretteri numerici, grazie!")
    finally:
        print("chiudo l'applicazione")

moltiplicatore()