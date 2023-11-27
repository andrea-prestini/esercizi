def divisore(a,b):
    try:
        risultato = a/b
        print("il risultato è " + str(risultato))
        
    except ZeroDivisionError as identifier:
        print("la divisione per 0 non è ammessa!")

print(divisore(1,3))
print(divisore(5,0))