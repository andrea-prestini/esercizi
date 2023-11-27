def myFun(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)
 
 
# Now we can use *args or **kwargs to
# pass arguments to this function :
args = ("Geeks", "for", "Geeks")
myFun(*args)
 
kwargs = {"arg1": "Geeks", "arg2": "for", "arg3": "Geeks"}
myFun(**kwargs)

print("-" * 80)

def myFun(*args, **kwargs):
    print("args: ", args)
    print("kwargs: ", kwargs)
 
 
# Now we can use both *args ,**kwargs
# to pass arguments to this function :
myFun('geeks', 'for', 'geeks', first="Geeks", mid="for", last="Geeks")

print("_" * 80)

def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))
 
 
# Driver code
myFun(first='Geeks', mid='for', last='Geeks')

print("_" * 80)

def myFun(arg1, *argv):
    print("First argument :", arg1)
    for arg in argv:
        print("Next argument through *argv :", arg)
 
 
myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

print("-" * 80)

def miaFunzione(*args):
    for val in args:
        print(val)

elenco = ["uno", "due", "tre"]
print("passo come oggetto unico lista")
miaFunzione(elenco)
print("=" * 50)
print("passo come singoli valori di un elenco")
miaFunzione(*elenco)
