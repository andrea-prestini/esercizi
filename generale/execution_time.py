import time

# get the start time
st = time.time()

Max_numero = 1_000_000_000

lista = (x for x in range(Max_numero))

first = last = next(lista)
for last in lista: pass
et = time.time()

print(first, last)
elapsed_time = et - st
print("time to execution:", elapsed_time, "seconds")
print("time to execution:", elapsed_time / 60, "minutes")