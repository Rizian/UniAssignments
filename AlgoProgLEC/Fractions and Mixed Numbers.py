'''
Fractions and Mixed Numbers
'''
import math

Numer = int(input("Enter the Numerator Here >> "))

while Numer <= 0:
    Numer = int(input("The Numerator has to be greater than 0 \nEnter the Numerator Here >> "))

Denom = int(input("Enter the Denominator Here >> "))

while Denom <= 0:
    Denom = int(input("The Denominator has to be greater than 0 \nEnter the Denominator Here >> "))

Frac = f"{Numer} / {Denom}"             #sets the fraction as a string
ComDiv = math.gcd(Numer, Denom)         #finds the greatest common factor between numerator and denominator

if Numer // Denom == 0:             #checks if numerator is greater than denominator; yes = improper fraction, no = proper fraction
    print(f"{Frac} is a proper fraction.")
    if ComDiv != 1:                 #checks if fraction can be simplified
        Numer = int(Numer / ComDiv)
        Denom = int(Denom / ComDiv)         #overwrites numerator and denominator with their simplified values
        Frac = f"{Numer} / {Denom}"         #overwrites the string with new values. Frac does not get overwritten without this line
        print(f"This fraction can be simplified.\nThe simplified fraction is {Frac}")
    else:
        print(f"This fraction cannot be simplified.\n{Frac} is already in its simplest form.")
else:
    print(f"{Frac} is an improper fraction.")
    if ComDiv != 1:                                                                                 #------------------------------------------------------
        Numer = int(Numer / ComDiv)
        Denom = int(Denom / ComDiv)
        Frac = f"{Numer} / {Denom}"                                                                 #Tried making into a function reduce() but didn't work.
        print(f"This fraction can be simplified.\nThe simplified fraction is {Frac}.")
    else:
        print(f"This fraction cannot be simplified.\n{Frac} is already in its simplest form.")      #------------------------------------------------------
    print("It can also be written as a whole number or a mixed fraction.")
    WholeNum = Numer // Denom
    Remainder = Numer % Denom
    if Remainder == 0:
        print(f"{Frac} can be written as the whole number {WholeNum}.")
    else:
        print(f"{Frac} can be written as the mixed number {WholeNum} {Remainder} / {Denom}.")   #I regret calling the variable "Denom" cuz I keep typing in "Demon" instead :/