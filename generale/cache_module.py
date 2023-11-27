from functools import lru_cache
from time import perf_counter


# Naive factorial calculation
def fact_n(n):
    if n < 2:
        return 1
    else:
        return n * fact_n(n - 1)


# Cached factorial calculation
@lru_cache(maxsize=128)
def fact_n_cache(n):
    if n < 2:
        return 1
    else:
        return n * fact_n_cache(n - 1)


numero_fattoriale = 250
# Calculate factorial naively, no caching
start = perf_counter()
fact_n(numero_fattoriale)
end = perf_counter()
print('No Caching')
print('Time elapsed: ', (end - start) * 1000)

# Calculate factorial, with caching
start = perf_counter()
fact_n_cache(numero_fattoriale)
end = perf_counter()
print('Cached - 1st run')
print('Time elapsed: ', (end - start) * 1000)

# Calculate factorial, with caching again
start = perf_counter()
fact_n_cache(numero_fattoriale)
end = perf_counter()
print('Cached - 2nd run')
print('Time elapsed: ', (end - start) * 1000)
