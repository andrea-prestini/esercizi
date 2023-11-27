import sys
import time

numero = 1000000
numbers = [x for x in range(numero)]

trasformato1 = [x ** 2 +1 for x in numbers if (x ** 2 +1) % 2 == 0]
trasformato2 = (x ** 2 +1 for x in numbers if (x ** 2 +1) % 2 == 0)

t1 = time.process_time()
print(sum(trasformato2))
print(time.process_time()-t1)
print()
t2 = time.process_time()
print(sum(trasformato1))
print(time.process_time()-t2)
print("memory used:")
print(sys.getsizeof(trasformato1), "lista")
print(sys.getsizeof(trasformato2), "generatore")
