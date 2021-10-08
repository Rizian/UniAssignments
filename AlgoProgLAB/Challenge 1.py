'''
Challenge 1
'''
x = int(input("Enter a number: "))

if x % 11 == 0:
    print("a", end="")
if x % 9 == 0:
    print("b", end="")
if x % 7 == 0:
    print("c", end="")
if x % 2 == 0:
    print("d", end="")
if (x % 11 != 0 and x % 11 != 0 and x % 9 != 0 and x % 7 != 0 and x % 2 != 0):
    print("e", end="")

'''
could also use a list but less efficient lol
list1 = []

x = int(input("Enter a number: "))

if x % 11 == 0:
    list1.append("a")
if x % 9 == 0:
    list1.append("b")
if x % 7 == 0:
    list1.append("c")
if x % 2 == 0:
    list1.append("d")
if (x % 11 != 0 and x % 11 != 0 and x % 9 != 0 and x % 7 != 0 and x % 2 != 0):
    list1.append("e")

n = ''.join(list1)
print(n)
'''