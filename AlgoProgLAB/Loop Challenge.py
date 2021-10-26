loop = True
flag = True
while loop:
    inp = int(input("input a number >> "))
    if flag == True: 
        for i in range(inp):
            print("Hello World")
        flag = False
    if flag == False:
        for i in range(inp):
            print("Hi")
        flag = True
    if inp == -999:
        loop = False
    