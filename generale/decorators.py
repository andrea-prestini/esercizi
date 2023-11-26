import time


def times(f):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = f(*args, **kwargs)
        stop_time = time.time()
        dt = stop_time - start_time
        print(f'deltaT = {dt}')
        return result

    return wrapper


def prime_factoring(n):
    factors = []
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            n //= divisor
        divisor += 1

    return factors
