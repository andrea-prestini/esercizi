import timeit
import random


def test1():
    for i in range(1000):
        random.random()


def test2():
    random_num = random.random

    for i in range(1000):
        random_num()


if __name__ == "__main__":
    print("Running TEST...")
    dot_not = min(timeit.repeat(test1, repeat=10, number=10_000))
    ref = min(timeit.repeat(test2, repeat=10, number=10_000))

    print("Dot notation", round(dot_not, 5))
    print("Reference", round(ref, 5))

    percent_faster = (1 - (ref / dot_not)) * 100
    print(f'{(round(percent_faster, 2)):,} % faster')
