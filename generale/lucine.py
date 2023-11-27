
# n = int(input("Quanto grandi i disegni?\n"))
n = 5

# |%%--%%| <v5KjM5eLao|b7i2xeA66v>
"""°°°
## quadrato di asterischi
°°°"""
# |%%--%%| <b7i2xeA66v|w6nDi2icq3>

for i in range(n):
    for k in range(n):
        print("* ", end="")
    print("")

# |%%--%%| <w6nDi2icq3|nhA6SzNqs9>
"""°°°
## diagonale principale
°°°"""
# |%%--%%| <nhA6SzNqs9|74wflhaNKE>

for i in range(n):
    for j in range(n):
        if i == j:
            print("* ", end="")
        else:
            print(". ", end="")
    print("")

# |%%--%%| <74wflhaNKE|LtJLes26Ys>
"""°°°
## diagonale principale e diagonale secondaria
°°°"""
# |%%--%%| <LtJLes26Ys|DEWy0TLEyL>

for i in range(n):
    for j in range(n):
        if i == j or j == (n - 1 - i):
            print("* ", end="")
        else:
            print(". ", end="")
    print("")

# |%%--%%| <DEWy0TLEyL|xVubxVSAop>
"""°°°
## Triangolo sinistro
°°°"""
# |%%--%%| <xVubxVSAop|eJK1CZt4B7>

for i in range(n):
    for j in range(n):
        if i >= j:
            print("* ", end="")
        else:
            print(". ", end="")
    print("")

# |%%--%%| <eJK1CZt4B7|ySp5x4ESTV>
"""°°°
## Cornice
°°°"""
# |%%--%%| <ySp5x4ESTV|xU7rp1MhaW>

for i in range(n):
    for j in range(n):
        if (j == 0 or j == n-1) or (i == 0 or i == n-1):
            print("* ", end="")
        else:
            print(". ", end="")
    print("")

# |%%--%%| <xU7rp1MhaW|w5p0QKnWNU>
"""°°°
## Croce centrale
°°°"""
# |%%--%%| <w5p0QKnWNU|7finusQtsm>

# Croce centrale
for i in range(n):
    for j in range(n):
        if n % 2 != 0 and i == (n-1)/2 or j == (n-1)/2 or \
                n % 2 == 0 and j == (n/2) or i == (n/2) or \
                i == (n/2)-1 or j == (n/2)-1:
            print("* ", end="")
        else:
            print(". ", end="")
    print("")
