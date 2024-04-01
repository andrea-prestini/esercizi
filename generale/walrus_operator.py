def f(x):
    return x - 3


results_walrus = [result for x in range(20) if (result := f(x)) > 3]

print(results_walrus)
