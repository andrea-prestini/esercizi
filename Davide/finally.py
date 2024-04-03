def prova1():
    while True:
        try:
            raise Exception("Bad idea")
        except Exception:
            print("Breaking")
            break
        finally:
            continue


def prova2() -> int:
    try:
        raise ValueError("Bad value")
    except ValueError:
        print("Errore")
        return 1
    finally:
        return 0


def prova3():
    while True:
        try:
            raise Exception("BAD")
        except Exception:
            print("Breaking")
            break

        continue
