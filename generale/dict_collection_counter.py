from collections import Counter


nums = [1, 2, 3, 3, 2, 2, 2, 2, 1, 1, 1, 6, 5, 6, 6, 6,]

counter = Counter(nums)


k = 2

k_elements = {k: counter[k] for k in list(counter)[:k]}

print(counter)
print()
print(f"{k} elements ->", k_elements)
