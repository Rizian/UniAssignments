# =============================================================================================================================

# calculates the amount of days in decimal form from given hours, minutes and seconds values
def get_days(i, j, k):
    # increments the higher time hierarchy value while either Minutes or Seconds is at 60 or above until they are below 60
    # is ultimately unecessary for calculations but it helps to understand while manually validating results
    # while k >= 60:
    #     j += 1
    #     k -= 60
    # while j >= 60:
    #     i += 1
    #     j -= 60
    
    # Days equals:
    # 24 Hours
    # 24 * 60 Minutes = 1440 Minutes
    # 24 * 60 * 60 Seconds = 86400 Seconds
    x = (i / 24) + (j / 1440) + (k / 86400)

    return round(x, 4)  # rounds the result to 4 decimal places and returns it

# asks user to input the values of hours, minutes and seconds, then prints the result of days
def convert_to_days():
    hours = int(input("Enter the number of hours: "))
    minutes = int(input("Enter the number of minutes: "))
    seconds = int(input("Enter the number of seconds: "))

    days = get_days(hours, minutes, seconds)

    print(f"The number of days is: {days}")

# convert_to_days()

# =============================================================================================================================

# calculates the weight on another planet (default = approx. gravity of Jupiter)
def calc_weight_on_planet(mass = int, gravity = 23.1):
    weight = (int(mass) / 9.8) * gravity
    print(float(weight))


# calc_weight_on_planet(120)
# calc_weight_on_planet(120, 9.8)
# calc_weight_on_planet(120, 23.1)

# =============================================================================================================================

# calculates the number of molecules in n grams of an element using the element's atomic mass (default = gold (Au))
def num_atoms(grams, am = 196.97):
    molNum = (grams / am) * (6.022 * (10 ** 23))  # Avogadro's number = 6.022x10^23 = IB Chem HL PTSD
    print (f"{molNum:.10e}")

# num_atoms(10)
# num_atoms(10, 12.001)
# num_atoms(10, 1.008)

# =============================================================================================================================

# calculates a height value based on desired width and aspect ratio of current values
def calc_new_height():
    oldWidth = int(input("Enter the current width >> "))
    oldHeight = int(input("Enter the current height >> "))
    newWidth = int(input("Enter the desired width >> "))

    newHeight = (oldHeight / oldWidth) * newWidth

    print(f"The corresponding height is {newHeight:.1f}")

# calc_new_height()

# =============================================================================================================================

# function to convert fahrenheit into celsius
def convert_to_celsius(temp_f):
    temp_c = (5 / 9) * (temp_f - 32)
    return temp_c

# function to convert celsius into kelvin
def convert_to_kelvin(temp_c):
    temp_k = temp_c + 273.15
    return temp_k

# asks for a temperature in Fahrenheit, then converts/calculates it and returns the temperature in Fahrenheit, Celsius, and Kelvin.
def convert_temp():
    temp_f = eval(input("Enter the temperature in Fahrenheit >> "))

    temp_c = convert_to_celsius(temp_f)
    temp_k = convert_to_kelvin(temp_c)

    print(f"The temperature in Fahrenheit is {temp_f} °F")  # degrees symbol = Alt+0176
    print(f"The temperature in Celsius is {temp_c} °C")
    print(f"The temperature in Kelvin is {temp_k} K")       # kelvin doesn't use degrees symbol because it is calibrated to absolute zero; is an absolute value.

# convert_temp()