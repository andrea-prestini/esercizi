import random
import sys
import heapq
import time

max_estremo = 10_000_000
max_nums = 10_000_000

lista1 = [random.randint(1, max_nums) for x in range(max_estremo)]
lista2 = [random.randint(1, max_nums) for x in range(max_estremo)]
print("dimensione lista1", sys.getsizeof(lista1) / 1024, "KB")
print("dimensione lista2", sys.getsizeof(lista2) / 1024, "KB")

# tranforme lists into heaps
heapq.heapify(lista1)
heapq.heapify(lista2)
print()
print("dimensione dopo trasformazione in heap")

print("dimensione lista1", sys.getsizeof(lista1) / 1024, "KB")
print("dimensione lista2", sys.getsizeof(lista2) / 1024, "KB")
print()
print("Effettuiamo il test di velocità sulle due data structures")
# test min lista standard
start = time.perf_counter()
minimo1 = min(lista1)
print("minimo lista1:", minimo1)
end = time.perf_counter()
print("tempo esecuzione min lista1", (end - start) * 1000)

print()
print()


start = time.perf_counter()
print("minimo lista2:", lista2[0])
end = time.perf_counter()
print("tempo esecuzione min lista2", (end - start) * 1000)
