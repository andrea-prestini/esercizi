import math
import time
from multiprocessing import Pool


def task(arg):
    return sum([math.sqrt(i) for i in range(1, arg)])


core = 8

if __name__ == "__main__":
    start = time.time()
    print("Starting tasks...")
    with Pool(core) as pool:
        results = pool.map(task, range(1, 50000))
    print("Done!")
    end = time.time()
    print("Took {} seconds".format(end - start))
