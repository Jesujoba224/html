
class Computer:
    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print(f"Selling Price: {self.__maxprice}")

    def setMaxPrice(self, price):
        self.__maxprice = price


c = Computer()
c.sell()

# Trying to change the price directly
c.__maxprice = 1000
c.sell()

# Using setter method to change the price
c.setMaxPrice(1000)
c.sell()
