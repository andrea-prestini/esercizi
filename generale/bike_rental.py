class bickeShop:
    def __init__(self, stock) -> None:
        self.stock = stock

    def displayBike(self):
        print('Totale Bikes', self.stock)

    def rentForBike(self, qty):
        if qty <= 0:
            print('Enter positive value...')
        elif qty > self.stock:
            print('Enter value less then stock...')
        else:
            print('Total Prices:', qty * 100)
            print('Totale Bikes:', self.stock)


while True:
    obj = bickeShop(100)
    uc = int(
        input(
            """
1 Display Stock
2 Rent a Bike
3 Exit\n"""
        )
    )

    if uc == 1:
        obj.displayBike()
    elif uc == 2:
        n = int(input('Enter the Qty: --'))
        obj.rentForBike(n)
    else:
        break
