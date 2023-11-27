from itertools import islice
# from python 3.10 we have pairwise

numbers = [10, 20, 33, 40, 50, 60, 70, 80]
b = ["a", "b", "c", "d"]

result = 0
# loops as usually very slow
for num in numbers:
    result += num

print("Loop", result)

print("Modulo sum", sum(numbers))
print("-" * 50)
# use enumerate instead of loop
print("Use Enumerate")
for idx, val in enumerate(numbers, start=1):
    print(idx, val)


print("-" * 50)

# use zip for multiple iterable
print("Use Zip")
for val1, val2 in zip(numbers, b):
    print(val1, val2)

print("-" * 50)

# use generator instead list
print("Use generator")
events = [("learn", 5), ("learn", 10), ("relax", 20)]

study_time = (event[1] for event in events if event[0] == "learn")
minutes_study = sum(study_time)
print(minutes_study)

print("-" * 50)

# use itertools
print("Use itertools islice")

lines = ["line1", "line2", "line3", "line4", "line5",
         "line6", "line7", "line8", "line9", "line10"]

first_five_line = islice(lines, 0, 5)
for line in first_five_line:
    print(line)

print("-" * 50)

print("Use itertools pairwise")
data = "ABCDEFG"

# for pair in pairwise(data):
#     print(pair[0], pair[1])
