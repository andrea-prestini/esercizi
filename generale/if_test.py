from timeit import timeit


def test_if(text: str):
    if text == 'a':
        ...
    if text == 'b':
        ...
    if text == 'c':
        ...


def test_if_else(text: str):
    if text == 'a':
        ...
    elif text == 'b':
        ...
    elif text == 'c':
        ...
    else:
        ...


letter = 'a'

test_if(letter)
test_if_else(letter)

test_if_time = timeit('test_if(letter)', globals=globals())
test_if_else_time = timeit('test_if_else(letter)', globals=globals())


print('if_normale', round(test_if_time, 3))
print('if_else', round(test_if_else_time, 3))
