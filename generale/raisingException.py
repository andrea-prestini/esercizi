
while True:
    try:
        a = int(input("numero: "))
        if 10 < a < 20:
            raise Exception("Valore inserito errato!")
        else:
            print("Valore accettato...")
            break
    except Exception as e:
        print(e)
        continue
