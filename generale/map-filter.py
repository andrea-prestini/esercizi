numero = 5
numbers = [x for x in range(1, numero)]

trasformato1 = [x ** 2 +1 for x in numbers if x % 2 == 0]
trasformato2 = map(
                   lambda x: x**2+1,
                   (filter(lambda x: x % 2 == 0, numbers))
                  )




print("{:,d}".format(sum(trasformato1)))
print("{:,d}".format(sum(trasformato2)))
print("{:,.2f}".format(sum(trasformato1)))
print("{:,.2f}".format(sum(trasformato2)))
print("con allineamento")
print("{:>30,.2f}".format(sum(trasformato1)))
print("{:>30,.2f}".format(sum(trasformato2)))