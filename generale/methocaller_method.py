from operator import methodcaller


names = ["Bob", "James", "Billy", "Sandra", "Blake"]


starts_with_b = methodcaller = methodcaller("startswith", "B")


filtered = filter(starts_with_b, names)

print(list(filtered))
