'''
Challenge 3: Make a string output in spongebobcase
'''

x = input("input text: ")

counter = True
for i in x:
    if i == " ":
        print(" ", end="")
    elif counter == True:
        print(i.upper(), end="")
        counter = False
    else:
        print(i.lower(), end="")
        counter = True