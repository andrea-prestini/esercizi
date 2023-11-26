@lambda _: _()
def result() -> int:
    a = 6
    b = 7
    return a * b


assert isinstance(result, int)
assert result == 42
assert 'a' not in locals()
assert 'b' not in locals()
