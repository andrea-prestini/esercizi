# Errori di sintassi

a = 0

    # Output:
    # SyntaxError: invalid syntax

    # Eccezioni (errori logici)

# 5/0
# Traceback (most recent call last):
#  File "<ipython-input-21-0106664d39e8>", line 1, in <module>
#    5/0
# ZeroDivisionError: division by zero


print(dir(locals()['__builtins__']))

# Output:
# ['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError', '__IPYTHON__', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'cell_count', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'debugcell', 'debugfile', 'delattr', 'dict', 'dir', 'display', 'divmod', 'enumerate', 'eval', 'exec', 'filter', 'float', 'format', 'frozenset', 'get_ipython', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'range', 'repr', 'reversed', 'round', 'runcell', 'runfile', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']


# TRY

# 5 + 'c'

try:
    n1 = int(input('Inserisci un numero: '))
    n2 = int(input('Inserisci un secondo numero: '))
    print("il risultato è:", n1+n2)

except TypeError:
    print("Attenzione, non è possibile sommare " + str(type(n1)) + " con "+str(type(n2)) +
          ": reinserisci i valori")

# Output:
# Inserisci un numero: 5

# Inserisci un secondo numero: c
# Traceback (most recent call last):

#  File "<ipython-input-92-ef6a543c150d>", line 3, in <module>
#    n2 = int(input('Inserisci un secondo numero: '))

# ValueError: invalid literal for int() with base 10: 'c'


try:
    n1 = int(input('Inserisci un numero: '))
    n2 = int(input('Inserisci un secondo numero: '))
    print("il risultato è:", n1+n2)

except TypeError:
    print("Attenzione, non è possibile sommare i due numeri: reinserisci i valori")
except ValueError:
    print("Attenzione, non è possibile convertire in intero uno dei due valori inseriti")


# Posso scrivere il precedente esempio in quest'altro modo:


try:
    n1 = int(input('Inserisci un numero: '))
    n2 = int(input('Inserisci un secondo numero: '))
    print("il risultato è:", n1+n2)

except (TypeError, ValueError):
    print("Attenzione, non è possibile sommare i due numeri: reinserisci i valori")
#
#
# # o anche in quest'altro:
try:
    n1 = int(input('Inserisci un numero: '))
    n2 = int(input('Inserisci un secondo numero: '))
    print("il risultato è:", n1+n2)

except Exception:
    print("Attenzione, non è possibile sommare i due numeri: reinserisci i valori")
#

# Raise

listacasuale = [0, 3, 5]

for i in listacasuale:
    if i == 0:
        raise ZeroDivisionError("Attenzione: divisione per 0!")

    else:
        r = 1/int(i)
        print("Il valore della lista è pari a ", i)
    break

print("Il reciproco di ", i, "è", r)

# Output:

#    Traceback (most recent call last):

#  File "<ipython-input-133-8e0ecfc2ba98>", line 5, in <module>
#    raise ZeroDivisionError("Attenzione: divisione per 0!")

# ZeroDivisionError: Attenzione: divisione per 0!


try:
    num = int(input("inserisci un numero: "))
    assert num % 2 == 1
except:
    print("Non hai inserito un numero dispari")
else:
    num2 = num * num
    print("il quadrato del numero dispari "+str(num)+" è pari a", num2)

# num = 16
# Non hai inserito un numero dispari

# num = 13
# il quadrato del numero dispari 13 è pari a 169


# Finally

file = open('test.txt', 'w')

try:
    file.write("Testing.")
    print("Sto scrivendo sul file test.txt.")
except IOError:
    print("Non potresti sovrascrivere il file.")
else:
    print("Scrittura eseguita correttamente.")
finally:
    file.close()
    print("File chiuso.")

# Output:
# Sto scrivendo sul file test.txt.
# Scrittura eseguita correttamente.
# File chiuso.
