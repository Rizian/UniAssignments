class Retail_Item:
    "This is a class for a retail item"

    # Instantiation
    def __init__(self, type="Not Specified", amount=0, price=0.00):
        self.setType(type)
        self.setAmount(amount)
        self.setPrice(price)

    # Mutator methods with output type conversions and input validation for __amount and __price 
    def setType(self, type) -> str:
        self.__type = type
    def setAmount(self, amount) -> int:
        if amount >= 0:
            self.__amount = amount
        else:
            self.__amount = 0
            print("Amount cannot be negative")
            print("Please enter non-negative integer")
    def setPrice(self, price) -> float:
        if price >= 0:
            self.__price = price
        else:
            self.__price = 0.00
            print("Price cannot be negative")
            print("Please enter non-negative number")

    # Accessor methods
    def getType(self):
        return self.__type
    def getAmount(self):
        return self.__amount
    def getPrice(self):
        return self.__price

    # Prints formatted string when called
    def __str__(self):
        return f"{self.getType()}\t\t\t{self.getAmount()}\t\t${self.getPrice():.2f}"


# def main():
#     name1 = input("Name of item 1: ")
#     amount1 = int(input("Amount of item 1: "))
#     price1 = float(input("Price of item 1: "))

#     name2 = input("Name of item 2: ")
#     amount2 = int(input("Amount of item 2: "))
#     price2 = float(input("Price of item 2: "))

#     item1 = Retail_Item(name1, amount1, price1)
#     item2 = Retail_Item(name2, amount2, price2)
    
#     print("Item\t\t\tAmount\t\tPrice")
#     print("-----------------------------------------------")
#     print(item1)
#     print(item2)

def mainloop():
    li = []
    
    count = int(input("How many items do you want to buy? >> "))
    print("")

    for i in range(count):
        name = input(f"Name of item {i+1}: ")
        amount = int(input(f"Amount of item {i+1}: "))
        price = float(input(f"Price of item {i+1}: "))
        
        li.append(Retail_Item(name, amount, price))
        print("")

    print("Item\t\t\tAmount\t\tPrice")
    print("-----------------------------------------------")
    for i in li:
        print(i)

if __name__ == "__main__":
    # main()
    mainloop()