### Ciclo For 

x = [2,3,4,5]
prod = 1

for val in x:
    x = prod
    prod = prod * val
    print ("Moltiplicando "+str(val)+ " per " +str(x) +" otteniamo " 
           +str(prod)) 

# Risultato:
# Moltiplicando 2 per 1 otteniamo 2
# Moltiplicando 3 per 2 otteniamo 6
# Moltiplicando 4 per 6 otteniamo 24
# Moltiplicando 5 per 24 otteniamo 120

## funzione Range

list(range(5))
# Risultato [0, 1, 2, 3, 4]

list(range(7,15))
# Risultato [7, 8, 9, 10, 11, 12, 13, 14]

list(range(7,15,2))
# Risultato [7, 9, 11, 13]


## Funzione range in for loops

item = ['banana', 'mela', 'arancia']

for val in range(len(item)):
    print ('Vorrei mangiare una',item[val])

# Risultato:
# Vorrei mangiare una banana
# Vorrei mangiare una mela
# Vorrei mangiare una arancia    


## Ciclo For con blocco else
num = 1

for val in range(num,25,3):
    print(val)
else:
    print('Nessun elemento rimanente')

# Risultato:
# 1
# 4
# 7
# 10
# 13
# 16
# 19
# 22
# Nessun elemento rimanente


età = 35
dict1 = {25: 'ragazzo',42: 'donna', 7: 'bimbo', 57:'signore'}

for val in dict1:
    if val == età:
        print (dict1[età])
        break
else:
    print("Età della persona non presente nel dizionario")


# Risultato:
# Età della persona non presente nel dizionario

#------------------------------------------------------------


### While loops

a = (5,7,98,24,47)
i = 0
somma = 0
while i < 5:
    print(a[i])
    somma = somma + a[i]
    i = i + 1
print ('la somma della tupla è pari a: '+str(somma))

# Risultato:
# 5
# 7
# 98
# 24
# 47
# la somma della tupla è pari a: 181


## Ciclo while con blocco else
import random
count = 1

while count < 8:
   guess = random.randint(1,8)    
   if count >= 1:
        count +=1
       
   if guess == count:
        print ("il numero random e count sono pari a "+str(guess))
        print ("Hai vinto!")
        
        break
   elif count == 8:
        print ("Hai perso")
        print ("dopo 8 iterazioni count è diverso da guess")
else:
    print ("Prova ancora")
        
# Risultato:
# Hai perso
# dopo 8 iterazioni count è diverso da guess
# Prova ancora    



## Istruzione break
### Ciclo For 

x = [2,3,4,5]
prod = 1

for val in x:
    x = prod
    prod = prod * val
    if prod > 20:
        print ('X è pari a '+str(x) +' mentre prod è uguale a '+str(prod))
        break


# Risultato
# X è pari a 6 mentre prod è uguale a 24

## break ciclo while

a = (5,7,98,24,47)
i = 0
somma = 0
while i < 5:
    somma = somma + a[i]
    i = i + 1
    if i == 4:
       print ('Raggiunta la quarta iterazione del ciclo!'+
              ' La somma della tupla è pari a: '+str(somma))
       break
# Risultato:
# Raggiunta la quarta iterazione del ciclo! La somma della tupla è pari a: 134    
    
## Istruzione Continue
# Ciclo for

vals = [1, 2, 3, 4, 5]
for i in vals:
    if i == 2:
        continue
    print(i**2)
    
# Risultato: 
# 1
# 9
# 16
# 25
 

# Ciclo while

vals = [1, 2, 3, 4, 5]
i = 1
while i <= 5:
    if i == 2:
        i=i+1
        continue
        
    print(i**2)
    i += 1
# Risutalto:
# 1
# 9
# 16
# 25    