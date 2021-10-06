print("Triangle Perimeter")
edge1 = float(input("Enter the length of edge 1: "))
edge2 = float(input("Enter the length of edge 2: "))
edge3 = float(input("Enter the length of edge 3: "))

if edge1 + edge2 > edge3 and edge1 + edge3 > edge2 and edge2 + edge3 > edge1:
    print(f"The perimeter of the triangle is {edge1+edge2+edge3}!")
else:
    print("invalid input. Values don't represent a triangle and cannot be calculated!")