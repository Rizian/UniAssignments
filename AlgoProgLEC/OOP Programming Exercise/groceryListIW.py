"""
Grocery program to help calculate the total price of shopping from a specific list of food items.
The list is as follows:
    ITEM NAME             | PRICE
    Dry Cured Iberian Ham | $177.80
    Wagyu Steaks          | $450.00
    Matsutake Mushrooms   | $272.00
    Kopi Luwak Coffee     | $306.50
    Moose Cheese          | $487.20
    White Truffles        | $3600.00
    Blue Fin Tuna         | $3603.00
    Le Bonnotte Potatoes  | $270.81
"""
# Import the Food Item class from the 
from foodItemsIW import FoodItemIW

# Function to loop inputs for multiple inputs
def inputLoopIW():
    orders = []     # list for containing all the food items

    # While loop to validate count
    while True:
        # count to specify how many items to buy / length of the succeeding for loop
        count = int(input("How many items will you order today?\n>> "))
        if count < 1:
            print("[[ Number of items must be at least 1. ]]")   # tells the user to input a positive number and then restarts the while loop
            print("")                                            # brackets and empty line for readability and emphasis
        else:
            break   # stops the while loop

    # For loop asking the user to input the values for each food item
    for i in range(count):
        print(f"Item #{i+1} - ")

        # asks the user to input the following values in order to instantiate the food items
        name = input("Enter food item you would like to buy:\n>> ")
        # While loop for validating input for amount
        while True:
            amount = eval(input("How much would you like to buy (in lbs):\n>> ")) # eval() is used here because it can either be an integer or a float depending
            if amount < 0:
                print("[[       Amount cannot be negative       ]]")    # tells the user to input a non-negative number and then restarts the while loop
                print("[[  Please enter a non-negative number.  ]]")    # brackets and empty line for readability and emphasis
                print("")
            else:
                break   # stops the while loop

        # creates the food items based on the input values and then stores the created food item into the list
        orders.append(FoodItemIW(name, amount))

        print("")   # prints empty line
    
    # Returns the list of food items
    return orders

# Function to display the contents of the order
def displayListIW(list):
        print("You have chosen to purchase the following:\n")
        # For loop to print each item in the order list
        for i in list:
            print(f"Item #{list.index(i)+1} -\n{i}\n")  # no need to type in and format each FoodItem class attribute
                                                        # we just need to call each item as it is already formatted in the __str__
                                                        # outputs a new line at the end of each just for readability

def calcTotalCostIW(list):
    # sets total_cost to initial state of 0.00 
    total_cost = 0.00

    # For loop to add the cost of each order to total_cost
    for i in list:
        total_cost += i.getOrderPriceIW()
    
    # ensures total_cost is rounded to 2 decimal places then returns it
    return round(total_cost, 2)

# Main function
def main():
    # prints the list of available food items to buy
    print("""                Available Items
    ---------------------------------------
          ITEM NAME       | PRICE (per lbs)
    Dry Cured Iberian Ham |     $177.80
    Wagyu Steaks          |     $450.00
    Matsutake Mushrooms   |     $272.00
    Kopi Luwak Coffee     |     $306.50
    Moose Cheese          |     $487.20
    White Truffles        |    $3600.00
    Blue Fin Tuna         |    $3603.00
    Le Bonnotte Potatoes  |     $270.81
    """)
    # While loop for validating that all inputs are correct
    while True:
        # assigns the returned list from input loop into a callable variable
        orders = inputLoopIW()
        # displays the contents of the assigned list
        displayListIW(orders)
        # confirmation input
        confirm = input("Is this correct? (Y/N)\n>> ").lower()  # lower() to force all charcters to lowercase, no need to type in the exact matching case
        if confirm == "y" or confirm == "yes":
            break
        elif confirm == "n" or confirm == "no":
            orders.clear()  # clears the assigned list in order to assign a new list later
            continue        # restarts the loop
        else:
            print("unknown input, assuming \"No\"") # will notify user of unknown input then restarts the loop anyway
            orders.clear()                          # clears the assigned list in order to assign a new list later
            continue                                # restarts the loop
    
    # calculates the total cost of all the orders
    total_cost = calcTotalCostIW(orders)

    # Prints a formatted string stating the totoal cost of all the orders
    print(f"\nThe total cost of the order is ${total_cost:.2f}")

# makes sure that the program is only run in this file
if __name__ == "__main__":
    main()
