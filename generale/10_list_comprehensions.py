import pprint
values = [x+1 for x in range(10)]  # simple list

# Comprehension condition
evens = [number for number in range(50) if number % 2 == 0]

# Strings that start with "a" and end in "y"

options = ["any", "albany", "apple", "world", "hello", ""]
valid_strings = [
    string
    for string in options
    if len(string) >= 2
    if string[0] == "a"
    if string[-1] == "y"
]

# Flattening a matrix (list of list)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]

# If else in list comprehension
categories = ["Even" if x % 2 == 0 else "Odd" for x in range(10)]

# Build a 3D list
printer = pprint.PrettyPrinter()

lst = [
    [[num for num in range(5)]
     for _ in range(5)]
    for _ in range(5)
]

# List comp with funcitons


def square(x):
    return x**2


squared_numbers = [square(x) for x in range(10)]

# Dictionary comprehension
pairs = [("a", 1), ("b", 2), ("c", 3)]

my_dict = {k: v**2 for k, v in pairs}

# Remove duplicates from a list while applying a function
nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique_squares = {x**2 for x in nums}
print(unique_squares)

# Generator comprehension
sum_of_squares = sum(x**2 for x in range(1_000_000))

# crea un sovraccarico di memoria
sum_of_squares = sum([x**2 for x in range(1_000_000)])
