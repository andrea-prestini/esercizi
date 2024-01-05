from functools import wraps
import random

# inseriamo un parametro direttamente usato dal decoratore


def power_of(exponent):

    def decorator(fnc):

        def inner():
            return fnc() ** exponent

        return inner

    return decorator


@power_of(3)
def random_odd_digit():
    return random.choice([1, 3, 5, 7, 9])


print("stampo numero dispari casuale -->", random_odd_digit())


# parametri nel decoratore
def create_decorator(argument):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            print(f'hai inserito il paramentro {argument}\n' * argument)
            retval = function(*args, **kwargs)
            return retval
        return wrapper
    return decorator


@create_decorator(3)
def miaFunzione(x):
    return f"ho stampato {x}"


print(miaFunzione(10))
