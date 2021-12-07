"""
Food item class module to import into main grocery program.
"""
class FoodItemIW:
    "Class for a single type of food item"
    
    # Generates attributes of the class when instantiated
    def __init__(self, foodname, foodamount):
        self.__name = foodname
        self.__amount = foodamount

        # calls the methods calculate values while instantiating __standardPrice and __orderPrice attributes
        self.__priceListIW()
        self.calcCostIW()

    # Prints all the attributes in a formatted string
    def __str__(self):
        return f"Item: {self.__name}\nPrice: ${self.__standardPrice:.2f}/lbs\nAmount ordered: {self.__amount}\nOrder price: ${self.__orderPrice:.2f}"

    # Defines the standard price attribute based on the name of the food item
    def __priceListIW(self):
        if self.__name == "Dry Cured Iberian Ham":
            self.__standardPrice = 177.80
        elif self.__name == "Wagyu Steaks":
            self.__standardPrice = 450.00
        elif self.__name == "Matsutake Mushrooms":
            self.__standardPrice = 272.00
        elif self.__name == "Kopi Luwak Coffee":
            self.__standardPrice = 306.50
        elif self.__name == "Moose Cheese":
            self.__standardPrice = 487.20
        elif self.__name == "White Truffle":
            self.__standardPrice = 3600.00
        elif self.__name == "Blue Fin Tuna":
            self.__standardPrice = 3603.00
        elif self.__name == "Le Bonnotte Potatoes":
            self.__standardPrice = 270.81
        else:
            self.__standardPrice = 0.00

    # Calculates the total cost of the order based on the standard price and the amount of the item ordered
    def calcCostIW(self):
        total_cost = self.__standardPrice * self.__amount
        self.__orderPrice = round(total_cost, 2)            # ensuring that the value gets returned with 2 decimal places
    
    # Getter Functions
    def getAttributesIW(self):            # Getter function to return all attributes at once
        return self.__name, self.__amount, self.__standardPrice, self.__orderPrice
    def getNameIW(self):
        return self.__name
    def getAmountIW(self):
        return self.__amount
    def getStandardPriceIW(self):
        return self.__standardPrice
    def getOrderPriceIW(self):
        return self.__orderPrice