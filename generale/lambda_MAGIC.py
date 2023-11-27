def f(x):
    return 3*x+1


print("il risultato è:", f(2))


# LAMBDA è una funziona anonima in python! Dobbiamo darle un nome...

g = lambda x: 3*x+1
print(g(2))
print(g(4))
print(g(12))


mia_func = lambda x, y: x if x > y else y

