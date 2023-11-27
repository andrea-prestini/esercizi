import time

st = time.process_time()

Max_numero = 1_000_000_000

lista = (x for x in range(Max_numero))

first = last = next(lista)
for last in lista: pass

et = time.process_time()

print(first, last)

execution_time = et - st

print("CPU time to execution:", execution_time, "seconds")
print("CPU time to execution:", execution_time / 60, "minutes")
