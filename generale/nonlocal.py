def init_count():

    count = 0

    def add(amount):
        nonlocal count
        count += amount
        return count

    def get_count():
        return count

    return add, get_count


# unpacking del return funzione init_count
# uno = add, due = get_count
uno, due = init_count()

# chiamata funzione add per 2 volte
uno(10)
uno(20)

# chiamata funzione get_count ottenendo il valore attuale di count
print(due())
